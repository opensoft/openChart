# Telephone Encounter Documentation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Documents clinical telephone contacts with caller identity, advice, disposition, and escalation.
Topics: openchart-feature-catalog, clinical-documentation, frappe, telephone-encounter
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-008 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Structured callback outcomes** — Could close the loop on unresolved calls.

## Focus

Documents clinical telephone contacts with caller identity, advice, disposition, and escalation. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Clinician or triage nurse may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires caller identity, call direction, reason, assessment, advice, and disposition.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable draft record; validation failure creates no accepted clinical content.
- **Transitions:** Draft → Triage Review → Signed; urgent dispositions require acknowledged escalation. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a signed telephone encounter with explicit follow-up state; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Telephone Encounter` is a submittable clinical DocType with naming series `OC-.#####`; key fields are patient, caller, direction, started_at, reason, assessment, advice, disposition.
- **Workflow:** Frappe Workflow implements Draft → Triage Review → Signed; urgent dispositions require acknowledged escalation. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Triage Nurse`, `OC Clinician` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Desk form, call print format, and optional inbound-call API; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
