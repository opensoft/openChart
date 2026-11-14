# Two-way SMS Appointment Confirmation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Interprets consented inbound SMS replies to confirm, decline, or request help for an appointment.
Topics: openchart-feature-catalog, scheduling, frappe, sms-confirmation
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-014 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Multilingual keyword sets** — Support approved reply vocabularies by patient language.

## Focus

This feature isolates closed-loop SMS confirmation and exception routing for scheduled appointments.

## Behavior

- A reminder provides explicit reply choices such as confirm, cancel request, or help.
- Inbound messages are matched to a recent appointment using verified destination and correlation token.
- Recognized confirmation updates confirmation state without changing clinical appointment state.
- Cancellation language creates a policy-evaluated request rather than cancelling blindly.
- Ambiguous, unmatched, or free-text replies route to a staff work queue with the original message.
- Opt-out keywords immediately suppress future SMS and preserve consent-change provenance.

## Frappe realization

- **DocTypes:** `OC Appointment Message` with direction, provider_message_id, appointment, normalized_intent, status, and redacted payload reference.
- **API:** a signed whitelisted webhook validates provider signatures, deduplicates callbacks, and invokes `open_chart.api.v1.scheduling.record_reply`.
- **Workflow:** Received → Interpreted → Applied/Escalated; Assignment Rules and Notification Log alert staff to exceptions.

## Boundaries

Owns: scheduling-specific SMS interpretation and confirmation. Consumes: messages, consent, and appointment context. Emits: confirmation or staff task. Does not own: general patient messaging.

## Open questions

- How long may an inbound reply be correlated without an explicit token?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Appointment Reminder Cadence](openchart-feature-catalog-sch-013-appointment-reminder-cadence.md)
