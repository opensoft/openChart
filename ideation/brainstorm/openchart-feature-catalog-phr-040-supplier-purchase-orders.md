# Supplier Purchase Orders — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Creates, approves, sends, and receives dispensary medication purchase orders with supplier, package, lot, and discrepancy controls.
Topics: openchart-feature-catalog, eprescribing, frappe, pharmacy-purchasing
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-040 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Controlled-substance ordering adapter** — Jurisdiction-specific controlled ordering could plug into the same approval and receiving evidence model.

## Focus

This feature isolates dispensary procurement from clinical prescribing. It supports human approval, supplier communication, receipt matching, and discrepancy evidence.

## Behavior

- Purchasing staff build a draft from approved replenishment requests or manual inventory need.
- Each line identifies supplier item, medication/product code, package size, quantity, price, destination, and controlled status.
- Approval checks supplier authorization, budget hook, package multiple, duplicate open orders, and required controlled-order process.
- Submission freezes the commitment and sends a traceable supplier order through an approved channel.
- Receiving records partial, complete, substituted, damaged, short, over, or rejected quantities with lot and expiry.
- Product substitutions require pharmacist review before stock becomes available.

## Frappe realization

- **DocTypes:** Submittable `OC Pharmacy Purchase Order` and `OC Pharmacy Receipt` with product, package, lot, expiry, price, and discrepancy child rows.
- **Workflow:** Draft → Inventory Review → Purchasing Approval → Ordered → Partially Received/Received/Closed, with controlled-product gates.
- **Roles/API:** Inventory staff request, purchasing staff commit, pharmacists approve substitutions, and guarded APIs integrate suppliers.
- **Surfaces:** Purchase workspace, supplier Print Format/PDF, receipt barcode form, and outstanding-order Query Report support procurement.

## Boundaries

Owns: dispensary supplier commitment and receiving evidence. Consumes: replenishment requests, supplier records, product catalog, and approvals. Emits: orders, receipts, and stock intake events. Does not own: general accounts payable, claims, or clinical selection.

## Open questions

- Where should financial posting responsibility end when openPractice or ERPNext is installed?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Medication Reorder Points](openchart-feature-catalog-phr-038-medication-reorder-points.md)
