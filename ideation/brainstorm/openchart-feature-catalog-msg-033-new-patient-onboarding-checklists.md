# New-patient Onboarding Checklists — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Generates role-assigned onboarding tasks from an approved checklist while preserving patient progress, evidence, and exceptions.
Topics: openchart-feature-catalog, messaging-tasks, frappe, onboarding-checklist
Repository context: openChart — Frappe v15 native EMR; catalog entry MSG-033 (Messaging Tasks Notifications And Reminders)
Captured: 2026-08-24

## Possible feats

- **Onboarding readiness view** — Show missing patient, staff, and external prerequisites before the first visit.

## Focus

This feature isolates coordinated new-patient setup work such as records collection, consent review, portal activation, and clinical intake follow-up.

## Behavior

- An onboarding episode begins from an accepted patient registration event and active checklist version.
- Checklist steps declare owner role or pool, due offset, dependency, patient-visible label, and completion evidence.
- Conditional steps evaluate approved intake facts and record why they were included or skipped.
- Each generated task is independently assignable, completable, reopenable, and auditable.
- Dependencies block completion only where policy requires and display the unmet predecessor.
- Patient-facing prompts use preferences and never expose internal-only checklist steps.
- Checklist version changes affect future episodes unless a manager explicitly migrates open episodes with a preview.
- Episode completion summarizes completed, waived, skipped, and unresolved steps; waivers require reason and authority.

## Frappe realization

- **DocTypes:** `OC Onboarding Checklist`, `OC Onboarding Step`, `OC Patient Onboarding Episode`, and `OC Onboarding Step Instance` store version, conditions, ownership, due offsets, evidence, and state.
- **Workflow:** episode states Active → Blocked/Ready → Completed/Cancelled; waiver is a role-gated action.
- **Automation:** registration `after_insert` enqueues generation; `scheduler_events` issues due reminders without duplicating tasks.
- **Assignment/notifications:** Assignment Rules resolve role/pool destinations; Notification Log and approved patient channels deliver prompts.
- **Surfaces:** Desk progress board, patient portal checklist, and onboarding aging report.

## Boundaries

Owns: onboarding checklist orchestration and progress. Consumes: registration, intake facts, task/evidence services, and communication preferences. Emits: assigned tasks and readiness state. Does not own: patient identity, consent content, or clinical intake records.

## Open questions

- Which checklist steps may patients self-attest versus require staff verification?

## Relationships

[Synthesis: Messaging Tasks Notifications And Reminders](openchart-feature-catalog-synthesis-msg.md) · [Contextual Clinical Task Creation](openchart-feature-catalog-msg-007-contextual-clinical-task-creation.md)
