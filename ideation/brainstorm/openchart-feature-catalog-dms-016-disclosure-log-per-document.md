# Disclosure Log Per Document — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records every authorized external disclosure against the exact document version, recipient, purpose, authority, channel, and delivery outcome.
Topics: openchart-feature-catalog, documents, frappe, disclosure-log
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-016 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Patient disclosure accounting view** — Present a permissioned, explainable history of qualifying disclosures and corrections.

## Focus

This feature isolates durable disclosure evidence at document-version granularity.

## Behavior

- Any external share or ROI delivery creates a pending disclosure event before transmission.
- The event identifies exact source versions or packet manifest, recipient, destination, purpose, authority, minimum-necessary basis, and actor.
- Transmission success, failure, cancellation, and recipient confirmation are separate outcomes.
- Retries append attempts under the same disclosure event and never imply multiple legal disclosures without policy basis.
- A corrected recipient or destination creates a successor event with reason rather than editing delivered history.
- Authorized Privacy staff can inspect disclosure history from a patient or document timeline.
- Direct File URLs and unlogged external downloads are blocked for governed classes.

## Frappe realization

- **DocTypes:** `OC Disclosure Event` (patient, recipient, purpose, authority_basis, channel, state, disclosed_at) with child `OC Disclosed Item` (document_version, checksum, packet_page_range) and `OC Delivery Attempt`.
- **Workflow:** Authorized → Sending → Delivered, with Failed, Cancelled, Recalled, and Corrected states.
- **Roles/permissions:** Release Specialist initiates; Privacy Officer audits/corrects; ordinary clinicians see only policy-allowed disclosure summaries; destinations use permlevel 2.
- **Hooks/API:** Export/download whitelisted methods require a disclosure context; `on_submit` emits immutable audit events and prevents direct governed File sharing.
- **Surfaces:** Document and patient disclosure timelines, Query Report, and disclosure-accounting Print Format.

## Boundaries

Owns: disclosure event, item manifest, recipient evidence, and delivery outcomes. Consumes: authorization, sealed packet or document versions, and channel receipts. Emits: auditable disclosure accounting. Does not own: recipient identity system, ROI scope, or source document content.

## Open questions

- Which internal transfers count as disclosures under configurable organizational policy?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [ROI Fulfillment Packet Assembly](openchart-feature-catalog-dms-015-roi-fulfillment-packet-assembly.md)
