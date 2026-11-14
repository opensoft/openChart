# Clinical Label Printing Engine — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Renders and prints specimen, address, and pharmacy labels from approved data snapshots with symbology, stock, and reprint controls.
Topics: openchart-feature-catalog, documents, frappe, label-printing
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-027 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Scanner verification loop** — Scan a printed barcode before use to confirm it decodes to the intended immutable payload.

## Focus

This feature isolates shared label rendering and print evidence while domain owners retain authority over label content.

## Behavior

- A permitted workflow requests a label kind, source record, stock template, printer, copies, and purpose.
- The engine snapshots allowlisted source values and validates mandatory identifiers, expiry, and barcode payload length.
- A preview shows human-readable text, encoded value, stock dimensions, and clipping warnings.
- Printing uses the approved snapshot so later source edits cannot change an in-flight label silently.
- Specimen, address, and pharmacy labels remain visibly distinct and cannot substitute templates across kinds.
- Failed or partial jobs remain unresolved; reprints require reason and display reprint sequence when policy requires.
- The engine records requester, source version, template version, output checksum, printer, and completion receipt.

## Frappe realization

- **DocTypes:** `OC Label Template` (kind, stock, symbology, Jinja layout, allowed_fields, version) and `OC Label Print Request` (source Dynamic Link, snapshot JSON, printer, copies, state).
- **Print formats:** Frappe Jinja Print Formats render PDF/ZPL-compatible outputs; barcode/QR generation and dimension tests use stock metadata.
- **Workflow/permissions:** Requested → Previewed → Released → Printed; domain-specific requester roles submit, Label Administrator approves templates, Print Operator handles failures.
- **API/jobs:** Guarded `open_chart.api.v1.documents.request_label`; RQ printer connector and idempotent status callbacks.
- **Surfaces:** Label preview dialog, reprint reason prompt, queue workspace, and template test page using synthetic data.

## Boundaries

Owns: label templates, render snapshot, symbology validation, print request, and reprint evidence. Consumes: authorized source values, stock, and printer. Emits: label output event. Does not own: specimen accessioning, medication dispensing, address authority, or printer firmware.

## Open questions

- Which barcode symbologies and minimum print-quality tests are required for each label kind?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Envelope and Label Stock Templates](openchart-feature-catalog-dms-029-envelope-and-label-stock-templates.md)
