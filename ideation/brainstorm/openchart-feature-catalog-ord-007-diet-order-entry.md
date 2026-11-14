# Diet Order Entry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures diet, texture, fluid, allergen, supplement, and timing instructions for nutrition fulfillment.
Topics: openchart-feature-catalog, cpoe, frappe, diet-orders
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-007 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Conflict visualization** — Compare a proposed diet with active nutrition restrictions before signature.

## Focus

This feature isolates structured clinical nutrition orders.

## Behavior

- Clinicians select diet pattern, texture, fluid consistency, restrictions, supplements, meal timing, and start time.
- Known food allergies and active nutrition orders appear alongside the composer.
- Incompatible texture, fluid, or allergen selections block signing with a specific conflict message.
- A replacement order explicitly supersedes the active diet rather than silently coexisting.
- Nutrition staff acknowledge and fulfill the current accepted order.
- Free-text comments supplement but cannot replace required structured safety fields.

## Frappe realization

- **DocTypes:** submittable `OC Clinical Order` with order_class `Diet`; child `OC Diet Instruction` stores diet, texture, fluid, restrictions, and supplements.
- **Workflow:** Draft → Pending Signature → Active → Acknowledged → Completed or Superseded.
- **Roles/permissions:** `OC Ordering Clinician` submits; `OC Nutrition Staff` acknowledges; allergy fields remain read-only references.
- **Hooks/API/surface:** `validate` checks incompatibilities, `on_submit` runs CDS and supersession logic, and filtered REST reads support the nutrition queue.

## Boundaries

Owns: clinical nutrition order. Consumes: allergies and diet catalog. Emits: current nutrition instruction. Does not own: menus, food inventory, or dietary assessment.

## Open questions

- Should multiple additive supplements coexist with exactly one primary diet order?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Order Hold And Resume](openchart-feature-catalog-ord-025-order-hold-and-resume.md)
