# Resource Calendar — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Tracks the availability and reservation of rooms, equipment, and other schedulable resources.
Topics: openchart-feature-catalog, scheduling, frappe, resource-calendar
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-003 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Maintenance-aware capacity** — Remove resources automatically during approved service windows.

## Focus

This feature isolates calendar control for non-provider resources required by care delivery.

## Behavior

- Schedulers open a room or equipment calendar and see reservations, holds, maintenance, and free periods.
- Resource type determines allowed booking granularity and whether concurrent use is permitted.
- A reservation links to its appointment and carries setup and turnover buffers.
- Users cannot reserve inactive or out-of-service resources.
- A race for the same exclusive interval returns a conflict instead of overwriting the first reservation.
- Authorized operators can place a reasoned operational hold without exposing patient details.

## Frappe realization

- **DocTypes:** `OC Schedulable Resource` and `OC Resource Reservation` with resource, appointment, interval, buffers, state, and hold_reason.
- **Surface:** enable Frappe's native Calendar view per DocType and resource-type List filters.
- **Validation:** `validate` checks overlap and operating state; `open_chart.api.v1.scheduling.reserve_resource` performs transactional writes.

## Boundaries

Owns: resource availability and reservations. Consumes: resource master status and appointment demand. Emits: reservation conflicts and capacity. Does not own: maintenance work orders.

## Open questions

- Which resource classes may safely support fractional concurrent capacity?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Multi-resource Appointment Booking](openchart-feature-catalog-sch-032-multi-resource-appointment-booking.md)
