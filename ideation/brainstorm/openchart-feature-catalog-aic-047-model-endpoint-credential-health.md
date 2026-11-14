# Model Endpoint Credential Health — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Monitors model endpoint identity, availability, certificate, credential, and rotation state without exposing secrets.
Topics: openchart-feature-catalog, clinical-ai, frappe, endpoint-health
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-047 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Zero-downtime credential rotation** — Validate a successor credential in shadow health checks before human-approved cutover.

## Focus

This feature isolates operational trust and secret lifecycle for inference endpoints.

## Behavior

- Operators register endpoint identity expectations, certificate rules, secret owner, rotation interval, and health-check method.
- Scheduled checks record DNS/TLS identity, reachability, schema response, credential validity, and provider status without patient context.
- Expiry warnings route to secret owners and site administrators before the due date.
- Failed identity or credential checks suspend new invocations under policy and preserve manual workflows.
- Rotation requires dual-control where configured, masked validation, explicit cutover, and rollback reference.
- Logs never store secret values, authorization headers, or patient prompts.

## Frappe realization

- **DocTypes:** `OC AI Endpoint Health`, `OC AI Credential Rotation` and adapter secret metadata store expected identity, nonsecret fingerprints, due dates, checks, owner, and state.
- **Workflow:** rotation Planned → Successor Entered → Validated → Approved → Cut Over/Rolled Back.
- **Roles/permissions:** `OC AI Infrastructure Operator` manages encrypted Password fields; auditors read nonsecret evidence only.
- **Jobs/surfaces:** scheduler health probes and expiry checks; Notifications, Number Cards, and Script Report show state; adapter hook denies unhealthy endpoints.

## Boundaries

Owns: endpoint and credential operational health evidence. Consumes: endpoint metadata, encrypted credentials, and health policy. Emits: healthy, warning, or deny state. Does not own: provider security or capability activation alone.

## Open questions

- Which health failures warrant immediate suspension versus bounded retries?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Inference Latency And Fallback Policy](openchart-feature-catalog-aic-048-inference-latency-and-fallback-policy.md)
