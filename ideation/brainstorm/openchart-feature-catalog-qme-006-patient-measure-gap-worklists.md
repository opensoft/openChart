# Patient Measure Gap Worklists — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Converts not-met and incomplete measure results into prioritized, accountable patient worklists without autonomously directing care.
Topics: openchart-feature-catalog, quality-reporting, frappe, measure-gap-worklist
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-006 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Previsit gap briefing** — Assemble open measure gaps for clinician review before a scheduled encounter.

## Focus

Operational follow-up for measurement gaps while preserving the distinction between a reporting gap and a clinical recommendation.

## Behavior

- Completed measure runs create candidates for not-met, missing-data, and unresolved-exclusion results.
- Rules prioritize by deadline, measure weight, attribution, freshness, and configurable clinical review flags.
- Authorized coordinators assign, snooze, dismiss, or escalate items with a reason and due date.
- A gap can close through new accepted evidence, valid exclusion, attribution change, or documented non-action disposition.
- Clinical action always requires an authorized clinician and is never placed automatically from a measure gap.
- Patient opt-out, sensitive-record restrictions, and no-longer-attributed status suppress inappropriate outreach.
- Recalculation reconciles duplicate items and reopens a gap only with a new result version.

## Frappe realization

- **DocTypes:** Add `OC Measure Gap Task` linked to patient result, assignee, priority, disposition, due date, and resolution evidence.
- **Workflow:** Use new, assigned, in-review, snoozed, resolved, dismissed, and reopened states with Assignment Rules.
- **Roles and hooks:** Grant `OC Care Coordinator` workflow access, `OC Clinician` clinical disposition authority, and reconcile tasks after result completion.
- **Surfaces:** Provide a Kanban queue, patient-chart panel, team Number Cards, and permissioned Query Report.

## Boundaries

Owns: quality-gap task lifecycle. Consumes: patient results, attribution, consent, schedules, and permissions. Emits: assignments, dispositions, and closure evidence. Does not own: diagnosis, treatment, orders, or outreach delivery.

## Open questions

- Which gap categories may coordinators close without clinician review?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
