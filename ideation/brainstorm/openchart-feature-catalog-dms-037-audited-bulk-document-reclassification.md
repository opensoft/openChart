# Audited Bulk Document Reclassification — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets authorized records staff reclassify or reroute selected documents in bulk through previewed, reasoned, reversible metadata operations.
Topics: openchart-feature-catalog, documents, frappe, bulk-reclassification
Repository context: openChart — Frappe v15 native EMR; catalog entry DMS-037 (Documents Scanning Templates And Printing)
Captured: 2026-08-24

## Possible feats

- **Policy-change migration planner** — Generate a staged batch when taxonomy or department ownership changes across many records.

## Focus

This feature isolates safe mass metadata correction without bulk-editing immutable files or patient identity.

## Behavior

- A Health Information Manager selects documents through an ACL-filtered query and chooses target class, department, tags, or storage category.
- The system freezes the selection and previews per-item old values, proposed values, policy effects, and blockers.
- Patient association, file content, signatures, accepted dates, and source provenance are never editable through this operation.
- Legal hold, class incompatibility, consent, active disclosure, and insufficient permission can block individual items.
- Approval requires a batch reason and may require second review for sensitive class changes.
- Execution processes idempotently, records success or failure per item, and never hides partial completion.
- Reversal creates a compensating batch using recorded prior values; it does not delete the original audit.

## Frappe realization

- **DocTypes:** `OC Document Bulk Change` (operation, frozen_filter JSON, reason, state, counts, reverses) with child `OC Document Bulk Change Item` (document_version, before JSON, after JSON, blockers, outcome).
- **Workflow:** Preparing → Preview → Approval → Executing → Reconciled, with Partial, Rejected, Cancelled, and Reversed states.
- **Roles/permissions:** Health Information Manager prepares; Privacy Reviewer approves sensitive changes; RQ integration role applies only submitted item plans.
- **Jobs/API:** Guarded bulk-plan and approve methods; bounded RQ workers use item idempotency keys and emit websocket progress.
- **Surfaces:** Desk preview grid, blocker filters, before/after export, and reconciliation Script Report.

## Boundaries

Owns: frozen selection, proposed metadata changes, approvals, item outcomes, and compensating reversal. Consumes: current metadata, ACL, and policy checks. Emits: audited metadata successor events. Does not own: file content edits, patient reassignment, clinical fact changes, or silent rollback.

## Open questions

- Which metadata changes require successor document versions rather than separate classification events?

## Relationships

[Synthesis: Documents Scanning And Printing](openchart-feature-catalog-synthesis-dms.md) · [Document Tagging and Saved Searches](openchart-feature-catalog-dms-033-document-tagging-and-saved-searches.md)
