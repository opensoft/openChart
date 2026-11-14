# Prompt And Context Audit Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Stores replayable prompt, policy, and context manifests for each invocation while minimizing duplicated PHI.
Topics: openchart-feature-catalog, clinical-ai, frappe, prompt-audit
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-021 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Controlled replay workspace** — Reconstruct an invocation against frozen inputs in an isolated evaluation environment.

## Focus

This feature isolates the evidence needed to explain and reproduce what a model received at generation time.

## Behavior

- Every invocation records prompt template and version, policy version, model deployment, parameters, source identifiers and versions, retrieval query, and context digest.
- Full context is retained only where policy requires; otherwise manifests point to versioned sources or encrypted snapshots.
- Authorized auditors can compare current records with the generation-time manifest and identify missing sources.
- Replay is disabled by default for live providers and requires an explicit evaluation purpose and permission.
- Redaction and retention actions preserve a tombstone and digest so audit gaps remain visible.
- Missing capture prevents an output from entering consequential review workflows.

## Frappe realization

- **DocTypes:** `OC AI Invocation` with prompt template Link, policy/model versions, parameter JSON, context manifest child rows, digest, provider trace, and replay eligibility.
- **Roles/permissions:** `OC AI Auditor` reads manifests; PHI snapshots use permlevel 2 and site-specific user permissions.
- **Hooks/API:** invocation creation is mandatory inside `open_chart.api.v1.ai.invoke`; `validate` enforces digest and source version fields; direct writes are guarded.
- **Jobs/surfaces:** rq replay jobs run only in evaluation queues; audit Script Report compares artifacts with invocation evidence.

## Boundaries

Owns: invocation-time prompt and context evidence. Consumes: templates, source snapshots, model configuration, and policy. Emits: replayable manifests and audit records. Does not own: source retention, model evaluation conclusions, or output acceptance.

## Open questions

- Which capabilities justify encrypted context snapshots instead of references plus digests?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [AI Interaction Export Feed](openchart-feature-catalog-aic-029-ai-interaction-export-feed.md)
