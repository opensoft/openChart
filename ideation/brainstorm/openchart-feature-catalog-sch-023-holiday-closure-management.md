# Holiday Closure Management — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies facility closure or reduced-hours calendars with explicit impact handling for existing appointments.
Topics: openchart-feature-catalog, scheduling, frappe, holiday-closures
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-023 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Regional closure library** — Seed reviewable holidays by jurisdiction without auto-publishing them.

## Focus

This feature isolates facility-level closures and reduced operating hours, including their booking impact.

## Behavior

- Managers create full-day or partial-day closures for one or more facilities with reason and effective local time.
- A preview lists conflicting appointments, classes, resources, and scheduled reminders.
- Publishing blocks new bookings but never silently changes existing appointments.
- Affected bookings enter an assigned disruption queue for resolution.
- Reduced hours preserve capacity inside the remaining interval and close only the excluded range.
- Changes after publication record a new version and rerun impact detection.

## Frappe realization

- **DocTypes:** `OC Holiday Closure` and child facility rows with local date, interval, closure level, reason, and version.
- **Workflow:** Draft → Impact Reviewed → Published → Superseded/Cancelled.
- **Automation:** auto-repeat can seed annual patterns; `scheduler_events` activates dated closures and Notification doctypes alert assigned schedulers.

## Boundaries

Owns: schedulable facility closure periods. Consumes: facility calendars and current bookings. Emits: blocked capacity and disruption tasks. Does not own: workforce leave.

## Open questions

- How should partially staffed emergency services be represented during a closure?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Schedule Change Broadcasts](openchart-feature-catalog-sch-055-schedule-change-broadcasts.md)
