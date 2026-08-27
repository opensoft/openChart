# Copy-Forward with Provenance — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Copies selected prior note content into a new draft with visible origin, age, and mandatory review marking.
Topics: openchart-feature-catalog, clinical-documentation, frappe, copy-forward
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-032 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Staleness rules** — Could warn when copied facts exceed a configured age.

## Focus

Copies selected prior note content into a new draft with visible origin, age, and mandatory review marking. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Clinician may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires authorized source note, selected sections, destination draft, and copy reason.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable copied record; validation failure creates no accepted clinical content.
- **Transitions:** Copied → Reviewed or Removed; unreviewed fragments block signature. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives editable copied content that remains marked until actively reviewed; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Copied Note Fragment` is a submittable clinical DocType with naming series `OC-.#####`; key fields are source_note, source_section, destination_note, copied_at, copied_by, review_status.
- **Workflow:** Frappe Workflow implements Copied → Reviewed or Removed; unreviewed fragments block signature. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Clinician` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Section selection dialog, provenance highlighting, and pre-sign validation; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
