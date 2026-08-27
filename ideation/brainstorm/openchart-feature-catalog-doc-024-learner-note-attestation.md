# Learner Note Attestation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures resident or student authorship and the supervising clinician’s required attestation statement.
Topics: openchart-feature-catalog, clinical-documentation, frappe, learner-documentation
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-024 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Program-specific attestation text** — Could be governed as templates.

## Focus

Captures resident or student authorship and the supervising clinician’s required attestation statement. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Learner and supervising clinician may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires learner note, training role, supervisor, attestation type, and review edits.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable learner draft record; validation failure creates no accepted clinical content.
- **Transitions:** Learner Draft → Supervisor Review → Returned or Attested → Signed. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a signed note with distinct author, editor, and attester provenance; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Clinical Attestation` is a submittable clinical DocType with naming series `OC-.#####`; key fields are clinical_note, learner, learner_role, supervisor, attestation_text, attested_at.
- **Workflow:** Frappe Workflow implements Learner Draft → Supervisor Review → Returned or Attested → Signed. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Student Clinician`, `OC Resident Clinician`, `OC Supervising Clinician` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Learner workspace, attestation dialog, and print signature block; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
