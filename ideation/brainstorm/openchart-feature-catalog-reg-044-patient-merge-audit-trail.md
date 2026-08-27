# Patient Merge Audit Trail — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Preserves an immutable, inspectable account of every approved patient merge, moved reference, field decision, and post-merge correction.
Topics: openchart-feature-catalog, registration, frappe, merge-audit
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-044 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Merge impact export** — Produce a regulator- or privacy-review package with redacted reference details.

## Focus

Make identity consolidation reconstructable after execution without relying only on generic database history.

## Behavior

- Merge execution creates a sealed event recording source, survivor, approvals, policy, and timestamps.
- Every reparented, aliased, retained, or blocked reference receives an outcome entry.
- Field-level survivor choices preserve prior values and the reviewer who selected them.
- Authorized users can trace a retired patient reference to the survivor without reopening the source chart.
- Corrections append a linked audit event and never rewrite the original merge record.
- Access to audit detail is itself logged and respects sensitive-record restrictions.

## Frappe realization

- **DocTypes:** submittable `OC Patient Merge Audit` and child `OC Merge Audit Item` with immutable hashes, reference type, old/new links, outcome, and error.
- **Workflow:** Generated → Reconciled → Sealed; correction uses a new submitted `OC Merge Audit Correction`.
- **Roles/permissions:** `OC Identity Reviewer` reads summaries; `OC Privacy Officer` and `OC Auditor` access detail; no user edits submitted records.
- **API/surfaces:** `open_chart.api.v1.registration.read_merge_audit`; merge timeline, Script Report, and controlled PDF print format.

## Boundaries

Owns: immutable evidence of merge execution and correction. Consumes: approved merge plan and execution results. Emits: traceability and reconciliation findings. Does not own: duplicate detection or merge approval.

## Open questions

- Which cryptographic sealing approach is appropriate for a Frappe-native audit record?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
