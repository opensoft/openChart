# Specialty Benefit Investigation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates benefits, network restrictions, site-of-care rules, and financial-assistance findings for a specialty medication referral.
Topics: openchart-feature-catalog, eprescribing, frappe, specialty-benefits
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-023 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Assistance-program referral tracking** — Approved programs could be linked with patient consent and expiration dates.

## Focus

This feature isolates the evidence-based investigation required before many specialty therapies can be dispensed. It separates verified payer facts from estimates, staff notes, and clinical decisions.

## Behavior

- A specialty coordinator opens an investigation for a selected therapy, patient, coverage, and intended site of care.
- The case records pharmacy versus medical benefit, network restrictions, specialty pharmacy mandates, cost sharing, and assistance options.
- Every finding stores source, contact or transaction reference, timestamp, verification status, and expiration.
- Missing or conflicting facts become assigned follow-ups rather than guessed defaults.
- Sensitive financial-assistance data is permissioned separately and disclosed only with appropriate patient authorization.
- Completion produces a reviewed summary for the care team without ordering, authorizing, or dispensing therapy.

## Frappe realization

- **DocTypes:** `OC Specialty Benefit Investigation` with child findings, contacts, assistance options, documents, and provenance links.
- **Workflow:** Open → Information Gathering → Verification → Reviewed → Complete/Unable to Complete.
- **Roles:** `OC Specialty Pharmacy Coordinator`, `OC Coverage Specialist`, and clinical reviewers receive field-level and transition-specific permissions.
- **Surfaces:** Specialty workspace, Kanban, task assignments, due-date reports, and a restricted patient-cost panel support coordination.

## Boundaries

Owns: specialty benefit investigation and verified summary. Consumes: coverage, therapy context, payer responses, and patient authorization. Emits: restrictions, next-step tasks, and cost findings. Does not own: payer adjudication, clinical appropriateness, or dispensing.

## Open questions

- Which assistance-program data may be retained in the clinical repository?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Specialty Authorization Tracking](openchart-feature-catalog-phr-024-specialty-authorization-tracking.md)
