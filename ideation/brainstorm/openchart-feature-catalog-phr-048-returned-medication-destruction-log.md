# Returned-Medication Destruction Log — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Tracks custody, quarantine, witness verification, method, and final disposition for returned or unusable medications awaiting destruction.
Topics: openchart-feature-catalog, eprescribing, frappe, medication-destruction
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-048 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Destruction manifest export** — Sites could produce regulator- or vendor-ready manifests from witnessed events.

## Focus

This feature isolates chain of custody and destruction evidence. A returned medication never re-enters available stock unless a separately governed policy explicitly permits and documents it.

## Behavior

- Staff receive returned, expired, damaged, recalled, contaminated, or otherwise unusable medication into quarantine.
- Intake captures source category, product, quantity, lot when known, controlled status, receiver, time, and secure location.
- The system assigns custody and requires reconciled quantity before transfer or destruction.
- Controlled or policy-designated products require two authorized witnesses with segregation of duties.
- Final disposition records method, vendor or facility, date, quantity, witnesses, manifest reference, and discrepancies.
- Submitted events post inventory adjustments and preserve immutable custody history and attachments.

## Frappe realization

- **DocTypes:** `OC Medication Return Custody` and submittable `OC Medication Destruction` store chain-of-custody events, native barcodes, witnesses, quantities, and manifests.
- **Workflow:** Received → Quarantined → Scheduled → Witnessed Destruction/Transferred → Closed, with discrepancy review.
- **Roles:** Pharmacy inventory staff receive; pharmacists and designated witnesses approve; no actor can satisfy both required witness fields.
- **Surfaces:** Barcode intake, custody ledger, destruction Print Format, and overdue-quarantine Query Report support compliance.

## Boundaries

Owns: returned-stock custody, quarantine, destruction evidence, and ledger adjustment. Consumes: physical medication, lot data, policy, and authorized witnesses. Emits: manifests and inventory disposition. Does not own: environmental regulation or vendor disposal operations.

## Open questions

- Which return categories may be accepted from patients, and what identifying data may be retained?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Expired-Stock Quarantine](openchart-feature-catalog-phr-041-expired-stock-quarantine.md)
