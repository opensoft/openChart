#!/usr/bin/env python3
"""The check harness (T013; SC-006). Collect-then-report; exit 0/2.

Arms, in order:

1. POSITIVE — validate() green on the real tree, and green on an
   un-overlaid temp copy (proving the copy machinery itself).
2. NEGATIVE CORPUS — every fixture under tests/fixtures/failure/ fires
   its declared finding/decision; the ratchet holds the corpus at
   exactly NEGATIVE_RATCHET fixtures covering exactly RESULT_CLASSES.
3. NEUTRALIZATION PROBES — each validate-arm checker is monkeypatched
   to silence and the finding must DISAPPEAR: proof the arm watches
   that checker, not an accident of another one. Decision arms are
   probed for input sensitivity (flip the discriminating input, the
   decision must flip).
4. PLANTED SAFETY — key material and a missing synthetic marker planted
   in a temp tree must fire OC-FIXTURE-SAFETY.
5. GUARD PROBE — scripts/guard_probe.py under a frappe stub fires the
   bench-side refusal codes (subprocess; see its docstring).
6. UNFIRED AUDIT — every OC-* code literal in executable Python under
   scripts/ and open_chart/ must have been observed firing by arms 1-5.
   (docker/run-checks.sh's step/result lines are shell, not Python, and
   are exercised by the Docker gate itself.)
"""

from __future__ import annotations

import ast
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

import validate as validate_mod  # noqa: E402
from open_chart.intake import core  # noqa: E402

FAILURE_DIR = ROOT / "tests/fixtures/failure"

FINDING_RATCHET = "OC-NEGATIVE-RATCHET"

#: failure class -> the checker its finding must come from (arm 3).
CLASS_CHECKER = {
    "pin_drift": "pin_drift_errors",
    "census_gap": "census_errors",
    "doctype_shape": "doctype_shape_errors",
    "roundtrip_loss": "roundtrip_errors",
}

#: What validate(root) actually reads — the temp-copy footprint.
TREE_PARTS = ("contracts", "open_chart", "tests")

CODE_PATTERN = re.compile(r"^OC-[A-Z][A-Z-]+[A-Z]$")


def copy_tree(target: Path) -> Path:
    for part in TREE_PARTS:
        shutil.copytree(ROOT / part, target / part)
    return target


def apply_overlay(root: Path, overlay: list) -> None:
    for item in overlay or []:
        target = root / str(item.get("path"))
        if "content" in item:
            target.write_text(str(item["content"]))
        elif "append" in item:
            target.write_text(target.read_text() + str(item["append"]))
        else:
            raise ValueError(f"overlay item for {item.get('path')!r} has neither content nor append")


def ratchet_errors(corpus: list[dict]) -> list[str]:
    """Exactly NEGATIVE_RATCHET fixtures, exactly RESULT_CLASSES covered."""
    errors: list[str] = []
    if len(corpus) != validate_mod.NEGATIVE_RATCHET:
        errors.append(
            f"{FINDING_RATCHET}: corpus holds {len(corpus)} fixtures, ratchet demands "
            f"{validate_mod.NEGATIVE_RATCHET}; the corpus only grows deliberately"
        )
    seen = {str(f.get("class")) for f in corpus}
    declared = set(validate_mod.RESULT_CLASSES)
    for missing in sorted(declared - seen):
        errors.append(f"{FINDING_RATCHET}: declared class {missing!r} has no fixture")
    for extra in sorted(seen - declared):
        errors.append(f"{FINDING_RATCHET}: fixture class {extra!r} is not declared in RESULT_CLASSES")
    return errors


def decision_arm(fixture: dict) -> str:
    inputs = fixture.get("inputs") or {}
    if fixture.get("arm") == "identity_decision":
        return core.identity_decision(
            inputs.get("existing") or [],
            str(inputs.get("patient")),
            str(inputs.get("issuer_or_endpoint")),
            str(inputs.get("value")),
        )
    decision, _ = core.idempotency_decision(
        inputs.get("existing") or [],
        str(inputs.get("patient")),
        str(inputs.get("idempotency_key")),
        str(inputs.get("incoming_hash")),
    )
    return decision


def executable_code_universe() -> set[str]:
    universe: set[str] = set()
    for base in (ROOT / "scripts", ROOT / "open_chart"):
        for path in sorted(base.rglob("*.py")):
            tree = ast.parse(path.read_text())
            for node in ast.walk(tree):
                if isinstance(node, ast.Constant) and isinstance(node.value, str):
                    for token in re.findall(r"OC-[A-Z][A-Z-]*[A-Z]", node.value):
                        if CODE_PATTERN.match(token):
                            universe.add(token)
    return universe


def main() -> int:  # noqa: PLR0915 — one linear battery, reported at the end
    failures: list[str] = []
    fired: set[str] = set()

    def observe(findings: list[str]) -> list[str]:
        for finding in findings:
            for token in re.findall(r"OC-[A-Z][A-Z-]*[A-Z]", finding):
                fired.add(token)
        return findings

    # -- arm 1: positive ---------------------------------------------------
    clean = observe(validate_mod.validate(ROOT))
    if clean:
        failures.extend(f"positive arm: real tree not green: {f}" for f in clean)
    with tempfile.TemporaryDirectory(prefix="oc-harness-") as tmp:
        copied = copy_tree(Path(tmp) / "clean")
        residue = observe(validate_mod.validate(copied))
        if residue:
            failures.extend(f"positive arm: temp copy not green: {f}" for f in residue)

    # -- arm 2 + 3: negative corpus with neutralization probes -------------
    corpus = [core.load_yaml(p) for p in sorted(FAILURE_DIR.glob("*.yaml"))]
    ratchet = ratchet_errors(corpus)
    if ratchet:
        failures.extend(ratchet)
    probe = ratchet_errors(corpus[:-1]) if corpus else []
    if not any(FINDING_RATCHET in f for f in probe):
        failures.append("ratchet self-probe: removing a fixture did not fire the ratchet")
    else:
        observe(probe)

    for fixture in corpus:
        klass, arm, expect = (str(fixture.get(k)) for k in ("class", "arm", "expect"))
        label = f"negative[{klass}]"
        if arm == "validate":
            with tempfile.TemporaryDirectory(prefix="oc-harness-") as tmp:
                mutated = copy_tree(Path(tmp) / "mutated")
                apply_overlay(mutated, fixture.get("overlay"))
                findings = observe(validate_mod.validate(mutated))
                if not any(expect in f for f in findings):
                    failures.append(f"{label}: expected {expect} did not fire")
                checker = CLASS_CHECKER[klass]
                original = getattr(validate_mod, checker)
                setattr(validate_mod, checker, lambda root: [])
                try:
                    silenced = validate_mod.validate(mutated)
                finally:
                    setattr(validate_mod, checker, original)
                if any(expect in f for f in silenced):
                    failures.append(
                        f"{label}: {expect} still fired with {checker} neutralized — "
                        "the finding is not coming from the checker this arm watches"
                    )
        else:
            decision = decision_arm(fixture)
            if decision != expect:
                failures.append(f"{label}: decision {decision!r}, expected {expect!r}")
            # input-sensitivity probe: flip the discriminating input.
            flipped = {**fixture, "inputs": dict(fixture.get("inputs") or {})}
            if arm == "identity_decision":
                flipped["inputs"]["patient"] = str(
                    (flipped["inputs"].get("existing") or [{}])[0].get("patient")
                )
            else:
                flipped["inputs"]["incoming_hash"] = str(
                    (flipped["inputs"].get("existing") or [{}])[0].get("content_hash")
                )
            if decision_arm(flipped) == expect:
                failures.append(f"{label}: decision is input-insensitive (probe)")

    # -- arm 4: planted safety ---------------------------------------------
    with tempfile.TemporaryDirectory(prefix="oc-harness-") as tmp:
        planted = copy_tree(Path(tmp) / "planted")
        secret = "AGE-SECRET-KEY-1" + "SYNPROBE" * 2  # assembled, never committed whole
        (planted / "tests/fixtures/medx/planted-key.yaml").write_text(
            f"synthetic: true\nnote: {secret}\n"
        )
        (planted / "tests/fixtures/medx/no-synthetic-marker.yaml").write_text("kind: SYN-thing\n")
        findings = observe(validate_mod.fixture_safety_errors(planted))
        if not any("key material" in f for f in findings):
            failures.append("planted key material did not fire OC-FIXTURE-SAFETY")
        if not any("synthetic: true" in f for f in findings):
            failures.append("missing synthetic marker did not fire OC-FIXTURE-SAFETY")

    # -- arm 5: guard probe (frappe stub, subprocess) ------------------------
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts/guard_probe.py")],
        capture_output=True,
        text=True,
        check=False,
    )
    for line in completed.stdout.splitlines():
        if line.startswith("FIRED "):
            fired.add(line.split(" ", 1)[1].strip())
    if completed.returncode != 0:
        failures.append(
            f"guard probe exited {completed.returncode}:\n{completed.stdout}\n{completed.stderr}"
        )

    # -- arm 6: unfired audit -------------------------------------------------
    for code in sorted(executable_code_universe() - fired):
        failures.append(f"unfired audit: {code} is defined in executable source but never fired")

    if failures:
        for failure in failures:
            print(f"HARNESS FAIL: {failure}")
        return 2
    print(
        f"OK harness: positive green, {len(corpus)} negative fixtures fired with "
        f"neutralization probes, planted safety fired, guard probe fired, "
        f"{len(executable_code_universe())} OC- codes all observed firing"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
