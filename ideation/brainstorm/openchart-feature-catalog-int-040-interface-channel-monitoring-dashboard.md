# Interface Channel Monitoring Dashboard — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enables interface operators and service owners to turn message counts, latency, acknowledgments, errors, queue depth, and endpoint health into near-real-time throughput and failure visibility per channel.
Topics: openchart-feature-catalog, interoperability, frappe, channel-monitoring
Repository context: openChart — Frappe v15 native EMR; catalog entry INT-040 (Interoperability Exchange And APIs)
Captured: 2026-08-24

## Possible feats

- **Policy-aware automation** — Add human-reviewed rules that prioritize exceptions and due work while preserving consent, provenance, and explicit authority.

## Focus

This feature isolates interface channel monitoring dashboard: near-real-time throughput and failure visibility per channel. It keeps transport and workflow decisions explicit rather than hiding them inside unrelated clinical screens.

## Behavior

- **Actor:** Interface operators and service owners initiate or administer the capability under role and patient-context checks.
- **Input:** The system accepts message counts, latency, acknowledgments, errors, queue depth, and endpoint health and records the initiating actor, purpose, source, and correlation ID.
- **Output:** A successful operation produces near-real-time throughput and failure visibility per channel plus a durable audit reference.
- **States:** Records move through healthy, warning, degraded, halted, maintenance; transitions are server-authoritative and timestamped.
- **Permissions:** Read, administer, approve, replay, and export rights are separable; patient and facility user permissions narrow row access.
- **Edge cases:** Retries use stable idempotency keys, late responses retain their original correlation, and accepted clinical records are corrected by succession rather than overwritten.
- **Error path:** Stale telemetry is labeled explicitly and cannot present an unobserved channel as healthy.
- **Safety:** Imports and disclosures enforce consent and minimum-necessary rules, and no integration failure or score triggers autonomous clinical action.

## Frappe realization

- **DocTypes:** `OC Interface Channel Metric` uses naming series `OC-INT-.YYYY.-.#####` with Links for consumer, patient, organization, and source; JSON payload metadata; state, purpose, correlation ID, policy version, and provenance fields.
- **Workflow:** A Frappe Workflow models `healthy, warning, degraded, halted, maintenance` with reasons mandatory on rejection, override, replay, suspension, and retirement transitions.
- **Roles and permissions:** `Integration Operator` receives task-specific DocPerms; `Interoperability Manager`, `Clinical Data Auditor`, and `System Manager` have distinct administration, review, and emergency levels, constrained by user permissions.
- **Hooks and jobs:** `validate` enforces identifiers, policy, consent, and transition invariants; `on_update` emits canonical events; `scheduler_events` and RQ background jobs execute channels, retries, expiry, and reconciliation outside web requests.
- **API:** Extend Frappe's native REST and OAuth2 with whitelisted `open_chart.api.v1.channels.metrics` methods; direct clinical writes remain guarded behind the supported `open_chart.api.v1` surface.
- **Surfaces:** Provide a Dashboard Charts, Number Cards, and channel workspace, with realtime websocket progress, Notification Log assignments, and Query or Script Reports for exceptions and audit evidence.

## Boundaries

Owns: the configuration, state, evidence, and operator controls for interface channel monitoring dashboard. Consumes: authorized identity, consent, source data, policy versions, and partner configuration. Emits: typed outcomes, canonical events, provenance, metrics, and audit evidence. Does not own: external partner uptime.

## Open questions

- Which conformance profile, retention period, approval threshold, and facility-level override should govern the first supported release?

## Relationships

[Synthesis: Interoperability Exchange And APIs](openchart-feature-catalog-synthesis-int.md)
