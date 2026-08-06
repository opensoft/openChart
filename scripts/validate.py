#!/usr/bin/env python3
"""openChart repository validator (feature 001; brief D7, D8, D9).

Bench-free: everything here reads repo content — DocType JSON, vendored
fixtures, the pin record, the census — and never imports frappe.
Bench-dependent checks (site install, migrations, the live golden round
trip) run inside docker/compose.yaml and are GATED: absent Docker, a
loud banner names exactly what was not proven. A silent skip is
forbidden (the MedxFactory program's D9 pattern, inherited).

Exit codes: 0 clean, 1 environment/usage error, 2 findings.
Finding codes (OC-*): every code must fire from a fixture or a probe —
the unfired audit holds this file to it.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    print(f"ERROR: PyYAML is required: {exc}", file=sys.stderr)
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from open_chart.intake import core as intake_core  # noqa: E402

PIN_PATH = Path("contracts/medx-pin.yaml")
CENSUS_PATH = Path("contracts/intake-census.yaml")
DOCTYPE_ROOT = Path("open_chart/open_chart/doctype")
FIXTURE_ROOT = Path("tests/fixtures")
FAILURE_ROOT = FIXTURE_ROOT / "failure"

FINDING_PIN_DRIFT = "OC-PIN-DRIFT"
FINDING_CENSUS_GAP = "OC-CENSUS-GAP"
FINDING_DOCTYPE_SHAPE = "OC-DOCTYPE-SHAPE"
FINDING_ROUNDTRIP_LOSS = "OC-ROUNDTRIP-LOSS"
FINDING_FIXTURE_SAFETY = "OC-FIXTURE-SAFETY"

RESULT_CLASSES = (
    "pin_drift",
    "census_gap",
    "doctype_shape",
    "roundtrip_loss",
    "identity_conflict",
    "idempotency_divergence",
)

#: Negative-corpus ratchet; T013 sets the final value.
NEGATIVE_RATCHET = 0


def finding(rel, message: str) -> str:
    return f"{rel}: {message}"


def load_yaml(path: Path):
    with open(path) as handle:
        return yaml.safe_load(handle)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def docker_gate() -> tuple[bool, str]:
    """Never a silent skip: both branches say what the gate did NOT prove."""
    if shutil.which("docker"):
        return True, (
            "NOTE bench-dependent checks are Docker-gated and did not run in\n"
            "  this invocation: run `make validate-docker` for site install,\n"
            "  migrations, and the live golden intake round trip."
        )
    return False, (
        "==================================================================\n"
        "SKIP bench-dependent checks — docker is not available.\n"
        "  NOT PROVEN on this machine: site install, migrations, and the\n"
        "  live golden intake round trip. Repo-content checks all ran.\n"
        "=================================================================="
    )


def pin_drift_errors(root: Path) -> list[str]:
    """Every vendored digest re-verified against the pin record (D8)."""
    pin = load_yaml(root / PIN_PATH)
    errors: list[str] = []
    for row in (pin.get("pin") or {}).get("vendored") or []:
        rel = str(row.get("vendored_path"))
        target = root / rel
        if not target.is_file():
            errors.append(finding(PIN_PATH, f"{FINDING_PIN_DRIFT}: vendored file {rel!r} is missing"))
        elif sha256_file(target) != str(row.get("sha256")):
            errors.append(
                finding(
                    PIN_PATH,
                    f"{FINDING_PIN_DRIFT}: {rel!r} pinned at {str(row.get('sha256'))[:12]}… but "
                    f"holds {sha256_file(target)[:12]}…; re-vendor deliberately, never hand-edit",
                )
            )
    return errors


def _doctype_json(root: Path, doctype: str) -> dict | None:
    slug = doctype.lower().replace(" ", "_")
    path = root / DOCTYPE_ROOT / slug / f"{slug}.json"
    if not path.is_file():
        return None
    return json.loads(path.read_text())


def _entry_leaves(entry, prefix: str = "") -> set[str]:
    leaves: set[str] = set()
    if isinstance(entry, dict):
        for key, value in entry.items():
            dotted = f"{prefix}.{key}" if prefix else str(key)
            if isinstance(value, dict):
                leaves |= _entry_leaves(value, dotted)
            else:
                leaves.add(dotted)
    return leaves


def census_errors(root: Path) -> list[str]:
    """Every golden field mapped (D9), every mapped field present (shape)."""
    census = load_yaml(root / CENSUS_PATH)
    body = census.get("census") or {}
    errors: list[str] = []
    for family in body.get("families") or []:
        doctype = str(family.get("doctype"))
        mapped = {str(f.get("golden")) for f in family.get("fields") or []}
        fixture = load_yaml(root / str(family.get("fixture")))
        for entry in ((fixture.get("envelope") or {}).get("content") or {}).get("entries") or []:
            for leaf in _entry_leaves(entry):
                if leaf not in mapped:
                    errors.append(
                        finding(
                            CENSUS_PATH,
                            f"{FINDING_CENSUS_GAP}: golden field {leaf!r} of family "
                            f"{family.get('record_family')!r} has no census mapping; an unmapped "
                            "field is intake content the app would silently drop (G2)",
                        )
                    )
        doc = _doctype_json(root, doctype)
        if doc is None:
            errors.append(finding(CENSUS_PATH, f"{FINDING_DOCTYPE_SHAPE}: census names {doctype!r} but no DocType JSON exists"))
            continue
        fieldnames = {str(f.get("fieldname")) for f in doc.get("fields") or []}
        for row in family.get("fields") or []:
            if str(row.get("fieldname")) not in fieldnames:
                errors.append(
                    finding(
                        CENSUS_PATH,
                        f"{FINDING_DOCTYPE_SHAPE}: census maps {row.get('golden')!r} to "
                        f"{doctype}.{row.get('fieldname')} but the DocType lacks that field",
                    )
                )
    for family in body.get("declared_only_families") or []:
        if _doctype_json(root, str(family.get("doctype"))) is None:
            errors.append(
                finding(CENSUS_PATH, f"{FINDING_DOCTYPE_SHAPE}: declared family {family.get('record_family')!r} has no DocType JSON")
            )
    return errors


def doctype_shape_errors(root: Path) -> list[str]:
    """Structural rules every OC DocType observes (brief D1, D3, D4)."""
    census = load_yaml(root / CENSUS_PATH)
    common = [str(f) for f in ((census.get("census") or {}).get("common_fields") or [])]
    statement_doctypes = {
        str(f.get("doctype"))
        for key in ("families", "declared_only_families")
        for f in ((census.get("census") or {}).get(key) or [])
    }
    errors: list[str] = []
    base = root / DOCTYPE_ROOT
    if not base.is_dir():
        return [finding(DOCTYPE_ROOT, f"{FINDING_DOCTYPE_SHAPE}: no doctype directory")]
    for slug_dir in sorted(p for p in base.iterdir() if p.is_dir() and not p.name.startswith("__")):
        path = slug_dir / f"{slug_dir.name}.json"
        rel = path.relative_to(root)
        if not path.is_file():
            errors.append(finding(rel, f"{FINDING_DOCTYPE_SHAPE}: doctype dir without its JSON"))
            continue
        try:
            doc = json.loads(path.read_text())
        except json.JSONDecodeError as exc:
            errors.append(finding(rel, f"{FINDING_DOCTYPE_SHAPE}: invalid JSON: {exc}"))
            continue
        name = str(doc.get("name"))
        if not name.startswith("OC "):
            errors.append(finding(rel, f"{FINDING_DOCTYPE_SHAPE}: DocType {name!r} must be OC-prefixed"))
        if doc.get("module") != "Open Chart":
            errors.append(finding(rel, f"{FINDING_DOCTYPE_SHAPE}: module must be 'Open Chart'"))
        fieldnames = {str(f.get("fieldname")) for f in doc.get("fields") or []}
        if name in statement_doctypes:
            for required in common:
                if required not in fieldnames:
                    errors.append(
                        finding(
                            rel,
                            f"{FINDING_DOCTYPE_SHAPE}: statement DocType lacks common spine field "
                            f"{required!r} (census common_fields)",
                        )
                    )
            kinds = [f for f in doc.get("fields") or [] if f.get("fieldname") == "assertion_kind"]
            if kinds and str(kinds[0].get("default")) != "patient_reported":
                errors.append(
                    finding(rel, f"{FINDING_DOCTYPE_SHAPE}: assertion_kind must default to patient_reported (FR-008)")
                )
    return errors


def fixture_safety_errors(root: Path) -> list[str]:
    """SYN- discipline and no key material in fixtures."""
    errors: list[str] = []
    for path in sorted((root / FIXTURE_ROOT).rglob("*.yaml")):
        rel = path.relative_to(root)
        text = path.read_text(errors="ignore")
        if "BEGIN PRIVATE KEY" in text or "AGE-SECRET-KEY-1" in text:
            errors.append(finding(rel, f"{FINDING_FIXTURE_SAFETY}: key material in a fixture"))
        doc = None
        try:
            doc = yaml.safe_load(text.split("# VENDORED", 1)[-1]) if text.startswith("#") else yaml.safe_load(text)
        except Exception:  # noqa: BLE001
            continue
        if isinstance(doc, dict) and doc.get("synthetic") is not True and "failure" not in str(rel):
            errors.append(finding(rel, f"{FINDING_FIXTURE_SAFETY}: fixture must declare synthetic: true"))
    return errors


def roundtrip_errors(root: Path) -> list[str]:
    """The bench-free half of FR-009 (T011): golden payload -> statement
    rows -> projection back -> field-for-field comparison. The live half
    (real DocTypes) is the Docker-gated bench suite."""
    return intake_core.simulated_roundtrip_errors(root)


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    errors.extend(pin_drift_errors(root))      # T003
    errors.extend(census_errors(root))         # T004
    errors.extend(doctype_shape_errors(root))  # T008
    errors.extend(roundtrip_errors(root))      # T011
    errors.extend(fixture_safety_errors(root))
    return errors


def main() -> int:
    errors = validate(ROOT)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 2
    _, banner = docker_gate()
    print(banner, file=sys.stderr)
    print("OK openChart repository checks clean", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
