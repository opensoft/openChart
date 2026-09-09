# Imaging Scheduling Integration — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Exchanges imaging readiness, resource requirements, appointment state, and identifiers with a scheduling service without moving clinical authority out of openChart.
Topics: openchart-feature-catalog, imaging, frappe, scheduling-integration
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-005 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Readiness-aware slot search** — Filter candidate slots by protocol, equipment, staffing, and preparation lead time.

## Focus

This feature isolates the contract between imaging clinical state and internal or external scheduling systems.

## Behavior

- Only active orders meeting configured protocol and safety prerequisites become schedulable.
- The integration sends study duration, modality, equipment, location, staff, preparation lead time, and patient constraints.
- Returned bookings are matched by immutable correlation identifiers and checked against current order state.
- Duplicate, stale, or conflicting callbacks enter reconciliation rather than changing appointments silently.
- Cancellation and rescheduling events update imaging work state and supersede obsolete instructions.
- Delivery failures retry idempotently and expose an operations task after the configured threshold.

## Frappe realization

- **DocTypes:** `OC Imaging Scheduling Link` stores order, external appointment ID, correlation ID, readiness snapshot, status, and last error.
- **Workflow:** Not Ready → Ready → Booking Pending → Scheduled → Reconciliation Required → Closed.
- **Roles/permissions:** imaging coordinators resolve conflicts; integration users receive scoped API permissions; clinical fields remain read-only to connectors.
- **Hooks/API/surfaces:** whitelisted callbacks verify signatures; RQ jobs handle retries; a Script Report shows unmatched or stale transactions.

## Boundaries

Owns: imaging-scheduling linkage and reconciliation evidence. Consumes: order readiness and scheduling outcomes. Emits: schedulable demand and appointment-linked state. Does not own: enterprise calendar supply or scanner operation.

## Open questions

- What minimum event contract supports both Frappe-native and external scheduling implementations?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
