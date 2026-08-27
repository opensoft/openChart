# Virtual Visit No-Show Workflow — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates outreach and accountable disposition when a patient does not answer or arrive for a virtual visit.
Topics: openchart-feature-catalog, telehealth, frappe, virtual-no-show
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-020 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Attempt cadence template** — Configure reviewed contact attempts by service without exposing sensitive details in messages.

## Focus

This feature isolates day-of no-answer detection, outreach attempts, and final virtual-visit disposition.

## Behavior

- Staff see whether the patient has not launched, is waiting elsewhere, disconnected, or failed identity checks before declaring no-show.
- After the configured grace period, authorized staff start an outreach episode rather than closing the appointment automatically.
- Each portal, phone, SMS, or email attempt records channel, actor, time, outcome, and minimum-necessary message template.
- A responding patient may be admitted, rescheduled, redirected, or marked too late according to human-applied policy.
- Final No Show or No Answer requires a reason and closes outstanding room grants and waiting presence.
- Safety-sensitive services may create a reviewed follow-up task, but no absence triggers autonomous clinical action.

## Frappe realization

- **DocTypes/workflow:** `OC Virtual No Show Episode` and child `OC Contact Attempt` use Open, Contacting, Recovered, Rescheduled, No Show, and Escalated states.
- **Automation:** scheduler events may flag overdue arrivals and notify assigned staff; only an authorized transition finalizes disposition.
- **Surfaces/permissions:** Telehealth Operations Kanban, appointment timeline, and Query Report serve staff; patient-facing messages use Notifications and consented channels.

## Boundaries

Owns: virtual no-answer evidence and disposition workflow. Consumes: appointment, arrival, room, and communication state. Emits: disposition and follow-up assignment. Does not own: fee assessment or clinical outreach policy.

## Open questions

- Which services require active safety follow-up when a patient misses a virtual appointment?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
