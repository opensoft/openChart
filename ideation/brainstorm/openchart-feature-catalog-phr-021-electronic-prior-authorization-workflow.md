# Electronic Prior Authorization Workflow — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Initiates, answers, submits, and tracks an electronic prior-authorization case from prescribing context through payer determination.
Topics: openchart-feature-catalog, eprescribing, frappe, electronic-prior-authorization
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-021 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Renewal authorization calendar** — Approved cases could produce review tasks before authorization expiration.

## Focus

This feature isolates the stateful ePA exchange and accountable responses. It keeps payer questions, submitted answers, attachments, and determinations tied to one prescription context.

## Behavior

- A user initiates ePA from a coverage restriction or manually when payer policy requires it.
- The service verifies patient, coverage, medication, prescriber, and request identifiers before creating the case.
- Payer questions route to assigned staff with required fields, due dates, and source wording preserved.
- Clinical answers and attachments require authorized review before submission and become immutable sent versions.
- The case tracks initiated, questions received, in preparation, submitted, pending, approved, denied, withdrawn, expired, and error states.
- Approval never transmits or changes a prescription automatically; the prescriber decides any next clinical action.

## Frappe realization

- **DocTypes:** `OC Prior Authorization` with child questions, answers, attachments, events, and determination fields links patient, coverage, and `OC Prescription`.
- **Workflow:** Initiated → Evidence Needed → Clinical Review → Ready to Submit → Submitted → Approved/Denied/Withdrawn/Expired with role-specific actions.
- **Roles/API:** `OC Prior Authorization Specialist` prepares; `OC Prescriber` attests clinical answers; guarded methods handle payer exchange and callbacks.
- **Surfaces/hooks:** Kanban/worklist, due-date Assignment Rules, Notifications, background polling, and realtime updates expose case progress.

## Boundaries

Owns: ePA case, submitted answers, evidence package, and determination history. Consumes: payer questions, coverage, chart evidence, and prescriber attestations. Emits: ePA messages and operational tasks. Does not own: payer decision or automatic prescription modification.

## Open questions

- Which answer types require prescriber attestation versus delegated submission?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Prior-Authorization Evidence Assembly](openchart-feature-catalog-phr-022-prior-authorization-evidence-assembly.md)
