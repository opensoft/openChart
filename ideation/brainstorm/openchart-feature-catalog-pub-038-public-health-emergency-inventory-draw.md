# Public Health Emergency Inventory Draw — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records incident-specific draws, transfers, use, waste, and reconciliation of public-health emergency supplies.
Topics: openchart-feature-catalog, public-health, frappe, emergency-inventory
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-038 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Cache distribution manifest** — Track custody transfers across temporary sites and mobile teams.

## Focus

Auditable incident inventory movement with funding, lot, custody, and destination context.

## Behavior

- Authorized users select incident, source facility/cache, destination, item/lot, quantity, unit, purpose, and custodian.
- Transactions include allocation, draw, transfer, administration/use, waste, return, and adjustment.
- Every custody handoff records sending and receiving acknowledgment or an unresolved exception.
- Lot expiry or quarantine blocks normal draw and requires a separately authorized exception.
- Balances reconcile by incident, facility, funding source, lot, and transaction state.
- Closing an incident requires disposition of residual stock and explanation of unresolved variances.

## Frappe realization

- **DocTypes:** Add submittable `OC Emergency Inventory Transaction`, child lines, and `OC Inventory Custody Handoff` linked to incident and lot.
- **Workflow:** Use draft, dispatched, received, disputed, reconciled, cancelled, and amended transaction states.
- **Permissions:** Restrict by incident/facility User Permissions; require `OC Emergency Inventory Manager` for adjustments and exceptions.
- **Surfaces:** Provide barcode Print Formats, transfer mobile Web Form, balance Script Report, and incident closeout dashboard.

## Boundaries

Owns: emergency inventory custody and reconciliation. Consumes: incident, facilities, lots, funding, and users. Emits: balances, handoffs, and variances. Does not own: procurement, financial valuation, or clinical use records.

## Open questions

- Which non-vaccine supplies justify inclusion without turning this into general ERP inventory?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
