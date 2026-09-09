# Explainability And Input Panel — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Shows reviewers why an AI output was produced, which inputs were used, and which limitations apply without overstating causal certainty.
Topics: openchart-feature-catalog, clinical-ai, frappe, explainability
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-038 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Source exclusion inspection** — Reveal which eligible sources were omitted by policy, permissions, freshness, or retrieval limits.

## Focus

This feature isolates a common reviewer panel for provenance, evidence, model behavior, and uncertainty.

## Behavior

- Every supported artifact exposes capability, model/version, profile, generated time, source list, citations, confidence meaning, and policy limits.
- The panel distinguishes provider explanations, retrieval evidence, deterministic rules, and openChart-computed metadata.
- Reviewers can inspect source versions they are authorized to read and see inaccessible or expired evidence as labeled gaps.
- The interface avoids causal claims when the model supplies only attention, feature contribution, or similarity signals.
- Users can report unsupported claims, missing sources, or misleading explanations from the panel.
- Absence of explanation support is visible and can block capabilities whose policy requires it.

## Frappe realization

- **DocTypes:** `OC AI Explanation` stores artifact Link, explanation type, method/version, input manifest, citations, limitations, and report disposition.
- **Roles/permissions:** source permissions are rechecked at view time; auditors may see manifests while reviewers see only workflow-relevant evidence.
- **Hooks/API/surfaces:** whitelisted explanation endpoint composes normalized evidence; reusable Desk dialog and portal component render it; client code never fetches unauthorized sources.
- **Reports:** unsupported-claim feedback becomes assignments and aggregate Script Reports.

## Boundaries

Owns: explanation presentation and provenance navigation. Consumes: artifact, invocation, citations, model metadata, and permissions. Emits: reviewer understanding and issue reports. Does not own: proof of clinical correctness or model internals.

## Open questions

- Which explanation methods are sufficiently stable and meaningful for each capability class?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [AI Artifact Registry](openchart-feature-catalog-aic-001-ai-artifact-registry.md)
