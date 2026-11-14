# Scanner Ingest Integration — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Ingests pages from workstation or network scanners into a quarantined Frappe document-capture session with device provenance.
Topics: openchart-feature-catalog, documents, frappe, scanner-ingest
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-002 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Scan profile presets** — Offer governed duplex, grayscale, resolution, and blank-page settings by document class.

## Focus

This feature isolates scanner acquisition and transport; it does not decide patient identity or clinical meaning.

## Behavior

- A Scanning Operator starts a capture session and chooses a registered TWAIN bridge or network scanner inbox.
- The connector reports device identity, profile, page count, resolution, color mode, and acquisition timestamps.
- Pages arrive in a private quarantine and appear progressively in a reorderable preview.
- The operator may rotate, delete blank pages, rescan a page, or cancel before committing the batch.
- Interrupted sessions remain Recoverable with a clear count of received and missing pages.
- Unsupported formats, malware findings, and device-identity failures stop import and preserve an error receipt.
- Committing seals the original page files and hands the session to PDF assembly or batch splitting.

## Frappe realization

- **DocTypes:** `OC Scan Device` (device_key, connector_type, facility, enabled, profile JSON) and `OC Scan Session` (operator, device, state, expected_pages, received_pages) with child `OC Scanned Page` rows linked to private `File` records.
- **Files/hooks:** Frappe file manager stores quarantined page Files; `open_chart.documents.on_file` verifies session token, MIME type, and checksum on File `after_insert`.
- **Workflow:** Capturing → Review → Committed, with Recoverable, Rejected, and Cancelled states.
- **Roles/permissions:** Scanning Operator captures; Document Integration Manager registers devices; facility user permissions constrain device and session access.
- **API/surfaces:** Token-scoped `open_chart.api.v1.documents.receive_scan_page` is idempotent by device/page key; Desk capture workspace receives websocket progress events.

## Boundaries

Owns: scanner registration, capture session, raw-page quarantine, and acquisition provenance. Consumes: connector-authenticated pages and facility context. Emits: sealed scan session. Does not own: scanner drivers, patient matching, OCR, or final chart attachment.

## Open questions

- Should the first release support a managed desktop bridge, watched network folders, or both?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Multi-page PDF Assembly](openchart-feature-catalog-dms-003-multi-page-pdf-assembly.md)
