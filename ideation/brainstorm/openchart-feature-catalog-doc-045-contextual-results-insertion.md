# Contextual Results Insertion — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Inserts selected result values into a note draft as source-linked snapshots rather than detached copied text.
Topics: openchart-feature-catalog, clinical-documentation, frappe, results-context
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-045 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Trend snippets** — Could insert a reviewed multi-result summary.

## Focus

Inserts selected result values into a note draft as source-linked snapshots rather than detached copied text. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Clinician may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires authorized result, selected components, display format, and destination section.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable inserted record; validation failure creates no accepted clinical content.
- **Transitions:** Inserted → Reviewed; amended or corrected source results display a warning. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a timestamped result citation with values and source status; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Note Evidence Reference` is a submittable clinical DocType with naming series `OC-.#####`; key fields are clinical_note, section_key, result_reference, component_snapshot, observed_at, inserted_at.
- **Workflow:** Frappe Workflow implements Inserted → Reviewed; amended or corrected source results display a warning. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Clinician`, `OC Nurse` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Result picker client script and citation-aware print rendering; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
