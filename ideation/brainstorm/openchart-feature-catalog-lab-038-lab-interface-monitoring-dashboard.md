# Lab Interface Failure Monitoring Dashboard — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Shows inbound and outbound laboratory interface health, failures, latency, queue depth, and acknowledgment gaps by connector.
Topics: openchart-feature-catalog, laboratory, frappe, interface-monitoring
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-038 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Lab Interface Failure Monitoring Dashboard assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates interface observability and incident projection as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Interface Operator supplies connector heartbeat, transaction states, error classes, retry counts, queue age, acknowledgments, and maintenance windows.
- The system produces an operational dashboard with actionable failure assignments and exposes its current state to permitted users.
- The governed lifecycle is Healthy → Degraded → Failed → Recovering → Healthy; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Planned outages, transient retries, data errors, and credential failures remain distinct and use different escalation policies.

## Frappe realization

- **DocTypes:** `OC Lab Interface Health` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Healthy → Degraded → Failed → Recovering → Healthy; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Interface Operator` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.lab_interface_monitoring_dashboard` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Interface%20Health` reads and a Desk worklist or report.

## Boundaries

Owns: interface observability and incident projection. Consumes: transaction logs, connector profiles, workers, and maintenance schedules. Emits: an operational dashboard with actionable failure assignments. Does not own: clinical result acknowledgment or hidden automatic data correction.

## Open questions

- Which organization-level policy values and exception thresholds for lab interface failure monitoring dashboard must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
