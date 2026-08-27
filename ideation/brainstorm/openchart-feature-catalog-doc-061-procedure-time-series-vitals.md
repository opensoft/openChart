# Procedure Time-Series Vitals — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records high-frequency vital observations against procedure phases with device or manual source attribution.
Topics: openchart-feature-catalog, clinical-documentation, frappe, procedure-vitals
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-061 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Streaming adapters** — Could prefill device readings for human verification.

## Focus

Records high-frequency vital observations against procedure phases with device or manual source attribution. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Procedure nurse or clinician may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires procedure, phase, timestamp, vital values, units, source device, and recorder.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable active record; validation failure creates no accepted clinical content.
- **Transitions:** Active → Completed → Accepted; corrected observations succeed originals. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a chronological observation series available to procedure and sedation records; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Procedure Observation Series` is a submittable clinical DocType with naming series `OC-.#####`; key fields are encounter, procedure, phase, observed_at, observation_table, device_reference, recorder.
- **Workflow:** Frappe Workflow implements Active → Completed → Accepted; corrected observations succeed originals. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Procedure Nurse`, `OC Clinician` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Fast-entry grid, device integration hook, and procedure trend print chart; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
