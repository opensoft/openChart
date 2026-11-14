# Auditor Evidence Package Assembly — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Assembles purpose-bound audit packages containing specifications, calculations, provenance, approvals, submissions, receipts, and sampled patient evidence.
Topics: openchart-feature-catalog, quality-reporting, frappe, audit-evidence
Repository context: openChart — Frappe v15 native EMR; catalog entry QME-034 (Quality Measures Regulatory Reporting)
Captured: 2026-08-24

## Possible feats

- **Auditor request matrix** — Map each request item to evidence, owner, disclosure authority, status, and delivery receipt.

## Focus

Reproducible evidence packaging with minimum-necessary disclosure, integrity manifests, and review before release.

## Behavior

- An audit coordinator records requester, authority, purpose, period, scope, requested items, due date, and secure delivery method.
- Package candidates include measure releases, test evidence, period configuration, run traces, mappings, waivers, approvals, submissions, and receipts.
- Patient samples require explicit selection criteria, patient-level authorization, and redaction review.
- The assembler identifies missing, stale, restricted, or integrity-failed evidence before approval.
- Every included file receives a manifest entry with source, version, hash, disclosure class, and generated timestamp.
- Reviewer approval locks package contents; changes create a successor package.
- Delivery and auditor follow-up are recorded without granting auditors unrestricted application access.

## Frappe realization

- **DocTypes:** Add `OC Audit Evidence Request`, `OC Audit Evidence Package`, and child request, manifest, redaction, approval, and delivery rows.
- **Workflow:** Use intake, assembling, exception, privacy-review, approval, released, follow-up, closed, and superseded states.
- **Permissions and jobs:** Apply purpose-scoped `OC Audit Coordinator`, `OC Privacy Officer`, and `OC Quality Approver` roles; assemble and hash in rq.
- **Surfaces:** Provide request Kanban, evidence checklist, redaction review, Jinja cover sheet, and permissioned encrypted download.

## Boundaries

Owns: audit request tracking, evidence assembly, redaction, manifest, and delivery proof. Consumes: reporting artifacts, source permissions, authority, and retention policy. Emits: reviewed evidence packages and gaps. Does not own: auditor authority, legal interpretation, or unrestricted chart disclosure.

## Open questions

- Which patient-level evidence packages require privacy-officer approval regardless of requester authority?

## Relationships

[Synthesis: Quality Measures And Regulatory Reporting](openchart-feature-catalog-synthesis-qme.md)
