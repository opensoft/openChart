# Self-Hosted Open-Weights Profile — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Defines infrastructure, isolation, licensing, update, and evidence requirements for locally operated open-weight models.
Topics: openchart-feature-catalog, clinical-ai, frappe, self-hosted-models
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-032 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Air-gapped deployment dossier** — Capture hashes, containers, weights, runtime, and validation evidence for disconnected sites.

## Focus

This feature isolates a deployment profile for self-hosted inference without assuming local hosting is inherently safe.

## Behavior

- Operators register weight identifier and hash, license, runtime image digest, quantization, hardware, network policy, data paths, and update source.
- Health checks verify model identity, schema behavior, resource limits, and absence of unapproved outbound connections.
- Each deployment pins validation evidence for its exact weights and runtime combination.
- Weight, runtime, quantization, or material hardware changes create a new version requiring reevaluation.
- Operators can monitor capacity, queue depth, and failure state without viewing patient prompts.
- Self-hosting does not bypass enablement, human review, fairness, or provenance requirements.

## Frappe realization

- **DocTypes:** `OC Self Hosted Model Profile` stores immutable digests, license evidence, runtime/hardware metadata, network policy, health state, and evaluation Links.
- **Workflow:** Draft → Infrastructure Review → Validation → Approved → Available → Suspended/Retired.
- **Roles/permissions:** `OC AI Infrastructure Operator` maintains runtime fields; AI governors approve use; clinical payloads remain inaccessible.
- **Hooks/jobs/reports:** scheduler health probes via adapter; change validation creates successors; Workspace reports capacity and identity drift.

## Boundaries

Owns: self-hosted deployment identity and operating evidence. Consumes: weights, runtime, infrastructure, and validation runs. Emits: governed deployment profile and health. Does not own: model license interpretation or clinical activation.

## Open questions

- Which runtime measurements are needed to prove an air-gapped deployment remains unchanged?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Model Endpoint Credential Health](openchart-feature-catalog-aic-047-model-endpoint-credential-health.md)
