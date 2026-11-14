# Standing Preventive Lab Orders — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Creates time-bounded preventive laboratory authorizations that generate reviewable annual or interval collection instances.
Topics: openchart-feature-catalog, laboratory, frappe, standing-orders
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-028 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Standing Preventive Lab Orders assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates preventive standing-order schedule and occurrence lineage as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Ordering Clinician supplies patient, panel, indication, cadence, earliest and latest dates, occurrence limit, ordering authority, and expiration.
- The system produces a signed standing authorization plus traceable collection instances and exposes its current state to permitted users.
- The governed lifecycle is Draft → Active → Due → Exhausted, Expired, or Cancelled; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Each occurrence checks current eligibility and catalog status; expiry or exhausted counts prevent further collections.

## Frappe realization

- **DocTypes:** `OC Standing Lab Order` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Draft → Active → Due → Exhausted, Expired, or Cancelled; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Ordering Clinician` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.standing_preventive_lab_orders` is the supported write method, with allowlisted `/api/resource/OC%20Standing%20Lab%20Order` reads and a Desk worklist or report.

## Boundaries

Owns: preventive standing-order schedule and occurrence lineage. Consumes: lab catalog, ordering authority, patient context, and cadence rules. Emits: a signed standing authorization plus traceable collection instances. Does not own: appointment booking or automatic renewal beyond signed authority.

## Open questions

- Which organization-level policy values and exception thresholds for standing preventive lab orders must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
