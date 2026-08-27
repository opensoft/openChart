# Model Evaluation Case Registry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Curates versioned synthetic or de-identified evaluation cases with expected criteria, provenance, and authorized use.
Topics: openchart-feature-catalog, clinical-ai, frappe, evaluation-cases
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-022 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Coverage matrix** — Show which specialties, risks, languages, demographics, and failure modes lack evaluation cases.

## Focus

This feature isolates golden-set case governance from model runs and release decisions.

## Behavior

- Evaluation authors create synthetic or explicitly de-identified input bundles for one capability and schema version.
- Each case defines expected facts, prohibited claims, citation requirements, scoring rubric, demographic strata, and provenance.
- Clinical reviewers approve cases and lock accepted versions; edits create successors.
- Access and export restrictions follow the case's data classification and consent basis.
- Cases can be active, quarantined for leakage concerns, retired, or superseded.
- Production feedback cannot enter a case set until separately reviewed and de-identified.

## Frappe realization

- **DocTypes:** `OC AI Evaluation Case` with capability, input Attach/JSON, rubric child table, expected evidence, prohibited output, strata, classification, and successor Link.
- **Workflow:** Draft → Clinical Review → Privacy Review → Approved → Active → Quarantined/Retired.
- **Roles/permissions:** `OC AI Evaluator`, `OC Clinical AI Reviewer`, and `OC Privacy Reviewer` hold separate transition rights.
- **Hooks/surfaces:** `validate` enforces SYN- identifiers or de-identification evidence; Data Import supports curated batches; coverage Query Report and Workspace manage sets.

## Boundaries

Owns: governed evaluation inputs and rubrics. Consumes: capability schemas and reviewed synthetic/de-identified data. Emits: immutable case versions for runs. Does not own: production retraining or release approval.

## Open questions

- What minimum case diversity is required before a capability can leave shadow mode?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Model Regression Scoring Runs](openchart-feature-catalog-aic-023-model-regression-scoring-runs.md)
