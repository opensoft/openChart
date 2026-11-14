# Syndromic Surveillance Pipeline — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enables public-health interface operators to turn jurisdiction, facility, trigger, message profile, routing, credentials, and submission schedule into minimum-necessary syndromic messages with acknowledgment evidence.
Topics: openchart-feature-catalog, interoperability, frappe, syndromic-surveillance
Repository context: openChart — Frappe v15 native EMR; catalog entry INT-046 (Interoperability Exchange And APIs)
Captured: 2026-08-24

## Possible feats

- **Policy-aware automation** — Add human-reviewed rules that prioritize exceptions and due work while preserving consent, provenance, and explicit authority.

## Focus

This feature isolates syndromic surveillance pipeline: minimum-necessary syndromic messages with acknowledgment evidence. It keeps transport and workflow decisions explicit rather than hiding them inside unrelated clinical screens.

## Behavior

- **Actor:** Public-health interface operators initiate or administer the capability under role and patient-context checks.
- **Input:** The system accepts jurisdiction, facility, trigger, message profile, routing, credentials, and submission schedule and records the initiating actor, purpose, source, and correlation ID.
- **Output:** A successful operation produces minimum-necessary syndromic messages with acknowledgment evidence plus a durable audit reference.
- **States:** Records move through configured, testing, active, warning, suspended; transitions are server-authoritative and timestamped.
- **Permissions:** Read, administer, approve, replay, and export rights are separable; patient and facility user permissions narrow row access.
- **Edge cases:** Retries use stable idempotency keys, late responses retain their original correlation, and accepted clinical records are corrected by succession rather than overwritten.
- **Error path:** Missing required data or transport failure queues a retry and compliance-visible exception.
- **Safety:** Imports and disclosures enforce consent and minimum-necessary rules, and no integration failure or score triggers autonomous clinical action.

## Frappe realization

- **DocTypes:** `OC Syndromic Submission` uses naming series `OC-INT-.YYYY.-.#####` with Links for consumer, patient, organization, and source; JSON payload metadata; state, purpose, correlation ID, policy version, and provenance fields.
- **Workflow:** A Frappe Workflow models `configured, testing, active, warning, suspended` with reasons mandatory on rejection, override, replay, suspension, and retirement transitions.
- **Roles and permissions:** `Public Health Interface Operator` receives task-specific DocPerms; `Interoperability Manager`, `Clinical Data Auditor`, and `System Manager` have distinct administration, review, and emergency levels, constrained by user permissions.
- **Hooks and jobs:** `validate` enforces identifiers, policy, consent, and transition invariants; `on_update` emits canonical events; `scheduler_events` and RQ background jobs execute channels, retries, expiry, and reconciliation outside web requests.
- **API:** Extend Frappe's native REST and OAuth2 with whitelisted `open_chart.api.v1.public_health.syndromic` methods; direct clinical writes remain guarded behind the supported `open_chart.api.v1` surface.
- **Surfaces:** Provide a submission dashboard and exception report, with realtime websocket progress, Notification Log assignments, and Query or Script Reports for exceptions and audit evidence.

## Boundaries

Owns: the configuration, state, evidence, and operator controls for syndromic surveillance pipeline. Consumes: authorized identity, consent, source data, policy versions, and partner configuration. Emits: typed outcomes, canonical events, provenance, metrics, and audit evidence. Does not own: public-health case investigation.

## Open questions

- Which conformance profile, retention period, approval threshold, and facility-level override should govern the first supported release?

## Relationships

[Synthesis: Interoperability Exchange And APIs](openchart-feature-catalog-synthesis-int.md)
