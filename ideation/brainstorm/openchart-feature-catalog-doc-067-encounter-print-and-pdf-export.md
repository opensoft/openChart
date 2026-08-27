# Encounter Print and PDF Export — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Produces permission-filtered encounter renditions with signatures, succession status, provenance, and release markings.
Topics: openchart-feature-catalog, clinical-documentation, frappe, encounter-export
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-067 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Standards-based document packaging** — Could accompany the human-readable PDF.

## Focus

Produces permission-filtered encounter renditions with signatures, succession status, provenance, and release markings. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Authorized chart user may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires encounter, selected authorized sections, rendition purpose, and disclosure context.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable requested record; validation failure creates no accepted clinical content.
- **Transitions:** Requested → Generated → Delivered or Failed; exports are immutable artifacts. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives a watermarked print or PDF rendition with an audit record and content hash; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Encounter Export` is a submittable clinical DocType with naming series `OC-.#####`; key fields are encounter, requested_by, purpose, included_records, generated_at, file, content_hash.
- **Workflow:** Frappe Workflow implements Requested → Generated → Delivered or Failed; exports are immutable artifacts. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Clinician`, `OC Health Information Manager`, `OC Auditor` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Jinja Print Formats, Letter Heads, PDF generation, and export log; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
