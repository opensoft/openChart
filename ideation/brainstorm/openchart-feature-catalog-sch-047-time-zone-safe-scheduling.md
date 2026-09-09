# Time-zone-safe Scheduling — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Preserves unambiguous appointment timing across patient, provider, facility, and telehealth time zones.
Topics: openchart-feature-catalog, scheduling, frappe, time-zones
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-047 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Travel-aware display** — Let patients preview an appointment in a temporary destination time zone.

## Focus

This feature isolates time-zone capture, conversion, display, and daylight-saving edge cases.

## Behavior

- Every booking stores an authoritative instant plus facility time zone and the displayed local offset snapshot.
- Patients may choose display in facility or profile time zone, with both labels shown when they differ.
- Ambiguous or nonexistent daylight-saving local times cannot be booked without selecting a valid resolved instant.
- Recurrence expansion applies the intended local wall time and reports offset changes in preview.
- Notifications include time zone abbreviation and offset rather than a bare local time.
- Facility time-zone changes trigger review for future bookings and never rewrite historical instants.

## Frappe realization

- **DocTypes:** scheduling DocTypes use Datetime plus explicit IANA time_zone and offset_snapshot fields where provenance matters.
- **Validation:** shared server utilities reject ambiguous local inputs and normalize through the guarded API; client scripts preview conversions.
- **Surface:** Calendar, portal, print formats, and Notification templates use one formatter with actor and facility context.

## Boundaries

Owns: scheduling time interpretation and display rules. Consumes: local time input and IANA zones. Emits: authoritative instants and labels. Does not own: user profile location.

## Open questions

- Which time zone should be primary for telehealth appointments with a traveling patient?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Telehealth Slot Types](openchart-feature-catalog-sch-031-telehealth-slot-types.md)
