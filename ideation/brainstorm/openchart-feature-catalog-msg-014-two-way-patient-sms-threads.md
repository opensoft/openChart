# Two-way Patient SMS Threads — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Supports consent-aware two-way SMS conversations with patient identity matching, staff assignment, and complete delivery evidence.
Topics: openchart-feature-catalog, messaging-tasks, frappe, two-way-sms
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-014 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **SMS-to-workflow commands** — Map reviewed patient keywords such as confirm, cancel, or call-me to proposed staff actions.

## Focus

This feature isolates patient SMS as an assigned, closed-loop conversation that can reach non-portal patients while protecting identity and consent.

## Behavior

- Staff start a thread only after channel preference, consent, do-not-contact, and destination validation.
- Outbound content shows an external-channel warning and applies approved minimum-necessary policy.
- Provider webhooks record queued, sent, delivered, failed, and inbound events with provider identifiers.
- Inbound messages match an active thread and patient using destination, source number, and bounded correlation rules.
- Ambiguous or unknown senders enter a restricted identity-review queue without displaying chart context.
- Each thread has one staff or pool assignment, service state, unread count, and response deadline.
- Opt-out keywords close promotional outreach immediately and route clinically necessary communication for policy review.
- Attachments or unsupported media generate a safe notice and staff exception rather than silent loss.

## Frappe realization

- **DocTypes:** `OC Patient SMS Thread`, `OC SMS Message`, and `OC SMS Webhook Event` store patient, phone, consent basis, assignment, provider IDs, direction, body, and status.
- **Integration:** Frappe SMS settings select the approved gateway; signed whitelisted webhook methods validate and deduplicate provider events.
- **Assignment/notifications:** Assignment Rules route inbound threads; Notification Log alerts the assigned staff or pool.
- **Permissions:** Patient Communications User and Communications Supervisor use facility/patient user permissions; raw webhook payloads are audit-restricted.
- **Surfaces:** Desk chat-style page, patient communication timeline, exception queue, and delivery Script Report.

## Boundaries

Owns: SMS thread state, message evidence, and staff custody. Consumes: patient identity, consent, preferences, and gateway events. Emits: communication attempts, replies, and opt-out signals. Does not own: carrier delivery or clinical advice policy.

## Open questions

- What identity challenge is required before discussing sensitive information in an inbound SMS thread?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Unified Patient Communication Attempt Log](openchart-feature-catalog-msg-037-unified-patient-communication-attempt-log.md)
