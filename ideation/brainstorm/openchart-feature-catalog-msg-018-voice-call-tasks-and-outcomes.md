# Voice-call Tasks and Outcomes — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Structures outbound and inbound call work with attempt timing, interpreter needs, outcome codes, and follow-up actions.
Topics: openchart-feature-catalog, messaging-tasks, frappe, voice-call-tasks
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-018 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Softphone launch integration** — Start an approved call from the task while passing only the minimum routing context.

## Focus

This feature isolates human phone-call work and structured outcomes rather than telephony infrastructure or scripted clinical programs.

## Behavior

- Staff create or receive a call task with patient, purpose, destination, due time, assignment, and interpreter requirement.
- Starting an attempt records actor and time before displaying the verified destination number.
- Staff choose an approved outcome such as reached patient, reached proxy, voicemail, no answer, wrong number, declined, or escalated.
- Outcomes may require notes, identity-verification result, follow-up task, or next-attempt time.
- Proxy contact records relationship and authority without assuming consent from mere availability.
- Wrong-number and do-not-call outcomes immediately raise contact-data or registry review.
- A call task remains open when its outcome policy requires another attempt or supervisor action.
- Completion history preserves every attempt and its source, even when later corrected.

## Frappe realization

- **DocTypes:** `OC Voice Call Task`, `OC Call Attempt`, and `OC Call Outcome` store purpose, destination reference, interpreter flag, timestamps, code, notes, and follow-up.
- **Workflow:** Planned → In Progress → Waiting/Completed/Escalated/Cancelled with outcome-driven guarded transitions.
- **API/client:** a call-start method reveals the number only after permission and do-not-contact checks; Quick Entry captures attempt outcomes.
- **Assignment/notification:** Assignment Rules route tasks; Notification Log tracks due and reassigned work.
- **Reports:** Query Report covers reach rate, attempts per completion, outcome mix, and overdue calls.

## Boundaries

Owns: call-task state and structured attempt outcomes. Consumes: contact data, consent, interpreter needs, and scripts. Emits: communication attempts and follow-up tasks. Does not own: telephony service, recording, or clinical script content.

## Open questions

- Which call purposes may leave voicemail, and what content is permitted?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Post-procedure Scripted Follow-up Calls](openchart-feature-catalog-msg-035-post-procedure-scripted-follow-up-calls.md)
