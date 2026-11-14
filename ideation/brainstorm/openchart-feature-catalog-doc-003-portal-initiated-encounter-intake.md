# Portal-Initiated Encounter Intake — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets a patient submit governed pre-encounter information that staff must reconcile before it enters the clinical record.
Topics: openchart-feature-catalog, clinical-documentation, frappe, portal-intake
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-003 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Adaptive intake questions** — Could respond to the selected visit reason.

## Focus

Lets a patient submit governed pre-encounter information that staff must reconcile before it enters the clinical record. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Patient or authorized portal proxy may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires visit reason, symptoms, attachments, consent acknowledgements, and proxy authority.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable submitted record; validation failure creates no accepted clinical content.
- **Transitions:** Submitted → Identity Review → Clinical Review → Accepted or Returned. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives an intake submission linked to a proposed encounter and reconciliation queue; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Encounter Intake` is a submittable clinical DocType with naming series `OC-.#####`; key fields are patient, proxy, reason, symptom_table, attachments, consent_snapshot, encounter.
- **Workflow:** Frappe Workflow implements Submitted → Identity Review → Clinical Review → Accepted or Returned. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Portal Patient`, `OC Registration User`, `OC Clinician` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Authenticated Web Form and portal status page; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
