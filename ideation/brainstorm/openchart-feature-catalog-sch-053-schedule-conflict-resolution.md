# Schedule Conflict Resolution — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Guides authorized staff from detected schedule conflicts to a documented keep, move, substitute, or cancel resolution.
Topics: openchart-feature-catalog, scheduling, frappe, conflict-resolution
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-053 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Resolution playbooks** — Offer reviewed action sequences for common disruption types.

## Focus

This feature isolates human resolution of existing conflicts rather than conflict detection itself.

## Behavior

- A work queue groups unresolved conflicts by severity, facility, date, constrained entity, and source event.
- Staff inspect affected bookings, patient contact constraints, and safe alternatives within their permissions.
- Resolution options include acknowledged coexistence, reschedule, resource swap, provider substitution, cancellation request, or escalation.
- The chosen action is revalidated before application and records reason and actor.
- Partial failures leave unresolved items visible and do not mark the conflict complete.
- Closing a conflict requires every affected commitment to have a terminal disposition.

## Frappe realization

- **DocTypes:** `OC Conflict Resolution Case` with source conflicts and child actions, owners, target dates, state, and completion evidence.
- **Workflow:** Open → Assigned → Resolving → Resolved/Escalated; Assignment Rules route by facility and conflict type.
- **Surface:** Kanban and Script Report queues call guarded scheduling actions; realtime events refresh affected calendars.

## Boundaries

Owns: conflict case orchestration and disposition. Consumes: detected conflicts and authorized alternatives. Emits: governed scheduling actions. Does not own: detection rules.

## Open questions

- Which conflict classes require patient contact before any operational change?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Double-booking Warnings](openchart-feature-catalog-sch-025-double-booking-warnings.md)
