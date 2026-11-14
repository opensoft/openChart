# Note View and Edit Audit Trail — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records every authorized note view, draft edit, signature, addendum, amendment, print, and release event.
Topics: openchart-feature-catalog, clinical-documentation, frappe, note-audit
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-069 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Anomaly rules** — Could flag unusual access for human privacy review.

## Focus

Records every authorized note view, draft edit, signature, addendum, amendment, print, and release event. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Privacy officer, auditor, or authorized investigator may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires user, patient, note, event type, timestamp, purpose, session, and change metadata.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable audit events are append-only; ingestion failures block sensitive write actions or raise critical alerts record; validation failure creates no accepted clinical content.
- **Transitions:** Audit events are append-only; ingestion failures block sensitive write actions or raise critical alerts. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives an append-only audit trail queryable under restricted oversight permissions; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Clinical Access Audit` is a submittable clinical DocType with naming series `OC-.#####`; key fields are patient, clinical_note, actor, action, occurred_at, purpose, session_id, metadata_hash.
- **Workflow:** Frappe Workflow implements Audit events are append-only; ingestion failures block sensitive write actions or raise critical alerts. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Privacy Officer`, `OC Auditor` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** doc_events hooks, API middleware, restricted Script Report, and audit export; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
