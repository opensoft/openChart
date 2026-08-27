# Medication Reorder Points — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Monitors available medication stock against configurable reorder points and creates reviewable replenishment requests.
Topics: openchart-feature-catalog, eprescribing, frappe, reorder-points
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-038 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Demand-informed recommendation** — Usage history could suggest reorder settings for manager approval without placing orders automatically.

## Focus

This feature isolates threshold-based inventory replenishment signals. It creates a reviewable request and never commits a supplier purchase autonomously.

## Behavior

- Inventory managers configure minimum, target, maximum, lead time, package multiple, and preferred supplier by item and location.
- Availability changes or scheduled evaluation compare usable stock and open purchase quantities with the active rule.
- Crossing a threshold creates or updates one deduplicated replenishment request with calculation evidence.
- Quarantined, expired, reserved, and recalled stock is excluded from available quantity.
- Managers adjust, approve, defer, or close requests with reasons and can see demand and shortage context.
- Approved requests may seed a purchase order draft but cannot submit it automatically.

## Frappe realization

- **DocTypes:** `OC Medication Reorder Rule` and `OC Replenishment Request` store effective thresholds, calculation snapshot, status, and purchase-order link.
- **Hooks/jobs:** Ledger updates enqueue checks; daily `scheduler_events` catches drift and deduplicates open requests.
- **Roles:** Inventory managers publish rules and approve requests; purchasing roles own supplier commitments.
- **Surfaces:** Low-stock Number Cards, replenishment worklist, trend chart, and rule coverage report support review.

## Boundaries

Owns: reorder policy evaluation and replenishment request. Consumes: available stock, open purchase quantities, and configured rules. Emits: reviewable purchase demand. Does not own: supplier commitment or automatic procurement.

## Open questions

- Which demand signals are trustworthy enough to inform but not automate reorder recommendations?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Supplier Purchase Orders](openchart-feature-catalog-phr-040-supplier-purchase-orders.md)
