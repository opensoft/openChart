# Rapid Clinician Consult Chat — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides fast clinician-to-clinician consult chat with chart snapshot links, response expectations, and explicit disposition.
Topics: openchart-feature-catalog, messaging-tasks, frappe, clinician-consult
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-028 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Consult availability presence** — Publish service-level availability without exposing personal schedule details.

## Focus

This feature isolates time-sensitive informal consultation that needs more structure than chat but less ceremony than a formal referral.

## Behavior

- An authorized clinician starts a consult with patient, question, urgency, requested specialty or colleague, and selected chart snapshot links.
- Snapshot links identify source version and require current chart permission when opened.
- The receiving clinician may accept, decline with reason, redirect to an eligible service, or request clarification.
- Accepted consults show a response target and escalation policy appropriate to urgency.
- Replies are append-only and identify author, time, and linked evidence.
- Closure requires a disposition such as advice provided, formal referral recommended, direct evaluation needed, or no recommendation.
- Consult content is not automatically part of the legal clinical note; users receive a prompt to document through the proper workflow when required.
- Unavailable or unauthorized recipients route to a service pool or exception without exposing patient context.

## Frappe realization

- **DocTypes:** `OC Rapid Consult`, `OC Consult Entry`, and `OC Consult Snapshot Link` hold patient, requester, service, urgency, sources, state, target, and disposition.
- **Workflow:** Requested → Accepted/Declined/Redirected → Active → Closed/Escalated.
- **Assignment/notifications:** Assignment Rules select specialty pools; Notification Log and websocket realtime events support rapid desk delivery.
- **Permissions:** Clinician and Consult Service Manager roles combine patient/facility user permissions with service membership.
- **Surfaces/API:** chat-style Desk page, chart launch action, and guarded accept/reply/disposition methods.

## Boundaries

Owns: consult request, conversation, response state, and disposition. Consumes: patient context, clinician eligibility, and coverage. Emits: advice conversation and follow-up prompts. Does not own: formal referral, orders, or clinical-note attestation.

## Open questions

- Which consult dispositions must trigger mandatory chart documentation before closure?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Order Clarification Threads](openchart-feature-catalog-msg-029-order-clarification-threads.md)
