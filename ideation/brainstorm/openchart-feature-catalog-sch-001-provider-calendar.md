# Provider Calendar — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents each provider's bookable, held, and unavailable time in one operational calendar.
Topics: openchart-feature-catalog, scheduling, frappe, provider-calendar
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-001 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Cross-provider overlay** — Compare selected provider calendars without merging ownership.

## Focus

This feature isolates the provider-centric calendar used to inspect and manage clinical time.

## Behavior

- Schedulers view day, week, and month ranges in the provider's configured time zone.
- Entries distinguish available slots, appointments, holds, breaks, and exceptions by state and color.
- Selecting an entry opens its source record; selecting free time starts a booking with provider and time prefilled.
- Role and user permissions limit calendars and patient details visible to each user.
- Concurrent changes refresh the affected range and warn before a stale edit is saved.
- Cancelled appointments remain traceable but do not continue to consume capacity.

## Frappe realization

- **DocTypes:** `OC Provider Schedule` with provider, location, starts_at, ends_at, state, and source Link fields; `OC Appointment` supplies bookings.
- **Surface:** configure Frappe's native Calendar view per DocType with server-side permission queries and a scheduling Desk workspace.
- **API/events:** expose guarded reads and writes through `open_chart.api.v1.scheduling`; publish websocket updates after validated changes.

## Boundaries

Owns: provider-time presentation. Consumes: availability, appointments, holds, and exceptions. Emits: calendar selections and change events. Does not own: clinical documentation or provider identity.

## Open questions

- Should non-clinical holds reveal their reason outside scheduling leadership?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Provider Availability Exceptions](openchart-feature-catalog-sch-022-provider-availability-exceptions.md)
