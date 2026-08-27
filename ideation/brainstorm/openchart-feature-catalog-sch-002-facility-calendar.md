# Facility Calendar — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Shows appointments, closures, and capacity commitments across a facility's services and spaces.
Topics: openchart-feature-catalog, scheduling, frappe, facility-calendar
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-002 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Campus rollup** — Combine permitted facility calendars into a regional operations view.

## Focus

This feature isolates the location-wide calendar needed to coordinate operational capacity.

## Behavior

- Schedulers filter a facility calendar by service, provider, room, resource, and appointment state.
- Closures and reduced-capacity periods appear alongside bookings without masquerading as patient appointments.
- Users can drill from a capacity band to the underlying appointment or closure record.
- Patient identifiers are hidden for roles granted aggregate facility access only.
- Conflicting facility closure edits are rejected with the current record returned for review.
- Facility time zones govern display and booking while preserving UTC timestamps.

## Frappe realization

- **DocTypes:** `OC Facility Schedule` with facility, service, starts_at, ends_at, capacity, and state; links to `OC Appointment` and `OC Holiday Closure`.
- **Surface:** use Frappe's native Calendar view per DocType plus filtered List and Dashboard views in the scheduling workspace.
- **Permissions:** grant facility-scoped user permissions to Scheduler and Scheduling Manager roles; aggregate viewers receive permlevel-limited fields.

## Boundaries

Owns: facility-level schedule projection. Consumes: bookings, closures, and capacity declarations. Emits: facility availability context. Does not own: facility master data.

## Open questions

- Should one calendar span facilities with different local time zones?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Holiday Closure Management](openchart-feature-catalog-sch-023-holiday-closure-management.md)
