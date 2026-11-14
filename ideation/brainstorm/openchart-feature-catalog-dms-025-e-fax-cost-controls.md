# E-fax Cost Controls — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies transparent page, destination, retry, and budget controls to e-fax use without overriding authorized urgent communication silently.
Topics: openchart-feature-catalog, documents, frappe, fax-cost-control
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-025 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Channel alternative suggestion** — Show approved lower-cost delivery options when purpose, consent, and recipient capability permit.

## Focus

This feature isolates operational spend governance around fax transmission while preserving human override authority.

## Behavior

- A Communications Administrator configures provider rates, page thresholds, international destinations, retry limits, and facility budgets.
- Before queueing, the sender sees estimated pages, cost band, retry policy, and any threshold requiring approval.
- Ordinary transmissions over policy enter Cost Approval Required rather than failing without explanation.
- Authorized urgent overrides require reason and are visibly separated from routine approvals.
- Actual provider-rated cost reconciles to the transmission and attempt records after delivery or failure.
- Duplicate, oversized, excessive-retry, and unusual-destination patterns create review alerts.
- Cost controls never reduce packet content automatically or change clinical/disclosure scope.

## Frappe realization

- **DocTypes:** `OC Fax Cost Policy` (facility, provider, rates, thresholds, budget, effective dates) and `OC Fax Cost Approval` linked to outbound fax.
- **Workflow:** Estimated → Within Policy/Approval Required → Approved, with Denied, Urgent Override, and Reconciled outcomes.
- **Roles/permissions:** Communications Administrator configures; Department Approver decides thresholds; sender may request but not self-approve beyond limit.
- **Hooks/reports:** Outbound Fax `validate` calculates estimate; provider callback records actual Currency values; monthly Script Report and Dashboard Charts show variance.
- **Surfaces:** Inline estimate, approval Assignment, Number Cards, and facility budget alerts.

## Boundaries

Owns: fax pricing policy, estimates, approvals, actual-cost reconciliation, and anomaly alerts. Consumes: packet page count, destination, provider rates, and attempts. Emits: send authorization or cost exception. Does not own: clinical urgency, disclosure scope, carrier billing disputes, or packet alteration.

## Open questions

- Which urgent roles may override cost controls, and what retrospective review is required?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Outbound Fax Delivery Tracking](openchart-feature-catalog-dms-024-outbound-fax-delivery-tracking.md)
