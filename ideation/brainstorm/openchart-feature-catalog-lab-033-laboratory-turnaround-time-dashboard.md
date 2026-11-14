# Laboratory Turnaround Time Dashboard — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Measures ordered-to-collected, collected-to-received, received-to-resulted, and resulted-to-filed intervals by test and laboratory.
Topics: openchart-feature-catalog, laboratory, frappe, turnaround-time
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-033 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Laboratory Turnaround Time Dashboard assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates operational TAT measurement and attribution as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Operations Manager supplies order, specimen, accession, result, and filing timestamps; test, priority, lab, site, and exception dimensions.
- The system produces auditable turnaround distributions, breach worklists, and trend charts and exposes its current state to permitted users.
- The governed lifecycle is Event Projection → Daily Aggregation → Published Dashboard; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Missing timestamps and paused or patient-caused delays are reported separately rather than silently excluded.

## Frappe realization

- **DocTypes:** `OC Lab TAT Metric` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Event Projection → Daily Aggregation → Published Dashboard; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Operations Manager` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.laboratory_turnaround_time_dashboard` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20TAT%20Metric` reads and a Desk worklist or report.

## Boundaries

Owns: operational TAT measurement and attribution. Consumes: laboratory event timestamps, catalog expectations, and exception reasons. Emits: auditable turnaround distributions, breach worklists, and trend charts. Does not own: staff performance conclusions, contractual penalties, or clinical urgency decisions.

## Open questions

- Which organization-level policy values and exception thresholds for laboratory turnaround time dashboard must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
