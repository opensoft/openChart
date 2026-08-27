# Specialty Authorization Tracking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Tracks specialty-medication authorization dependencies, appeals, effective periods, and renewal milestones across payer and clinical teams.
Topics: openchart-feature-catalog, eprescribing, frappe, specialty-authorization
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-024 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Appeal evidence timeline** — Teams could compare denial reasons, added evidence, and successive determinations in one view.

## Focus

This feature isolates long-running authorization coordination for specialty medications. It layers milestones around ePA cases without flattening payer determinations or clinical review into a single status.

## Behavior

- Coordinators link one or more ePA, medical-benefit, appeal, or assistance cases to the specialty therapy episode.
- The tracker shows prerequisites, owner, due date, payer status, effective period, quantity limits, and renewal date.
- Denials retain exact reasons and support a separately reviewed appeal path.
- Conflicting or expired determinations block a misleading ready-to-dispense status.
- Scheduled reminders create review tasks before effective periods lapse.
- Authorization completion informs coordination but never starts dispensing or administration automatically.

## Frappe realization

- **DocTypes:** `OC Specialty Authorization Episode` links authorization cases and contains milestone, determination, appeal, and effective-period child rows.
- **Workflow:** Intake → Prerequisites → Submitted → Pending → Approved/Denied/Appeal → Expired/Closed.
- **Hooks:** `scheduler_events` creates renewal tasks; linked ePA updates recalculate readiness and publish notifications.
- **Surfaces:** Gantt/Kanban, coordinator dashboard, expiring-authorizations Query Report, and patient timeline summary support operations.

## Boundaries

Owns: cross-case authorization milestones and effective readiness. Consumes: benefit investigation, ePA determinations, and therapy plans. Emits: due tasks and reviewed readiness status. Does not own: payer decisions, prescribing, dispensing, or administration.

## Open questions

- How should conflicting pharmacy-benefit and medical-benefit authorizations be represented?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Specialty Dispensing Coordination](openchart-feature-catalog-phr-025-specialty-dispensing-coordination.md)
