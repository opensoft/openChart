# Serial Laboratory Result Graphing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Graphs selected laboratory observations over time with range bands, event annotations, and explicit unit or method discontinuities.
Topics: openchart-feature-catalog, laboratory, frappe, result-graphing
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-019 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Serial Laboratory Result Graphing assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates visual trend presentation as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Clinician supplies patient, analyte, date range, normalized values, units, methods, reference ranges, and annotation events.
- The system produces an interactive longitudinal chart linked to every source observation and exposes its current state to permitted users.
- The governed lifecycle is Configured → Rendered; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Incomparable units or methods split the series unless an approved conversion exists; missing values are never interpolated as results.

## Frappe realization

- **DocTypes:** `OC Lab Graph Preference` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Configured → Rendered; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Clinician` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.serial_result_graphing` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Graph%20Preference` reads and a Desk worklist or report.

## Boundaries

Owns: visual trend presentation. Consumes: filed results, normalization, reference ranges, and clinical event dates. Emits: an interactive longitudinal chart linked to every source observation. Does not own: predictive interpretation or automatic treatment advice.

## Open questions

- Which organization-level policy values and exception thresholds for serial laboratory result graphing must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
