"""Bench-dependent intake tests (T010/T011 live half; runs in docker/).

These execute inside the Docker-gated bench (`make validate-docker`) —
the same pure functions the repo validator exercises bench-free, here
driven through real DocTypes, the real permission model, and the real
guard flags. Every scenario is a spec scenario:

- golden round trip, zero loss (FR-009, SC-002)
- idempotent replay / divergent replay refused (FR-004, SC-003)
- succession amendment with auditable prior (FR-006, SC-003)
- direct table write rejected (FR-007; the D6 rejection test)
- identity conflict enters review, never merge (FR-002, SC-003)
- accepted submission immutable in place (FR-006)

All data is synthetic (SYN- discipline, FR-012).
"""

import copy
import json

import frappe
from frappe.tests.utils import FrappeTestCase

from open_chart.api import v1
from open_chart.intake import core

CONTEXT = {"submitter_context": "SYN-TENANT/SYN-OPERATOR-01", "purpose_or_consent_ref": "SYN-CONSENT-0001"}


def new_patient(suffix: str) -> str:
    doc = frappe.get_doc(
        {"doctype": "OC Patient", "patient_name": f"SYN-PATIENT-{suffix}"}
    ).insert(ignore_permissions=True)
    return doc.name


class TestIntakeAPI(FrappeTestCase):
    def setUp(self):
        self.patient = new_patient(frappe.generate_hash(length=6))
        self.payload = core.build_payload()

    def submit(self, key="SYN-IDEMPOTENCY-0001", payload=None):
        return v1.submit(
            patient=self.patient,
            contract_version=self.payload["contract_version"],
            idempotency_key=key,
            payload=json.dumps(payload or self.payload),
            **CONTEXT,
        )

    def test_golden_roundtrip_zero_loss(self):
        result = self.submit()
        census = core.load_census()
        findings = []
        for family, body in self.payload["families"].items():
            projected = [
                core.project_row(r, census) for r in result["rows"] if r["record_family"] == family
            ]
            findings.extend(core.roundtrip_loss(body["entries"], projected, family))
        self.assertEqual(findings, [], "golden round trip must lose nothing (FR-009)")

    def test_idempotent_replay_returns_existing(self):
        first = self.submit()
        before = frappe.db.count("OC Intake Submission", {"patient": self.patient})
        replay = self.submit()
        self.assertEqual(first["submission"]["name"], replay["submission"]["name"])
        self.assertEqual(
            before, frappe.db.count("OC Intake Submission", {"patient": self.patient})
        )

    def test_divergent_replay_refused(self):
        self.submit()
        diverged = copy.deepcopy(self.payload)
        diverged["families"]["medication"]["entries"][0]["dose_amount"] = 40
        with self.assertRaises(frappe.ValidationError):
            self.submit(payload=diverged)

    def test_amend_creates_successor(self):
        first = self.submit()
        amended_payload = copy.deepcopy(self.payload)
        amended_payload["families"]["medication"]["entries"][0]["dose_amount"] = 10
        successor = v1.amend(
            first["submission"]["name"],
            json.dumps(amended_payload),
            reason="SYN dose corrected by patient",
            submitter_context=CONTEXT["submitter_context"],
        )
        self.assertEqual(successor["submission"]["predecessor"], first["submission"]["name"])
        self.assertEqual(successor["submission"]["submission_version"], 2)
        prior = v1.read_submission(first["submission"]["name"])
        self.assertEqual(prior["submission"]["lifecycle_state"], "amended")
        self.assertTrue(prior["rows"], "prior accepted content stays auditable (FR-006)")

    def test_direct_table_write_rejected(self):
        with self.assertRaises(frappe.ValidationError):
            frappe.get_doc(
                {
                    "doctype": "OC Medication Statement",
                    "patient": self.patient,
                    "submission": "SYN-NOT-A-SUBMISSION",
                    "source_entry_id": "SYN-DIRECT-WRITE",
                    "reported_text": "written straight to the table",
                }
            ).insert()

    def test_identity_conflict_enters_review(self):
        other = new_patient(frappe.generate_hash(length=6))
        first = v1.register_external_identifier(
            self.patient, "SYN-ISSUER", "openchart", "SYN-EXT-0001"
        )
        self.assertEqual(first["status"], "active")
        second = v1.register_external_identifier(
            other, "SYN-ISSUER", "openchart", "SYN-EXT-0001"
        )
        self.assertEqual(second["status"], "identity_review", "never a merge (FR-002)")

    def test_accepted_submission_immutable(self):
        first = self.submit()
        doc = frappe.get_doc("OC Intake Submission", first["submission"]["name"])
        doc.submitter_context = "SYN-TAMPER"
        frappe.flags.oc_api_write = True
        try:
            with self.assertRaises(frappe.ValidationError):
                doc.save()
        finally:
            frappe.flags.oc_api_write = False
