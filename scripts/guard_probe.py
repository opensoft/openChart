#!/usr/bin/env python3
"""Frappe-stub guard probe (T013; FR-006, FR-007; brief D6).

The controller guards and API refusals only execute with frappe
importable — which would leave their finding codes unfired in the
bench-free harness. This probe installs a MINIMAL frappe stub (flags,
throw, the module skeleton), imports the real guard and API modules
against it, and watches each refusal fire:

- OC-DIRECT-WRITE      (write without the API flag)
- OC-ACCEPTED-IMMUTABLE (in-place edit of an accepted submission)
- OC-CONTEXT-REQUIRED   (missing submitter/purpose context)
- OC-IDEMPOTENCY-DIVERGED (same key, different content)

Each arm also proves the LEGAL path passes under the same stub, so the
guard is shown to discriminate, not merely to throw. Run as a
subprocess by scripts/harness.py; prints one ``FIRED <code>`` line per
observed refusal. Exit 0 clean, 2 on any probe failure.
"""

from __future__ import annotations

import sys
import types
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]


class StubThrow(Exception):
    pass


def install_stub() -> types.ModuleType:
    frappe = types.ModuleType("frappe")
    frappe.flags = SimpleNamespace()
    frappe.fired = []

    def _throw(message, *args, **kwargs):
        frappe.fired.append(str(message))
        raise StubThrow(str(message))

    frappe.throw = _throw
    frappe.msgprint = lambda *a, **k: None
    frappe.get_all = lambda *a, **k: []
    frappe.only_for = lambda *a, **k: None
    frappe.session = SimpleNamespace(user="SYN-STUB-USER")
    frappe.utils = SimpleNamespace(now_datetime=lambda: "2026-08-05T00:00:00Z")
    frappe.whitelist = lambda *a, **k: (lambda func: func)
    frappe.publish_realtime = lambda *a, **k: None

    model = types.ModuleType("frappe.model")
    document = types.ModuleType("frappe.model.document")

    class Document:  # the stub base the guards extend
        pass

    document.Document = Document
    model.document = document
    frappe.model = model
    sys.modules["frappe"] = frappe
    sys.modules["frappe.model"] = model
    sys.modules["frappe.model.document"] = document
    return frappe


def main() -> int:
    frappe = install_stub()
    sys.path.insert(0, str(ROOT))
    from open_chart.api import v1  # noqa: E402 — must import AFTER the stub
    from open_chart.intake import core, guarded  # noqa: E402

    failures: list[str] = []

    def expect_fire(label: str, code: str, arm) -> None:
        before = len(frappe.fired)
        try:
            arm()
            failures.append(f"{label}: no refusal fired (expected {code})")
            return
        except StubThrow:
            pass
        message = frappe.fired[before] if len(frappe.fired) > before else ""
        if code in message:
            print(f"FIRED {code}")
        else:
            failures.append(f"{label}: fired {message!r}, expected {code}")

    def expect_pass(label: str, arm) -> None:
        try:
            arm()
        except StubThrow as exc:
            failures.append(f"{label}: legal path refused: {exc}")

    # -- OC-DIRECT-WRITE ------------------------------------------------
    doc = guarded.GuardedDocument()
    doc.doctype = "OC Medication Statement"
    frappe.flags = SimpleNamespace()
    expect_fire("direct write", "OC-DIRECT-WRITE", doc.validate)
    frappe.flags = SimpleNamespace(oc_api_write=True)
    expect_pass("API-flagged write", doc.validate)

    # -- OC-ACCEPTED-IMMUTABLE -------------------------------------------
    class ProbeSubmission(guarded.GuardedSubmission):
        def __init__(self, before_fields, current_fields):
            self._before = before_fields
            self._current = dict(current_fields)
            self.doctype = "OC Intake Submission"
            self.name = "SYN-SUB-PROBE"
            self.lifecycle_state = self._current["lifecycle_state"]

        def is_new(self):
            return False

        def get_doc_before_save(self):
            before = dict(self._before)
            return SimpleNamespace(lifecycle_state=before["lifecycle_state"], get=before.get)

        @property
        def meta(self):
            return SimpleNamespace(
                fields=[SimpleNamespace(fieldname=k, fieldtype="Data") for k in self._current]
            )

        def get(self, key):
            return self._current.get(key)

    accepted = {"lifecycle_state": "accepted", "submitter_context": "SYN-OK"}
    frappe.flags = SimpleNamespace(oc_api_write=True)
    tampered = ProbeSubmission(accepted, {**accepted, "submitter_context": "SYN-TAMPER"})
    expect_fire("accepted tamper", "OC-ACCEPTED-IMMUTABLE", tampered.validate)

    transition = ProbeSubmission(accepted, {**accepted, "lifecycle_state": "amended"})
    frappe.flags = SimpleNamespace(oc_api_write=True, oc_api_amend=True)
    expect_pass("accepted -> amended under amend flag", transition.validate)
    frappe.flags = SimpleNamespace(oc_api_write=True)
    tamper2 = ProbeSubmission(accepted, {**accepted, "lifecycle_state": "amended"})
    expect_fire("amend transition without amend flag", "OC-ACCEPTED-IMMUTABLE", tamper2.validate)

    # -- OC-CONTEXT-REQUIRED ----------------------------------------------
    expect_fire("empty context", "OC-CONTEXT-REQUIRED", lambda: v1._require_context("", ""))
    expect_fire(
        "purpose missing", "OC-CONTEXT-REQUIRED", lambda: v1._require_context("SYN-CTX", " ")
    )
    expect_pass("full context", lambda: v1._require_context("SYN-CTX", "SYN-CONSENT"))

    # -- OC-IDEMPOTENCY-DIVERGED -------------------------------------------
    payload = core.build_payload()
    v1._existing_submissions = lambda patient: [
        {
            "patient": "SYN-PAT-PROBE",
            "idempotency_key": "SYN-KEY-PROBE",
            "content_hash": "0" * 64,  # cannot equal any real content hash
            "name": "SYN-SUB-1",
        }
    ]
    expect_fire(
        "divergent replay",
        "OC-IDEMPOTENCY-DIVERGED",
        lambda: v1.submit(
            patient="SYN-PAT-PROBE",
            contract_version=payload["contract_version"],
            idempotency_key="SYN-KEY-PROBE",
            payload=payload,
            submitter_context="SYN-CTX",
            purpose_or_consent_ref="SYN-CONSENT",
        ),
    )

    if failures:
        for failure in failures:
            print(f"GUARD-PROBE FAIL: {failure}")
        return 2
    print("GUARD-PROBE OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
