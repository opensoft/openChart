# E-Signature Queue — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents each clinician with permission-filtered notes awaiting their signature, co-signature, or attestation.
Topics: openchart-feature-catalog, clinical-documentation, frappe, signature-queue
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-034 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Batch navigation** — Could streamline review without enabling blind batch signing.

## Focus

Presents each clinician with permission-filtered notes awaiting their signature, co-signature, or attestation. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Clinician or supervisor may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires assigned signature requests, due dates, priority, and signature role.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable open record; validation failure creates no accepted clinical content.
- **Transitions:** Open → Viewed → Signed, Returned, Reassigned, or Expired. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a work queue with direct review and sign or return actions; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Signature Request` is a submittable clinical DocType with naming series `OC-.#####`; key fields are clinical_note, requested_signer, signature_role, requested_at, due_at, priority.
- **Workflow:** Frappe Workflow implements Open → Viewed → Signed, Returned, Reassigned, or Expired. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Clinician`, `OC Supervising Clinician` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Query Report, workspace Number Cards, and workflow notifications; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
