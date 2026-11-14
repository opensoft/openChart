# Procedure Scheduling — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates procedure bookings with authorized requests, required teams, rooms, equipment, durations, and readiness gates.
Topics: openchart-feature-catalog, scheduling, frappe, procedure-scheduling
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-038 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Procedure block optimization** — Compare case sequencing options without autonomous clinical prioritization.

## Focus

This feature isolates the higher-complexity operational booking of procedures.

## Behavior

- A scheduler selects an authorized procedure request and reviews duration, location class, team roles, equipment, and readiness requirements.
- Candidate times satisfy all mandatory resources and configured setup, cleanup, and recovery intervals.
- The booking can remain Tentative while named readiness gates are unresolved.
- Confirmation records the source request, requirement snapshot, reservations, and responsible scheduler.
- Material changes revalidate resources and display patient and team notification impacts.
- Cancellation releases resources and preserves the procedure request for explicit disposition.

## Frappe realization

- **DocTypes:** `OC Procedure Booking` with source request, procedure code, state, intervals, readiness table, team roles, and reservations.
- **Workflow:** Draft → Tentative → Ready → Confirmed → In Progress → Complete/Cancelled; role actions are explicit.
- **Surface/API:** Gantt and Calendar views coordinate rooms and teams; guarded methods reserve multi-resource requirements transactionally.

## Boundaries

Owns: procedure booking logistics and readiness state. Consumes: authorized procedure intent and resource requirements. Emits: coordinated schedule. Does not own: consent, orders, or procedure documentation.

## Open questions

- Which readiness gates must block confirmation versus only day-of execution?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Procedure Preparation Instructions](openchart-feature-catalog-sch-039-procedure-preparation-instructions.md)
