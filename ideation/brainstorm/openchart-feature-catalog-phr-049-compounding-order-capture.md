# Compounding Order Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures a prescriber-reviewed compounded medication formula, ingredients, concentrations, preparation instructions, beyond-use expectations, and dispensing requirements.
Topics: openchart-feature-catalog, eprescribing, frappe, compounding
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-049 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Master-formula linkage** — Governed pharmacy formulas could seed editable orders while preserving the exact version used.

## Focus

This feature isolates prescription capture for medications that cannot be represented by a standard product alone. It supports detailed human-authored formula instructions without claiming manufacturing validation.

## Behavior

- The prescriber identifies dosage form, total quantity, route, SIG, indication, and whether a named formula is used.
- Ingredient rows capture substance, strength or concentration, quantity, unit, role, and permitted substitutions.
- The order records preparation notes, packaging, storage, flavoring, allergen concerns, and expected beyond-use requirements.
- Unit, concentration, ingredient duplication, and total-quantity inconsistencies are checked and explained.
- A pharmacist clarification response may propose changes, but the prescriber must sign any material successor order.
- The transmitted or printed prescription preserves exact structured components and human-readable rendition.

## Frappe realization

- **DocTypes:** Submittable `OC Compounded Prescription` extends the Prescription family with ingredient and preparation child tables and formula-version links.
- **Workflow:** Draft → Pharmacist Clarification if needed → Ready to Sign → Signed → Routed, preserving successor amendments.
- **Roles/API:** Prescribers author/sign; pharmacists respond to clarifications; guarded APIs render and route supported structured or document payloads.
- **Surfaces:** Compound composer, calculation panel, detailed prescription Print Format, and clarification workspace support use.

## Boundaries

Owns: compounded prescription intent, components, instructions, and clarification lineage. Consumes: ingredient terminology, formula references, and prescriber authority. Emits: signed compound order. Does not own: preparation execution, sterility assurance, or autonomous formulation.

## Open questions

- Which compounding profiles can be exchanged electronically versus requiring a signed document rendition?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Prescription Print Report](openchart-feature-catalog-phr-051-prescription-print-report.md)
