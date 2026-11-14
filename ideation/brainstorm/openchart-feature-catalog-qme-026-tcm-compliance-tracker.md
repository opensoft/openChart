# Transitional Care Management Compliance Tracker — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Tracks discharge receipt, interactive contact, medication reconciliation, visit timing, and evidence exceptions for transitional care compliance.
Topics: openchart-feature-catalog, quality-reporting, frappe, tcm-compliance
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-026 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Deadline recovery planner** — Show remaining compliant milestones and escalation options after a delayed transition event.

## Focus

Time-sensitive TCM milestone accountability from transition notification through reviewed episode close.

## Behavior

- A transition episode starts from an accepted discharge event or authorized manual intake with source provenance.
- The tracker calculates contact and visit due dates using the approved rule release, discharge date, and risk level.
- Milestones record attempts, successful contact, medication reconciliation, scheduled and completed visit, and responsible staff.
- Missing or conflicting discharge dates, risk levels, or facility types create exceptions before deadlines are inferred.
- Status is collecting, at-risk, milestone-met, milestone-missed, review, compliant, noncompliant, or superseded.
- Clinical work is initiated only by authorized users; the tracker may notify and assign but not place orders.
- Episode close preserves source cutoff, milestone evidence, exceptions, and reviewer attestation.

## Frappe realization

- **DocTypes:** Add `OC TCM Compliance Episode` and child `OC TCM Milestone` with transition source, dates, risk, attempts, evidence Dynamic Links, owner, and status.
- **Workflow:** Use active, at-risk, review, compliant, noncompliant, and superseded states with Assignment Rules.
- **Jobs and hooks:** Calculate deadlines on accepted transition, schedule reminders and overdue checks, and refresh after source succession.
- **Surfaces:** Provide Calendar/Gantt views, milestone Kanban, patient-chart card, and compliance Script Report.

## Boundaries

Owns: TCM milestone tracking and compliance evidence. Consumes: transitions, contacts, encounters, medication reconciliation, staff assignments, and rules. Emits: deadlines, alerts, and reviewed status. Does not own: clinical care, scheduling, billing, or discharge authority.

## Open questions

- How should failed contact attempts affect local escalation while remaining distinct from official compliance interpretation?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
