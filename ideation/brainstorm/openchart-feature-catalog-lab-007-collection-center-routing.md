# Collection Center Routing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Routes laboratory orders to eligible collection centers based on test capability, geography, hours, payer constraints, and patient choice.
Topics: openchart-feature-catalog, laboratory, frappe, collection-routing
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-007 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Collection Center Routing assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates collection destination selection and route history as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Coordinator supplies ordered tests, patient location, collection-center capabilities, operating hours, coverage constraints, and preferences.
- The system produces a reviewable destination recommendation and confirmed route and exposes its current state to permitted users.
- The governed lifecycle is Proposed → Confirmed → Rerouted or Fulfilled; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- No eligible center produces an exception work item with the unsatisfied requirements instead of an arbitrary destination.

## Frappe realization

- **DocTypes:** `OC Collection Route` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Proposed → Confirmed → Rerouted or Fulfilled; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Coordinator` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.collection_center_routing` is the supported write method, with allowlisted `/api/resource/OC%20Collection%20Route` reads and a Desk worklist or report.

## Boundaries

Owns: collection destination selection and route history. Consumes: orders, site directory, capability schedules, and patient preferences. Emits: a reviewable destination recommendation and confirmed route. Does not own: appointment scheduling, transportation, or payer authorization.

## Open questions

- Which organization-level policy values and exception thresholds for collection center routing must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
