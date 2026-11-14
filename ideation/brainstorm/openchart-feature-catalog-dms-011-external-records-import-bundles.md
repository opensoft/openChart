# External Records Import Bundles — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Imports prior-chart migration packages into a quarantined manifest where files, metadata, identity, and provenance are reviewed before chart attachment.
Topics: openchart-feature-catalog, documents, frappe, records-import
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-011 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Migration reconciliation report** — Compare expected package inventory with accepted, rejected, duplicate, and unresolved items.

## Focus

This feature isolates governed intake of an external records bundle rather than treating an archive as trusted chart content.

## Behavior

- A Migration Operator uploads a supported archive plus source-system and export metadata.
- The system quarantines the package, scans it, validates its manifest, and enumerates every file before extraction.
- Each item receives source identifiers, checksum, media type, proposed class, and patient-match state.
- Unsupported, missing, extra, corrupt, path-traversal, and duplicate items become explicit exceptions.
- Reviewers accept, reject, or defer each item; package-level completion requires every item to have a terminal disposition.
- Accepted items create typed document records while retaining original bundle and source-path provenance.
- Rerunning an import is idempotent by source package and item identifiers and never silently duplicates accepted content.

## Frappe realization

- **DocTypes:** `OC External Record Import` (source_system, package_id, manifest_file, state, counts) with child `OC Import Bundle Item` (source_path, checksum, proposed_class, patient, disposition, created_document).
- **Files/jobs:** Private Frappe File stores the sealed package and extracted quarantined files; `open_chart.documents.on_file` validates archive safety, then RQ jobs inventory and stage items.
- **Workflow:** Uploaded → Validating → Item Review → Reconciled, with Invalid Package and Partial states.
- **Roles/permissions:** Migration Operator uploads; Patient Identity Reviewer matches; Health Information Manager finalizes; integration users cannot accept clinical attachment.
- **API/surfaces:** `open_chart.api.v1.documents.import_bundle` plus Data Import mappings; Desk reconciliation workspace and Script Report show item-level outcomes.

## Boundaries

Owns: package manifest, quarantine, item disposition, and source provenance. Consumes: prior-chart package and patient matching. Emits: accepted typed documents and reconciliation report. Does not own: vendor export generation, patient merge, or discrete clinical-data reconciliation.

## Open questions

- Which package formats and manifest fields constitute the minimum migration contract?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Outside-record Diff View](openchart-feature-catalog-dms-036-outside-record-diff-view.md)
