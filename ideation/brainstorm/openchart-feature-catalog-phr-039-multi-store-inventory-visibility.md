# Multi-Store Inventory Visibility — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Shows permissioned, freshness-labeled medication availability across dispensary locations without promising transfer or patient fulfillment.
Topics: openchart-feature-catalog, eprescribing, frappe, multi-store-inventory
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-039 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Inter-store transfer request** — Authorized staff could request a lot-aware transfer with acceptance at both locations.

## Focus

This feature isolates cross-location stock visibility for staff coordination. It distinguishes reported availability from reservable stock and avoids exposing sensitive controlled inventory broadly.

## Behavior

- Authorized users search an item and view available quantity by store, lot constraints, service status, and data freshness.
- Results distinguish exact product, therapeutically related product, and unavailable product without implying substitution.
- Controlled and sensitive inventory may show coarse availability or no quantity according to role and policy.
- Stale, offline, quarantined, reserved, and non-transferable stock is visibly separated.
- Users can contact a store or open a transfer request but cannot reserve or reroute a prescription from the search result alone.
- Every cross-store lookup and restricted-detail access is audited.

## Frappe realization

- **DocTypes:** Location-aware medication ledger read models expose item, lot, availability, restriction, and freshness from each tenant/site adapter.
- **Permissions/API:** User Permissions constrain facilities; a whitelisted federated availability API returns policy-filtered results.
- **Surfaces:** Desk search dialog, availability map/list, stale-site indicators, and cross-store audit report support operations.
- **Hooks/jobs:** Background synchronization and websocket updates refresh summaries without bypassing local stock authority.

## Boundaries

Owns: policy-filtered availability view and lookup audit. Consumes: authoritative local ledgers and location permissions. Emits: availability observations and transfer/contact intents. Does not own: substitution, reservation, or inter-site stock authority.

## Open questions

- What quantity granularity should be visible for controlled substances across locations?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Dispensary Inventory Counts](openchart-feature-catalog-phr-037-dispensary-inventory-counts.md)
