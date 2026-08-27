# Governed Chart Summary Drafting — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Generates a source-cited chart summary draft that a clinician must review, edit, and accept before clinical use.
Topics: openchart-feature-catalog, clinical-documentation, frappe, chart-summary
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-038 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Purpose-specific summaries** — Could support transfer, intake, or pre-round review.

## Focus

Generates a source-cited chart summary draft that a clinician must review, edit, and accept before clinical use. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Clinician may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires authorized chart scope, time window, purpose, and source records.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable generated record; validation failure creates no accepted clinical content.
- **Transitions:** Generated → Human Review → Accepted as Note or Discarded. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a draft summary with citations, omissions notice, and human review state; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Chart Summary Draft` is a submittable clinical DocType with naming series `OC-.#####`; key fields are patient, purpose, source_snapshot, generated_text, citations, reviewer, accepted_note.
- **Workflow:** Frappe Workflow implements Generated → Human Review → Accepted as Note or Discarded. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Clinician`, `OC Clinical Supervisor` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Background job, review workspace, and open_chart.api.v1 acceptance method; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
