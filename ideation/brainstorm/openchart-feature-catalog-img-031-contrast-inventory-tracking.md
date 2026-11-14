# Contrast Inventory Tracking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Tracks contrast stock, lot, expiry, location, reservation, administration consumption, waste, and recall linkage for imaging operations.
Topics: openchart-feature-catalog, imaging, frappe, contrast-inventory
Repository context: openChart — Frappe v15 native EMR; catalog entry IMG-031 (Imaging Workflows)
Captured: 2026-08-24

## Possible feats

- **Expiry-aware replenishment** — Forecast reviewed reorder needs from scheduled demand and expiring stock.

## Focus

This feature isolates clinical traceability and imaging availability for contrast inventory while leaving general procurement external.

## Behavior

- Authorized staff receive contrast by product, concentration, package, lot, expiry, quantity, and storage location.
- Scheduled studies may reserve expected quantity without decrementing stock until issue or administration.
- Performance documentation reconciles administered, opened, returned, and wasted quantities against lot numbers.
- Expired, quarantined, recalled, or unavailable stock cannot be issued for use.
- Count adjustments require a reason, actor, timestamp, and optional witness according to policy.
- Recall queries identify affected administrations and create reviewed outreach tasks without autonomous patient action.

## Frappe realization

- **DocTypes:** `OC Contrast Stock Item`, `OC Contrast Lot`, and `OC Contrast Movement` linked to performance and administration records.
- **Workflow:** Available → Reserved → Issued → Consumed or Returned, with Quarantined, Recalled, Expired, and Wasted dispositions.
- **Roles/permissions:** inventory staff transact; technologists consume against studies; managers adjust; clinical users read administration provenance.
- **Hooks/API/surfaces:** server validates nonnegative balances and lot eligibility; barcode client actions support issue; reports show expiry, recall, and variance.

## Boundaries

Owns: contrast lot traceability and imaging stock movements. Consumes: receiving data, schedule demand, and administrations. Emits: availability, consumption, and recall cohorts. Does not own: purchasing, accounts payable, or general enterprise inventory.

## Open questions

- Should openChart maintain stock balances directly or reconcile a specialized inventory system while retaining clinical lot traceability?

## Relationships

[Synthesis: Imaging Workflows](openchart-feature-catalog-synthesis-img.md)
