# Order-to-Report Turnaround Metrics — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Measures imaging turnaround intervals from accepted order through protocol, performance, preliminary interpretation, final signature, and delivery using auditable event timestamps.
Topics: openchart-feature-catalog, imaging, frappe, turnaround-metrics
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-026 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Delay attribution review** — Separate patient, scheduling, acquisition, interpretation, and interface delay intervals.

## Focus

This feature isolates reproducible operational timing measures rather than relying on mutable status dates.

## Behavior

- Metrics derive from accepted timestamped events with defined clocks and facility time zones.
- Reports show order-to-schedule, schedule-to-start, acquisition duration, completion-to-preliminary, completion-to-final, and final-to-delivery intervals.
- Cancelled, partial, corrected, external, and downtime cases are classified rather than silently mixed.
- Users can filter by modality, study, priority, facility, reader group, and reporting period.
- Metric definitions and exclusions are versioned and displayed with results.
- Drill-down respects patient permissions and aggregate suppression rules.

## Frappe realization

- **DocTypes:** `OC Imaging Metric Definition` versions interval anchors and exclusions; derived facts reference canonical order, performance, report, and communication events.
- **Roles/permissions:** imaging managers view aggregates; quality reviewers drill down; ordinary users see only authorized patient episodes.
- **Jobs/surfaces:** scheduled RQ jobs materialize metric facts; Query/Script Reports, Number Cards, and Dashboard Charts present trends.
- **Audit/API:** read-only metrics API returns definition version and source event IDs; corrections trigger bounded recomputation.

## Boundaries

Owns: metric definitions, derived intervals, and operational projections. Consumes: imaging lifecycle events. Emits: performance measures and delay cohorts. Does not own: staffing evaluation, compensation, or autonomous queue prioritization.

## Open questions

- Which intervals should pause during documented patient or external-system delays?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
