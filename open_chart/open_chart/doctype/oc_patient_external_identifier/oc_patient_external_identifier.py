"""OC Patient External Identifier controller (brief D3: statement identity;
external identifiers carry status/version lifecycle rather than mutating
in place)."""
try:
    import frappe
    from frappe.model.document import Document
except ImportError:  # bench-free repo validation
    Document = object


class OCPatientExternalIdentifier(Document):
    pass
