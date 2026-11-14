# Full EHI Export Including Media — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enables patients, authorized representatives, and compliance staff to turn patient, legal scope, date range, export format, media inclusion, destination, and purpose into complete machine-readable EHI archive with manifest, media, checksums, and exclusions report.
Topics: openchart-feature-catalog, interoperability, frappe, ehi-export
Repository context: openChart — Frappe v15 native EMR; catalog entry INT-058 (Interoperability Exchange And APIs)
Captured: 2026-08-24

## Possible feats

- **Policy-aware automation** — Add human-reviewed rules that prioritize exceptions and due work while preserving consent, provenance, and explicit authority.

## Focus

This feature isolates full ehi export including media: complete machine-readable EHI archive with manifest, media, checksums, and exclusions report. It keeps transport and workflow decisions explicit rather than hiding them inside unrelated clinical screens.

## Behavior

- **Actor:** Patients, authorized representatives, and compliance staff initiate or administer the capability under role and patient-context checks.
- **Input:** The system accepts patient, legal scope, date range, export format, media inclusion, destination, and purpose and records the initiating actor, purpose, source, and correlation ID.
- **Output:** A successful operation produces complete machine-readable EHI archive with manifest, media, checksums, and exclusions report plus a durable audit reference.
- **States:** Records move through requested, identity-review, collecting, packaging, ready, delivered, expired, failed; transitions are server-authoritative and timestamped.
- **Permissions:** Read, administer, approve, replay, and export rights are separable; patient and facility user permissions narrow row access.
- **Edge cases:** Retries use stable idempotency keys, late responses retain their original correlation, and accepted clinical records are corrected by succession rather than overwritten.
- **Error path:** Oversized or unavailable media is reported explicitly and never omitted silently.
- **Safety:** Imports and disclosures enforce consent and minimum-necessary rules, and no integration failure or score triggers autonomous clinical action.

## Frappe realization

- **DocTypes:** `OC EHI Export Job` uses naming series `OC-INT-.YYYY.-.#####` with Links for consumer, patient, organization, and source; JSON payload metadata; state, purpose, correlation ID, policy version, and provenance fields.
- **Workflow:** A Frappe Workflow models `requested, identity-review, collecting, packaging, ready, delivered, expired, failed` with reasons mandatory on rejection, override, replay, suspension, and retirement transitions.
- **Roles and permissions:** `EHI Export Specialist` receives task-specific DocPerms; `Interoperability Manager`, `Clinical Data Auditor`, and `System Manager` have distinct administration, review, and emergency levels, constrained by user permissions.
- **Hooks and jobs:** `validate` enforces identifiers, policy, consent, and transition invariants; `on_update` emits canonical events; `scheduler_events` and RQ background jobs execute channels, retries, expiry, and reconciliation outside web requests.
- **API:** Extend Frappe's native REST and OAuth2 with whitelisted `open_chart.api.v1.portability.ehi_export` methods; direct clinical writes remain guarded behind the supported `open_chart.api.v1` surface.
- **Surfaces:** Provide a EHI request page and package manifest viewer, with realtime websocket progress, Notification Log assignments, and Query or Script Reports for exceptions and audit evidence.

## Boundaries

Owns: the configuration, state, evidence, and operator controls for full ehi export including media. Consumes: authorized identity, consent, source data, policy versions, and partner configuration. Emits: typed outcomes, canonical events, provenance, metrics, and audit evidence. Does not own: legal interpretation of designated record set.

## Open questions

- Which conformance profile, retention period, approval threshold, and facility-level override should govern the first supported release?

## Relationships

[Synthesis: Interoperability Exchange And APIs](openchart-feature-catalog-synthesis-int.md)
