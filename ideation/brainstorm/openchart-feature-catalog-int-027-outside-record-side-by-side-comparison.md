# Outside-record Side-by-side Comparison — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enables clinicians and reconciliation specialists to turn local record, external candidate, normalized fields, source, and effective dates into field-level differences with accept, reject, and defer controls.
Topics: openchart-feature-catalog, interoperability, frappe, record-comparison
Repository context: openChart — Frappe v15 native EMR; catalog entry INT-027 (Interoperability Exchange And APIs)
Captured: 2026-08-24

## Possible feats

- **Policy-aware automation** — Add human-reviewed rules that prioritize exceptions and due work while preserving consent, provenance, and explicit authority.

## Focus

This feature isolates outside-record side-by-side comparison: field-level differences with accept, reject, and defer controls. It keeps transport and workflow decisions explicit rather than hiding them inside unrelated clinical screens.

## Behavior

- **Actor:** Clinicians and reconciliation specialists initiate or administer the capability under role and patient-context checks.
- **Input:** The system accepts local record, external candidate, normalized fields, source, and effective dates and records the initiating actor, purpose, source, and correlation ID.
- **Output:** A successful operation produces field-level differences with accept, reject, and defer controls plus a durable audit reference.
- **States:** Records move through unreviewed, matching, conflicting, accepted, rejected, deferred; transitions are server-authoritative and timestamped.
- **Permissions:** Read, administer, approve, replay, and export rights are separable; patient and facility user permissions narrow row access.
- **Edge cases:** Retries use stable idempotency keys, late responses retain their original correlation, and accepted clinical records are corrected by succession rather than overwritten.
- **Error path:** Unmapped or clinically ambiguous fields remain unresolved and are never auto-selected.
- **Safety:** Imports and disclosures enforce consent and minimum-necessary rules, and no integration failure or score triggers autonomous clinical action.

## Frappe realization

- **DocTypes:** `OC External Record Comparison` uses naming series `OC-INT-.YYYY.-.#####` with Links for consumer, patient, organization, and source; JSON payload metadata; state, purpose, correlation ID, policy version, and provenance fields.
- **Workflow:** A Frappe Workflow models `unreviewed, matching, conflicting, accepted, rejected, deferred` with reasons mandatory on rejection, override, replay, suspension, and retirement transitions.
- **Roles and permissions:** `Clinical Reconciliation Specialist` receives task-specific DocPerms; `Interoperability Manager`, `Clinical Data Auditor`, and `System Manager` have distinct administration, review, and emergency levels, constrained by user permissions.
- **Hooks and jobs:** `validate` enforces identifiers, policy, consent, and transition invariants; `on_update` emits canonical events; `scheduler_events` and RQ background jobs execute channels, retries, expiry, and reconciliation outside web requests.
- **API:** Extend Frappe's native REST and OAuth2 with whitelisted `open_chart.api.v1.exchange.compare` methods; direct clinical writes remain guarded behind the supported `open_chart.api.v1` surface.
- **Surfaces:** Provide a two-column comparison page, with realtime websocket progress, Notification Log assignments, and Query or Script Reports for exceptions and audit evidence.

## Boundaries

Owns: the configuration, state, evidence, and operator controls for outside-record side-by-side comparison. Consumes: authorized identity, consent, source data, policy versions, and partner configuration. Emits: typed outcomes, canonical events, provenance, metrics, and audit evidence. Does not own: the external source's correctness.

## Open questions

- Which conformance profile, retention period, approval threshold, and facility-level override should govern the first supported release?

## Relationships

[Synthesis: Interoperability Exchange And APIs](openchart-feature-catalog-synthesis-int.md)
