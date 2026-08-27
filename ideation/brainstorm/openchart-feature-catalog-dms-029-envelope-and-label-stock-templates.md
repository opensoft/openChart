# Envelope and Label Stock Templates — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Defines versioned physical stock geometry, printer compatibility, margins, orientation, and calibration for reliable envelope and label output.
Topics: openchart-feature-catalog, documents, frappe, print-stock
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-029 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Calibration test sheet** — Print measurable guides and record per-printer offsets against a stock version.

## Focus

This feature isolates physical media definitions shared by envelope, address-label, specimen-label, and other print workflows.

## Behavior

- A Print Administrator defines stock kind, dimensions, rows, columns, gaps, margins, feed orientation, and printable area.
- Templates declare compatible printers and render languages plus facility-specific calibration offsets.
- Synthetic preview shows clipping, overlap, barcode quiet-zone, and nonprintable-margin violations.
- A stock version requires test-print evidence before activation.
- Active versions are immutable; dimension or calibration changes create successors.
- Print requests fail clearly when printer, stock, template, or orientation is incompatible.
- Retired stock remains resolvable for historical job reproduction but cannot receive new jobs.

## Frappe realization

- **DocTypes:** `OC Print Stock` (kind, dimensions, grid, margins, orientation, version, state) and child `OC Stock Printer Calibration` (printer, offsets, tested_at, evidence_file).
- **Workflow:** Draft → Test Print → Approved → Active, with Failed Calibration, Retired, and Superseded states.
- **Roles/permissions:** Print Administrator authors; Print Quality Reviewer approves; requesters may select only active facility-compatible stock.
- **Print formats:** Jinja Print Format test sheets and PDF/ZPL render validators use stock geometry and synthetic sample values.
- **Surfaces:** Stock designer, visual ruler preview, compatibility report, and calibration history.

## Boundaries

Owns: stock geometry, compatibility, calibration, version, and test evidence. Consumes: printer capabilities and render template dimensions. Emits: approved physical-layout contract. Does not own: label content, printer queue, consumable inventory, or postal rules.

## Open questions

- Should calibration be per physical printer, printer model, driver version, or all three?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Front-desk Print Queue Management](openchart-feature-catalog-dms-026-front-desk-print-queue-management.md)
