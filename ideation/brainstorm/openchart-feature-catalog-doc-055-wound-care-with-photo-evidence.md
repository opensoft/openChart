# Wound Care with Photo Evidence — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Documents wound location, dimensions, characteristics, treatment, and consent-governed photographs over time.
Topics: openchart-feature-catalog, clinical-documentation, frappe, wound-documentation
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-055 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Calibrated image measurement** — Could be proposed with human confirmation.

## Focus

Documents wound location, dimensions, characteristics, treatment, and consent-governed photographs over time. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Wound care clinician or nurse may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires wound identity, measurements, assessment, intervention, image, consent, and capture metadata.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable draft record; validation failure creates no accepted clinical content.
- **Transitions:** Draft → Reviewed → Signed; image replacement requires a new assessment record. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a signed wound episode entry with protected image provenance; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Wound Assessment` is a submittable clinical DocType with naming series `OC-.#####`; key fields are encounter, wound, body_location, measurements, characteristics, treatment, photo, consent_snapshot.
- **Workflow:** Frappe Workflow implements Draft → Reviewed → Signed; image replacement requires a new assessment record. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Wound Care Clinician`, `OC Nurse` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Body-location client control, mobile Image capture, and restricted print format; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
