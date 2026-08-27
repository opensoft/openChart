# Multi-resource Appointment Booking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Confirms one appointment only when every required provider, room, equipment, and support resource is reserved together.
Topics: openchart-feature-catalog, scheduling, frappe, multi-resource-booking
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-032 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Resource substitution sets** — Allow reviewed equivalent equipment or rooms within a requirement class.

## Focus

This feature isolates atomic reservation of several independent resources for one care event.

## Behavior

- Appointment requirements resolve into mandatory and optional resource roles with intervals and buffers.
- Slot search returns only combinations satisfying all mandatory roles.
- Confirmation locks and reserves resources in a deterministic order to prevent partial race-condition bookings.
- If any reservation fails, all new reservations roll back and the appointment remains unconfirmed.
- Resource substitutions must satisfy the same class and record the selected alternative.
- Reschedule and cancellation update the complete reservation set as one governed change.

## Frappe realization

- **DocTypes:** child `OC Appointment Resource Requirement` and `OC Resource Reservation` records linked to `OC Appointment`.
- **API:** `open_chart.api.v1.scheduling.book_multi_resource` performs transaction-scoped validation and ordered locks.
- **Surface:** booking dialog shows requirement fulfillment; resource and provider Calendar views project the shared appointment.

## Boundaries

Owns: all-or-none reservation coordination. Consumes: appointment requirements and resource availability. Emits: confirmed reservation set. Does not own: resource maintenance or credentials.

## Open questions

- Which optional resources should hold capacity before final confirmation?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Rule-based Booking Constraints](openchart-feature-catalog-sch-007-rule-based-booking-constraints.md)
