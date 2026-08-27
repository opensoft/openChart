# Pending Results Worklist — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Shows ordered tests that have not reached a terminal result state, organized by expected turnaround time and operational exception.
Topics: openchart-feature-catalog, laboratory, frappe, pending-results
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-016 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Pending Results Worklist assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates pending-result projection and operational prioritization as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Coordinator supplies orders, accessions, collection states, outbound acknowledgments, expected turnaround times, and current result status.
- The system produces a permission-filtered worklist of pending obligations and next actions and exposes its current state to permitted users.
- The governed lifecycle is Expected → In Process → Delayed, Resulted, Cancelled, or Failed; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Cancelled orders, partial panels, add-ons, and externally delayed tests retain distinct reasons instead of one generic pending state.

## Frappe realization

- **DocTypes:** `OC Pending Result Projection` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Expected → In Process → Delayed, Resulted, Cancelled, or Failed; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Coordinator` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.pending_results_worklist` is the supported write method, with allowlisted `/api/resource/OC%20Pending%20Result%20Projection` reads and a Desk worklist or report.

## Boundaries

Owns: pending-result projection and operational prioritization. Consumes: order, specimen, accession, interface, and result events. Emits: a permission-filtered worklist of pending obligations and next actions. Does not own: laboratory analysis or result clinical review.

## Open questions

- Which organization-level policy values and exception thresholds for pending results worklist must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
