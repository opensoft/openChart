# Pain Reassessment Workflow — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Schedules and documents pain reassessment after an intervention with explicit overdue and exception states.
Topics: openchart-feature-catalog, clinical-documentation, frappe, pain-reassessment
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-056 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Intervention-specific timing policies** — Could set reassessment windows.

## Focus

Schedules and documents pain reassessment after an intervention with explicit overdue and exception states. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Nurse or clinician may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires baseline pain, intervention reference, expected reassessment time, new score, and response.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable due record; validation failure creates no accepted clinical content.
- **Transitions:** Due → Completed, Deferred with Reason, or Overdue → Escalated. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a closed-loop pain assessment pair or an escalated overdue task; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Pain Reassessment` is a submittable clinical DocType with naming series `OC-.#####`; key fields are encounter, baseline_observation, intervention, due_at, score, response, exception_reason.
- **Workflow:** Frappe Workflow implements Due → Completed, Deferred with Reason, or Overdue → Escalated. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Nurse`, `OC Clinician` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Assignment Rule, scheduler notifications, bedside form, and overdue report; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
