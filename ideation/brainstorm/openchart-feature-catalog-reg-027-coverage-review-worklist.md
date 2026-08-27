# Coverage Review Worklist — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Routes incomplete, conflicting, or unverified registration coverage records to accountable staff for resolution.
Topics: openchart-feature-catalog, registration, frappe, coverage-worklist
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-027 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Aging and urgency rules** — Prioritize unresolved coverage based on arrival date and configured service context.

## Focus

Coordinate human resolution of coverage-data quality exceptions, not electronic eligibility transactions.

## Behavior

- The system creates work items for unmatched payers, missing subscriber facts, conflicting order, expired cards, or OCR review.
- Each item records reason, patient, coverage, due date, priority, owner, and source registration.
- Coverage Reviewer can resolve, request patient information, mark not applicable, or escalate.
- Resolution requires structured outcome and notes when original data is retained.
- Duplicate work items for the same unresolved condition are consolidated without losing source references.
- Overdue and blocked items appear in supervisor views and do not disappear when an appointment passes.

## Frappe realization

- **DocTypes:** `OC Coverage Review Item` with issue_type, coverage, sources, priority, due_on, resolution, and Assignment integration.
- **Workflow:** Open → In Progress → Waiting for Information, Escalated, Resolved, or Canceled.
- **Roles/permissions:** `OC Coverage Reviewer` works items; `OC Registration Supervisor` reassigns and closes exceptions.
- **API/surfaces:** `open_chart.api.v1.registration.resolve_coverage_issue`; Desk worklist, Kanban, Number Cards, and aging Query Report.

## Boundaries

Owns: coverage-data exception routing and resolution. Consumes: registration validation findings. Emits: accountable corrections and status. Does not own: eligibility inquiry or claim follow-up.

## Open questions

- Which unresolved issue types should block registration readiness versus remain follow-up tasks?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
