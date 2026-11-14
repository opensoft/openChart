# Task Due Dates and Recurrence — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies explicit deadlines and bounded recurrence patterns to tasks while preserving each occurrence as independent accountable work.
Topics: openchart-feature-catalog, messaging-tasks, frappe, task-recurrence
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-009 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Business-calendar deadlines** — Calculate due times against facility hours, holidays, and urgency-specific service levels.

## Focus

This feature isolates temporal task policy: deadlines, reminders, overdue transitions, and recurrence materialization.

## Behavior

- Task creators set a due datetime directly or select an approved service-level rule.
- Optional recurrence supports daily, weekly, monthly, interval, and bounded end conditions with a named timezone.
- Every generated occurrence has its own assignee, state, due time, completion evidence, and source lineage.
- Editing a series requires an explicit scope of this occurrence, future occurrences, or the pattern only.
- Missed scheduler runs catch up idempotently without generating duplicate occurrences.
- Overdue state is derived from accepted due time and completion state, not a mutable checkbox.
- Recurrence stops on its end condition or human cancellation; source-record closure may prompt but not silently stop it.
- Daylight-saving gaps and overlaps resolve by stored timezone policy and display an explanation.

## Frappe realization

- **DocTypes:** `OC Task Schedule` and `OC Clinical Task` store recurrence rule, timezone, next run, series Link, occurrence key, due basis, and end condition.
- **Automation:** Frappe auto-repeat may represent simple reviewed patterns; `scheduler_events` and background jobs materialize clinically governed occurrences idempotently.
- **Hooks:** validation rejects unbounded or contradictory rules; cancellation records scope and reason.
- **Surfaces:** Calendar and Gantt views, overdue List filters, Number Cards, and a recurrence preview dialog.
- **Notifications:** Notification Log and Frappe Notification issue due-soon and overdue events according to quiet-hours policy.

## Boundaries

Owns: task temporal rules and occurrence lineage. Consumes: task type, facility calendar, and notification policy. Emits: occurrences and due events. Does not own: clinical cadence decisions or appointment scheduling.

## Open questions

- Which recurring clinical tasks require a maximum horizon or periodic reauthorization?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Reminder Cadence Engine](openchart-feature-catalog-msg-019-reminder-cadence-engine.md)
