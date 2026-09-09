# Outbound Fax Delivery Tracking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Sends approved document packets by e-fax and records destination verification, attempts, provider receipts, and confirmed terminal outcomes.
Topics: openchart-feature-catalog, documents, frappe, outbound-fax
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-024 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Destination directory verification** — Require recent human verification for frequently used clinical fax endpoints.

## Focus

This feature isolates accountable e-fax transmission of an already authorized, sealed artifact.

## Behavior

- An authorized sender selects a sealed document or packet, recipient, verified fax number, purpose, and disclosure authority.
- The system displays a minimum-necessary preview and requires destination confirmation before queueing.
- The provider receives an immutable outbound copy with cover sheet and correlation identifier.
- Queued, transmitting, delivered, failed, cancelled, and uncertain are distinct states based on signed callbacks.
- Retries follow bounded policy and remain attempts under one transmission; changed destination requires a new transmission.
- Delivered means provider-confirmed terminal delivery, not recipient review or clinical acknowledgment.
- Every attempt creates disclosure evidence and preserves provider response codes without exposing document content.

## Frappe realization

- **DocTypes:** `OC Outbound Fax` (source_file, checksum, recipient, fax_number_snapshot, authority, state, disclosure_event) with child `OC Fax Attempt`.
- **Workflow:** Draft → Destination Verified → Queued → Delivered, with Failed, Uncertain, Cancelled, and Superseded states.
- **Roles/permissions:** Authorized Fax Sender prepares; Release Specialist handles ROI packets; integration role transmits only approved source Files.
- **API/jobs:** RQ sends via adapter; signed callback method updates idempotently; scheduler_events reconcile uncertain provider states.
- **Surfaces:** Fax Outbox workspace, delivery receipt Print Format, alerts, and Script Report for failures and retries.

## Boundaries

Owns: transmission intent, destination snapshot, attempts, provider receipts, and terminal state. Consumes: authorized sealed artifact and fax provider. Emits: delivery and disclosure evidence. Does not own: recipient acknowledgment, carrier infrastructure, or source packet authorization.

## Open questions

- When should uncertain delivery require manual phone verification rather than automated retry?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [E-fax Cost Controls](openchart-feature-catalog-dms-025-e-fax-cost-controls.md)
