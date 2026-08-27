# Cumulative Laboratory Results Flowsheet — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents serial laboratory observations in a date-by-component grid with units, flags, status, and source context preserved.
Topics: openchart-feature-catalog, laboratory, frappe, results-flowsheet
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-018 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Cumulative Laboratory Results Flowsheet assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates longitudinal tabular presentation as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Clinician supplies patient, selected panels or analytes, date range, result statuses, normalized concepts, units, and reference ranges.
- The system produces a longitudinal read-only flowsheet with drill-down to source results and exposes its current state to permitted users.
- The governed lifecycle is Saved Definition → Rendered View; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Mixed units, methods, corrected values, and preliminary results are visibly separated rather than collapsed into a misleading row.

## Frappe realization

- **DocTypes:** `OC Lab Flowsheet Definition` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Saved Definition → Rendered View; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Clinician` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.cumulative_results_flowsheet` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Flowsheet%20Definition` reads and a Desk worklist or report.

## Boundaries

Owns: longitudinal tabular presentation. Consumes: filed results, normalization, ranges, and access permissions. Emits: a longitudinal read-only flowsheet with drill-down to source results. Does not own: editing results or declaring trends clinically significant.

## Open questions

- Which organization-level policy values and exception thresholds for cumulative laboratory results flowsheet must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
