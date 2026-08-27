# Appointment-to-Encounter Creation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Converts a scheduled appointment into a traceable clinical encounter without rekeying patient or visit context.
Topics: openchart-feature-catalog, clinical-documentation, frappe, appointment-conversion
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-001 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Pre-visit chart preparation** — Could assemble unresolved tasks before conversion.

## Focus

Converts a scheduled appointment into a traceable clinical encounter without rekeying patient or visit context. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Front-desk staff or the assigned clinician may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires an eligible appointment, patient identity, service, and arrival context.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable planned record; validation failure creates no accepted clinical content.
- **Transitions:** Planned → Arrived → In Progress → Closed; Cancelled remains non-clinical. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a draft encounter linked to its originating appointment; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Clinical Encounter` is a submittable clinical DocType with naming series `OC-.#####`; key fields are appointment, patient, encounter_type, service_date, responsible_clinician, source_provenance.
- **Workflow:** Frappe Workflow implements Planned → Arrived → In Progress → Closed; Cancelled remains non-clinical. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Registration User`, `OC Clinician` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Desk appointment action and encounter Quick Entry; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
