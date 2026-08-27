# Reportable Condition Worklist — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Gives public-health reporters a deadline-aware queue of potential and confirmed reportable conditions requiring disposition or submission.
Topics: openchart-feature-catalog, public-health, frappe, reportable-condition-worklist
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-025 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Coverage handoff** — Transfer accountability across shifts while retaining deadline ownership.

## Focus

One operational queue joining trigger evidence, reporting status, statutory timing, and accountable assignment.

## Behavior

- Reporters filter candidates by jurisdiction, condition, facility, deadline, evidence status, and assignee.
- Rows distinguish unreviewed trigger, report in progress, submitted, rejected, duplicate, excluded, and closed.
- Priority derives from governed deadline profiles and displays its calculation.
- Assignment, transfer, escalation, and disposition record actor, time, and reason.
- Clinical uncertainty remains visible and cannot be resolved by operational staff without authority.
- Missing rule or deadline configuration produces an explicit policy-gap lane.

## Frappe realization

- **DocTypes:** Add `OC Reportability Review Item` linked to triggers, reports, jurisdiction profile, deadline, and Assignment.
- **Workflow:** Use new, assigned, awaiting-clinical-review, reporting, submitted, resolved, and escalated states.
- **Permissions:** Give `OC Public Health Reporter` operational access and restrict clinical dispositions to `OC Clinician`.
- **Surfaces:** Build List/Kanban views, aging Query Reports, Number Cards, and deadline Notifications with no PHI in email bodies.

## Boundaries

Owns: review accountability and operational disposition. Consumes: trigger events, case reports, deadlines, and assignments. Emits: escalations and workflow status. Does not own: diagnosis or report payloads.

## Open questions

- Which deadline breaches require escalation outside the application?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
