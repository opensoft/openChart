# Permissioned Cross-Patient Encounter Search — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Finds encounters across authorized patient cohorts using structured filters without bypassing row-level and purpose-of-use controls.
Topics: openchart-feature-catalog, clinical-documentation, frappe, encounter-search
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-068 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **De-identified aggregate counts** — Could support service planning.

## Focus

Finds encounters across authorized patient cohorts using structured filters without bypassing row-level and purpose-of-use controls. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Authorized clinical or health information user may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires date range, encounter type, clinician, location, diagnosis, documentation status, and permitted cohort.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable search is read-only; exports require a distinct authorized request record; validation failure creates no accepted clinical content.
- **Transitions:** Search is read-only; exports require a distinct authorized request. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a paginated result set with reason-for-access audit context; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Encounter Search Audit` is a submittable clinical DocType with naming series `OC-.#####`; key fields are user, purpose, filter_hash, result_count, executed_at, export_requested.
- **Workflow:** Frappe Workflow implements Search is read-only; exports require a distinct authorized request. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Clinical Supervisor`, `OC Health Information Manager`, `OC Auditor` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Query Report or Script Report with user permissions and saved filters; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
