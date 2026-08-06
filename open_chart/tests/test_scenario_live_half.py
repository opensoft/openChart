"""The p4 scenario live half (scenario s1 follow-up; runs in docker/).

Named by scenario report SYN-SCENARIO-REPORT-0001's claim boundary:
the golden patient's UPDATED supplement submission (melatonin added,
prior entry verbatim, source_record_version 2) driven through the LIVE
open_chart.api.v1 on a real site — submit the baseline, amend with the
updated list, read back with zero loss and auditable succession.

Additive consumption of the published scenario corpus: no API change,
no version change, no declaration change.
"""

import copy
import json

import frappe
from frappe.tests.utils import FrappeTestCase

from open_chart.api import v1
from open_chart.intake import core

CONTEXT = {"submitter_context": "SYN-TENANT/SYN-OPERATOR-01", "purpose_or_consent_ref": "SYN-CONSENT-0001"}

SCENARIO_FIXTURE = "tests/fixtures/medx/scenario-intake-supplements-successor.yaml"


def successor_entries():
    doc = core.load_yaml(core.REPO_ROOT / SCENARIO_FIXTURE)
    return (doc.get("envelope") or {}).get("content", {}).get("entries") or []


class TestScenarioLiveHalf(FrappeTestCase):
    def setUp(self):
        self.patient = frappe.get_doc(
            {"doctype": "OC Patient", "patient_name": f"SYN-S1-PATIENT-{frappe.generate_hash(length=6)}"}
        ).insert(ignore_permissions=True).name
        self.payload = core.build_payload()

    def test_updated_supplement_submission_live(self):
        first = v1.submit(
            patient=self.patient,
            contract_version=self.payload["contract_version"],
            idempotency_key=f"SYN-S1-{frappe.generate_hash(length=8)}",
            payload=json.dumps(self.payload),
            **CONTEXT,
        )
        updated = copy.deepcopy(self.payload)
        entries = successor_entries()
        self.assertEqual(len(entries), 2, "the updated list carries the prior entry plus melatonin")
        self.assertEqual(
            entries[0],
            self.payload["families"]["supplement"]["entries"][0],
            "the prior reported entry is verbatim in the updated submission",
        )
        updated["families"]["supplement"]["entries"] = entries
        successor = v1.amend(
            first["submission"]["name"],
            json.dumps(updated),
            reason="SYN updated supplement list: melatonin added (scenario s1)",
            submitter_context=CONTEXT["submitter_context"],
        )
        self.assertEqual(successor["submission"]["predecessor"], first["submission"]["name"])
        census = core.load_census()
        findings = []
        for family, body in updated["families"].items():
            projected = [
                core.project_row(r, census) for r in successor["rows"] if r["record_family"] == family
            ]
            findings.extend(core.roundtrip_loss(body["entries"], projected, family))
        self.assertEqual(findings, [], "the updated submission must read back with zero loss (live)")
        prior = v1.read_submission(first["submission"]["name"])
        self.assertEqual(prior["submission"]["lifecycle_state"], "amended")
        self.assertTrue(prior["rows"], "prior accepted content stays auditable")
        melatonin = [
            r for r in successor["rows"]
            if r["record_family"] == "supplement" and r["fields"].get("source_entry_id") == "SYN-INTAKE-SUPLINE-0002"
        ]
        self.assertEqual(len(melatonin), 1, "the added supplement is stored exactly once")
        self.assertEqual(melatonin[0]["fields"].get("assertion_kind"), "patient_reported")
