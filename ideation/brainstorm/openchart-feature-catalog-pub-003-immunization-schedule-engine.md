# Immunization Schedule Engine — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Evaluates versioned vaccine schedule rules by age, indication, risk context, and accepted dose history.
Topics: openchart-feature-catalog, public-health, frappe, immunization-schedule
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-003 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Policy release comparison** — Preview cohort effects before activating a new schedule release.

## Focus

A governed, explainable rules engine that evaluates immunization series without autonomously ordering care.

## Behavior

- Clinical users request evaluation for a patient and an effective schedule date.
- Inputs include birth date, accepted doses, indications, contraindication context, and configured policy release.
- The engine returns series status, supporting rule identifiers, evidence dates, and missing-data warnings.
- Every result identifies the rule release and patient-data snapshot used.
- Ambiguous history yields an indeterminate result rather than an invented recommendation.
- Publishing or activating rule releases requires authorized review and never changes prior evaluations.

## Frappe realization

- **DocTypes:** Add `OC Immunization Schedule Release`, child `OC Schedule Rule`, and immutable `OC Schedule Evaluation` with JSON evidence plus structured result rows.
- **Workflow:** Govern releases through draft, clinical-review, published, active, and retired states with one active release per jurisdiction and date.
- **Roles:** Restrict authoring to `OC Clinical Rules Author`, approval to `OC Public Health Clinical Reviewer`, and viewing to clinical roles.
- **Hooks and API:** Run deterministic validation on release publication; expose `open_chart.api.v1.evaluate_immunization_schedule` and a Script Report showing rule explanations.

## Boundaries

Owns: versioned schedule logic and evaluations. Consumes: accepted immunizations, demographics, indications, and governed policy content. Emits: explainable series status. Does not own: orders, administrations, or external schedule licensing.

## Open questions

- Which schedule authority datasets can be redistributed with the application?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
