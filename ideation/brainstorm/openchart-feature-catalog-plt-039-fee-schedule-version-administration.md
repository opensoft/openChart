# Fee Schedule Version Administration — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Maintains effective-dated fee schedule versions and code prices as governed reference configuration for downstream billing owners.
Topics: openchart-feature-catalog, platform, frappe, fee-schedules
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-039 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Price-change impact report** — Compare versions and identify unusually large or missing code changes before publication.

## Focus

This feature isolates reference fee configuration in openChart while leaving claims, invoices, contracts, and revenue operations outside its boundary.

## Behavior

- Fee administrators create a schedule for an organization, site scope, currency, purpose, effective dates, and source.
- Version lines link active procedure codes to amounts, units, modifiers, and optional location overrides.
- Dry run validates code versions, duplicates, gaps, overlaps, currency consistency, and change thresholds.
- Schedules move through Draft, Review, Published, Retired, and Superseded states.
- Publication never rewrites prior versions; consumers resolve the version effective for their documented date and context.
- Import errors and missing code mappings remain row-level exceptions and block activation when policy requires completeness.

## Frappe realization

- **DocTypes:** `OC Fee Schedule` and child `OC Fee Schedule Line` store organization, scope, version, dates, code Link, amount, modifier, and state.
- **Workflow:** Fee Administrator authors; Fee Approver publishes; openChart roles receive read-only reference access.
- **Import/surface:** Data Import mapping templates support dry run; Query Report compares versions and flags gaps or threshold breaches.
- **API:** read-only `open_chart.api.v1.platform.resolve_fee_reference` returns amount plus schedule version and provenance to authorized consumers.

## Boundaries

Owns: versioned fee reference configuration. Consumes: procedure code releases, organizational scope, and approved source data. Emits: effective fee references and change events. Does not own: payer contracts, charge capture, claims, invoices, or payment.

## Open questions

- Should location overrides inherit unchanged lines or require a fully explicit schedule?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Terminology And Code-set Updates](openchart-feature-catalog-plt-038-terminology-and-code-set-updates.md)
