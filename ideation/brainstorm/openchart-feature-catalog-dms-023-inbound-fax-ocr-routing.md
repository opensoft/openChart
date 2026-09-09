# Inbound Fax OCR Routing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Receives inbound e-faxes into quarantine and uses OCR evidence to propose patient, document class, and department routing for human review.
Topics: openchart-feature-catalog, documents, frappe, inbound-fax
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-023 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Known-sender profiles** — Apply sender-specific cover-page, routing, and expected-document rules without bypassing identity review.

## Focus

This feature isolates first-party fax intake and triage from external fax transport and final chart attachment.

## Behavior

- A signed provider webhook creates one inbound fax receipt with sender, called number, timestamps, page count, and delivery identifier.
- The received PDF remains private and quarantined while malware, checksum, and page-count checks run.
- Background OCR proposes patient, class, urgency, and department with confidence and source-page evidence.
- Fax Triage staff accept, edit, or reject each proposal before routing or attachment.
- No patient match sends the receipt to the unmatched queue; unreadable or incomplete transmissions request manual handling.
- Duplicate transport callbacks are idempotent and append no duplicate document.
- Sender identity, raw provider payload digest, OCR run, and every triage decision remain auditable.

## Frappe realization

- **DocTypes:** `OC Inbound Fax` (provider_id, sender, called_number, received_at, page_count, File, state) linked to OCR run and indexing review.
- **Files/hooks/jobs:** Frappe private file manager plus `open_chart.documents.on_file`; RQ OCR and triage-suggestion jobs start only after transport and malware validation.
- **Workflow:** Received → Processing → Triage → Routed/Attached, with Unmatched, Incomplete, Duplicate, and Rejected states.
- **Roles/permissions:** Fax Triage reviews; Patient Identity Reviewer resolves matches; fax integration role can create receipts but cannot read chart data.
- **API/surfaces:** Signed `open_chart.api.v1.documents.receive_fax` webhook, Fax Inbox workspace, Assignment Rules, and aging dashboard.

## Boundaries

Owns: inbound receipt, quarantined file, triage proposals, and disposition. Consumes: e-fax payload, OCR, and patient search. Emits: routed or typed document candidate. Does not own: carrier transport, patient merge, or automatic clinical action.

## Open questions

- Which sender and called-number signals may influence routing without creating unsafe trust shortcuts?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Department Document Routing Inbox](openchart-feature-catalog-dms-007-department-document-routing-inbox.md)
