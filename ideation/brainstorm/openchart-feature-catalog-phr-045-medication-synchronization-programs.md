# Medication Synchronization Programs — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates patient-approved refill alignment into recurring medication pickup or delivery appointments with prescriber and pharmacy handoffs.
Topics: openchart-feature-catalog, eprescribing, frappe, medication-synchronization
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-045 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Synchronization readiness call** — A pre-cycle checklist could confirm medication changes, remaining supply, and delivery preferences.

## Focus

This feature isolates appointment-style medication synchronization. It coordinates dates and tasks but never renews, changes, or dispenses a prescription automatically.

## Behavior

- A patient or authorized proxy consents to a program and selects eligible maintenance medications and preferred cycle date.
- Staff record current supply, refill availability, short-fill needs, prescriber contacts, and exclusions.
- Each cycle creates review tasks for changed therapy, insufficient refills, authorization, stock, and patient confirmation.
- Short-fill or alignment proposals require prescriber and pharmacist decisions where applicable.
- Missed contact, hospitalization, medication change, or patient pause moves the cycle to exception review.
- Completion records pickup or delivery coordination separately from dispense and adherence evidence.

## Frappe realization

- **DocTypes:** `OC Medication Sync Program` and `OC Medication Sync Cycle` link patient consent, medications, target date, tasks, exceptions, and outcomes.
- **Workflow:** Enrollment → Active → Cycle Review → Ready → Coordinated, with Paused, Exception, and Ended states.
- **Hooks/jobs:** `scheduler_events` generate cycles and assignments before target dates; changes to linked prescriptions flag review.
- **Surfaces:** Calendar, patient portal consent/status page, coordinator Kanban, and due-cycle Query Report support the program.

## Boundaries

Owns: synchronization enrollment, cycle coordination, and exceptions. Consumes: consent, medication list, prescription/refill status, and patient preferences. Emits: tasks and appointment-style milestones. Does not own: prescription renewal, dispensing, or adherence determination.

## Open questions

- How should synchronization coordinate across multiple external pharmacies without implying shared inventory authority?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Adherence Follow-Up Tasks](openchart-feature-catalog-phr-046-adherence-follow-up-tasks.md)
