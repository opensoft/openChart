# Chief Complaint and Visit Reason Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Preserves the patient-stated reason for care alongside a normalized clinical visit reason.
Topics: openchart-feature-catalog, clinical-documentation, frappe, chief-complaint
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-012 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Multilingual patient wording** — Could be retained beside a reviewed translation.

## Focus

Preserves the patient-stated reason for care alongside a normalized clinical visit reason. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Rooming staff or clinician may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires patient wording, source, onset, and optional normalized reason.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable draft concerns may be corrected; accepted wording is superseded, not overwritten record; validation failure creates no accepted clinical content.
- **Transitions:** Draft concerns may be corrected; accepted wording is superseded, not overwritten. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a provenance-bearing chief complaint available to note sections and search; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Encounter Concern` is a submittable clinical DocType with naming series `OC-.#####`; key fields are encounter, patient_wording, normalized_concept, onset, source_actor, recorded_at.
- **Workflow:** Frappe Workflow implements Draft concerns may be corrected; accepted wording is superseded, not overwritten. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Clinical Assistant`, `OC Nurse`, `OC Clinician` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Encounter Quick Entry and portal intake mapping; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
