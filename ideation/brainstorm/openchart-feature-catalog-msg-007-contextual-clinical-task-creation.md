# Contextual Clinical Task Creation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets authorized users create an accountable task from any supported clinical context without duplicating the source record.
Topics: openchart-feature-catalog, messaging-tasks, frappe, clinical-task
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-007 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Context-specific task presets** — Offer reviewed defaults for common result, order, encounter, and medication follow-ups.

## Focus

This feature isolates the universal create-task action and its provenance-safe link to the chart artifact that prompted work.

## Behavior

- An authorized user starts a task from a patient, encounter, result, order, medication, document, or message.
- The form captures title, instructions, assignee or pool, priority, due date, and optional completion requirement.
- The task stores a Dynamic Link and a minimum context snapshot so its origin remains understandable if the source changes.
- Assignment choices are constrained by facility, care-team, role, and source-record permissions.
- Creation validates that the source and patient relationship are still accessible at submit time.
- A task may be saved as draft or activated; only active tasks notify recipients and enter work queues.
- Duplicate creation warnings use source, task type, assignee, and open state but never silently suppress a task.
- Cancelling the source does not cancel the task automatically; it flags the task for human review.

## Frappe realization

- **DocTypes:** `OC Clinical Task` uses naming series, source Dynamic Link, patient Link, context snapshot JSON, assignee/pool, due datetime, priority, and requirement Link.
- **Workflow:** Draft → Active → In Progress/Waiting → Completed/Cancelled with reasoned cancellation.
- **Client/API:** standardized Create Task desk action and `open_chart.api.v1.messaging.create_task` validate source authority and accepted task types.
- **Assignment/notification:** Frappe Assignment Rules may select a destination; ToDo and Notification Log projections are generated from the authoritative task.
- **Permissions:** Clinical Task User, Task Supervisor, and source-specific user permissions control creation and visibility.

## Boundaries

Owns: task creation, state, and source provenance. Consumes: clinical context, identity, and assignment policy. Emits: active task and notifications. Does not own: source record state or clinical orders.

## Open questions

- Which source types require mandatory task templates rather than free-form instructions?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Task Completion Evidence Capture](openchart-feature-catalog-msg-010-task-completion-evidence-capture.md)
