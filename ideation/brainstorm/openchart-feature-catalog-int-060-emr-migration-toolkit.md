# EMR Migration Toolkit — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enables implementation teams and clinical data stewards to turn source inventory, extract files, mapping template, validation rules, cutover plan, and rehearsal baseline into repeatable staged migrations with dry-run, reconciliation, and signed acceptance evidence.
Topics: openchart-feature-catalog, interoperability, frappe, emr-migration
Repository context: openChart — Frappe v15 native EMR; catalog entry INT-060 (Interoperability Exchange And APIs)
Captured: 2026-08-24

## Possible feats

- **Policy-aware automation** — Add human-reviewed rules that prioritize exceptions and due work while preserving consent, provenance, and explicit authority.

## Focus

This feature isolates emr migration toolkit: repeatable staged migrations with dry-run, reconciliation, and signed acceptance evidence. It keeps transport and workflow decisions explicit rather than hiding them inside unrelated clinical screens.

## Behavior

- **Actor:** Implementation teams and clinical data stewards initiate or administer the capability under role and patient-context checks.
- **Input:** The system accepts source inventory, extract files, mapping template, validation rules, cutover plan, and rehearsal baseline and records the initiating actor, purpose, source, and correlation ID.
- **Output:** A successful operation produces repeatable staged migrations with dry-run, reconciliation, and signed acceptance evidence plus a durable audit reference.
- **States:** Records move through assessed, mapped, rehearsing, validated, cutover-ready, migrated, rolled-back; transitions are server-authoritative and timestamped.
- **Permissions:** Read, administer, approve, replay, and export rights are separable; patient and facility user permissions narrow row access.
- **Edge cases:** Retries use stable idempotency keys, late responses retain their original correlation, and accepted clinical records are corrected by succession rather than overwritten.
- **Error path:** Failed reconciliation blocks cutover and rollback affects only the current migration batch.
- **Safety:** Imports and disclosures enforce consent and minimum-necessary rules, and no integration failure or score triggers autonomous clinical action.

## Frappe realization

- **DocTypes:** `OC Migration Project` uses naming series `OC-INT-.YYYY.-.#####` with Links for consumer, patient, organization, and source; JSON payload metadata; state, purpose, correlation ID, policy version, and provenance fields.
- **Workflow:** A Frappe Workflow models `assessed, mapped, rehearsing, validated, cutover-ready, migrated, rolled-back` with reasons mandatory on rejection, override, replay, suspension, and retirement transitions.
- **Roles and permissions:** `Clinical Data Migration Manager` receives task-specific DocPerms; `Interoperability Manager`, `Clinical Data Auditor`, and `System Manager` have distinct administration, review, and emergency levels, constrained by user permissions.
- **Hooks and jobs:** `validate` enforces identifiers, policy, consent, and transition invariants; `on_update` emits canonical events; `scheduler_events` and RQ background jobs execute channels, retries, expiry, and reconciliation outside web requests.
- **API:** Extend Frappe's native REST and OAuth2 with whitelisted `open_chart.api.v1.migration.projects` methods; direct clinical writes remain guarded behind the supported `open_chart.api.v1` surface.
- **Surfaces:** Provide a migration workspace, Gantt, and quality dashboard, with realtime websocket progress, Notification Log assignments, and Query or Script Reports for exceptions and audit evidence.

## Boundaries

Owns: the configuration, state, evidence, and operator controls for emr migration toolkit. Consumes: authorized identity, consent, source data, policy versions, and partner configuration. Emits: typed outcomes, canonical events, provenance, metrics, and audit evidence. Does not own: source vendor extraction services.

## Open questions

- Which conformance profile, retention period, approval threshold, and facility-level override should govern the first supported release?

## Relationships

[Synthesis: Interoperability Exchange And APIs](openchart-feature-catalog-synthesis-int.md)
