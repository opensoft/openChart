# Barcode Batch Auto-splitting — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Splits a scanned batch at recognized separator sheets into proposed document bundles for operator confirmation.
Topics: openchart-feature-catalog, documents, frappe, barcode-splitting
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-004 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Separator sheet generator** — Print facility-scoped barcode sheets for common document classes and destinations.

## Focus

This feature isolates non-destructive batch segmentation using governed barcode separators.

## Behavior

- A Scanning Operator submits a committed multi-page batch for separator detection.
- The system recognizes only signed, unexpired separator formats configured for the current facility.
- Each recognized separator starts a proposed bundle and may suggest class, department, or patient lookup token.
- Separator pages are excluded from output by default but retained in the immutable batch manifest.
- Missing first separators, consecutive separators, unknown codes, and unreadable barcodes create visible exceptions.
- The operator can merge, split, reorder, or reject proposals before confirmation.
- Confirmation seals bundle boundaries and emits independent assembly requests; no suggested patient match is accepted automatically.

## Frappe realization

- **DocTypes:** `OC Barcode Separator Template` (facility, purpose, payload_schema, signing_key_id, expiry) and `OC Batch Split Proposal` with child `OC Proposed Bundle` and page-range rows.
- **Hooks/jobs:** An RQ barcode job reads quarantined page Files; `open_chart.documents.on_file` records separator evidence without modifying source attachments.
- **Workflow:** Detecting → Operator Review → Confirmed, with Ambiguous and Rejected states.
- **Roles/permissions:** Scanning Operator reviews splits; Document Configuration Manager controls templates; patient tokens remain permlevel 1.
- **Surfaces:** Desk thumbnail strip highlights separators and exceptions; a Jinja Print Format creates QR/barcode separator sheets with facility Letter Head.

## Boundaries

Owns: separator definitions, split proposals, confirmed ranges, and separator provenance. Consumes: scan-session pages. Emits: bundle manifests. Does not own: document assembly, definitive patient matching, or clinical classification approval.

## Open questions

- How should separator signing keys rotate while old batches remain reproducible?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Multi-page PDF Assembly](openchart-feature-catalog-dms-003-multi-page-pdf-assembly.md)
