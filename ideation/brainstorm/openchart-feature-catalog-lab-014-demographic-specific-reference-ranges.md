# Demographic-Specific Reference Ranges — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Selects reference ranges by age, sex context, pregnancy state, specimen, method, and performing laboratory with transparent precedence.
Topics: openchart-feature-catalog, laboratory, frappe, reference-ranges
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-014 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Demographic-Specific Reference Ranges assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates range eligibility and deterministic selection as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Medical Director supplies analyte, units, specimen, method, lab, demographic criteria, effective dates, and limits.
- The system produces one pinned applicable range or an explicit ambiguity and exposes its current state to permitted users.
- The governed lifecycle is Draft → Reviewed → Approved → Active → Retired; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Overlapping equally specific ranges block publication or route results to range review rather than selecting by record order.

## Frappe realization

- **DocTypes:** `OC Reference Range` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Draft → Reviewed → Approved → Active → Retired; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Medical Director` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.demographic_specific_reference_ranges` is the supported write method, with allowlisted `/api/resource/OC%20Reference%20Range` reads and a Desk worklist or report.

## Boundaries

Owns: range eligibility and deterministic selection. Consumes: laboratory methods, demographic context, and governance approvals. Emits: one pinned applicable range or an explicit ambiguity. Does not own: changing patient demographics or assigning clinical significance.

## Open questions

- Which organization-level policy values and exception thresholds for demographic-specific reference ranges must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
