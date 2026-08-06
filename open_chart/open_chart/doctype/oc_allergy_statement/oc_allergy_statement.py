"""OC Allergy Statement controller (FR-005: statement DocTypes preserve
the full reported detail census of the golden intake layer; unknown
optional values persist as explicitly unknown, never inferred; FR-008:
assertion_kind is always patient_reported and read-only -- no diagnosis,
order, recommendation, or autonomous action follows from this record)."""
try:
    import frappe
    from frappe.model.document import Document
except ImportError:  # bench-free repo validation
    Document = object


class OCAllergyStatement(Document):
    pass
