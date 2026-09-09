# Third-next-available Metric — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Computes the third-next-available access interval using versioned, explainable inclusion rules.
Topics: openchart-feature-catalog, scheduling, frappe, third-next-available
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-036 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Access trend alerts** — Notify leaders when sustained access intervals exceed reviewed targets.

## Focus

This feature isolates a comparable prospective access metric rather than general capacity reporting.

## Behavior

- The metric scans qualifying open slots from a defined observation timestamp.
- Rules specify appointment type, provider or service scope, slot exclusions, and treatment of same-day openings.
- The third qualifying slot determines calendar-day and business-day access intervals.
- Fewer than three openings returns Insufficient Availability, not a misleading maximum value.
- Results show definition version, source horizon, qualifying slots, and computation time.
- Aggregation across providers retains enough detail to explain weighting and missing values.

## Frappe realization

- **DocTypes:** `OC Access Metric Definition` and `OC Access Metric Result` with scope, observation time, slot references, intervals, and status.
- **Automation:** scheduled background jobs compute snapshots; `scheduler_events` supports daily service-level runs.
- **Reports:** Query/Script Reports and Dashboard Charts show trends with definition metadata and permission filters.

## Boundaries

Owns: third-next-available calculation and provenance. Consumes: qualifying slot projection. Emits: access metric result. Does not own: access targets or staffing changes.

## Open questions

- Which same-day and reserved slots should be excluded for each service?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Scheduling Capacity Dashboard](openchart-feature-catalog-sch-035-scheduling-capacity-dashboard.md)
