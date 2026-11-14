# OCR Full-text Extraction — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Produces provenance-rich searchable text from accepted images and PDFs without treating OCR output as clinical truth.
Topics: openchart-feature-catalog, documents, frappe, ocr-extraction
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-005 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Layout-aware text view** — Preserve page, region, table, and reading-order coordinates for review and highlighting.

## Focus

This feature isolates asynchronous text extraction and confidence evidence from document indexing decisions.

## Behavior

- An accepted or quarantined document version enters OCR Pending when its class permits extraction.
- A background job sends the minimum necessary file to the configured local or contracted OCR adapter.
- The result stores page text, word confidence, language, coordinates, engine version, and processing time.
- OCR text is visibly labeled machine-extracted and never replaces the source image or signed narrative.
- Failed, timed-out, encrypted, and unsupported pages enter explicit retryable or terminal states.
- Authorized staff can view source and extracted text side by side and report unusable output.
- Reprocessing creates a new OCR run; search continues using the currently approved run until replacement succeeds.

## Frappe realization

- **DocTypes:** `OC OCR Run` (document_version, adapter, engine_version, state, language, started_at, completed_at) with child `OC OCR Page Result` (page, text, confidence, coordinates JSON, error_code).
- **Jobs/hooks:** `open_chart.documents.on_file` enqueues `frappe.enqueue` RQ work after malware clearance; scheduler events retry transient failures with bounded backoff.
- **Roles/permissions:** Document Indexer reads OCR output; OCR Processor integration role has source-read and result-create only; sensitive classes use permlevel 2.
- **API/surfaces:** `open_chart.api.v1.documents.request_ocr` and adapter callback methods use idempotency keys; Desk split-view and job dashboard expose progress.
- **Search:** Only an approved successful run feeds the document search index, always ACL-filtered against the source document.

## Boundaries

Owns: OCR requests, outputs, confidence, engine provenance, and retry state. Consumes: permitted document versions. Emits: candidate text and coordinates. Does not own: medical interpretation, patient matching, or acceptance of extracted metadata.

## Open questions

- Which document classes may use an external OCR service versus local-only processing?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [OCR-assisted Indexing Suggestions](openchart-feature-catalog-dms-006-ocr-assisted-indexing-suggestions.md)
