# Versioned Reference Range Editor — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets laboratory leaders author, validate, approve, activate, and retire reference ranges without rewriting ranges attached to prior results.
Topics: openchart-feature-catalog, laboratory, frappe, range-governance
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-041 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Versioned Reference Range Editor assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates reference-range content lifecycle as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Medical Director supplies analyte, specimen, method, units, demographic criteria, limits, critical limits, rationale, approvers, and effective dates.
- The system produces an approved succession chain of range versions and exposes its current state to permitted users.
- The governed lifecycle is Draft → Validation → Approved → Scheduled → Active → Retired; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Overlaps, gaps, unit mismatches, and retroactive effective dates require explicit review before activation.

## Frappe realization

- **DocTypes:** `OC Reference Range Version` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Draft → Validation → Approved → Scheduled → Active → Retired; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Medical Director` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.versioned_reference_range_editor` is the supported write method, with allowlisted `/api/resource/OC%20Reference%20Range%20Version` reads and a Desk worklist or report.

## Boundaries

Owns: reference-range content lifecycle. Consumes: laboratory concepts, methods, units, governance roles, and synthetic test cases. Emits: an approved succession chain of range versions. Does not own: reinterpreting historical results without a separately governed process.

## Open questions

- Which organization-level policy values and exception thresholds for versioned reference range editor must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
