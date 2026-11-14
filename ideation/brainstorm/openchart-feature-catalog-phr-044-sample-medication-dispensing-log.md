# Sample Medication Dispensing Log — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records accountable issuance of medication samples with patient, product, lot, expiry, quantity, prescriber, and counseling evidence.
Topics: openchart-feature-catalog, eprescribing, frappe, medication-samples
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-044 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Sample recall outreach** — Lot-based queries could create reviewed patient-contact lists when a manufacturer recall occurs.

## Focus

This feature isolates sample issuance from ordinary retail dispensing and prescribing. It preserves lot accountability and patient instructions even when no external pharmacy transaction occurs.

## Behavior

- Authorized staff select a patient, sample product, quantity, lot, expiry, prescriber authorization, and intended directions.
- The system verifies lot availability, expiry, sample eligibility, and any configured controlled-product prohibition.
- Patient identity and product are confirmed before handoff using barcode or controlled manual verification.
- Counseling and written-instruction delivery are documented before completion.
- Submission reduces sample inventory and records the issuance on the patient timeline.
- Corrections, returns, and recalled lots use linked events rather than deleting the issuance.

## Frappe realization

- **DocTypes:** Submittable `OC Medication Sample Dispense` links patient, authorizing prescriber, product, native barcode, lot, expiry, quantity, SIG, and counseling.
- **Workflow:** Authorized → Prepared → Verified Handoff → Completed, with Return and Correction paths.
- **Roles:** Clinical staff prepare; authorized prescriber or pharmacist verifies according to site policy; inventory roles manage sample lots.
- **Surfaces:** Quick Entry, barcode form, patient timeline, sample ledger report, and instruction Print Format support use.

## Boundaries

Owns: sample issuance and sample-stock movement. Consumes: authorization, patient identity, product lot, and directions. Emits: patient event, inventory decrement, and recall traceability. Does not own: manufacturer program governance or medication administration.

## Open questions

- Which roles may authorize and hand off samples under each jurisdiction?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Drug Recall Lot Traceability](openchart-feature-catalog-phr-055-drug-recall-lot-traceability.md)
