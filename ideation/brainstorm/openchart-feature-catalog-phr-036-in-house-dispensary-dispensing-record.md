# In-House Dispensary Dispensing Record — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records pharmacist-verified dispensing against a prescription with product, quantity, lot, expiry, patient, and handoff provenance.
Topics: openchart-feature-catalog, eprescribing, frappe, dispensing-record
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-036 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Partial-fill series** — Multiple accountable dispensing events could close one prescription quantity over time with remaining-balance controls.

## Focus

This feature isolates the accepted dispensing event for an openChart-operated dispensary. It is distinct from prescribing, administration, inventory movement, and patient-reported medication use.

## Behavior

- Authorized dispensary staff select an eligible prescription and verify patient, product, strength, dosage form, quantity, and destination.
- Lot, expiry, manufacturer, package identifier, and stock location are captured from barcode or controlled manual entry.
- The system checks prescription status, remaining quantity, product match, stock state, and expiry before allowing pharmacist verification.
- Partial, complete, declined, returned-to-stock, and not-dispensed outcomes are represented explicitly.
- Pharmacist verification submits an immutable dispensing record and posts linked inventory movements.
- Corrections use cancellation or successor records with reason; they never rewrite the accepted event.

## Frappe realization

- **DocTypes:** Submittable `OC Dispense` with naming series `OC-DSP-.YYYY.-.#####` and child lines links `OC Prescription`, stock batch, lot, expiry, and handoff.
- **Workflow:** Draft → Technician Prepared → Pharmacist Verification → Dispensed/Not Dispensed, with controlled cancellation and successor correction.
- **Roles/API:** `OC Pharmacy Technician` prepares; `OC Pharmacist` verifies and submits through guarded v1 dispensing methods.
- **Surfaces/hooks:** Dispensary workspace, barcode scan fields, `on_submit` stock movement, patient timeline, and receipt Print Format support operations.

## Boundaries

Owns: verified dispensing fact and prescription quantity application. Consumes: prescription, patient identity, inventory lot, and pharmacist authority. Emits: dispense event, inventory movement, and status update. Does not own: medication administration, claims, or adherence.

## Open questions

- Which correction cases require cancelling the dispense versus a separate reversal event?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Dispensary Inventory Counts](openchart-feature-catalog-phr-037-dispensary-inventory-counts.md)
