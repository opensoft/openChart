# Room Assignment — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Assigns and releases care rooms against appointment needs, occupancy, cleaning state, and location permissions.
Topics: openchart-feature-catalog, scheduling, frappe, room-assignment
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-029 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Room recommendation** — Rank compatible ready rooms while keeping staff in control of assignment.

## Focus

This feature isolates operational room placement during patient flow.

## Behavior

- Staff see rooms as Ready, Occupied, Cleaning, Held, or Out of Service with capability attributes.
- Assignment checks location, appointment requirements, occupancy, and any isolation or accessibility flags supplied by authorized context.
- Assigning a room records the patient appointment and timestamp without exposing the occupant on broad displays.
- Transfer releases the prior room and assigns the next as one validated operation.
- Completion moves the room to its configured turnover state.
- Conflicting simultaneous assignments reject the later request and return current occupancy.

## Frappe realization

- **DocTypes:** `OC Care Room` and `OC Room Assignment` with appointment, room, assigned_at, released_at, state, and requirements snapshot.
- **Workflow/API:** Assigned → Occupied → Released/Transferred; guarded methods lock the room row during mutation.
- **Surface:** resource Calendar, facility flow board, and List views expose room state with role-based patient detail.

## Boundaries

Owns: current room occupancy assignment. Consumes: appointment needs and room readiness. Emits: assignment and release events. Does not own: environmental cleaning execution.

## Open questions

- Which room requirements can be inferred versus requiring explicit staff confirmation?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Resource Calendar](openchart-feature-catalog-sch-003-resource-calendar.md)
