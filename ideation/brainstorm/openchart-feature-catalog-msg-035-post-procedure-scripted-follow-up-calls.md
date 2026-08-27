# Post-procedure Scripted Follow-up Calls — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Generates scheduled follow-up call tasks with versioned scripts, structured outcomes, and governed escalation after procedures.
Topics: openchart-feature-catalog, messaging-tasks, frappe, post-procedure-follow-up
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-035 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Follow-up completion bundle** — Present call evidence, escalations, linked encounters, and unresolved actions for procedural review.

## Focus

This feature isolates human-performed scripted outreach after a procedure without allowing script responses to diagnose or direct autonomous treatment.

## Behavior

- An accepted procedure completion event creates follow-up calls at offsets from an approved protocol version.
- Each task includes patient, procedure reference, due window, assigned pool, interpreter need, and versioned script.
- Staff verify patient or proxy identity before displaying protected questions.
- Answers use structured options plus permitted notes and preserve who reported them.
- Reviewed trigger answers create an urgent clinician-review task or display approved emergency instructions; they do not diagnose.
- No answer follows the protocol's bounded retry and fallback policy.
- Call completion requires outcome, script completion or exception, and links to any generated work.
- Procedure cancellation, readmission, or clinician stop instruction suppresses future calls with recorded reason.

## Frappe realization

- **DocTypes:** `OC Follow-up Call Protocol`, `OC Follow-up Call Instance`, and `OC Script Response` store procedure type, offsets, script version, task, responses, triggers, and disposition.
- **Workflow:** Planned → Due/In Progress → Completed/Escalated/Unreachable/Cancelled.
- **Automation:** procedure event hooks create bounded instances; `scheduler_events` activates due call tasks idempotently.
- **Assignment/notifications:** Assignment Rules route by procedure service and coverage; Notification Log signals due and trigger-generated work.
- **Surfaces:** guided call page, patient timeline summary, and follow-up outcome Script Report.

## Boundaries

Owns: post-procedure call protocol execution and response evidence. Consumes: procedure completion, scripts, contact policy, and call outcomes. Emits: completed follow-up and clinician-review work. Does not own: procedure record, diagnosis, or treatment decisions.

## Open questions

- Which trigger responses require synchronous handoff rather than queue escalation?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Voice-call Tasks and Outcomes](openchart-feature-catalog-msg-018-voice-call-tasks-and-outcomes.md)
