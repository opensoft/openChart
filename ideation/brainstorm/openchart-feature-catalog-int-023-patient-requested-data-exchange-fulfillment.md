# Patient-requested Data Exchange Fulfillment — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enables patients, authorized representatives, and release staff to turn requester authority, destination, format, scope, delivery method, and due date into tracked electronic fulfillment or a reasoned denial with appeal path.
Topics: openchart-feature-catalog, interoperability, frappe, patient-exchange-request
Repository context: openChart — Frappe v15 native EMR; catalog entry INT-023 (Interoperability Exchange And APIs)
Captured: 2026-08-24

## Possible feats

- **Policy-aware automation** — Add human-reviewed rules that prioritize exceptions and due work while preserving consent, provenance, and explicit authority.

## Focus

This feature isolates patient-requested data exchange fulfillment: tracked electronic fulfillment or a reasoned denial with appeal path. It keeps transport and workflow decisions explicit rather than hiding them inside unrelated clinical screens.

## Behavior

- **Actor:** Patients, authorized representatives, and release staff initiate or administer the capability under role and patient-context checks.
- **Input:** The system accepts requester authority, destination, format, scope, delivery method, and due date and records the initiating actor, purpose, source, and correlation ID.
- **Output:** A successful operation produces tracked electronic fulfillment or a reasoned denial with appeal path plus a durable audit reference.
- **States:** Records move through submitted, identity-review, scope-review, producing, delivered, denied, appealed; transitions are server-authoritative and timestamped.
- **Permissions:** Read, administer, approve, replay, and export rights are separable; patient and facility user permissions narrow row access.
- **Edge cases:** Retries use stable idempotency keys, late responses retain their original correlation, and accepted clinical records are corrected by succession rather than overwritten.
- **Error path:** Identity mismatch, unavailable destination, or protected-content conflict pauses fulfillment without silently narrowing scope.
- **Safety:** Imports and disclosures enforce consent and minimum-necessary rules, and no integration failure or score triggers autonomous clinical action.

## Frappe realization

- **DocTypes:** `OC Patient Exchange Request` uses naming series `OC-INT-.YYYY.-.#####` with Links for consumer, patient, organization, and source; JSON payload metadata; state, purpose, correlation ID, policy version, and provenance fields.
- **Workflow:** A Frappe Workflow models `submitted, identity-review, scope-review, producing, delivered, denied, appealed` with reasons mandatory on rejection, override, replay, suspension, and retirement transitions.
- **Roles and permissions:** `Release of Information Specialist` receives task-specific DocPerms; `Interoperability Manager`, `Clinical Data Auditor`, and `System Manager` have distinct administration, review, and emergency levels, constrained by user permissions.
- **Hooks and jobs:** `validate` enforces identifiers, policy, consent, and transition invariants; `on_update` emits canonical events; `scheduler_events` and RQ background jobs execute channels, retries, expiry, and reconciliation outside web requests.
- **API:** Extend Frappe's native REST and OAuth2 with whitelisted `open_chart.api.v1.exchange.patient_request` methods; direct clinical writes remain guarded behind the supported `open_chart.api.v1` surface.
- **Surfaces:** Provide a patient portal request form and staff Kanban, with realtime websocket progress, Notification Log assignments, and Query or Script Reports for exceptions and audit evidence.

## Boundaries

Owns: the configuration, state, evidence, and operator controls for patient-requested data exchange fulfillment. Consumes: authorized identity, consent, source data, policy versions, and partner configuration. Emits: typed outcomes, canonical events, provenance, metrics, and audit evidence. Does not own: external destination operation.

## Open questions

- Which conformance profile, retention period, approval threshold, and facility-level override should govern the first supported release?

## Relationships

[Synthesis: Interoperability Exchange And APIs](openchart-feature-catalog-synthesis-int.md)
