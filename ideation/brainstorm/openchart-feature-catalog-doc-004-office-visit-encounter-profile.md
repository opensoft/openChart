# Office Visit Encounter Profile — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies office-specific sections, locations, and closure checks to ambulatory encounters.
Topics: openchart-feature-catalog, clinical-documentation, frappe, office-visit
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-004 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Rooming milestones** — Could drive an ambulatory flow board.

## Focus

Applies office-specific sections, locations, and closure checks to ambulatory encounters. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Ambulatory clinician may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires an encounter designated as an in-person office visit.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable configuration is draft record; validation failure creates no accepted clinical content.
- **Transitions:** Configuration is Draft → Active → Retired; encounters snapshot the active version. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives an encounter profile with room, service, note, and checkout requirements; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Encounter Profile` is a standard versioned configuration DocType with naming series `OC-.#####`; key fields are profile_code, care_setting, required_sections, location_rules, closure_rules.
- **Workflow:** Frappe Workflow implements Configuration is Draft → Active → Retired; encounters snapshot the active version. Published versions are retired and replaced by a new version; encounter snapshots stay stable.
- **Roles and permissions:** `OC Clinical Administrator`, `OC Clinician` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Desk configuration and encounter form client script; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
