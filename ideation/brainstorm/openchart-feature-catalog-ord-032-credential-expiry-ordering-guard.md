# Credential Expiry Ordering Guard — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Detects expiring or expired ordering credentials and prevents new restricted orders outside their effective authorization window.
Topics: openchart-feature-catalog, cpoe, frappe, credential-expiry
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-032 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Upcoming access impact list** — Show providers and restricted order classes affected by credentials nearing expiry.

## Focus

This feature isolates time-sensitive enforcement and notice around ordering credentials.

## Behavior

- Credentialing staff and providers receive advance notices according to credential type and risk.
- At order signature, effective dates are evaluated using the care location's configured time zone.
- An expired credential blocks new restricted orders even if the draft began earlier.
- Already accepted orders remain historically valid but may trigger a responsibility reassignment review.
- Renewal creates updated credential evidence and never rewrites the expired record.
- Scheduler failures appear as operational exceptions; server-side signature checks remain authoritative.

## Frappe realization

- **DocTypes:** `OC Ordering Privilege` stores valid_from, valid_until, renewal_source, predecessor, and immutable verification evidence.
- **Workflow:** Active → Expiring → Expired; successor verification returns authorization to Active.
- **Roles/permissions:** `OC Credentialing Officer` verifies; providers read notices; order submit checks cannot be overridden by client scripts.
- **Scheduler/API/surface:** daily scheduler creates notices and states; signature service evaluates dates directly; REST expiry filters support credentialing worklists.

## Boundaries

Owns: expiry status and ordering-time guard. Consumes: verified credential dates and facility time zone. Emits: notices and denials. Does not own: renewal approval.

## Open questions

- When should accepted high-risk orders be reassigned after the orderer's privilege expires?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Restricted Order Privileges](openchart-feature-catalog-ord-031-restricted-order-privileges.md)
