# Prior Authorization 278 Transport Channel — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enables payer interface administrators to turn trading partner, endpoint, identifiers, 278 profile, attachments route, credentials, and response timing into secure prior-authorization request and response transport with status correlation.
Topics: openchart-feature-catalog, interoperability, frappe, x12-prior-auth
Repository context: openChart — Frappe v15 native EMR; catalog entry INT-053 (Interoperability Exchange And APIs)
Captured: 2026-08-24

## Possible feats

- **Policy-aware automation** — Add human-reviewed rules that prioritize exceptions and due work while preserving consent, provenance, and explicit authority.

## Focus

This feature isolates prior authorization 278 transport channel: secure prior-authorization request and response transport with status correlation. It keeps transport and workflow decisions explicit rather than hiding them inside unrelated clinical screens.

## Behavior

- **Actor:** Payer interface administrators initiate or administer the capability under role and patient-context checks.
- **Input:** The system accepts trading partner, endpoint, identifiers, 278 profile, attachments route, credentials, and response timing and records the initiating actor, purpose, source, and correlation ID.
- **Output:** A successful operation produces secure prior-authorization request and response transport with status correlation plus a durable audit reference.
- **States:** Records move through configured, testing, active, degraded, suspended; transitions are server-authoritative and timestamped.
- **Permissions:** Read, administer, approve, replay, and export rights are separable; patient and facility user permissions narrow row access.
- **Edge cases:** Retries use stable idempotency keys, late responses retain their original correlation, and accepted clinical records are corrected by succession rather than overwritten.
- **Error path:** Unmatched responses enter a reconciliation queue and never update an authorization silently.
- **Safety:** Imports and disclosures enforce consent and minimum-necessary rules, and no integration failure or score triggers autonomous clinical action.

## Frappe realization

- **DocTypes:** `OC X12 Prior Auth Channel` uses naming series `OC-INT-.YYYY.-.#####` with Links for consumer, patient, organization, and source; JSON payload metadata; state, purpose, correlation ID, policy version, and provenance fields.
- **Workflow:** A Frappe Workflow models `configured, testing, active, degraded, suspended` with reasons mandatory on rejection, override, replay, suspension, and retirement transitions.
- **Roles and permissions:** `Payer Interface Administrator` receives task-specific DocPerms; `Interoperability Manager`, `Clinical Data Auditor`, and `System Manager` have distinct administration, review, and emergency levels, constrained by user permissions.
- **Hooks and jobs:** `validate` enforces identifiers, policy, consent, and transition invariants; `on_update` emits canonical events; `scheduler_events` and RQ background jobs execute channels, retries, expiry, and reconciliation outside web requests.
- **API:** Extend Frappe's native REST and OAuth2 with whitelisted `open_chart.api.v1.connectors.x12_prior_auth` methods; direct clinical writes remain guarded behind the supported `open_chart.api.v1` surface.
- **Surfaces:** Provide a channel console and unmatched-response report, with realtime websocket progress, Notification Log assignments, and Query or Script Reports for exceptions and audit evidence.

## Boundaries

Owns: the configuration, state, evidence, and operator controls for prior authorization 278 transport channel. Consumes: authorized identity, consent, source data, policy versions, and partner configuration. Emits: typed outcomes, canonical events, provenance, metrics, and audit evidence. Does not own: clinical or payer authorization decisions.

## Open questions

- Which conformance profile, retention period, approval threshold, and facility-level override should govern the first supported release?

## Relationships

[Synthesis: Interoperability Exchange And APIs](openchart-feature-catalog-synthesis-int.md)
