# Point-Of-Care Test Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures bedside or clinic glucose, strep, urine, pregnancy, and similar point-of-care test results with device, operator, lot, and patient context.
Topics: openchart-feature-catalog, laboratory, frappe, poct
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-043 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Point-Of-Care Test Capture assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates POCT result capture and provenance as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC POCT Operator supplies patient, encounter, test, specimen, result, units, device, operator, reagent lot, timestamps, and comments.
- The system produces a signed POCT result clearly identified by method and care location and exposes its current state to permitted users.
- The governed lifecycle is Draft → Device or Manual Capture → Validation → Final or Invalid; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Invalid operator certification, expired lots, failed QC, missing patient match, or out-of-range device output blocks finalization.

## Frappe realization

- **DocTypes:** `OC Point Of Care Test` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Draft → Device or Manual Capture → Validation → Final or Invalid; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC POCT Operator` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.point_of_care_test_capture` is the supported write method, with allowlisted `/api/resource/OC%20Point%20Of%20Care%20Test` reads and a Desk worklist or report.

## Boundaries

Owns: POCT result capture and provenance. Consumes: patient context, POCT catalog, devices, operator credentials, lots, and QC eligibility. Emits: a signed POCT result clearly identified by method and care location. Does not own: central laboratory analysis or treatment decisions.

## Open questions

- Which organization-level policy values and exception thresholds for point-of-care test capture must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
