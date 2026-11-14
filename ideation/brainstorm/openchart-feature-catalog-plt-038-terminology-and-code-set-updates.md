# Terminology And Code-set Updates — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Imports, validates, versions, and activates licensed terminology and code-set releases with impact and rollback controls.
Topics: openchart-feature-catalog, platform, frappe, terminology-updates
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-038 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Retired-code remediation queues** — Assign owners to records or mappings affected by newly inactive codes.

## Focus

This feature isolates update administration for ICD, CPT, LOINC, and similar feeds without redistributing content beyond its license.

## Behavior

- Terminology administrators register a source, edition, version, release date, license basis, digest, and effective date.
- Import dry run validates schema, duplicates, hierarchy, mappings, additions, changes, and retirements against the active version.
- Releases move through Received, Validating, Review, Approved, Scheduled, Active, Failed, Retired, and Rolled Back states.
- Impact reports identify saved rules, forms, fee schedules, reports, and mappings that reference changed codes.
- Activation is atomic by code system and preserves historical display for records pinned to prior versions.
- Failed validation or license mismatch blocks activation and retains no unauthorized distributable payload.

## Frappe realization

- **DocTypes:** `OC Code System Release`, `OC Terminology Concept`, and `OC Concept Map Version` store metadata, effective state, and source provenance.
- **Import/automation:** governed Data Import mappings and RQ jobs stage large feeds; indexed shadow tables cut over only after validation.
- **Permissions:** Terminology Administrator prepares; Terminology Approver activates; ordinary roles receive read-only effective lookups.
- **Patches:** schema or mapping migrations run as idempotent patches, while fixtures contain only redistributable baseline metadata.

## Boundaries

Owns: code-set release lifecycle, validation, activation, and impact evidence. Consumes: authorized vendor or public feeds and mappings. Emits: versioned lookup content and retirement events. Does not own: terminology licensing or clinical code selection.

## Open questions

- Which code systems require parallel active editions during payer or regulatory transition periods?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Data Import Mapping And Dry Run](openchart-feature-catalog-plt-024-data-import-mapping-and-dry-run.md) · [Fee Schedule Version Administration](openchart-feature-catalog-plt-039-fee-schedule-version-administration.md)
