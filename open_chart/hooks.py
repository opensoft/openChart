"""open_chart Frappe hooks (feature 001; brief D1/D6).

The supported surface is the versioned API (open_chart.api.v1) plus the
doc_events declared here. Extensions — MedxEHR included — never write
intake tables directly; permissions and the compatibility tests enforce
it.
"""

app_name = "open_chart"
app_title = "Open Chart"
app_publisher = "opensoft"
app_description = "Original Frappe-native clinical charting — expanded patient intake foundation"
app_license = "AGPL-3.0"

# Supported events for extension consumers (MedxEHR): emitted on the
# lifecycle transitions of the intake envelope, never on internal saves.
doc_events = {
    "OC Intake Submission": {
        "on_update": "open_chart.api.v1.emit_submission_event",
    }
}
