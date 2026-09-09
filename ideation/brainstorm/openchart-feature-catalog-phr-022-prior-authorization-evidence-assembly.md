# Prior-Authorization Evidence Assembly — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Assembles a reviewable prior-authorization evidence packet from permissioned chart facts with source citations and minimum-necessary controls.
Topics: openchart-feature-catalog, eprescribing, frappe, prior-auth-evidence
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-022 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Payer-criteria checklist templates** — Sites could configure evidence prompts by medication and plan without auto-asserting eligibility.

## Focus

This feature isolates evidence selection and packet composition before ePA submission. Suggested evidence remains a draft until an authorized human confirms relevance, accuracy, consent, and disclosure scope.

## Behavior

- Staff start from payer questions or criteria and search permissioned diagnoses, notes, therapies, results, and medication trials.
- Each selected fact retains source document, author, accepted version, date, and relevant excerpt or structured value.
- Generated summaries are clearly labeled drafts with citations and cannot introduce unsupported facts.
- Sensitive records require purpose and consent checks before inclusion.
- A reviewer can remove, annotate, or replace evidence and sees exactly what will leave the chart.
- Submission freezes a versioned packet digest and disclosure audit linked to the ePA case.

## Frappe realization

- **DocTypes:** `OC Prior Authorization Evidence Packet` and child `OC Evidence Citation` store Dynamic Links, source versions, excerpts, inclusion reasons, and disclosure basis.
- **Workflow:** Draft Assembly → Privacy/Clinical Review → Approved for Submission → Submitted; successors preserve corrections.
- **Roles/API:** PA staff assemble, prescribers attest clinical claims, privacy roles review sensitive disclosures, and guarded APIs resolve citations.
- **Surfaces:** Evidence picker, side-by-side packet preview, Jinja PDF rendition, and disclosure report support review.

## Boundaries

Owns: selected evidence packet, citations, review, and disclosure record. Consumes: accepted chart records, payer criteria, consent, and ePA case. Emits: reviewed attachment or structured answers. Does not own: source chart facts, payer criteria truth, or autonomous clinical assertions.

## Open questions

- Which sensitive evidence categories always require separate privacy review?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Electronic Prior Authorization Workflow](openchart-feature-catalog-phr-021-electronic-prior-authorization-workflow.md)
