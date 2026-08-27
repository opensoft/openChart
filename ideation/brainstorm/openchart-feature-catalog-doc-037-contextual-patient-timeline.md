# Contextual Patient Timeline — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Displays permission-filtered encounters, notes, results, orders, and documents in a navigable longitudinal timeline.
Topics: openchart-feature-catalog, clinical-documentation, frappe, patient-timeline
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-037 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Episode clustering** — Could group related events without changing source records.

## Focus

Displays permission-filtered encounters, notes, results, orders, and documents in a navigable longitudinal timeline. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Authorized chart user may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires patient identity, date range, event filters, and current encounter context.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable index rows mirror source authority and rebuild asynchronously; they never replace sources record; validation failure creates no accepted clinical content.
- **Transitions:** Index rows mirror source authority and rebuild asynchronously; they never replace sources. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a chronological view with source links and provenance indicators; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Timeline Event Index` is a submittable clinical DocType with naming series `OC-.#####`; key fields are patient, event_type, event_reference, occurred_at, author, sensitivity.
- **Workflow:** Frappe Workflow implements Index rows mirror source authority and rebuild asynchronously; they never replace sources. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Clinician`, `OC Nurse`, `OC Health Information Manager` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Patient Desk page, whitelisted timeline query, and lazy loading; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
