# Point-Of-Care Quality Control Logging — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records control runs, expected ranges, lot and device context, failures, corrective actions, and release decisions for POCT operations.
Topics: openchart-feature-catalog, laboratory, frappe, poct-qc
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-044 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Point-Of-Care Quality Control Logging assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates POCT quality-control evidence and operational hold as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC POCT Coordinator supplies device, test, control level, lot, expected range, observed value, operator, time, failure reason, and corrective action.
- The system produces a QC pass or unresolved failure that governs device-test availability and exposes its current state to permitted users.
- The governed lifecycle is Due → Run → Passed or Failed → Corrective Action → Released; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Failed or overdue QC places the affected device and assay in hold until an authorized release is documented.

## Frappe realization

- **DocTypes:** `OC POCT Quality Control` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Due → Run → Passed or Failed → Corrective Action → Released; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC POCT Coordinator` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.point_of_care_quality_control` is the supported write method, with allowlisted `/api/resource/OC%20POCT%20Quality%20Control` reads and a Desk worklist or report.

## Boundaries

Owns: POCT quality-control evidence and operational hold. Consumes: devices, control lots, assay policy, operator credentials, and schedules. Emits: a QC pass or unresolved failure that governs device-test availability. Does not own: altering patient results or regulatory attestation beyond recorded evidence.

## Open questions

- Which organization-level policy values and exception thresholds for point-of-care quality control logging must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
