"""OC Observation Statement controller (FR-005: preserve full reported detail census)."""
try:
    import frappe
    from frappe.model.document import Document
except ImportError:  # bench-free repo validation
    Document = object


class OCObservationStatement(Document):
    pass
