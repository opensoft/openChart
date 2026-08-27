# Invalid Immunization Dose Review — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Flags doses that violate minimum age, interval, product, or series rules and routes them for documented clinical review.
Topics: openchart-feature-catalog, public-health, frappe, invalid-dose-review
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-006 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Repeat-dose candidate** — Feed reviewed invalidity into an explainable catch-up calculation.

## Focus

Human adjudication of potentially invalid doses without deleting historical administration evidence.

## Behavior

- The engine creates a review item when an accepted or imported dose fails a governed validity rule.
- Reviewers see the dose, violated rule, dates, calculations, source, and schedule release.
- Dispositions are valid, invalid, indeterminate, data-corrected, or rule-exception with rationale.
- Marking a dose invalid changes evaluation eligibility but never erases the historical event.
- Corrected dates or products require a successor administration record and automatic reevaluation.
- Conflicting registry and local determinations remain visible with separate authority labels.

## Frappe realization

- **DocTypes:** Add `OC Invalid Dose Review` linked to immunization, evaluation, and rule, with calculation evidence and disposition fields.
- **Workflow:** Use open, assigned, adjudicated, reopened, and superseded states with Assignment Rules.
- **Permissions:** Grant queue access to `OC Immunization Reviewer`; restrict final dispositions to `OC Clinician` at permlevel 1.
- **Hooks and surfaces:** Create items after schedule evaluation, trigger reevaluation after disposition, and provide a Query Report plus patient-chart warning panel.

## Boundaries

Owns: validity review and local disposition. Consumes: doses and schedule-rule evidence. Emits: eligibility status for forecasting. Does not own: source-record deletion or registry correction policy.

## Open questions

- Which rule exceptions require a second clinical reviewer?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
