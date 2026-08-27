# Personal Smart Phrases — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets clinicians insert governed personal quick text with parameters while preserving final note authorship.
Topics: openchart-feature-catalog, clinical-documentation, frappe, smart-phrases
Repository context: openChart — Frappe v15 native EMR; catalog entry DOC-019 (Encounters And Clinical Documentation)
Captured: 2026-08-24

## Possible feats

- **Usage analytics** — Could identify stale or risky phrase content.

## Focus

Lets clinicians insert governed personal quick text with parameters while preserving final note authorship. This feature isolates that capability from scheduling, billing, and other systems that may consume its governed outputs.

## Behavior

- **Actors:** Clinician may initiate the capability only for patients and encounters allowed by Frappe user permissions.
- **Inputs:** The workflow requires phrase trigger, expansion text, placeholders, scope, and active state.
- **Validation:** Patient identity, encounter authority, mandatory fields, source references, and current record versions are checked server-side.
- **Initial state:** A successful start creates a traceable personal phrases are draft record; validation failure creates no accepted clinical content.
- **Transitions:** Personal phrases are Draft → Active → Retired and are never submitted as clinical records. Every transition records actor, timestamp, and rationale where applicable.
- **Permissions:** Read, create, review, submit, print, and amend rights are evaluated separately; sensitive sections remain hidden when access is partial.
- **Edge cases:** Stale revisions, duplicate submissions, unavailable sources, revoked consent, and concurrent edits return explicit recoverable errors.
- **Output:** The user receives reviewable text inserted into a note without hidden automation; accepted clinical records are never silently rewritten.

## Frappe realization

- **DocTypes:** `OC Smart Phrase` is a submittable clinical DocType with naming series `OC-.#####`; key fields are owner, trigger, expansion, placeholder_schema, active.
- **Workflow:** Frappe Workflow implements Personal phrases are Draft → Active → Retired and are never submitted as clinical records. After submission, corrections use open_chart.api.v1 succession records; accepted rows are never edited in place.
- **Roles and permissions:** `OC Clinician` receive least-privilege DocPerms at permlevels 0–2 plus patient, facility, and owner user permissions.
- **Hooks and API:** `validate`, `before_save`, `on_submit`, and `on_update` enforce provenance and state invariants; supported writes use whitelisted `open_chart.api.v1` methods or guarded `/api/resource/...` reads.
- **Surfaces:** Editor autocomplete client script and phrase management list; client scripts handle conditional fields, stale-revision warnings, and explicit review confirmations.

## Boundaries

Owns: its clinical-documentation record, state, provenance, and review controls. Consumes: authorized patient, encounter, identity, consent, terminology, and source-record references. Emits: permission-filtered accepted records, audit events, notifications, and stable references for downstream consumers. Does not own: patient identity resolution, scheduling authority, billing adjudication, external terminology stewardship, or autonomous clinical decisions.

## Open questions

- Which policy details require organization-level configuration versus a shared openChart default?

## Relationships

[Synthesis: Encounters And Clinical Documentation](openchart-feature-catalog-synthesis-doc.md)
