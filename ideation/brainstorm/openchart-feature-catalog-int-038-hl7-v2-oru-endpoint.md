# HL7 v2 ORU Endpoint — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enables interface engineers and result sources to turn ORU messages, order identifiers, observations, units, reference ranges, flags, and performers into discrete or document results linked to the correct patient and order.
Topics: openchart-feature-catalog, interoperability, frappe, hl7-oru
Repository context: openChart — Frappe v15 native EMR; catalog entry INT-038 (Interoperability Exchange And APIs)
Captured: 2026-08-24

## Possible feats

- **Policy-aware automation** — Add human-reviewed rules that prioritize exceptions and due work while preserving consent, provenance, and explicit authority.

## Focus

This feature isolates hl7 v2 oru endpoint: discrete or document results linked to the correct patient and order. It keeps transport and workflow decisions explicit rather than hiding them inside unrelated clinical screens.

## Behavior

- **Actor:** Interface engineers and result sources initiate or administer the capability under role and patient-context checks.
- **Input:** The system accepts ORU messages, order identifiers, observations, units, reference ranges, flags, and performers and records the initiating actor, purpose, source, and correlation ID.
- **Output:** A successful operation produces discrete or document results linked to the correct patient and order plus a durable audit reference.
- **States:** Records move through received, parsed, matched, normalized, applied, acknowledged, quarantined; transitions are server-authoritative and timestamped.
- **Permissions:** Read, administer, approve, replay, and export rights are separable; patient and facility user permissions narrow row access.
- **Edge cases:** Retries use stable idempotency keys, late responses retain their original correlation, and accepted clinical records are corrected by succession rather than overwritten.
- **Error path:** Unit, code, patient, or order ambiguity prevents result posting and returns a precise acknowledgment.
- **Safety:** Imports and disclosures enforce consent and minimum-necessary rules, and no integration failure or score triggers autonomous clinical action.

## Frappe realization

- **DocTypes:** `OC HL7 ORU Message` uses naming series `OC-INT-.YYYY.-.#####` with Links for consumer, patient, organization, and source; JSON payload metadata; state, purpose, correlation ID, policy version, and provenance fields.
- **Workflow:** A Frappe Workflow models `received, parsed, matched, normalized, applied, acknowledged, quarantined` with reasons mandatory on rejection, override, replay, suspension, and retirement transitions.
- **Roles and permissions:** `HL7 Interface Operator` receives task-specific DocPerms; `Interoperability Manager`, `Clinical Data Auditor`, and `System Manager` have distinct administration, review, and emergency levels, constrained by user permissions.
- **Hooks and jobs:** `validate` enforces identifiers, policy, consent, and transition invariants; `on_update` emits canonical events; `scheduler_events` and RQ background jobs execute channels, retries, expiry, and reconciliation outside web requests.
- **API:** Extend Frappe's native REST and OAuth2 with whitelisted `open_chart.api.v1.hl7.oru` methods; direct clinical writes remain guarded behind the supported `open_chart.api.v1` surface.
- **Surfaces:** Provide a ORU channel page and result reconciliation queue, with realtime websocket progress, Notification Log assignments, and Query or Script Reports for exceptions and audit evidence.

## Boundaries

Owns: the configuration, state, evidence, and operator controls for hl7 v2 oru endpoint. Consumes: authorized identity, consent, source data, policy versions, and partner configuration. Emits: typed outcomes, canonical events, provenance, metrics, and audit evidence. Does not own: clinical interpretation of results.

## Open questions

- Which conformance profile, retention period, approval threshold, and facility-level override should govern the first supported release?

## Relationships

[Synthesis: Interoperability Exchange And APIs](openchart-feature-catalog-synthesis-int.md)
