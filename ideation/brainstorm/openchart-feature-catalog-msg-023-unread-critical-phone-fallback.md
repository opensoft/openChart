# Unread Critical Phone Fallback — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Creates a governed phone-contact fallback when a critical notification remains unread or unacknowledged beyond its deadline.
Topics: openchart-feature-catalog, messaging-tasks, frappe, phone-fallback
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-023 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Call-tree drill mode** — Exercise fallback contacts with synthetic alerts and compare expected versus actual reachability.

## Focus

This feature isolates transition from digital alerting to human phone outreach while keeping emergency response and clinical action outside the automation.

## Behavior

- An approved critical-message class defines whether fallback triggers on unread, unacknowledged, or declined state.
- At deadline, the service rechecks receipt state, current assignee, coverage, and cancellation before opening a call task.
- The call task identifies the message, required recipient role, approved contact sequence, and disclosure limits.
- A caller records reached, voicemail, no answer, wrong number, declined, or escalated outcomes.
- Reaching an unauthorized person does not count as acknowledgment and limits disclosed content.
- Successful qualified acknowledgment closes the fallback and updates the shared escalation instance.
- Exhausted phone attempts route to the configured final exception process without autonomous emergency dispatch.
- Duplicate deadline jobs resolve to one fallback instance through an event-policy idempotency key.

## Frappe realization

- **DocTypes:** `OC Phone Fallback Instance` links receipt/escalation, contact sequence, `OC Voice Call Task`, state, deadline, and outcome.
- **Automation:** `scheduler_events` enqueues deadline checks; transactional creation prevents duplicate call tasks.
- **Workflow:** Pending → Calling → Acknowledged/Exhausted/Cancelled with reason-gated closure.
- **Assignment/notifications:** Assignment Rules route callers; Notification Log prompts call staff and escalation supervisors.
- **Reports:** Script Report measures digital deadline misses, phone reach, time to acknowledgment, and exhaustion.

## Boundaries

Owns: fallback trigger, call-task linkage, and closure evidence. Consumes: receipt state, coverage, contact policy, and call outcomes. Emits: call work and escalation updates. Does not own: emergency dispatch or clinical response.

## Open questions

- Which critical classes require simultaneous rather than sequential phone fallback?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Urgent Message Escalation Ladders](openchart-feature-catalog-msg-005-urgent-message-escalation-ladders.md)
