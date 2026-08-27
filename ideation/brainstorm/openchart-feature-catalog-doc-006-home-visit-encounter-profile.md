# Home Visit Encounter Profile — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records destination, field safety, companions, and service context for care delivered in a home.
Topics: openchart-feature-catalog, clinical-documentation, frappe, home-visit
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-006 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Route sequencing** — Could optimize assigned visits while preserving clinical priority.

## Focus

Records destination, field safety, companions, and service context for care delivered in a home. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Home-visiting clinician may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires a home visit encounter, destination, attendance, and field observations.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable planned record; validation failure creates no accepted clinical content.
- **Transitions:** Planned → En Route → On Site → Completed or Unable to Complete. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a location-aware encounter context without exposing unnecessary address data; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Home Visit Context` is a submittable clinical DocType with naming series `OC-.#####`; key fields are encounter, destination_reference, arrived_at, departed_at, companions, safety_notes.
- **Workflow:** Frappe Workflow implements Planned → En Route → On Site → Completed or Unable to Complete. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Home Care Clinician`, `OC Care Coordinator` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Mobile-friendly Desk form and visit print format; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
