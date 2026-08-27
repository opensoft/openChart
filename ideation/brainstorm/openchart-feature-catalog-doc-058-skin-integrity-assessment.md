# Skin Integrity Assessment — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records pressure-injury risk and skin findings by location with reassessment cadence and escalation.
Topics: openchart-feature-catalog, clinical-documentation, frappe, skin-integrity
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-058 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Unit dashboards** — Could display due reassessments without exposing images.

## Focus

Records pressure-injury risk and skin findings by location with reassessment cadence and escalation. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Nurse or wound clinician may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires skin survey, risk instrument, devices, body locations, findings, and actions.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable draft record; validation failure creates no accepted clinical content.
- **Transitions:** Draft → Reviewed → Signed; concerning findings require acknowledged referral or plan. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a signed skin assessment with tracked exceptions; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Skin Integrity Assessment` is a submittable clinical DocType with naming series `OC-.#####`; key fields are encounter, instrument_version, score, finding_table, device_table, next_due_at.
- **Workflow:** Frappe Workflow implements Draft → Reviewed → Signed; concerning findings require acknowledged referral or plan. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Nurse`, `OC Wound Care Clinician` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Body map, bedside client script, and skin assessment print format; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
