# Verbal Order Documentation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records a verbal order read-back, receiver, ordering clinician, urgency, and required later authentication.
Topics: openchart-feature-catalog, clinical-documentation, frappe, verbal-orders
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-047 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Device or telephony metadata** — Could corroborate communication timing.

## Focus

Records a verbal order read-back, receiver, ordering clinician, urgency, and required later authentication. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Authorized order receiver and ordering clinician may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires verbal instruction, patient, order details, read-back confirmation, and urgency.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable received record; validation failure creates no accepted clinical content.
- **Transitions:** Received → Read Back Confirmed → Executed per order authority → Authenticated or Escalated. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a pending-authentication order record with complete communication provenance; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Verbal Order Record` is a submittable clinical DocType with naming series `OC-.#####`; key fields are encounter, order_text, giver, receiver, given_at, read_back, authentication_due_at.
- **Workflow:** Frappe Workflow implements Received → Read Back Confirmed → Executed per order authority → Authenticated or Escalated. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Nurse`, `OC Clinician`, `OC Clinical Supervisor` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Restricted Quick Entry, authentication queue, and verbal-order print block; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
