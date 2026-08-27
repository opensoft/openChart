# Correction Feedback For Evaluation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures reviewer edits and corrections as governed evaluation candidates without silently retraining production models.
Topics: openchart-feature-catalog, clinical-ai, frappe, correction-feedback
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-037 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Correction taxonomy mining** — Identify recurring reviewed error classes for new tests and prompt revisions.

## Focus

This feature isolates the safe learning loop from human corrections to future evaluation assets.

## Behavior

- Review workflows may capture original output, final edited form, structured correction classes, reviewer rationale, and source evidence.
- Reviewers can opt out of feedback reuse where policy or consent requires.
- Feedback enters a quarantine queue and is not sent to providers or training pipelines automatically.
- Curators verify data rights, de-identify where required, remove leakage, and choose evaluation-only, design-insight, or rejected disposition.
- Approved feedback can create successor evaluation cases with provenance to the correction, not alter prior golden answers silently.
- Metrics distinguish collected, curated, and incorporated feedback.

## Frappe realization

- **DocTypes:** `OC AI Correction Feedback` stores artifact, diff, taxonomy, rationale, consent/use basis, classification, curator, and resulting case Link.
- **Workflow:** Captured → Quarantined → Privacy Review → Clinical Curation → Evaluation Approved/Rejected.
- **Roles/permissions:** reviewers submit; privacy and evaluation curators access according to source classification; vendors receive no direct access.
- **Hooks/jobs/surfaces:** destination `on_submit` may calculate diff; rq de-identification support creates a review draft; Kanban curation queue and aggregate reports track outcomes.

## Boundaries

Owns: correction capture, curation, and evaluation reuse evidence. Consumes: generated and human-edited content plus reuse authority. Emits: approved evaluation candidates or design insights. Does not own: training or silent model updates.

## Open questions

- What consent or employment-policy basis governs reuse of clinician edits for evaluation?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Model Evaluation Case Registry](openchart-feature-catalog-aic-022-model-evaluation-case-registry.md)
