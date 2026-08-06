"""OC Patient controller (brief D1: local patient identity anchor)."""
try:
    import frappe
    from frappe.model.document import Document
except ImportError:  # bench-free repo validation
    Document = object


class OCPatient(Document):
    pass
