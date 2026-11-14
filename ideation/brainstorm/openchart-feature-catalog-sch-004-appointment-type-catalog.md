# Appointment Type Catalog — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Defines reusable appointment types with duration, color, modality, buffers, and booking defaults.
Topics: openchart-feature-catalog, scheduling, frappe, appointment-types
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-004 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Type bundles** — Package compatible appointment types into service-line offerings.

## Focus

This feature isolates the governed catalog that turns service intent into consistent slot requirements.

## Behavior

- Scheduling managers create active appointment types with name, duration, color, modality, and pre/post buffers.
- A type can declare default provider specialty, location class, and required resource classes.
- Schedulers see only types valid for the selected service and facility.
- Existing appointments retain a snapshot when type defaults later change.
- Inactivation blocks new bookings but leaves historical appointments readable.
- Duplicate active codes are rejected and invalid durations produce field-specific errors.

## Frappe realization

- **DocTypes:** `OC Appointment Type` with code, label, duration, color, modality, buffers, active, and child requirement rows.
- **Permissions:** Scheduling Manager writes; Scheduler reads; history is captured through Frappe Version and the activity feed.
- **Surface/API:** Quick Entry and List views manage definitions; guarded `open_chart.api.v1.scheduling` methods resolve eligible types.

## Boundaries

Owns: appointment-type definitions and booking defaults. Consumes: service, facility, and resource classifications. Emits: immutable booking snapshots. Does not own: clinical procedure definitions.

## Open questions

- Should duration overrides require a reason or manager approval?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Rule-based Booking Constraints](openchart-feature-catalog-sch-007-rule-based-booking-constraints.md)
