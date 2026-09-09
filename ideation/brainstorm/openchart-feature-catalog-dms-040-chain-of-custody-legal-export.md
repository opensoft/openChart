# Chain-of-custody Legal Export — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Produces a sealed legal export with exact document versions, manifests, checksums, access history, transformations, signatures, and transfer receipts.
Topics: openchart-feature-catalog, documents, frappe, custody-export
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-040 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Offline verification utility** — Let an authorized recipient validate manifest signatures and file checksums without openChart access.

## Focus

This feature isolates reproducible evidence packaging and custody transfer for approved legal requests.

## Behavior

- A Legal Records Specialist starts from an approved legal request or hold-authorized export scope.
- Selection freezes exact current or historical document versions, source checksums, metadata, and requested audit intervals.
- The export includes files, machine-readable manifest, human-readable index, provenance, transformations, signature evidence, and authorized custody events.
- A second reviewer verifies scope, exclusions, sensitive segments, and manifest completeness before sealing.
- Sealing computes per-file and package checksums and applies an organizational digital signature and trusted timestamp when configured.
- Each copy, handoff, download, media write, receipt, rejection, or return appends a custody event with actor and destination.
- Any package change breaks verification and requires a new export version; failed transfer never rewrites the sealed package.

## Frappe realization

- **DocTypes:** `OC Legal Export` (authority_reference, scope_version, state, package_file, manifest_file, checksum, signature_evidence) with child `OC Legal Export Item` and `OC Custody Event`.
- **Files/jobs:** RQ assembles private package and indexes using Frappe Print Formats; `open_chart.documents.on_file` verifies package lineage, then integrity jobs seal checksums.
- **Workflow:** Selecting → Scope Review → Building → Verification → Sealed → Transferred, with Build Failed, Rejected, Returned, and Superseded states.
- **Roles/permissions:** Legal Records Specialist selects; Legal/Privacy Reviewer approves; Custody Officer records transfer; package access uses restricted permlevel 2.
- **API/surfaces:** Guarded build, seal, and custody-event methods; Desk evidence workspace, manifest Script Report, transfer receipt, and chain-of-custody Print Format.

## Boundaries

Owns: frozen export scope, evidence manifest, sealed package, checksums, and custody ledger. Consumes: approved authority, immutable source versions, audit evidence, and signature service. Emits: verifiable legal package and transfer receipts. Does not own: legal advice, court admissibility decisions, courier operations, or source-record alteration.

## Open questions

- Which audit events and system logs belong in a minimum versus expanded legal export package?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Digital Signature Certificate Application](openchart-feature-catalog-dms-039-digital-signature-certificate-application.md)
