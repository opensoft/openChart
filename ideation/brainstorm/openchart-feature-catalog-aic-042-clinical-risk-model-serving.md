# Clinical Risk Model Serving — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Serves deterioration, no-show, readmission, and other validated risk scores with provenance, intended use, and human-only response workflows.
Topics: openchart-feature-catalog, clinical-ai, frappe, risk-model-serving
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-042 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Score trajectory review** — Display successive valid scores with input and model changes rather than implying continuous monitoring.

## Focus

This feature isolates governed runtime scoring for registered clinical and operational risk models.

## Behavior

- An approved event or authorized user requests a score for a declared model, population, use, and prediction horizon.
- The result shows score, band, generated time, input freshness, model/version, intended use, exclusions, and validation status.
- Scores outside population, with missing critical inputs, or beyond validity duration are labeled invalid or unavailable.
- A score may create a human-review work item only under approved policy; it cannot diagnose, order, schedule, cancel, or treat.
- Reviewers document acknowledgment and disposition separately from score generation.
- New model versions never overwrite historical scores.

## Frappe realization

- **DocTypes:** `OC AI Risk Score` stores patient/encounter, model/version, horizon, input manifest, score/band, validity, explanation, artifact, and review disposition.
- **Workflow:** Generated → Valid/Invalid → Pending Human Review → Reviewed/Expired.
- **Roles/permissions:** capability-specific clinical or operational roles view scores; service account cannot act on destination DocTypes.
- **Hooks/jobs/surfaces:** approved doc_events or scheduler enqueue scoring; whitelisted on-demand method; Workspace worklists and charts display provenance and freshness.

## Boundaries

Owns: versioned risk score and review evidence. Consumes: approved input context and validated model. Emits: informational score and optional human task. Does not own: diagnosis, treatment, scheduling action, or clinical monitoring.

## Open questions

- Which score classes may be recomputed on schedule versus only at explicit workflow milestones?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Clinical Model Validation Evidence](openchart-feature-catalog-aic-043-clinical-model-validation-evidence.md)
