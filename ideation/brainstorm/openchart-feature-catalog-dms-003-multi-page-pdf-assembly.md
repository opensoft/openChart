# Multi-page PDF Assembly — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Turns reviewed scan pages into a normalized, ordered PDF while retaining every source-page checksum and transformation.
Topics: openchart-feature-catalog, documents, frappe, pdf-assembly
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-003 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Assembly quality score** — Flag skew, clipping, low contrast, and unexpectedly blank pages before acceptance.

## Focus

This feature isolates deterministic assembly of one document from multiple captured pages.

## Behavior

- A Scanning Operator opens a committed scan session and confirms page order, orientation, and inclusion.
- The system renders a preview without changing sealed source pages.
- Assembly normalizes page dimensions and embeds only approved, loss-bounded transformations.
- The output records ordered source checksums, transformation parameters, renderer version, and output checksum.
- Password-protected, corrupt, oversized, or mixed unsupported inputs fail with page-specific diagnostics.
- A retry creates a new assembly attempt while retaining failed attempt evidence.
- Approval stores the PDF privately and makes it eligible for indexing; it does not attach it to a patient automatically.

## Frappe realization

- **DocTypes:** `OC Document Assembly` (scan_session, state, renderer_version, output_file, output_checksum) with child `OC Assembly Page` (source_file, sequence, rotation, crop, source_checksum).
- **Files/jobs:** Private Frappe `File` attachments hold sources and output; an RQ job performs PDF generation, with `open_chart.documents.on_file` checking output metadata before release.
- **Workflow:** Planned → Rendering → Review → Approved, with Failed and Superseded states.
- **Roles/permissions:** Scanning Operator plans and reviews; Document Processor integration user renders but cannot approve or associate a patient.
- **API/surfaces:** `open_chart.api.v1.documents.assemble_pdf` enqueues idempotently; a Desk page-grid preview and realtime progress show attempt state.

## Boundaries

Owns: page order, transformations, assembly attempts, and output integrity. Consumes: sealed source pages. Emits: normalized PDF and manifest. Does not own: OCR content, patient identity, or document classification.

## Open questions

- Which PDF archival profile and maximum page dimensions should be mandatory?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Scanner Ingest Integration](openchart-feature-catalog-dms-002-scanner-ingest-integration.md)
