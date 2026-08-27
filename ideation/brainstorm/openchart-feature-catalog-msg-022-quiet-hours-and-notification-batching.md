# Quiet Hours and Notification Batching — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Defers or groups noncritical notifications according to recipient-local quiet hours while preserving urgency and due-time guarantees.
Topics: openchart-feature-catalog, messaging-tasks, frappe, notification-batching
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-022 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Notification digest preview** — Show recipients how selected events would group before a batching policy is activated.

## Focus

This feature isolates timing suppression and digest composition for staff and patient notifications without changing underlying work-item deadlines.

## Behavior

- Recipients or administrators define timezone, quiet intervals, digest windows, and eligible notification classes.
- Critical classes bypass deferral only when an approved policy explicitly allows it.
- Deferred notifications retain original event time, intended channel, and latest permissible delivery time.
- Batching groups compatible events by recipient, purpose, and privacy class without mixing patient contexts in an unsafe summary.
- A digest links to individually permission-checked records and never transfers their authorization to the digest.
- Due-time risk releases a deferred event before the quiet period ends when policy requires.
- Preference changes or item closure before dispatch suppress obsolete events with a reason.
- Scheduler retries are idempotent and do not create duplicate digest membership.

## Frappe realization

- **DocTypes:** `OC Notification Timing Policy`, `OC Deferred Notification`, and `OC Notification Digest` store timezone, windows, class, deadline, members, and disposition.
- **Automation:** `scheduler_events` releases due notifications and builds digests through locked RQ jobs.
- **Notifications:** Notification Log remains the in-app event record; Frappe Notification, Email Accounts, and SMS settings dispatch allowed external projections.
- **Permissions:** users manage personal policies within organizational bounds; Messaging Policy Manager governs urgency classes and maximum delays.
- **Reports:** delayed, bypassed, suppressed, and duplicate-prevented events appear in a Script Report.

## Boundaries

Owns: delivery timing, deferral, and batching state. Consumes: notification events, recipient timezone, urgency, and preferences. Emits: released events or digests. Does not own: task deadlines, message content, or urgency classification.

## Open questions

- Which patient-facing purposes may be safely combined in one digest?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Unread Critical Phone Fallback](openchart-feature-catalog-msg-023-unread-critical-phone-fallback.md)
