# Inference Latency And Fallback Policy — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Governs timeouts, retries, queues, and explicit model fallbacks by capability without hiding substitutions from users or auditors.
Topics: openchart-feature-catalog, clinical-ai, frappe, inference-fallback
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-048 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Fallback simulation** — Exercise provider outages and queue saturation against synthetic workflows before policy activation.

## Focus

This feature isolates resilience behavior when an inference path is slow or unavailable.

## Behavior

- Governors define synchronous budget, background threshold, retry count, idempotency, fallback eligibility, and manual alternative for each capability.
- Timeout moves work to a visible queued or failed state; it never leaves the user believing generation completed.
- A fallback model runs only when separately approved for the same capability, data boundary, output schema, and human-review level.
- Every substitution is disclosed on the artifact and preserves both attempted and successful invocation records.
- Consequential workflows cannot weaken review requirements to meet latency targets.
- Circuit breakers and queue limits prevent provider failures from exhausting clinical application workers.

## Frappe realization

- **DocTypes:** `OC AI Runtime Policy` stores capability budgets, retry, queue, circuit, fallback deployments, disclosure, and manual path.
- **Workflow:** Draft → Reliability Test → Approved → Active → Suspended/Retired.
- **Roles/permissions:** infrastructure operators propose; AI governors approve fallback equivalence; clinicians view runtime disposition.
- **Hooks/jobs/surfaces:** adapter wrapper applies timeouts/circuit state; rq queues long work with idempotency keys; websocket status and Dashboard Charts expose latency and fallback rates.

## Boundaries

Owns: inference resilience and transparent fallback selection. Consumes: adapter health, capability policy, and approved deployments. Emits: queued, failed, primary, or disclosed fallback outcome. Does not own: manual workflow behavior or reduced human oversight.

## Open questions

- Which capabilities should prohibit model fallback and require manual completion instead?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Pluggable Model Adapter Contract](openchart-feature-catalog-aic-002-pluggable-model-adapter-contract.md)
