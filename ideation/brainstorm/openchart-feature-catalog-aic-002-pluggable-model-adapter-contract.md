# Pluggable Model Adapter Contract — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Defines a governed provider-neutral contract for ambient, summarization, drafting, and scoring model invocations.
Topics: openchart-feature-catalog, clinical-ai, frappe, model-adapters
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-002 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Capability conformance badges** — Publish which adapters pass streaming, citation, structured-output, and PHI-boundary tests.

## Focus

This feature isolates a stable invocation boundary so clinical workflows do not depend on one vendor's request, response, or authentication shape.

## Behavior

- Administrators register an adapter against explicit capabilities such as transcription, summarization, drafting, extraction, or risk scoring.
- Every request carries a capability, schema version, approved model deployment, context policy, timeout, and correlation identifier.
- Responses normalize content, citations, confidence, token usage, safety flags, and provider trace identifiers.
- Unsupported capability or schema combinations fail before patient context leaves openChart.
- Timeouts and provider errors produce reviewable failures; they never trigger a clinical action or invisible fallback.
- Adapter changes require validation and activation by an AI administrator.

## Frappe realization

- **DocTypes:** `OC AI Model Adapter` stores provider type, supported capabilities, endpoint reference, schema versions, timeout policy, and status; secrets remain in encrypted Password fields.
- **Workflow:** Draft → Validating → Approved → Active → Suspended/Retired.
- **Roles/permissions:** `OC AI Administrator` configures adapters and `OC AI Auditor` reads non-secret configuration evidence.
- **Hooks/API/background jobs:** adapter Python hooks expose typed invoke methods; `open_chart.api.v1.ai.invoke` validates policy; rq jobs handle long calls and publish websocket completion events.

## Boundaries

Owns: provider-neutral invocation and normalized response envelopes. Consumes: approved deployments and context policy. Emits: normalized generation results and telemetry. Does not own: workflow acceptance, model certification, or provider contracts.

## Open questions

- Which adapter capabilities must support deterministic structured output before activation?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Bring-Your-Own-Model Onboarding](openchart-feature-catalog-aic-031-bring-your-own-model-onboarding.md)
