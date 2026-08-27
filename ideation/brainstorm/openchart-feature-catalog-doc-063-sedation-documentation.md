# Sedation Documentation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates pre-sedation assessment, medication events, monitoring, recovery criteria, and responsible clinicians.
Topics: openchart-feature-catalog, clinical-documentation, frappe, sedation-record
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-063 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Recovery scoring instruments** — Could be versioned by age and service.

## Focus

Coordinates pre-sedation assessment, medication events, monitoring, recovery criteria, and responsible clinicians. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Sedation clinician and monitoring nurse may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires sedation plan, assessment, consent, medications, observations, airway events, and recovery score.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable planned record; validation failure creates no accepted clinical content.
- **Transitions:** Planned → Pre-Check → Sedating → Recovery → Discharge Ready → Signed. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a complete signed sedation record with phase transitions; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Sedation Record` is a submittable clinical DocType with naming series `OC-.#####`; key fields are encounter, procedure, consent_reference, pre_assessment, medication_table, observation_series, recovery_score.
- **Workflow:** Frappe Workflow implements Planned → Pre-Check → Sedating → Recovery → Discharge Ready → Signed. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Sedation Clinician`, `OC Procedure Nurse` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Phase-aware client script, medication timeline, and sedation Print Format; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
