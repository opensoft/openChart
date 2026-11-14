# Result Follow-Up Deadline — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Assigns and tracks a clinically meaningful follow-up deadline distinct from immediate result acknowledgment.
Topics: openchart-feature-catalog, cpoe, frappe, result-follow-up
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-039 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Linked-action completion** — Close follow-up only when a referenced appointment, order, message, or documented decision satisfies policy.

## Focus

This feature isolates accountable completion after a result has been reviewed.

## Behavior

- The reviewer selects a follow-up action, owner, target date, priority, and completion evidence requirement.
- Default deadlines from policy are displayed and may be changed only with reason when allowed.
- Acknowledging the result does not complete an outstanding follow-up task.
- The owner records completion, deferral, patient unreachable, refusal, or transfer with supporting references.
- Overdue actions escalate through the result accountability ladder.
- Automated suggestions may propose a deadline, but a clinician confirms it.

## Frappe realization

- **DocTypes:** `OC Result Follow-Up` with accountability, action_type, owner, due_at, state, disposition, evidence links, and provenance.
- **Workflow:** Planned → In Progress → Completed, Deferred, Unable to Complete, or Escalated.
- **Roles/permissions:** accountable clinician creates; assigned users update; `OC Result Oversight` reviews overdue cases.
- **Scheduler/API/surface:** daily/hourly scheduler escalates due tasks; REST filters by owner/state/due range and a Query Report supply follow-up worklists.

## Boundaries

Owns: result-linked follow-up commitment and completion evidence. Consumes: acknowledged result and chosen action. Emits: tasks, dispositions, and escalations. Does not own: the linked clinical action itself.

## Open questions

- Which evidence types are sufficient to close each follow-up action category?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Incidental Finding Follow-Up](openchart-feature-catalog-ord-043-incidental-finding-follow-up.md)
