# HL7 v2 ADT Endpoint — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enables interface engineers and registration systems to turn ADT messages, sender facility, version, profile, acknowledgment mode, and patient identifiers into validated admit, discharge, transfer, and demographic events with acknowledgments.
Topics: openchart-feature-catalog, interoperability, frappe, hl7-adt
Repository context: openChart — Frappe v15 native EMR; catalog entry INT-036 (Interoperability Exchange And APIs)
Captured: 2026-08-24

## Possible feats

- **Policy-aware automation** — Add human-reviewed rules that prioritize exceptions and due work while preserving consent, provenance, and explicit authority.

## Focus

This feature isolates hl7 v2 adt endpoint: validated admit, discharge, transfer, and demographic events with acknowledgments. It keeps transport and workflow decisions explicit rather than hiding them inside unrelated clinical screens.

## Behavior

- **Actor:** Interface engineers and registration systems initiate or administer the capability under role and patient-context checks.
- **Input:** The system accepts ADT messages, sender facility, version, profile, acknowledgment mode, and patient identifiers and records the initiating actor, purpose, source, and correlation ID.
- **Output:** A successful operation produces validated admit, discharge, transfer, and demographic events with acknowledgments plus a durable audit reference.
- **States:** Records move through received, parsed, matched, applied, acknowledged, rejected, quarantined; transitions are server-authoritative and timestamped.
- **Permissions:** Read, administer, approve, replay, and export rights are separable; patient and facility user permissions narrow row access.
- **Edge cases:** Retries use stable idempotency keys, late responses retain their original correlation, and accepted clinical records are corrected by succession rather than overwritten.
- **Error path:** Identity conflicts quarantine the message and return a non-success acknowledgment without silent merge.
- **Safety:** Imports and disclosures enforce consent and minimum-necessary rules, and no integration failure or score triggers autonomous clinical action.

## Frappe realization

- **DocTypes:** `OC HL7 ADT Message` uses naming series `OC-INT-.YYYY.-.#####` with Links for consumer, patient, organization, and source; JSON payload metadata; state, purpose, correlation ID, policy version, and provenance fields.
- **Workflow:** A Frappe Workflow models `received, parsed, matched, applied, acknowledged, rejected, quarantined` with reasons mandatory on rejection, override, replay, suspension, and retirement transitions.
- **Roles and permissions:** `HL7 Interface Operator` receives task-specific DocPerms; `Interoperability Manager`, `Clinical Data Auditor`, and `System Manager` have distinct administration, review, and emergency levels, constrained by user permissions.
- **Hooks and jobs:** `validate` enforces identifiers, policy, consent, and transition invariants; `on_update` emits canonical events; `scheduler_events` and RQ background jobs execute channels, retries, expiry, and reconciliation outside web requests.
- **API:** Extend Frappe's native REST and OAuth2 with whitelisted `open_chart.api.v1.hl7.adt` methods; direct clinical writes remain guarded behind the supported `open_chart.api.v1` surface.
- **Surfaces:** Provide a ADT channel page and message trace, with realtime websocket progress, Notification Log assignments, and Query or Script Reports for exceptions and audit evidence.

## Boundaries

Owns: the configuration, state, evidence, and operator controls for hl7 v2 adt endpoint. Consumes: authorized identity, consent, source data, policy versions, and partner configuration. Emits: typed outcomes, canonical events, provenance, metrics, and audit evidence. Does not own: bed-management policy.

## Open questions

- Which conformance profile, retention period, approval threshold, and facility-level override should govern the first supported release?

## Relationships

[Synthesis: Interoperability Exchange And APIs](openchart-feature-catalog-synthesis-int.md)
