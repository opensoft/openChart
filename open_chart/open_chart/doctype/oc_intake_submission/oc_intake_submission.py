"""OC Intake Submission controller (brief D4: explicit lifecycle_state
drives draft/submitted/accepted/amended, not Frappe docstatus semantics;
amendments are new documents linked via predecessor. Brief D5: the
(patient, idempotency_key) uniqueness for accepted submissions is
enforced by the API layer, not a DB-level unique index on this field
alone)."""
try:
    import frappe
    from frappe.model.document import Document
except ImportError:  # bench-free repo validation
    Document = object


class OCIntakeSubmission(Document):
    pass
