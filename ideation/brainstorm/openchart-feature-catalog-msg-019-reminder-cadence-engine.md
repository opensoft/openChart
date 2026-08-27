# Reminder Cadence Engine — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Schedules appointment, medication, follow-up, and preventive reminders from approved cadence policies with explicit stop conditions.
Topics: openchart-feature-catalog, messaging-tasks, frappe, reminder-engine
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-019 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Cadence simulation** — Preview every planned touchpoint, channel, quiet-hours shift, and stop condition for a synthetic patient.

## Focus

This feature isolates reminder scheduling and lifecycle across reminder purposes while leaving source clinical decisions authoritative elsewhere.

## Behavior

- A reminder instance begins from an authorized source event and an active purpose-specific cadence version.
- Policies define offsets, channels, maximum attempts, quiet-hours handling, and action-based stop conditions.
- Each planned touchpoint stores its source event, policy version, intended time, and deduplication key.
- Source cancellation, completion, opt-out, or supersession stops only the touches named by policy and records why.
- Patient preference and do-not-contact checks run when planning and again immediately before delivery.
- Missed scheduler windows catch up or skip according to explicit lateness policy.
- Conflicting reminders may consolidate only under an approved batching rule that preserves each purpose.
- No reminder independently changes medication, preventive, appointment, or follow-up clinical state.

## Frappe realization

- **DocTypes:** `OC Reminder Policy`, child `OC Reminder Step`, `OC Reminder Instance`, and `OC Reminder Touch` store purpose, source Dynamic Link, timing, state, channel, and stop reason.
- **Workflow:** policies use Draft → Review → Active → Retired; instances use Active → Satisfied/Stopped/Expired.
- **Automation:** `scheduler_events` enqueues due touches; RQ jobs lock, revalidate, render, and send idempotently.
- **Channels:** Frappe Notification, Notification Log, Email Accounts, and SMS settings support channel-specific dispatch and evidence.
- **Reports/API:** cadence preview API and Script Reports expose pending, suppressed, late, and stopped touches.

## Boundaries

Owns: reminder cadence, touchpoint state, and stop evidence. Consumes: source events, preferences, consent, templates, and channel outcomes. Emits: due communications and reminder metrics. Does not own: clinical indications or source completion.

## Open questions

- Which reminder types may share one patient-facing message without obscuring distinct actions?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Reminder Effectiveness Analytics](openchart-feature-catalog-msg-020-reminder-effectiveness-analytics.md)
