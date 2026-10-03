#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML>=6.0,<7"]
# ///
# noqa: SIZE_OK — one auditable, standalone live-scenario driver.

# ─── How to run ───
# 1. Install uv (if not installed):
#      curl -LsSf https://astral.sh/uv/install.sh | sh
# 2. Run directly (credentials are read only from the environment):
#      uv run scripts/run_p4_live.py
# 3. Offline check / contract help:
#      uv run scripts/run_p4_live.py --self-test
#      uv run scripts/run_p4_live.py --help
# ──────────────────
"""Execute p4's scenario-s1 live half and emit custody-bearing evidence.

One-to-one mapping to ``open_chart/tests/test_scenario_live_half.py``:
baseline ``submit``; verify the successor fixture has two entries and carries
the prior entry verbatim; ``amend``; verify predecessor linkage; project every
stored family through ``core.project_row`` and require ``roundtrip_loss == []``;
read the prior submission and require ``lifecycle_state == amended`` with rows
retained; require exactly one melatonin row with ``patient_reported`` assertion.

No socket is opened on import, ``--help``, or ``--self-test``. Network access is
confined to ``HttpClient.request`` and reached only from guarded ``main``.
"""
from __future__ import annotations

import copy
import datetime as dt
import hashlib
from http.client import HTTPException
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Final, TypeAlias
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.parse import quote
from urllib.request import HTTPRedirectHandler, Request, build_opener

ROOT: Final = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from open_chart.intake import core  # noqa: E402

JsonValue: TypeAlias = None | bool | int | float | str | list["JsonValue"] | dict[str, "JsonValue"]
JsonObject: TypeAlias = dict[str, JsonValue]
TIMEOUT_SECONDS: Final = 20.0
FEATURE_DIR: Final = "001-expanded-patient-intake"
FIXTURES: Final = (
    "tests/fixtures/medx/intake-medications.yaml",
    "tests/fixtures/medx/intake-supplements.yaml",
    "tests/fixtures/medx/intake-history.yaml",
    "tests/fixtures/medx/scenario-intake-supplements-successor.yaml",
)
HELP: Final = """p4 openChart live runner

Required: OC_API_KEY, OC_API_SECRET
Optional: OC_BASE=http://localhost:8001, OC_SITE=<Frappe Host header>
Outputs: var/p4-live/<UTC-run-id>/http.jsonl and
         specs/001-expanded-patient-intake/live-evidence/<run-id>/evidence.yaml
Flags: --self-test (offline), --help
"""


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def require_object(value: JsonValue, step: str) -> JsonObject:
    if not isinstance(value, dict):
        raise RunnerError(step, "expected a JSON object")
    return value


def require_list(value: JsonValue, step: str) -> list[JsonValue]:
    if not isinstance(value, list):
        raise RunnerError(step, "expected a JSON list")
    return value


@dataclass(frozen=True, slots=True)
class RunnerError(Exception):
    step: str
    detail: str
    status: int | None = None

    def __str__(self) -> str:
        suffix = f" (HTTP {self.status})" if self.status is not None else ""
        return f"{self.step}: {self.detail}{suffix}"


@dataclass(frozen=True, slots=True)
class Config:
    base_url: str
    api_key: str
    api_secret: str
    site: str | None

    @classmethod
    def from_env(cls) -> "Config":
        key = (os.environ.get("OC_API_KEY") or os.environ.get("QA_API_KEY", "")).strip()
        secret = (os.environ.get("OC_API_SECRET") or os.environ.get("QA_API_SECRET", "")).strip()
        if not key or not secret:
            raise RunnerError("configuration", "OC_API_KEY and OC_API_SECRET are required")
        return cls(
            base_url=validated_endpoint(os.environ.get("OC_BASE", "http://localhost:8001")),
            api_key=key,
            api_secret=secret,
            site=os.environ.get("OC_SITE") or os.environ.get("QA_SITE") or None,
        )


def validated_endpoint(value: str) -> str:
    """Reject credential-bearing endpoints before requests or retained evidence."""
    try:
        endpoint = urlsplit(value)
        valid = (endpoint.scheme in {"http", "https"} and endpoint.hostname
                 and endpoint.username is None and endpoint.password is None
                 and not endpoint.query and not endpoint.fragment
                 and not any(character.isspace() for character in value))
        endpoint.port  # Validate the port before execution.
    except ValueError:
        valid = False
    if not valid:
        raise RunnerError("configuration", "endpoint must be HTTP(S), without credentials, query or fragment")
    return value.rstrip("/")


@dataclass(frozen=True, slots=True)
class HttpReply:
    payload: JsonObject
    headers: dict[str, str]


class _RejectRedirects(HTTPRedirectHandler):
    """Do not forward endpoint-scoped credentials to a redirect target."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class HttpClient:
    def __init__(self, config: Config, raw_path: Path):
        validated_endpoint(config.base_url)
        self._config = config
        self._raw_path = raw_path
        raw_path.parent.mkdir(parents=True, exist_ok=False)

    def request(self, step: str, path: str, body: JsonObject) -> HttpReply:
        url = f"{self._config.base_url}{path}"
        headers = {
            "Accept": "application/json",
            "Authorization": f"token {self._config.api_key}:{self._config.api_secret}",
            "Content-Type": "application/json",
        }
        if self._config.site:
            headers["Host"] = self._config.site
        request = Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")
        started = utc_now()
        try:
            with build_opener(_RejectRedirects()).open(request, timeout=TIMEOUT_SECONDS) as response:  # noqa: S310
                raw = response.read()
                status = response.status
                response_headers = dict(response.headers.items())
        except HTTPError as exc:
            try:
                with exc:
                    raw = exc.read()
                    response_headers = dict(exc.headers.items())
            except (TimeoutError, URLError, HTTPException, OSError):
                self._log(step, url, body, started, exc.code, {}, b"")
                raise RunnerError(step, "transport failure reading refusal; payload omitted", exc.code) from None
            self._log(step, url, body, started, exc.code, response_headers, raw)
            raise RunnerError(step, self._error_detail(raw), exc.code) from None
        except (TimeoutError, URLError, HTTPException, OSError):
            self._log(step, url, body, started, None, {}, b"")
            raise RunnerError(step, "transport failure; payload omitted") from None
        self._log(step, url, body, started, status, response_headers, raw)
        try:
            decoded: JsonValue = json.loads(raw.decode())
        except (UnicodeDecodeError, json.JSONDecodeError):
            raise RunnerError(step, "non-JSON response; payload omitted", status) from None
        return HttpReply(require_object(decoded, step), response_headers)

    def method(self, step: str, method: str, body: JsonObject) -> HttpReply:
        reply = self.request(step, f"/api/method/{method}", body)
        return HttpReply(require_object(reply.payload.get("message"), step), reply.headers)

    def _log(
        self,
        step: str,
        url: str,
        body: JsonObject,
        started: str,
        status: int | None,
        headers: dict[str, str],
        raw: bytes,
    ) -> None:
        event = {
            "step": step,
            "request": {
                "at": started,
                "method": "POST",
                "body_sha256": hashlib.sha256(json.dumps(body).encode()).hexdigest(),
            },
            "response": {
                "at": utc_now(),
                "status": status,
                "body_sha256": hashlib.sha256(raw).hexdigest(),
                "bytes": len(raw),
            },
            "payloads_recorded": False,
        }
        with self._raw_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(event, sort_keys=True) + "\n")

    @staticmethod
    def _error_detail(raw: bytes) -> str:
        return "HTTP endpoint refused the request; response payload omitted"


def assertion(results: list[JsonObject], name: str, passed: bool, method: str, observed: JsonValue) -> None:
    results.append({"id": name, "result": "PASS" if passed else "FAIL", "method": method, "observed": observed})
    if not passed:
        raise RunnerError(name, f"assertion failed; observed={observed!r}")


def probe_identity(client: HttpClient) -> JsonObject:
    try:
        reply = client.method(
            "probe_deployed_identity",
            "frappe.utils.change_log.get_versions",
            {"include_disabled": True},
        )
    except RunnerError as exc:
        return {"probe": "frappe.utils.change_log.get_versions", "status": "unknown", "reason": str(exc)}
    return {
        "probe": "frappe.utils.change_log.get_versions",
        "status": "observed",
        "apps": reply.payload,
        "revision": "unknown_unless_reported_by_probe",
    }


def scenario_corpus() -> list[JsonObject]:
    return [
        {"path": rel, "sha256": hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()}
        for rel in FIXTURES
    ]


def execute(client: HttpClient, run_id: str, results: list[JsonObject]) -> JsonObject:
    payload: JsonObject = core.build_payload(ROOT)
    patient_label = f"SYN-S1-LIVE-{run_id.removeprefix('p4-')}"
    created = client.request(
        "create_synthetic_patient",
        f"/api/resource/{quote('OC Patient', safe='')}",
        {"patient_name": patient_label},
    ).payload
    patient = str(require_object(created.get("data"), "create_synthetic_patient").get("name") or "")
    assertion(results, "synthetic_patient_created", bool(patient), "POST OC Patient through Frappe DocType REST", patient)

    first = client.method(
        "submit_baseline",
        "open_chart.api.v1.submit",
        {
            "patient": patient,
            "contract_version": str(payload["contract_version"]),
            "idempotency_key": f"SYN-S1-{run_id}-baseline",
            "payload": json.dumps(payload, sort_keys=True),
            "submitter_context": "SYN-TENANT/SYN-OPERATOR-01",
            "purpose_or_consent_ref": "SYN-CONSENT-0001",
        },
    ).payload
    first_submission = require_object(first.get("submission"), "submit_baseline")
    first_name = str(first_submission.get("name") or "")
    assertion(results, "baseline_submitted", bool(first_name), "open_chart.api.v1.submit returned a submission name", first_name)

    updated: JsonObject = copy.deepcopy(payload)
    successor_doc: JsonObject = core.load_yaml(ROOT / FIXTURES[-1])
    envelope = require_object(successor_doc.get("envelope"), "load_successor_fixture")
    content = require_object(envelope.get("content"), "load_successor_fixture")
    entries = require_list(content.get("entries"), "load_successor_fixture")
    families = require_object(updated.get("families"), "build_baseline_payload")
    supplements = require_object(families.get("supplement"), "build_baseline_payload")
    baseline_entries = require_list(supplements.get("entries"), "build_baseline_payload")
    assertion(results, "successor_has_two_supplements", len(entries) == 2, "len(successor fixture entries) == 2", len(entries))
    assertion(results, "prior_supplement_verbatim", entries[0] == baseline_entries[0], "successor entry[0] equals baseline supplement entry[0]", entries[0])
    supplements["entries"] = entries

    successor = client.method(
        "amend_with_successor",
        "open_chart.api.v1.amend",
        {
            "submission_name": first_name,
            "payload": json.dumps(updated, sort_keys=True),
            "reason": "SYN updated supplement list: melatonin added (scenario s1)",
            "submitter_context": "SYN-TENANT/SYN-OPERATOR-01",
        },
    ).payload
    successor_submission = require_object(successor.get("submission"), "amend_with_successor")
    assertion(results, "successor_links_predecessor", successor_submission.get("predecessor") == first_name, "successor.submission.predecessor equals baseline name", successor_submission.get("predecessor"))

    rows = require_list(successor.get("rows"), "amend_with_successor")
    census = core.load_census(ROOT)
    findings: list[str] = []
    for family, body_value in families.items():
        body = require_object(body_value, "roundtrip_zero_loss")
        source_entries = require_list(body.get("entries"), "roundtrip_zero_loss")
        family_rows = [require_object(row, "roundtrip_zero_loss") for row in rows if require_object(row, "roundtrip_zero_loss").get("record_family") == family]
        projected = [core.project_row(row, census) for row in family_rows]
        findings.extend(core.roundtrip_loss(source_entries, projected, family))
    assertion(results, "successor_roundtrip_zero_loss", findings == [], "core.project_row + core.roundtrip_loss for every submitted family", findings)

    prior = client.method("read_prior_submission", "open_chart.api.v1.read_submission", {"submission_name": first_name}).payload
    prior_submission = require_object(prior.get("submission"), "read_prior_submission")
    prior_rows = require_list(prior.get("rows"), "read_prior_submission")
    assertion(results, "prior_lifecycle_amended", prior_submission.get("lifecycle_state") == "amended", "read_submission(prior).lifecycle_state == amended", prior_submission.get("lifecycle_state"))
    assertion(results, "prior_rows_retained", bool(prior_rows), "read_submission(prior).rows remains non-empty", len(prior_rows))

    melatonin = []
    for row_value in rows:
        row = require_object(row_value, "melatonin_exactly_once")
        fields = require_object(row.get("fields"), "melatonin_exactly_once")
        if row.get("record_family") == "supplement" and fields.get("source_entry_id") == "SYN-INTAKE-SUPLINE-0002":
            melatonin.append(row)
    assertion(results, "melatonin_exactly_once", len(melatonin) == 1, "filter successor rows by supplement + SYN-INTAKE-SUPLINE-0002", len(melatonin))
    melatonin_fields = require_object(melatonin[0].get("fields"), "melatonin_patient_reported")
    assertion(results, "melatonin_patient_reported", melatonin_fields.get("assertion_kind") == "patient_reported", "stored melatonin assertion_kind equals patient_reported", melatonin_fields.get("assertion_kind"))

    built_rows = core.build_rows(updated, census)
    return {
        "patient": patient,
        "baseline_submission": first_name,
        "successor_submission": successor_submission.get("name"),
        "baseline_content_sha256": core.content_hash(core.build_rows(payload, census)),
        "successor_content_sha256": core.content_hash(built_rows),
    }


def write_evidence(config: Config, run_id: str, started: str, raw_path: Path) -> int:
    results: list[JsonObject] = []
    identity: JsonObject = {"status": "unknown", "reason": "probe not attempted"}
    observations: JsonObject = {}
    error: str | None = None
    client = HttpClient(config, raw_path)
    identity = probe_identity(client)
    try:
        observations = execute(client, run_id, results)
    except RunnerError as exc:
        error = str(exc)
        if not results or results[-1].get("result") != "FAIL":
            results.append({"id": exc.step, "result": "FAIL", "method": "typed runner/transport boundary", "observed": str(exc)})
    passed = error is None and bool(results) and all(row.get("result") == "PASS" for row in results)
    evidence_dir = ROOT / "specs" / FEATURE_DIR / "live-evidence" / run_id
    evidence_dir.mkdir(parents=True, exist_ok=False)
    raw_ref = raw_path.relative_to(ROOT).as_posix()
    evidence: JsonObject = {
        "schema_version": 1,
        "kind": "medx_component_live_scenario_evidence",
        "run_id": run_id,
        "produced_at": utc_now(),
        "component": "p4-expanded-patient-intake-foundation",
        "base_url": config.base_url,
        "deployed_identity": identity,
        "auth": {"mode": "frappe_token", "role": "unobserved", "user": "unobserved", "credentials_recorded": False},
        "scenario_corpus": scenario_corpus(),
        "collection_context": {
            "started_at": started,
            "completed_at": utc_now(),
            "deployment": "local synthetic persistent Frappe QA",
            "transport": "HTTP through published Frappe REST and open_chart.api.v1 methods",
            "raw_evidence": {"path_or_uri": raw_ref, "sha256": hashlib.sha256(raw_path.read_bytes()).hexdigest()},
        },
        "assertions": results,
        "observations": observations,
        "verdict": "PASS" if passed else "FAIL",
        "failure": error,
        "evidence_provenance": "live_qa",
        "feeds_acceptance_report": False,
        "acceptance_identity_status": "unverified: a version-only probe does not attest deployed source revisions",
        "claim_boundary": "A PASS proves the named p4 scenario assertions on one local synthetic QA deployment over its real Frappe HTTP/API/DocType path. It is not clinical validation, production security/performance/availability evidence, or proof of production deployment posture.",
    }
    (evidence_dir / "evidence.yaml").write_text(json.dumps(evidence, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    print(f"{evidence['verdict']}: {evidence_dir.relative_to(ROOT) / 'evidence.yaml'}")
    return 0 if passed else 2


def self_test() -> int:
    payload = core.build_payload(ROOT)
    census = core.load_census(ROOT)
    rows = core.build_rows(payload, census)
    if core.content_hash(rows) != core.content_hash(copy.deepcopy(rows)):
        raise RunnerError("self_test", "content_hash is not deterministic")
    successor: JsonObject = core.load_yaml(ROOT / FIXTURES[-1])
    entries = require_list(require_object(require_object(successor["envelope"], "self_test")["content"], "self_test")["entries"], "self_test")
    if len(entries) != 2:
        raise RunnerError("self_test", "successor fixture must contain two entries")
    print("PASS: p4 offline self-test (no network)")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if args == ["--help"]:
        print(HELP)
        return 0
    if args == ["--self-test"]:
        return self_test()
    if args:
        print(HELP, file=sys.stderr)
        return 2
    config = Config.from_env()
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_id = f"p4-{stamp}-{os.getpid()}"
    return write_evidence(config, run_id, utc_now(), ROOT / "var" / "p4-live" / run_id / "http.jsonl")


if __name__ == "__main__":
    raise SystemExit(main())
