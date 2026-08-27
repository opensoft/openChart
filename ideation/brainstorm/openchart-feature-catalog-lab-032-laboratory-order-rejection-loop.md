# Laboratory Order Rejection Loop — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Routes reference-lab order errors back to authorized staff for correction, cancellation, or clarification with resubmission lineage.
Topics: openchart-feature-catalog, laboratory, frappe, order-rejections
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-032 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Laboratory Order Rejection Loop assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates external order rejection resolution as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Coordinator supplies outbound transaction, rejection code, laboratory message, affected items, correction fields, responder, and resolution.
- The system produces a closed rejection case linked to a corrected successor or justified cancellation and exposes its current state to permitted users.
- The governed lifecycle is Received → Assigned → Corrected and Resubmitted, Cancelled, or Escalated; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Repeated rejection cannot overwrite prior attempts; non-correctable clinical changes return to the ordering clinician.

## Frappe realization

- **DocTypes:** `OC Lab Order Rejection` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Received → Assigned → Corrected and Resubmitted, Cancelled, or Escalated; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Coordinator` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.laboratory_order_rejection_loop` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Order%20Rejection` reads and a Desk worklist or report.

## Boundaries

Owns: external order rejection resolution. Consumes: outbound transactions, lab responses, orders, and staff assignments. Emits: a closed rejection case linked to a corrected successor or justified cancellation. Does not own: external validation rules or changing signed clinical intent without authorization.

## Open questions

- Which organization-level policy values and exception thresholds for laboratory order rejection loop must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
