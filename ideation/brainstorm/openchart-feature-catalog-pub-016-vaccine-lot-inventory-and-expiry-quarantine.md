# Vaccine Lot Inventory And Expiry Quarantine — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Tracks vaccine lots by facility, expiry, quantity, funding source, and quarantine state to prevent use of unavailable stock.
Topics: openchart-feature-catalog, public-health, frappe, vaccine-lot-inventory
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-016 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Temperature excursion quarantine** — Hold affected lots pending documented viability review.

## Focus

Clinic vaccine lot availability and quarantine control, not a general enterprise inventory ledger.

## Behavior

- Inventory users receive lots with product, manufacturer, lot number, expiry, funding source, facility, and quantity.
- Transactions record receipt, transfer, administration draw, adjustment, return, waste, and emergency draw.
- Expired lots become quarantined automatically and disappear from normal administration selection.
- Manual quarantine requires reason, actor, effective time, and release authority.
- Negative on-hand balances are blocked; conflicting transactions retry under a document lock.
- Historical administrations retain lot snapshots even after depletion, return, or quarantine.

## Frappe realization

- **DocTypes:** Add `OC Vaccine Lot`, submittable `OC Vaccine Inventory Transaction`, and child line items with facility and funding dimensions.
- **Workflow:** Use available, quarantined, released, depleted, returned, and destroyed lot states; restrict quarantine release.
- **Permissions:** Grant operations to `OC Vaccine Inventory User` and overrides to `OC Vaccine Program Manager` with facility User Permissions.
- **Hooks and surfaces:** Validate balances on submit, run daily expiry quarantine, and provide lot List Views, expiry Query Report, barcode labels, and Number Cards.

## Boundaries

Owns: vaccine lot balances and usability states. Consumes: product catalog, facility, funding, and administration draws. Emits: selectable stock and transaction evidence. Does not own: general purchasing, accounting valuation, or clinical administration authority.

## Open questions

- Should general Frappe stock ledgers be integrated or deliberately isolated for clinical safety?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
