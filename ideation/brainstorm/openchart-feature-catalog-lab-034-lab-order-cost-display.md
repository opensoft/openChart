# Lab Order Cost Display — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Displays dated patient and organizational cost estimates beside laboratory choices before signature without suppressing clinical options.
Topics: openchart-feature-catalog, laboratory, frappe, cost-transparency
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-034 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Lab Order Cost Display assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates order-time estimate presentation as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Ordering Clinician supplies test, destination, payer context, site, estimate source, effective dates, uncertainty, and alternatives.
- The system produces a source-attributed estimate snapshot shown during ordering and exposes its current state to permitted users.
- The governed lifecycle is Requested → Available, Stale, or Unavailable → Displayed; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Unavailable or stale estimates show uncertainty and never block a medically appropriate order.

## Frappe realization

- **DocTypes:** `OC Lab Cost Estimate` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Requested → Available, Stale, or Unavailable → Displayed; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Ordering Clinician` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.lab_order_cost_display` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Cost%20Estimate` reads and a Desk worklist or report.

## Boundaries

Owns: order-time estimate presentation. Consumes: lab catalog, destination, coverage context, and pricing feeds. Emits: a source-attributed estimate snapshot shown during ordering. Does not own: billing, claims, final patient liability, or ranking clinical necessity by price.

## Open questions

- Which organization-level policy values and exception thresholds for lab order cost display must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
