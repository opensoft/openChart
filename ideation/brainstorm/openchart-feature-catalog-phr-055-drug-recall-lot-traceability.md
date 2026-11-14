# Drug Recall Lot Traceability — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Matches medication recall notices to in-house lots, dispensing records, samples, packs, and affected patient handoffs for reviewed action.
Topics: openchart-feature-catalog, eprescribing, frappe, drug-recalls
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-055 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Recall outreach campaign** — Approved affected-patient lists could feed consent-aware communication workflows with completion tracking.

## Focus

This feature isolates lot-level recall detection and accountable response. A match creates reviewed quarantine and follow-up work but never sends patient outreach or changes therapy autonomously.

## Behavior

- Authorized safety staff import or enter a recall with product identifiers, lots, reason, class, effective date, and source.
- The system matches in-stock lots, dispenses, samples, blister-pack components, returns, and transfers with confidence explanations.
- Exact matched stock is quarantined operationally; uncertain matches enter manual review.
- Staff verify affected quantities and generate a minimum-necessary patient or recipient review list from accepted records.
- Clinical leaders approve outreach, replacement, monitoring, or no-action plans before tasks are issued.
- The case tracks acknowledgements, dispositions, unresolved recipients, stock destruction/return, and final closure.

## Frappe realization

- **DocTypes:** `OC Medication Recall` with affected-lot, stock, dispense, recipient, action, and evidence child tables provides the case record.
- **Workflow:** Received → Matching Review → Active Response → Monitoring → Closed, with independent clinical and inventory approvals.
- **Hooks/jobs:** Recall activation queues deterministic lot matching and quarantine events; scheduled checks escalate unresolved actions.
- **Surfaces:** Recall command center, lot lineage report, permissioned recipient worklist, and closure report support response.

## Boundaries

Owns: local recall case, lot matching, response plan, and closure evidence. Consumes: authoritative notices, inventory lots, dispense/sample/pack records, and consent. Emits: quarantine, reviewed outreach tasks, and disposition evidence. Does not own: manufacturer recall authority or autonomous patient contact.

## Open questions

- What confidence threshold permits automatic operational quarantine while still requiring human match review?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Expired-Stock Quarantine](openchart-feature-catalog-phr-041-expired-stock-quarantine.md)
