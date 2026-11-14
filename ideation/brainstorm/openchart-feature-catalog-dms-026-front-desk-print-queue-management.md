# Front-desk Print Queue Management — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Queues approved print artifacts to facility printers with release, reprint, failure, and pickup evidence for front-desk workflows.
Topics: openchart-feature-catalog, documents, frappe, print-queue
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-026 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Badge-release printing** — Hold sensitive jobs until an authorized user releases them physically at the printer.

## Focus

This feature isolates controlled operational printing rather than treating browser print as an unaudited endpoint.

## Behavior

- An authorized user submits an already rendered artifact with printer, copies, duplex, color, stock, and pickup purpose.
- Queue policy verifies facility, printer capability, document sensitivity, and required secure-release mode.
- Print Operators see job metadata and preview classification but only content permitted by their role.
- Submitted, held, released, printing, printed, failed, cancelled, and collected are distinct states.
- Reprint requires a reason and creates a linked attempt without changing the original job.
- Printer offline, wrong stock, spool timeout, and partial print produce actionable failures and prevent false completion.
- Sensitive printed output requires collection confirmation or a documented destruction path for abandoned pages.

## Frappe realization

- **DocTypes:** `OC Printer` (facility, connector, capabilities, secure_release) and `OC Print Job` (source_file, checksum, settings JSON, classification, state) with attempt rows.
- **Workflow:** Submitted → Held/Released → Printing → Printed → Collected, with Failed, Cancelled, Reprint Requested, and Destroyed states.
- **Roles/permissions:** Print Requester submits; Print Operator releases; Front Desk User confirms collection; printer integration user sees only spool payload.
- **API/jobs:** `open_chart.api.v1.documents.queue_print`; RQ spool adapter and signed status callbacks update idempotently.
- **Surfaces:** Front Desk Print Queue workspace, realtime status, printer health dashboard, and pickup slip Print Format.

## Boundaries

Owns: print intent, release policy, spool attempts, status, reprint, and collection evidence. Consumes: sealed render, printer capabilities, and stock. Emits: controlled physical output event. Does not own: printer firmware, template authoring, or recipient identity proofing.

## Open questions

- Which classifications require secure badge release versus supervised front-desk collection?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Envelope and Label Stock Templates](openchart-feature-catalog-dms-029-envelope-and-label-stock-templates.md)
