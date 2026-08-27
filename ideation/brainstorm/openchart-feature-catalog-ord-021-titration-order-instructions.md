# Titration Order Instructions — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures bounded titration rules with targets, increments, intervals, maximums, monitoring, and escalation conditions.
Topics: openchart-feature-catalog, cpoe, frappe, titration-orders
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-021 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Titration trajectory view** — Compare authorized steps with observed measurements and recorded changes.

## Focus

This feature isolates explicit clinician authority for parameter-guided dose or rate adjustment.

## Behavior

- The orderer enters starting value, target range, measurement source, adjustment increment, interval, bounds, and escalation triggers.
- Structured units must be compatible across target and adjustment fields.
- The composer previews the full instruction in human-readable form for signer confirmation.
- Missing maximum, monitoring source, or stop condition blocks signing when policy requires it.
- Fulfillment staff record each adjustment and supporting observation without altering the order.
- Decision support may recommend a draft step, but a qualified human confirms each action according to policy.

## Frappe realization

- **DocTypes:** child `OC Titration Instruction` on `OC Clinical Order`; `OC Titration Action` links observation, prior value, new value, actor, and timestamp.
- **Workflow:** order Active → Target Met, Held, or Discontinued; action records are submitted evidence.
- **Roles/permissions:** `OC Prescriber` signs bounds; credentialed fulfillment roles record actions; permlevel 1 locks rule text.
- **Hooks/API/surface:** server validation checks units and bounds; guarded action API rejects out-of-range changes and exposes a patient-scoped trajectory report.

## Boundaries

Owns: titration authority and bounds. Consumes: observations and staff credentials. Emits: explicit adjustment actions. Does not own: device control or autonomous dosing.

## Open questions

- Which titration contexts require a second-clinician verification per adjustment?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Restricted Order Privileges](openchart-feature-catalog-ord-031-restricted-order-privileges.md)
