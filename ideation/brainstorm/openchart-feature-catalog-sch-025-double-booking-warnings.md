# Double-booking Warnings — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Detects overlapping provider, patient, room, and resource commitments and presents actionable conflict evidence.
Topics: openchart-feature-catalog, scheduling, frappe, conflict-warnings
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-025 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Conflict resolution assistant** — Rank safe alternatives without moving bookings automatically.

## Focus

This feature isolates overlap detection and warning severity at booking and schedule-edit time.

## Behavior

- Every create, reschedule, and resource change checks effective intervals including setup and turnover buffers.
- Conflicts identify the constrained entity, overlapping record, interval, and severity.
- Hard conflicts block confirmation; soft conflicts require an authorized reasoned acknowledgement.
- Permission-limited users see enough conflict context to act without seeing unrelated patient details.
- Race conditions are rechecked transactionally at save time.
- Resolved and overridden warnings remain attached to the booking audit trail.

## Frappe realization

- **DocTypes:** `OC Schedule Conflict` with booking, conflicting Dynamic Link, entity type, interval, severity, and resolution.
- **Hooks:** appointment `validate` and resource reservation validation use indexed overlap queries inside the guarded write path.
- **Surface:** client scripts show inline warnings; blocked saves return structured API errors; Query Reports list unresolved soft conflicts.

## Boundaries

Owns: overlap detection evidence. Consumes: booking and reservation intervals. Emits: block or warning. Does not own: overbooking authorization.

## Open questions

- Which overlaps are clinically tolerable enough to remain warnings rather than blocks?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Schedule Conflict Resolution](openchart-feature-catalog-sch-053-schedule-conflict-resolution.md)
