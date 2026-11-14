# Multi-Column Clinical Flowsheets — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides configurable observation grids whose rows are clinical measures and columns are time points or care events.
Topics: openchart-feature-catalog, clinical-documentation, frappe, flowsheets
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-052 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Threshold highlighting** — Could remain advisory and route reviewed alerts.

## Focus

Provides configurable observation grids whose rows are clinical measures and columns are time points or care events. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Nurse, clinician, or therapist may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires flowsheet definition, encounter, row values, observation times, units, and recorder.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable draft record; validation failure creates no accepted clinical content.
- **Transitions:** Draft → Active → Completed → Accepted; accepted corrections create successor observations. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives validated longitudinal observations with source-level provenance; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Clinical Flowsheet` is a submittable clinical DocType with naming series `OC-.#####`; key fields are encounter, definition_version, status, started_at, ended_at, observation_table.
- **Workflow:** Frappe Workflow implements Draft → Active → Completed → Accepted; accepted corrections create successor observations. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Nurse`, `OC Clinician`, `OC Therapist` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Grid client script, bedside entry view, and flowsheet print format; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
