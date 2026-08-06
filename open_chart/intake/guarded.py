"""Controller guards (T010; FR-006, FR-007; brief D4, D6).

The supported surface is `open_chart.api.v1` — these base classes make
every other write path fail loudly:

- ``GuardedDocument``: a write without the API flag is OC-DIRECT-WRITE
  (the D6 seam an extension cannot cross with a table write).
- ``GuardedSubmission``: accepted content is immutable; the ONLY legal
  change to an accepted submission is lifecycle_state -> amended, and
  only under the amend flag (succession, never in-place edit).
- ``GuardedIdentifier``: an active (issuer, value) pair on another
  patient forces identity_review — the decision itself is the pure
  ``core.identity_decision`` (never a merge, FR-002).

Bench-free imports stay legal: without frappe these classes are inert
(`Document = object`), so the repo validator and the simulated round
trip can import the package.
"""

from __future__ import annotations

try:
    import frappe
    from frappe.model.document import Document
except ImportError:  # bench-free repo validation
    frappe = None
    Document = object

from open_chart.intake import core

#: Set by api/v1.py around its own writes; never set anywhere else.
API_WRITE_FLAG = "oc_api_write"
#: Set by api/v1.py only around the accepted -> amended transition.
API_AMEND_FLAG = "oc_api_amend"

FINDING_DIRECT_WRITE = "OC-DIRECT-WRITE"
FINDING_ACCEPTED_IMMUTABLE = "OC-ACCEPTED-IMMUTABLE"


def _in_framework_context() -> bool:
    """Install/migrate machinery may touch documents; extensions may not."""
    flags = frappe.flags
    return bool(getattr(flags, "in_install", False) or getattr(flags, "in_migrate", False) or getattr(flags, "in_patch", False))


class GuardedDocument(Document):
    def validate(self):
        if frappe is None or _in_framework_context():
            return
        if not getattr(frappe.flags, API_WRITE_FLAG, False):
            frappe.throw(
                f"{FINDING_DIRECT_WRITE}: {self.doctype} is written only through "
                "open_chart.api.v1 (FR-007); direct table writes are rejected"
            )

    def on_trash(self):
        if frappe is None or _in_framework_context():
            return
        if not getattr(frappe.flags, API_WRITE_FLAG, False):
            frappe.throw(
                f"{FINDING_DIRECT_WRITE}: {self.doctype} deletion outside "
                "open_chart.api.v1 is rejected (FR-006 auditability)"
            )


class GuardedSubmission(GuardedDocument):
    def validate(self):
        super().validate()
        if frappe is None or self.is_new():
            return
        before = self.get_doc_before_save()
        if before is None or before.lifecycle_state != "accepted":
            return
        changed = {
            field.fieldname
            for field in self.meta.fields
            if field.fieldtype not in ("Section Break", "Column Break", "Tab Break")
            and self.get(field.fieldname) != before.get(field.fieldname)
        }
        if changed == {"lifecycle_state"} and self.lifecycle_state == "amended" and getattr(
            frappe.flags, API_AMEND_FLAG, False
        ):
            return
        if changed:
            frappe.throw(
                f"{FINDING_ACCEPTED_IMMUTABLE}: accepted submission {self.name} is immutable; "
                f"changed {sorted(changed)} — amendments create a successor (FR-006)"
            )


class GuardedIdentifier(GuardedDocument):
    def validate(self):
        super().validate()
        if frappe is None:
            return
        existing = frappe.get_all(
            "OC Patient External Identifier",
            filters={"name": ("!=", self.name)},
            fields=["patient", "issuer_or_endpoint", "value", "status"],
        )
        decision = core.identity_decision(
            existing, str(self.patient), str(self.issuer_or_endpoint), str(self.value)
        )
        if decision == core.DECISION_REVIEW and self.status != "identity_review":
            self.status = "identity_review"
            frappe.msgprint(
                f"external identifier ({self.issuer_or_endpoint}, {self.value}) is active on "
                "another patient; this registration enters identity review (FR-002 — never a merge)"
            )
