"""Pure intake logic (T009/T011; FR-002..FR-005, FR-009; brief D5, D9).

Everything here is bench-free: census-driven payload building, the
statement-row mapping and its inverse, the idempotency and identity
decisions, and the round-trip comparison. `api/v1.py` is a thin
frappe-bound shell over these functions; `scripts/validate.py` runs the
simulated round trip against the vendored golden fixtures on every
validate (OC-ROUNDTRIP-LOSS); the Docker-gated bench tests run the same
functions against real DocTypes.

Field semantics: a golden leaf absent from an entry stays ABSENT in the
row — explicitly unknown, never inferred (FR-005). The mapping itself
comes from contracts/intake-census.yaml as data; no field list in code.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

import yaml

#: open_chart/intake/core.py -> repo root (holds contracts/ and tests/).
REPO_ROOT = Path(__file__).resolve().parents[2]

CENSUS_PATH = "contracts/intake-census.yaml"

ASSERTION_KIND = "patient_reported"

FINDING_ROUNDTRIP = "OC-ROUNDTRIP-LOSS"

#: Idempotency decisions (D5). `diverged` is the refused shape: the same
#: (patient, idempotency_key) arriving with DIFFERENT content is a
#: client bug, never a silent overwrite.
DECISION_CREATE = "create"
DECISION_REPLAY = "replay"
DECISION_DIVERGED = "diverged"

#: Identity decisions (FR-002). Conflict never merges.
DECISION_REGISTER = "register"
DECISION_REVIEW = "identity_review"


def load_yaml(path: Path):
    with open(path) as handle:
        return yaml.safe_load(handle)


def load_census(root: Path | None = None) -> dict:
    return load_yaml((Path(root) if root else REPO_ROOT) / CENSUS_PATH)


def _get_dotted(entry: Mapping[str, Any], dotted: str):
    """Missing at any depth returns None — the explicit-unknown sentinel."""
    node: Any = entry
    for part in dotted.split("."):
        if not isinstance(node, Mapping) or part not in node:
            return None
        node = node[part]
    return node


def _set_dotted(target: dict, dotted: str, value) -> None:
    parts = dotted.split(".")
    node = target
    for part in parts[:-1]:
        node = node.setdefault(part, {})
    node[parts[-1]] = value


def build_payload(root: Path | None = None) -> dict:
    """The golden submission payload, derived from the vendored fixtures.

    One payload per census family that HAS a fixture; declared-only
    families are legally absent (edge case: the manifest says which
    families were submitted).
    """
    base = Path(root) if root else REPO_ROOT
    census = load_census(base)
    families: dict[str, Any] = {}
    contract_version = None
    for family in (census.get("census") or {}).get("families") or []:
        fixture = load_yaml(base / str(family.get("fixture")))
        envelope = fixture.get("envelope") or {}
        contract_version = str(fixture.get("bundle_version") or contract_version)
        families[str(family.get("record_family"))] = {
            "source_record_id": str(envelope.get("source_record_id")),
            "reported_at": str(envelope.get("reported_at")),
            "entries": (envelope.get("content") or {}).get("entries") or [],
        }
    return {"contract_version": str(contract_version), "families": families}


def family_maps(census: Mapping[str, Any]) -> dict[str, dict]:
    """record_family -> {doctype, golden->fieldname map} from the census."""
    maps: dict[str, dict] = {}
    for family in (census.get("census") or {}).get("families") or []:
        maps[str(family.get("record_family"))] = {
            "doctype": str(family.get("doctype")),
            "fields": {str(f.get("golden")): str(f.get("fieldname")) for f in family.get("fields") or []},
        }
    return maps


def build_rows(payload: Mapping[str, Any], census: Mapping[str, Any]) -> list[dict]:
    """Payload entries -> statement rows. Unknown census families refuse.

    Row shape: {"doctype", "record_family", "fields"}; fields carry only
    the leaves the entry actually reported, plus the constitutional
    assertion_kind (FR-008).
    """
    maps = family_maps(census)
    rows: list[dict] = []
    for family_name, body in (payload.get("families") or {}).items():
        if family_name not in maps:
            raise ValueError(f"unknown record_family {family_name!r}: not in the census")
        mapping = maps[family_name]
        for entry in body.get("entries") or []:
            fields: dict[str, Any] = {"assertion_kind": ASSERTION_KIND}
            for golden, fieldname in mapping["fields"].items():
                value = _get_dotted(entry, golden)
                if value is not None:
                    fields[fieldname] = value
            rows.append(
                {
                    "doctype": mapping["doctype"],
                    "record_family": family_name,
                    "fields": fields,
                }
            )
    return rows


def project_row(row: Mapping[str, Any], census: Mapping[str, Any]) -> dict:
    """The inverse mapping: a stored row projected back to golden leaves."""
    mapping = family_maps(census)[str(row.get("record_family"))]
    entry: dict[str, Any] = {}
    fields = row.get("fields") or {}
    for golden, fieldname in mapping["fields"].items():
        if fieldname in fields and fields[fieldname] is not None:
            _set_dotted(entry, golden, fields[fieldname])
    return entry


def _leaves(entry: Mapping[str, Any], prefix: str = "") -> dict[str, Any]:
    flat: dict[str, Any] = {}
    for key, value in entry.items():
        dotted = f"{prefix}.{key}" if prefix else str(key)
        if isinstance(value, Mapping):
            flat.update(_leaves(value, dotted))
        else:
            flat[dotted] = value
    return flat


def _equal(a, b) -> bool:
    """Field-for-field equality; numeric values compare by value (a Float
    field returns 20.0 for a stored 20 — that is representation, not loss)."""
    if a == b:
        return True
    try:
        return float(a) == float(b)
    except (TypeError, ValueError):
        return False


def roundtrip_loss(source_entries: list, projected_entries: list, family: str) -> list[str]:
    """Zero-loss comparison (FR-009). Loss in EITHER direction is a
    finding: a dropped source leaf is silent data loss; an extra
    projected leaf is fabrication — both are G2 failures."""
    findings: list[str] = []
    if len(source_entries) != len(projected_entries):
        return [
            f"{FINDING_ROUNDTRIP}: family {family!r} submitted {len(source_entries)} entries "
            f"but read back {len(projected_entries)}"
        ]
    for source, projected in zip(source_entries, projected_entries):
        src, out = _leaves(source), _leaves(projected)
        for leaf, value in src.items():
            if leaf not in out:
                findings.append(
                    f"{FINDING_ROUNDTRIP}: family {family!r} entry {source.get('entry_id')!r} "
                    f"lost {leaf!r} on the round trip"
                )
            elif not _equal(value, out[leaf]):
                findings.append(
                    f"{FINDING_ROUNDTRIP}: family {family!r} entry {source.get('entry_id')!r} "
                    f"field {leaf!r} submitted {value!r} but read back {out[leaf]!r}"
                )
        for leaf in out:
            if leaf not in src:
                findings.append(
                    f"{FINDING_ROUNDTRIP}: family {family!r} entry {source.get('entry_id')!r} "
                    f"read back fabricated field {leaf!r}"
                )
    return findings


def simulated_roundtrip_errors(root: Path | None = None) -> list[str]:
    """The bench-free half of FR-009: payload -> rows -> project -> compare.

    Exercises the SAME mapping functions the API uses; the live half
    (real DocTypes, real reads) is the Docker-gated bench test.
    """
    base = Path(root) if root else REPO_ROOT
    census = load_census(base)
    payload = build_payload(base)
    rows = build_rows(payload, census)
    findings: list[str] = []
    for family_name, body in (payload.get("families") or {}).items():
        projected = [project_row(r, census) for r in rows if r.get("record_family") == family_name]
        findings.extend(roundtrip_loss(body.get("entries") or [], projected, family_name))
    return findings


def content_hash(rows: list) -> str:
    """Canonical digest of the CLINICAL content of a submission's rows —
    what idempotency divergence is judged on. Execution metadata never
    participates (the bundle's equivalence discipline, applied here)."""
    canonical = [
        {"doctype": str(r.get("doctype")), "fields": r.get("fields") or {}}
        for r in sorted(rows, key=lambda r: (str(r.get("doctype")), str((r.get("fields") or {}).get("source_entry_id"))))
    ]
    return hashlib.sha256(json.dumps(canonical, sort_keys=True, default=str).encode()).hexdigest()


def idempotency_decision(
    existing: list, patient: str, idempotency_key: str, incoming_hash: str
) -> tuple[str, str | None]:
    """D5: uniqueness of (patient, idempotency_key) lives HERE, not in a
    DB constraint. `existing` rows carry patient/idempotency_key/
    content_hash/name for the patient's prior submissions."""
    for row in existing:
        if str(row.get("patient")) == patient and str(row.get("idempotency_key")) == idempotency_key:
            if str(row.get("content_hash")) == incoming_hash:
                return DECISION_REPLAY, str(row.get("name"))
            return DECISION_DIVERGED, str(row.get("name"))
    return DECISION_CREATE, None


def identity_decision(existing: list, patient: str, issuer_or_endpoint: str, value: str) -> str:
    """FR-002: an ACTIVE (issuer, value) pair on another patient means
    identity review — never a merge, never a silent second registration."""
    for row in existing:
        if (
            str(row.get("issuer_or_endpoint")) == issuer_or_endpoint
            and str(row.get("value")) == value
            and str(row.get("status")) == "active"
            and str(row.get("patient")) != patient
        ):
            return DECISION_REVIEW
    return DECISION_REGISTER


def successor_fields(prior: Mapping[str, Any], actor: str, reason: str, timestamp: str) -> dict:
    """D4 succession: the amendment is a NEW submission referencing its
    predecessor; the prior document is never edited in place and never
    Frappe-cancel-amended."""
    if not str(reason or "").strip():
        raise ValueError("an amendment requires a reason (FR-006)")
    return {
        "patient": str(prior.get("patient")),
        "contract_version": str(prior.get("contract_version")),
        "submission_version": int(prior.get("submission_version") or 1) + 1,
        "lifecycle_state": "accepted",
        "submitter_context": actor,
        "purpose_or_consent_ref": prior.get("purpose_or_consent_ref"),
        "submitted_time": timestamp,
        "provenance": f"amendment of {prior.get('name')}",
        "idempotency_key": f"{prior.get('idempotency_key')}::amend-{int(prior.get('submission_version') or 1) + 1}",
        "predecessor": str(prior.get("name")),
        "amendment_reason": reason,
    }
