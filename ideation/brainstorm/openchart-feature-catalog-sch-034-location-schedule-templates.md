# Location Schedule Templates — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Assigns versioned day patterns to locations and services to generate predictable future capacity.
Topics: openchart-feature-catalog, scheduling, frappe, location-templates
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-034 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Seasonal template set** — Switch reviewed location patterns by bounded season.

## Focus

This feature isolates where and when reusable day templates apply across a location's operating schedule.

## Behavior

- Managers assign a published day template to a location, service, weekday set, and effective date range.
- Assignment preview shows generated capacity, closures, and overlaps with existing assignments.
- More specific assignments have explicit precedence over location defaults.
- Publishing generates or projects only future availability and preserves already booked time.
- Gaps and conflicting precedence are flagged before activation.
- Retiring an assignment stops future generation while retaining its historical version.

## Frappe realization

- **DocTypes:** `OC Location Schedule Template` links location, service, `OC Day Template`, weekdays, effective dates, and precedence.
- **Workflow:** Draft → Previewed → Active → Retired; Frappe auto-repeat semantics support weekly application patterns.
- **Automation/surface:** `scheduler_events` extends the availability horizon; Calendar and Gantt views preview generated capacity.

## Boundaries

Owns: template-to-location assignment. Consumes: day templates, closures, and service scope. Emits: future baseline availability. Does not own: provider exceptions.

## Open questions

- How far ahead should template assignments materialize concrete slots?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Day Template Patterns](openchart-feature-catalog-sch-021-day-template-patterns.md)
