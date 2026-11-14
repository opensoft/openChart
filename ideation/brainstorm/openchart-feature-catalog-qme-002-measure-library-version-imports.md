# Measure Library Version Imports — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Imports, validates, approves, and retires measure specification releases while preserving immutable provenance and dependencies.
Topics: openchart-feature-catalog, quality-reporting, frappe, measure-library
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-002 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Release impact preview** — Show which historical rates and future periods would change before activating a new release.

## Focus

Governed lifecycle management for computable measure packages, value sets, metadata, and local mappings.

## Behavior

- A library manager uploads or retrieves a steward package and records source, checksum, release date, and license constraints.
- Import validates identifiers, dependency graphs, value-set references, logic syntax, and duplicate versions.
- Releases move through imported, validation-failed, under-review, approved, active, retired, and withdrawn states.
- Approval requires synthetic conformance cases and preserves their expected population outcomes.
- Active releases are immutable; corrections create successors with explicit replaced-version links.
- Period configuration cannot select withdrawn or unresolved releases without an authorized override and rationale.
- Users can compare metadata, logic changes, and mapping changes between releases.

## Frappe realization

- **DocTypes:** Add `OC Measure Definition`, `OC Measure Release`, `OC Measure Dependency`, and `OC Measure Test Case` with Attach, Code, JSON, checksum, effective dates, and successor links.
- **Workflow:** Require `OC Measure Librarian` import, `OC Measure Reviewer` approval, and separation of author and approver for activation.
- **Hooks and API:** Validate package structure on upload, run conformance jobs before approval, and expose guarded import/compare methods under `open_chart.api.v1.quality`.
- **Surfaces:** Provide a measure library workspace, release comparison Script Report, dependency graph HTML view, and validation-error list.

## Boundaries

Owns: local copies, provenance, validation, and lifecycle of measure releases. Consumes: authorized steward artifacts and terminology. Emits: approved immutable releases and change notices. Does not own: external intellectual property, steward policy, or clinical data.

## Open questions

- Which redistributable measure packages may ship with openChart versus requiring site-supplied imports?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
