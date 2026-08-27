# Failed Specimen Handling And Recollection — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records unusable specimens with coded reasons and creates an authorized, patient-visible recollection path without erasing the failed attempt.
Topics: openchart-feature-catalog, laboratory, frappe, recollection
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-031 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Failed Specimen Handling And Recollection assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates preanalytic failure and recollection lineage as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Coordinator supplies specimen, accession, failure reason, affected tests, collector, notification evidence, recollection eligibility, and priority.
- The system produces a preserved failure event and linked recollection request or terminal disposition and exposes its current state to permitted users.
- The governed lifecycle is Detected → Reviewed → Recollect Requested, Waived, or Closed → Recollected; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Insufficient quantity, hemolysis, clotting, contamination, leakage, temperature excursion, and patient refusal remain distinct.

## Frappe realization

- **DocTypes:** `OC Specimen Exception` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Detected → Reviewed → Recollect Requested, Waived, or Closed → Recollected; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Coordinator` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.failed_specimen_recollection` is the supported write method, with allowlisted `/api/resource/OC%20Specimen%20Exception` reads and a Desk worklist or report.

## Boundaries

Owns: preanalytic failure and recollection lineage. Consumes: collection events, accessions, test requirements, and ordering authority. Emits: a preserved failure event and linked recollection request or terminal disposition. Does not own: blame assignment, appointment scheduling, or automatic reorder beyond policy.

## Open questions

- Which organization-level policy values and exception thresholds for failed specimen handling and recollection must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
