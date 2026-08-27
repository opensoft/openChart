# Body-Area Examination Findings — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records examination findings by body area with explicit normal templates and exception editing.
Topics: openchart-feature-catalog, clinical-documentation, frappe, physical-exam
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-017 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Specialty body maps** — Could provide more granular finding locations.

## Focus

Records examination findings by body area with explicit normal templates and exception editing. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Examining clinician may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires body area, performed status, normal baseline, exceptions, and free-text detail.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable draft record; validation failure creates no accepted clinical content.
- **Transitions:** Draft → Confirmed with note → Accepted; corrections use succession. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a structured examination section that never assumes an unperformed exam; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Exam Finding` is a submittable clinical DocType with naming series `OC-.#####`; key fields are encounter, body_area, performed, finding_status, normal_template_version, exceptions.
- **Workflow:** Frappe Workflow implements Draft → Confirmed with note → Accepted; corrections use succession. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Clinician` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Body map client script, normal-default confirmation, and exam print section; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
