# Preventive Screening Rule Engine — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Produces explainable preventive-screening due lists from versioned age, risk, interval, and recommendation-grade rules.
Topics: openchart-feature-catalog, public-health, frappe, preventive-screening-rules
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-028 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Guideline comparison** — Show how alternative governed rule sets change a patient's due list.

## Focus

General preventive screening evaluation with recommendation grade and evidence, leaving action to clinicians.

## Behavior

- Clinical users evaluate a patient against an active screening-rule release and as-of date.
- Rules consider age, sex-relevant clinical factors, risk conditions, prior tests, intervals, and exclusions.
- Results are due, overdue, up-to-date, not-applicable, conditional, or indeterminate.
- Every result displays rule identifier, grade, source release, evidence inputs, and missing data.
- Users record reviewed dispositions without changing rule output or placing autonomous orders.
- Rule publication requires tests, review, effective dates, and preservation of prior evaluations.

## Frappe realization

- **DocTypes:** Add `OC Preventive Rule Release`, child `OC Screening Rule`, and immutable `OC Screening Evaluation` with structured evidence rows.
- **Workflow:** Govern releases through draft, test, clinical-review, published, active, and retired states.
- **Permissions:** Separate rule authors, `OC Preventive Care Reviewer`, and clinical consumers; apply patient User Permissions.
- **API and surfaces:** Add deterministic evaluation methods, a patient care-gap panel, cohort Query Report, and rule-test Script Report.

## Boundaries

Owns: versioned screening rules and evaluations. Consumes: accepted demographics, problems, results, and procedures. Emits: explainable due states. Does not own: orders, appointments, outreach, or proprietary guideline content.

## Open questions

- How should conflicting recommendation bodies be selected and displayed by site policy?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
