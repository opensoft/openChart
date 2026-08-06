"""OC Supplement Statement controller (FR-005: statement DocTypes preserve
the full reported detail census of the golden intake layer, including
formulation/product-or-ingredients detail plus route/timing/indication
capacity even where a golden fixture omits them -- unknown stays empty,
never inferred; FR-008: assertion_kind is always patient_reported and
read-only -- no prescription, order, administration, recommendation, or
autonomous action follows from this record)."""
try:
    import frappe
    from frappe.model.document import Document
except ImportError:  # bench-free repo validation
    Document = object


class OCSupplementStatement(Document):
    pass
