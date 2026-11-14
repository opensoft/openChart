# Interpreter-included Outbound Communications — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates qualified interpreter participation and translated materials for outbound patient communications requiring language support.
Topics: openchart-feature-catalog, messaging-tasks, frappe, interpreter-communications
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-025 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Interpreter conference launch** — Join staff, patient, and approved interpreter from a call task with audited participant roles.

## Focus

This feature isolates language-access fulfillment as part of communication planning and evidence, not merely a patient language field.

## Behavior

- Communication planning checks preferred spoken and written language plus documented interpreter need.
- Staff select a translated approved template, a qualified interpreter, or an exception path before outreach.
- Interpreter participation records organization, interpreter identifier, language, modality, start/end, and confidentiality status.
- Family-member interpretation requires explicit exception reason and patient agreement where policy permits it.
- Unavailable language support delays nonurgent contact or escalates urgent contact to a supervisor-defined alternative.
- Translated content version and source-language version remain linked for review.
- The patient communication log distinguishes interpreter-assisted, translated-only, and language-matched staff contact.
- Interpreter notes do not become clinical documentation unless entered through an authorized chart workflow.

## Frappe realization

- **DocTypes:** `OC Language Support Plan`, `OC Interpreter Participation`, and `OC Translation Version` link patient, communication, language, interpreter, modality, timing, and exceptions.
- **Workflow:** Requested → Scheduled/In Progress → Completed/Unavailable/Cancelled for interpreter participation.
- **Assignment:** Assignment Rules route language-support requests to qualified pools; Notification Log sends staff coordination events.
- **API/permissions:** guarded interpreter lookup returns minimum eligible identity; Language Access Coordinator manages providers and exceptions.
- **Surfaces:** call-task panel, outbound composition gate, Calendar view, and unmet-language-needs report.

## Boundaries

Owns: communication language-support coordination and evidence. Consumes: language preference, interpreter eligibility, templates, and communication plan. Emits: participation records and readiness state. Does not own: interpreter credentialing or clinical translation adjudication.

## Open questions

- Which outbound communication types require qualified interpretation rather than translated text alone?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Voice-call Tasks and Outcomes](openchart-feature-catalog-msg-018-voice-call-tasks-and-outcomes.md)
