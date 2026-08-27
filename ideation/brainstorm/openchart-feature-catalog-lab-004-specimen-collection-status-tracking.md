# Specimen Collection Status Tracking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Tracks each required specimen from scheduled collection through collected, missed, refused, or deferred states without conflating collection with laboratory receipt.
Topics: openchart-feature-catalog, laboratory, frappe, specimen-collection
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-004 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Specimen Collection Status Tracking assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates collection state and collector attribution as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Phlebotomist supplies lab order, specimen requirement, collector, collection site, timestamps, and disposition reason.
- The system produces an auditable specimen collection event stream and exposes its current state to permitted users.
- The governed lifecycle is Planned → Ready → Collected, Missed, Refused, or Deferred; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Partial panel collection keeps uncollected specimen requirements open and identifies which tests can proceed.

## Frappe realization

- **DocTypes:** `OC Specimen Collection` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Planned → Ready → Collected, Missed, Refused, or Deferred; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Phlebotomist` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.specimen_collection_status_tracking` is the supported write method, with allowlisted `/api/resource/OC%20Specimen%20Collection` reads and a Desk worklist or report.

## Boundaries

Owns: collection state and collector attribution. Consumes: signed orders, patient identity, collection schedules, and specimen requirements. Emits: an auditable specimen collection event stream. Does not own: accessioning, analysis, or result status.

## Open questions

- Which organization-level policy values and exception thresholds for specimen collection status tracking must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
