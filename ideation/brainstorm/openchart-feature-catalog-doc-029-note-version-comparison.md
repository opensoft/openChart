# Note Version Comparison — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Shows meaningful changes between drafts, accepted notes, addenda, and successors with provenance context.
Topics: openchart-feature-catalog, clinical-documentation, frappe, note-diff
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-029 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Semantic change grouping** — Could distinguish wording edits from clinical changes.

## Focus

Shows meaningful changes between drafts, accepted notes, addenda, and successors with provenance context. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Clinician, supervisor, or health information reviewer may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires two authorized note versions and their section provenance.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable requests are ephemeral audit-bearing records; no clinical content is changed record; validation failure creates no accepted clinical content.
- **Transitions:** Requests are ephemeral audit-bearing records; no clinical content is changed. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a read-only section-aware comparison with additions, removals, and source changes; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Note Comparison Request` is a submittable clinical DocType with naming series `OC-.#####`; key fields are left_note, right_note, requested_by, generated_at, comparison_hash.
- **Workflow:** Frappe Workflow implements Requests are ephemeral audit-bearing records; no clinical content is changed. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Clinician`, `OC Supervising Clinician`, `OC Health Information Manager` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Whitelisted comparison method and Desk diff page; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
