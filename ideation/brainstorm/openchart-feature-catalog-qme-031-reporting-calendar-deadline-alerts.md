# Annual Reporting Calendar And Deadline Alerts — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates program deadlines, internal milestones, owners, dependencies, and escalations across the annual quality-reporting cycle.
Topics: openchart-feature-catalog, quality-reporting, frappe, reporting-calendar
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-031 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Critical path forecast** — Predict which unresolved validations or approvals threaten an external deadline.

## Focus

One accountable calendar connecting external reporting dates to internal readiness and evidence tasks.

## Behavior

- A compliance officer records program, authority, due date, timezone, source citation, applicability, and responsible owner.
- Milestones include library update, period open, interim review, completeness check, lock, approval, submission, response, and archive.
- Deadlines can recur from approved templates but require annual confirmation before activation.
- Status is planned, confirmed, in-progress, at-risk, met, missed, waived, or superseded.
- Alerts escalate by configurable lead time, severity, dependency state, and owner chain.
- Date changes preserve prior values, source evidence, approver, and affected task recalculation.
- Calendar completion links to submission or evidence records rather than relying on an unchecked box.

## Frappe realization

- **DocTypes:** Add `OC Reporting Deadline` and child milestones with program, authority, source URL/Data, timezone, dates, owner, dependency links, and evidence.
- **Workflow:** Use draft, confirmed, active, met/missed/waived, and superseded states with `OC Compliance Officer` approval.
- **Scheduler and notifications:** Run daily alerts through scheduler events, Notification Log, Email Alerts, and Assignment Rules.
- **Surfaces:** Provide Calendar/Gantt views, annual workspace, at-risk Number Cards, and dependency Script Reports.

## Boundaries

Owns: local reporting calendar, milestones, alerts, and completion evidence. Consumes: authoritative dates, period state, tasks, and submission records. Emits: assignments, escalations, and audit history. Does not own: regulator deadlines or delivery guarantees.

## Open questions

- Which deadline sources can be monitored automatically without weakening mandatory human confirmation?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
