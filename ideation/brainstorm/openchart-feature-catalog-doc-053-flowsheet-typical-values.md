# Flowsheet Typical Values — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Offers configured typical values for rapid flowsheet entry while requiring explicit confirmation of each recorded observation.
Topics: openchart-feature-catalog, clinical-documentation, frappe, flowsheet-defaults
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-053 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Unit-specific typical sets** — Could adapt to service lines without silent defaults.

## Focus

Offers configured typical values for rapid flowsheet entry while requiring explicit confirmation of each recorded observation. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Nurse or clinician may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires flowsheet row, care context, typical value, applicability, and effective dates.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable draft record; validation failure creates no accepted clinical content.
- **Transitions:** Draft → Approved → Active → Retired. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a selectable default visibly distinguished from measured or observed input; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Flowsheet Typical Value` is a standard versioned configuration DocType with naming series `OC-.#####`; key fields are flowsheet_definition, row_key, context_expression, value, unit, effective_from.
- **Workflow:** Frappe Workflow implements Draft → Approved → Active → Retired. Published versions are retired and replaced by a new version; encounter snapshots stay stable.
- **Roles and permissions:** `OC Clinical Administrator`, `OC Nurse Educator`, `OC Nurse` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Configuration form and client-side typical-value confirmation; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
