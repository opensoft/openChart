# Wait-time Tracking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Derives patient wait and stage durations from auditable flow events for operations and service improvement.
Topics: openchart-feature-catalog, scheduling, frappe, wait-times
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-028 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Patient delay updates** — Send consented notices when expected waits cross a threshold.

## Focus

This feature isolates time-interval derivation and reporting from the flow states that supply timestamps.

## Behavior

- The system computes arrival-to-check-in, check-in-to-room, room-to-care, and total visit durations from valid events.
- Missing or corrected events mark affected metrics incomplete and trigger recomputation.
- Staff see current elapsed waits; managers see aggregated percentiles by service, location, and time band.
- Paused intervals and patient-requested delays follow explicit local definitions.
- Reports suppress or aggregate small cohorts according to privacy policy.
- Metrics never alter appointment priority or clinical urgency by themselves.

## Frappe realization

- **DocTypes:** `OC Appointment Wait Metric` with appointment, metric_type, starts_at, ends_at, duration, completeness, and source event versions.
- **Automation:** `on_update` queues recalculation; nightly `scheduler_events` reconciles missing or corrected metrics.
- **Reports:** Script Reports, Number Cards, and Dashboard Charts show current and percentile wait measures.

## Boundaries

Owns: derived operational durations. Consumes: flow event history. Emits: current and aggregate wait metrics. Does not own: triage acuity or staffing decisions.

## Open questions

- Which paused intervals should be excluded from patient-experienced wait time?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Real-time Patient Flow Board](openchart-feature-catalog-sch-027-real-time-patient-flow-board.md)
