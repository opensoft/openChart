# E/M Level Suggestion with Evidence — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Suggests an evaluation and management level from documented evidence while leaving coding selection to an authorized human.
Topics: openchart-feature-catalog, clinical-documentation, frappe, em-suggestion
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-042 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Policy version comparison** — Could explain changes after coding-rule updates.

## Focus

Suggests an evaluation and management level from documented evidence while leaving coding selection to an authorized human. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Clinician or clinical coder may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires encounter documentation, time attestations, problems, data, and risk evidence.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable generated record; validation failure creates no accepted clinical content.
- **Transitions:** Generated → Reviewed → Accepted, Changed, or Dismissed; never auto-submitted. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a non-binding level suggestion with transparent supporting and missing evidence; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC EM Suggestion` is a submittable clinical DocType with naming series `OC-.#####`; key fields are encounter, suggested_code, evidence_table, missing_evidence, generated_at, accepted_by.
- **Workflow:** Frappe Workflow implements Generated → Reviewed → Accepted, Changed, or Dismissed; never auto-submitted. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Clinician`, `OC Clinical Coder` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Whitelisted evaluation method and evidence side panel; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
