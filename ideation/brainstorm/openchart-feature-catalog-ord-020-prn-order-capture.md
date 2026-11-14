# PRN Order Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures as-needed orders with indication, minimum interval, dose limits, response assessment, and escalation parameters.
Topics: openchart-feature-catalog, cpoe, frappe, prn-orders
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-020 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **PRN effectiveness loop** — Link fulfillment responses back to ordering-clinician review without changing the order.

## Focus

This feature isolates complete, safe instructions for discretionary as-needed fulfillment.

## Behavior

- The orderer specifies the indication, observable trigger, minimum interval, maximum frequency or dose, and stop conditions.
- Required response assessment and reassessment timing are captured when relevant.
- Overlapping PRN orders for the same indication are displayed before signature.
- Missing indication or limit data blocks signing for governed orderables.
- Fulfillment records the trigger, action, response, and actor against the accepted order.
- PRN status does not authorize staff to exceed role scope or bypass escalation instructions.

## Frappe realization

- **DocTypes:** child `OC PRN Instruction` on submittable `OC Clinical Order` stores indication, trigger, interval, limits, reassessment, and escalation.
- **Workflow:** the parent order follows Draft → Active → Completed/Discontinued; PRN fulfillment is recorded separately.
- **Roles/permissions:** ordering roles author instructions; fulfillment roles create response records but cannot edit limits.
- **Hooks/API/surface:** `validate` enforces governed fields, `on_submit` checks duplicates, and v1 fulfillment methods expose active PRN orders by patient and class.

## Boundaries

Owns: PRN authorization parameters. Consumes: orderable policy and active orders. Emits: bounded as-needed instruction. Does not own: fulfillment judgment or medication administration.

## Open questions

- Which PRN classes require mandatory effectiveness documentation?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Titration Order Instructions](openchart-feature-catalog-ord-021-titration-order-instructions.md)
