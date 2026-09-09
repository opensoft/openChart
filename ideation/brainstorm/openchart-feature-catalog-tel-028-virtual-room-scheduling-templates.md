# Virtual Room Scheduling Templates — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Defines reusable virtual-room capacity, buffers, participant limits, and service defaults for scheduled care.
Topics: openchart-feature-catalog, telehealth, frappe, virtual-room-templates
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-028 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Adapter capacity forecast** — Compare scheduled room demand with contracted or self-hosted media capacity.

## Focus

This feature isolates reusable virtual-resource policy consumed by scheduling without owning the appointment calendar itself.

## Behavior

- Managers define templates by service, facility, duration, early-arrival window, cleanup buffer, participant limit, and media adapter.
- Effective dates and weekdays determine when a template supplies candidate virtual-room capacity.
- Booking reserves a logical room instance transactionally and never exposes reusable room credentials.
- Exceptions may close, extend, or substitute capacity with reason and effective interval.
- Template changes affect future uncommitted capacity while confirmed visits retain the version used at booking unless reviewed.
- Capacity conflicts return actionable alternatives and never double-assign an exclusive room or constrained adapter allocation.

## Frappe realization

- **DocTypes:** `OC Virtual Room Template`, `OC Virtual Room Instance`, and `OC Virtual Room Exception` store service defaults, intervals, adapter, capacity, reservation, and effective version.
- **Views/hooks:** Calendar and Gantt views show logical room supply; booking validation and scheduler jobs materialize a bounded horizon idempotently.
- **Permissions:** Telehealth Operations Manager edits templates, Scheduler reserves instances, and Audit Reviewer reads version and override history.

## Boundaries

Owns: virtual resource templates and reservations. Consumes: service and adapter capacity policy. Emits: available or reserved logical room. Does not own: provider calendars or media credentials.

## Open questions

- Should custom WebRTC rooms be created just in time while partner rooms are preprovisioned, or should both follow one lifecycle?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
