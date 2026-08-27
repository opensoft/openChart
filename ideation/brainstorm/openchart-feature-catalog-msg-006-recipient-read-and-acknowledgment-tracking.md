# Recipient Read and Acknowledgment Tracking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records per-recipient delivery, read, and explicit acknowledgment evidence for messages that require closed-loop handling.
Topics: openchart-feature-catalog, messaging-tasks, frappe, acknowledgment-tracking
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-006 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Acknowledgment compliance view** — Compare expected and actual response times by message class and recipient role.

## Focus

This feature isolates recipient-level evidence and semantics so delivery, opening, acknowledgment, and completed action cannot be conflated.

## Behavior

- Every intended recipient receives an independent receipt with required response type and deadline.
- Channel delivery updates mark attempted, delivered, bounced, or unknown without marking the message read.
- Opening an authorized message records first-read and latest-read timestamps with client source.
- Explicit acknowledgment requires a deliberate action and may require a structured response code or comment.
- Proxy acknowledgment is rejected unless policy grants that actor authority and records the represented recipient.
- Added recipients receive new receipts; removed recipients retain historical evidence and a removal reason.
- Offline or duplicate client events are idempotent and preserve the earliest valid transition.
- Senders see aggregate progress and permitted recipient details, not hidden channel preferences.

## Frappe realization

- **DocTypes:** `OC Message Receipt` and `OC Receipt Event` link message, recipient, channel, required action, timestamps, actor, and correlation key.
- **API:** guarded `open_chart.api.v1.messaging.mark_read` and `acknowledge` methods enforce recipient identity and idempotency.
- **Hooks:** delivery webhooks update receipts through validated adapters; `after_insert` writes corresponding Notification Log references.
- **Permissions:** recipients read their receipts; senders and Clinical Supervisors receive scoped aggregate access; auditors receive read-only permlevel 2 fields.
- **Reports:** Query Reports and Dashboard Charts expose delivery-to-read and read-to-acknowledgment intervals.

## Boundaries

Owns: per-recipient communication evidence. Consumes: recipient identity and channel events. Emits: read, acknowledgment, and timing metrics. Does not own: task completion or proof of clinical action.

## Open questions

- Which client events are sufficiently trustworthy to count as a read?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Closed-loop Alert Effectiveness Metrics](openchart-feature-catalog-msg-024-closed-loop-alert-effectiveness-metrics.md)
