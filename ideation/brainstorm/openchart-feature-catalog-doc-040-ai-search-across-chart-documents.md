# AI Search Across Chart Documents — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Searches authorized notes and scanned documents semantically while returning source excerpts and access-aware citations.
Topics: openchart-feature-catalog, clinical-documentation, frappe, chart-search
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-040 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Handwriting or fax OCR adapters** — Could add reviewed text layers to scans.

## Focus

Searches authorized notes and scanned documents semantically while returning source excerpts and access-aware citations. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Authorized chart user may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires patient scope, natural-language query, document filters, and user permissions.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable search is read-only; unavailable or unindexed sources are explicitly reported record; validation failure creates no accepted clinical content.
- **Transitions:** Search is read-only; unavailable or unindexed sources are explicitly reported. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives ranked cited results that open the authoritative source record; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Chart Search Audit` is a submittable clinical DocType with naming series `OC-.#####`; key fields are patient, query_hash, filters, result_references, searched_at, user.
- **Workflow:** Frappe Workflow implements Search is read-only; unavailable or unindexed sources are explicitly reported. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Clinician`, `OC Nurse`, `OC Health Information Manager` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Whitelisted search API, background indexing jobs, and patient search page; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
