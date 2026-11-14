# Day Template Patterns — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Defines reusable daily patterns of bookable time, holds, breaks, and appointment-type lanes.
Topics: openchart-feature-catalog, scheduling, frappe, day-templates
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-021 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Template utilization feedback** — Compare planned lanes with actual demand and use.

## Focus

This feature isolates reusable intra-day capacity patterns before they are assigned to calendars.

## Behavior

- Managers compose named templates from ordered time bands with start, end, capacity, allowed types, and break or hold purpose.
- Validation rejects overlapping exclusive bands and time ranges outside one local day.
- Templates are versioned and carry effective dates.
- Publishing a new version affects future generated availability only.
- A preview visualizes the pattern with buffers and capacity totals.
- Inactivation prevents new assignments while preserving schedules generated from older versions.

## Frappe realization

- **DocTypes:** `OC Day Template` with child `OC Day Template Band` and version, effective dates, time ranges, capacity, and allowed types.
- **Workflow:** Draft → Reviewed → Published → Retired; Scheduling Template Manager controls publication.
- **Surface:** custom form timeline preview plus List and Calendar-style rendering; Version records preserve definition history.

## Boundaries

Owns: reusable day-pattern definitions. Consumes: appointment types and capacity classes. Emits: versioned pattern for assignment. Does not own: provider-specific exceptions.

## Open questions

- Should template changes regenerate untouched future availability automatically?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Location Schedule Templates](openchart-feature-catalog-sch-034-location-schedule-templates.md)
