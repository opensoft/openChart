# Scheduling Capacity Dashboard — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Summarizes available, booked, held, closed, and overbooked capacity by service, provider, resource, and location.
Topics: openchart-feature-catalog, scheduling, frappe, capacity-dashboard
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-035 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Capacity scenario overlay** — Compare proposed templates with current published supply.

## Focus

This feature isolates operational visibility into schedule supply and utilization.

## Behavior

- Managers choose date range, facility, service, provider, appointment type, and modality filters.
- Measures distinguish nominal capacity, effective capacity, booked time, holds, closures, and approved overbooking.
- Users drill from aggregates to permitted source records.
- Definitions and refresh timestamps appear with every metric.
- Late-arriving changes refresh incrementally and a nightly reconciliation corrects drift.
- Small or sensitive slices obey role and privacy thresholds.

## Frappe realization

- **DocTypes:** `OC Scheduling Capacity Snapshot` with dimensional keys, measure values, definition_version, and computed_at.
- **Reports:** Scheduling Workspace uses Number Cards, Dashboard Charts, and Script Reports with permission-aware drill-through.
- **Automation:** realtime events update near-term measures; nightly `scheduler_events` rebuild authoritative snapshots.

## Boundaries

Owns: derived schedule-capacity measures. Consumes: availability, bookings, holds, closures, and overbooks. Emits: dashboards and exports. Does not own: staffing plans.

## Open questions

- Which capacity denominator best supports comparison across unlike appointment types?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Third-next-available Metric](openchart-feature-catalog-sch-036-third-next-available-metric.md)
