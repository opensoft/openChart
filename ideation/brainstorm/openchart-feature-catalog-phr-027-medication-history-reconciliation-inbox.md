# Medication History Reconciliation Inbox — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets clinicians compare external medication candidates with the local chart and record accept, reject, map, or defer decisions.
Topics: openchart-feature-catalog, eprescribing, frappe, history-reconciliation
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-027 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Source discrepancy summary** — Reviewers could see where patient report, network history, and local prescriptions disagree.

## Focus

This feature isolates the reconciliation decision surface for network medication history. It reuses provenance-bearing medication statements and keeps every source candidate and disposition visible.

## Behavior

- The inbox groups external candidates by retrieval, patient, medication identity, and likely local matches.
- Reviewers compare product, dose, dates, prescriber, pharmacy, source type, and confidence side by side.
- Each candidate is accepted as a new statement, mapped to existing history, rejected with reason, or deferred to a named reviewer.
- Acceptance requires the reviewer to choose assertion status and provenance; fill data alone cannot assert current use.
- Ambiguous identity, dosage, or duplication prevents silent write-through.
- Completion records reviewer signature, timestamp, source versions, and all item-level dispositions.

## Frappe realization

- **DocTypes:** `OC Medication History Reconciliation` with child dispositions links staged candidates and existing `OC Medication Statement` records.
- **Workflow:** Open → In Review → Needs Clarification → Signed Complete, with succession for later corrections.
- **Roles/API:** Clinical reconciliation roles use guarded `open_chart.api.v1.medications.reconcile_history`; direct statement writes remain blocked.
- **Surfaces:** Side-by-side Desk workspace, filters, assignment queue, and unresolved-items Query Report support review.

## Boundaries

Owns: reconciliation session and dispositions. Consumes: staged network candidates and local medication statements. Emits: reviewed successor statements and discrepancy evidence. Does not own: external data correctness or autonomous acceptance.

## Open questions

- Which medication history dispositions require a prescriber versus another licensed clinician?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Network Medication History Retrieval](openchart-feature-catalog-phr-026-network-medication-history-retrieval.md)
