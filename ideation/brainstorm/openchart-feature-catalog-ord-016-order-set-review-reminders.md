# Order Set Review Reminders — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Detects order sets approaching or exceeding review dates and routes accountable reminders through escalation.
Topics: openchart-feature-catalog, cpoe, frappe, order-set-review
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-016 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Evidence-change watch** — Flag sets whose cited guidance has been superseded for curator review.

## Focus

This feature isolates stale-content detection and accountable review scheduling.

## Behavior

- Published sets carry owner, review interval, next-review date, and escalation contacts.
- Owners receive reminders before due date and worklist entries when overdue.
- Completing review records disposition: no change, successor required, retire, or withdraw.
- Overdue status is visible to clinicians applying the set according to organization policy.
- Escalation never auto-publishes, edits, or retires clinical content.
- Reassignment preserves previous owner and reminder evidence.

## Frappe realization

- **DocTypes:** `OC Content Review Task` links the order set version, owner, due date, disposition, and completion evidence.
- **Workflow:** Due → In Review → Completed or Escalated; the order set retains its independent publication state.
- **Roles/permissions:** content owners update assigned tasks; `OC Order Set Publisher` controls resulting content transitions.
- **Scheduler/surface:** `scheduler_events.daily` creates reminders and escalations; REST filters on assignee/status/due_date and a Query Report provide the stale-content worklist.

## Boundaries

Owns: review deadlines, reminders, and disposition evidence. Consumes: published set metadata and ownership. Emits: review tasks and escalations. Does not own: content changes or withdrawal decisions.

## Open questions

- Should an overdue set remain usable with warning or become unavailable after a grace period?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Order Set Approval And Publishing](openchart-feature-catalog-ord-015-order-set-approval-and-publishing.md)
