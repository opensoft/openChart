# Model Regression Scoring Runs — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Executes repeatable model evaluations against approved cases and compares quality, safety, latency, and cost with release thresholds.
Topics: openchart-feature-catalog, clinical-ai, frappe, regression-scoring
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-023 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Candidate-versus-baseline dossier** — Generate a signed comparison packet for governance review.

## Focus

This feature isolates evaluation execution and regression evidence for model, prompt, adapter, or policy changes.

## Behavior

- An evaluator selects immutable case-set, model, prompt, adapter, and scoring versions for a run.
- Background jobs execute each case with fixed parameters and record outputs, citations, safety findings, latency, and cost.
- Deterministic scorers and blinded human reviewers produce separate scores and disagreement records.
- The run compares results with an approved baseline and flags threshold failures by stratum and failure class.
- A passing run supplies evidence but never activates a model automatically.
- Partial, timed-out, or contaminated runs remain visible and cannot be represented as passing.

## Frappe realization

- **DocTypes:** `OC AI Evaluation Run`, child case results, `OC AI Score`, and `OC AI Release Threshold` pin every component and baseline.
- **Workflow:** Planned → Running → Human Review → Complete/Invalidated.
- **Roles/permissions:** evaluators execute; blinded clinical scorers review assigned cases; AI governors approve thresholds separately.
- **Jobs/reports:** rq batches cases idempotently; scheduler resumes interrupted runs; Script Reports, Dashboard Charts, and PDF print format provide regression dossiers.

## Boundaries

Owns: repeatable run evidence and baseline comparison. Consumes: approved cases and component versions. Emits: scored evaluation dossier. Does not own: activation, clinical truth, or silent threshold changes.

## Open questions

- Which safety failures should invalidate an entire run regardless of aggregate score?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Shadow-Mode Deployment](openchart-feature-catalog-aic-024-shadow-mode-deployment.md)
