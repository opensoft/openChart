# Unit-Dose And Blister-Pack Support — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Supports pharmacist-verified packaging of dispensed medication into unit-dose or calendar blister packs with component and lot traceability.
Topics: openchart-feature-catalog, eprescribing, frappe, adherence-packaging
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-043 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Pack-change comparison** — Staff could compare successive cycle packs and highlight medication additions, removals, and timing changes.

## Focus

This feature isolates packaging instructions and verification for unit-dose and multi-medication blister packs. Packaging organizes dispensed doses but does not prove administration or adherence.

## Behavior

- Staff select eligible dispensing lines, pack type, cycle dates, administration times, and compartment layout.
- The system checks product stability, split/crush restrictions, lot expiry, prescription supply, and packaging compatibility when data exists.
- Each compartment maps to product, strength, quantity, lot, and intended time with a human-readable schedule.
- Changes after preparation invalidate verification and require repack or documented exception handling.
- A pharmacist verifies contents and labels before the pack is released.
- Returned, damaged, or corrected packs retain component and inventory reversal evidence.

## Frappe realization

- **DocTypes:** Submittable `OC Medication Pack` with compartment and component child tables links dispenses, lots, cycle dates, and verification.
- **Workflow:** Planned → Prepared → Pharmacist Check → Released/Rejected/Returned.
- **Surfaces:** Grid-based pack builder, barcode scanning, compartment-label Print Formats, and cycle worklist support preparation.
- **Hooks:** Submission reserves/consumes linked stock consistently and blocks expired or quarantined lots.

## Boundaries

Owns: packaging plan, component traceability, verification, and release. Consumes: verified dispenses, inventory lots, stability rules, and schedule. Emits: labeled pack and stock movements. Does not own: medication administration or adherence conclusions.

## Open questions

- Which stability and compatibility data can openChart distribute versus require sites to license?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Medication Synchronization Programs](openchart-feature-catalog-phr-045-medication-synchronization-programs.md)
