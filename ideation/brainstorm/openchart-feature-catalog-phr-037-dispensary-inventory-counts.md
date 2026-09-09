# Dispensary Inventory Counts — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Maintains lot-aware on-hand, reserved, quarantined, and available medication inventory with accountable count reconciliation.
Topics: openchart-feature-catalog, eprescribing, frappe, inventory-counts
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-037 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Cycle-count program** — Risk-based schedules could prioritize controlled, high-value, or fast-moving products for supervised counting.

## Focus

This feature isolates trustworthy dispensary quantity state by location, item, and lot. Physical counts and system quantities remain separately evidenced until an authorized reconciliation posts an adjustment.

## Behavior

- Staff view on-hand, reserved, quarantined, expired, and available quantities by item, lot, and storage location.
- Receiving, dispensing, transfer, return, destruction, and approved adjustment events change stock through traceable movements.
- A cycle or full count records expected quantity, observed quantity, counter, time, and variance.
- Significant or controlled-substance variances require independent review and cannot be silently adjusted.
- Negative availability, lot mismatch, duplicate scans, and concurrent updates are blocked or routed to exceptions.
- Submitted reconciliation preserves the original count and posts a separately attributable adjustment.

## Frappe realization

- **DocTypes:** `OC Medication Stock Ledger`, `OC Medication Lot`, and submittable `OC Inventory Count` with item/lot/location child rows provide the pharmacy-specific ledger.
- **Workflow:** Planned → Counting → Variance Review → Approved → Posted, with segregated counter and approver roles.
- **Roles/API:** Pharmacy inventory roles use guarded stock APIs; controlled inventory fields use restricted permlevels.
- **Surfaces:** Barcode count screen, location dashboard, variance Query Report, and immutable ledger view support operations.

## Boundaries

Owns: dispensary stock quantities, lot state, counts, and adjustments. Consumes: receiving, dispensing, transfer, return, and destruction events. Emits: availability and variance evidence. Does not own: general enterprise inventory or prescription decisions.

## Open questions

- Should Frappe ERPNext stock primitives be optional adapters or a required foundation for openChart dispensaries?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Medication Reorder Points](openchart-feature-catalog-phr-038-medication-reorder-points.md)
