# HISP Connectivity Management — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enables Direct and security administrators to turn HISP endpoints, account identifiers, certificates, routing settings, and test messages into validated HISP connections with health and failover evidence.
Topics: openchart-feature-catalog, interoperability, frappe, hisp-connectivity
Repository context: openChart — Frappe v15 native EMR; catalog entry INT-033 (Interoperability Exchange And APIs)
Captured: 2026-08-24

## Possible feats

- **Policy-aware automation** — Add human-reviewed rules that prioritize exceptions and due work while preserving consent, provenance, and explicit authority.

## Focus

This feature isolates hisp connectivity management: validated HISP connections with health and failover evidence. It keeps transport and workflow decisions explicit rather than hiding them inside unrelated clinical screens.

## Behavior

- **Actor:** Direct and security administrators initiate or administer the capability under role and patient-context checks.
- **Input:** The system accepts HISP endpoints, account identifiers, certificates, routing settings, and test messages and records the initiating actor, purpose, source, and correlation ID.
- **Output:** A successful operation produces validated HISP connections with health and failover evidence plus a durable audit reference.
- **States:** Records move through configured, testing, active, degraded, suspended, retired; transitions are server-authoritative and timestamped.
- **Permissions:** Read, administer, approve, replay, and export rights are separable; patient and facility user permissions narrow row access.
- **Edge cases:** Retries use stable idempotency keys, late responses retain their original correlation, and accepted clinical records are corrected by succession rather than overwritten.
- **Error path:** Failed tests prevent activation and production credentials never appear in reports.
- **Safety:** Imports and disclosures enforce consent and minimum-necessary rules, and no integration failure or score triggers autonomous clinical action.

## Frappe realization

- **DocTypes:** `OC HISP Connection` uses naming series `OC-INT-.YYYY.-.#####` with Links for consumer, patient, organization, and source; JSON payload metadata; state, purpose, correlation ID, policy version, and provenance fields.
- **Workflow:** A Frappe Workflow models `configured, testing, active, degraded, suspended, retired` with reasons mandatory on rejection, override, replay, suspension, and retirement transitions.
- **Roles and permissions:** `Direct Trust Administrator` receives task-specific DocPerms; `Interoperability Manager`, `Clinical Data Auditor`, and `System Manager` have distinct administration, review, and emergency levels, constrained by user permissions.
- **Hooks and jobs:** `validate` enforces identifiers, policy, consent, and transition invariants; `on_update` emits canonical events; `scheduler_events` and RQ background jobs execute channels, retries, expiry, and reconciliation outside web requests.
- **API:** Extend Frappe's native REST and OAuth2 with whitelisted `open_chart.api.v1.direct.hisp` methods; direct clinical writes remain guarded behind the supported `open_chart.api.v1` surface.
- **Surfaces:** Provide a connection console and health dashboard, with realtime websocket progress, Notification Log assignments, and Query or Script Reports for exceptions and audit evidence.

## Boundaries

Owns: the configuration, state, evidence, and operator controls for hisp connectivity management. Consumes: authorized identity, consent, source data, policy versions, and partner configuration. Emits: typed outcomes, canonical events, provenance, metrics, and audit evidence. Does not own: HISP service delivery.

## Open questions

- Which conformance profile, retention period, approval threshold, and facility-level override should govern the first supported release?

## Relationships

[Synthesis: Interoperability Exchange And APIs](openchart-feature-catalog-synthesis-int.md)
