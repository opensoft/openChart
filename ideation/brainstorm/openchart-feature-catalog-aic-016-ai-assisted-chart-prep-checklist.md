# AI-Assisted Chart-Prep Checklist — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Drafts a visit-specific preparation checklist from chart context for staff confirmation and assignment.
Topics: openchart-feature-catalog, clinical-ai, frappe, chart-prep
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-016 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Team prep board** — Aggregate reviewed checklist items across tomorrow's assigned visits without exposing unrelated patient data.

## Focus

This feature isolates AI-assisted preparation tasks before an encounter, distinct from chart summarization and clinical action.

## Behavior

- Staff request a checklist for an appointment using an approved profile and current chart snapshot.
- Suggested items may identify records to review, histories to reconcile, forms to obtain, or questions to ask.
- Every item shows its source and whether it is informational, administrative, or requires a qualified clinician.
- A human confirms, edits, assigns, dismisses, or completes each item.
- Generated items cannot close care gaps, reconcile records, place orders, or contact patients automatically.
- Canceled or reassigned appointments expire or reroute the checklist under ordinary permissions.

## Frappe realization

- **DocTypes:** `OC AI Chart Prep Checklist` with appointment, profile, artifact, source snapshot, and child `OC Chart Prep Item` containing class, assignee, disposition, and source.
- **Workflow:** Generated → Pending Review → Active → Completed/Expired.
- **Roles/permissions:** care-team and scheduling user permissions filter visibility; clinical items require clinical assignees.
- **Hooks/jobs/surfaces:** optional scheduler prequeues drafts; Assignment Rules run only after human activation; appointment dashboard and Kanban show confirmed items.

## Boundaries

Owns: suggested preparation checklist and human activation. Consumes: appointment and chart context. Emits: assigned, reviewed prep work. Does not own: clinical reconciliation, patient outreach, or care-gap closure.

## Open questions

- Which administrative checklist classes may be activated by nonclinical staff?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Pre-Visit Chart Summary](openchart-feature-catalog-aic-007-pre-visit-chart-summary.md)
