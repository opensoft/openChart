# Offline Mobile Documentation Queue — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Queues encrypted mobile encounter drafts offline and reconciles them safely when connectivity returns.
Topics: openchart-feature-catalog, clinical-documentation, frappe, offline-documentation
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-070 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Selective offline patient lists** — Could be pre-authorized for home visits.

## Focus

Queues encrypted mobile encounter drafts offline and reconciles them safely when connectivity returns. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Authorized mobile clinician may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires device-bound session, encounter snapshot, local edits, attachments, and base revisions.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable queued offline record; validation failure creates no accepted clinical content.
- **Transitions:** Queued Offline → Syncing → Applied, Conflict, Rejected, or Expired; signing requires online verification. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives synchronized drafts or explicit conflicts without silent overwrite or offline signature; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Mobile Sync Envelope` is a submittable clinical DocType with naming series `OC-.#####`; key fields are device_id, user, encounter, base_revision, payload_hash, queued_at, synced_at, conflict_status.
- **Workflow:** Frappe Workflow implements Queued Offline → Syncing → Applied, Conflict, Rejected, or Expired; signing requires online verification. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Mobile Clinician`, `OC Clinical Administrator` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Mobile Web Form/PWA surface, whitelisted sync API, and conflict workspace; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
