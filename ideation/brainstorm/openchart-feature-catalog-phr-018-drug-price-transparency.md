# Drug Price Transparency — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Compares clearly sourced patient-cost estimates and cash options at prescribe time without representing estimates as guarantees.
Topics: openchart-feature-catalog, eprescribing, frappe, drug-price
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-018 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Patient cost discussion record** — Prescribers could document that options were reviewed without storing unnecessary financial detail.

## Focus

This feature isolates comprehensible price display across benefit and permitted cash-discount sources. It emphasizes assumptions, freshness, and uncertainty rather than optimizing medication choice automatically.

## Behavior

- The user sees estimated out-of-pocket cost for the selected product, quantity, pharmacy, and coverage scenario.
- Comparable generic, therapeutic, mail-order, and cash options appear only when a source supports them.
- Every value shows source, timestamp, quantity, days supply, pharmacy assumptions, and estimate disclaimer.
- Missing prices, incompatible quantities, coupons with restrictions, and stale results are visibly distinguished.
- Selecting an option changes only an editable draft and requires fresh clinical and benefit review.
- Price viewing and option selection are audited without exposing values to roles lacking coverage access.

## Frappe realization

- **DocTypes:** Child `OC Medication Price Option` belongs to `OC Benefit Inquiry` and stores source, scenario, currency, amount range, assumptions, and expiry.
- **Permissions:** Financially sensitive fields use higher permlevels while clinical users receive the minimum needed for shared decision-making.
- **Surfaces:** A normalized comparison table, accessibility-friendly labels, and print-disabled sensitive panel present estimates.
- **Hooks:** Server normalization rejects mismatched units and expires options after configured freshness windows.

## Boundaries

Owns: normalized price estimate display and provenance. Consumes: benefit responses and approved price sources. Emits: user-selected draft option and audit event. Does not own: claims adjudication, coupon eligibility, or guaranteed patient cost.

## Open questions

- Which price sources may be shown together without creating misleading equivalence?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Real-Time Benefit And Formulary Check](openchart-feature-catalog-phr-017-real-time-benefit-and-formulary-check.md)
