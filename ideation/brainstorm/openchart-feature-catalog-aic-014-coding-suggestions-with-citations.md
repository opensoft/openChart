# Coding Suggestions With Citations — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Suggests documentation-supported codes with exact text citations for qualified human review and downstream handoff.
Topics: openchart-feature-catalog, clinical-ai, frappe, coding-suggestions
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-014 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Unsupported-code challenge** — Require reviewers to resolve any candidate whose cited text does not satisfy configured evidence rules.

## Focus

This feature isolates clinical-document coding assistance without owning billing or final code submission.

## Behavior

- A coder or clinician requests candidates from an accepted, permissioned documentation set.
- Each candidate shows code system, code, display, cited text spans, source version, rationale, and confidence.
- Reviewers accept, modify, reject, or flag each candidate and retain the original suggestion.
- A code without a valid citation cannot be accepted through this workflow.
- Amended source documentation marks dependent suggestions stale.
- Accepted candidates are exported as reviewed coding evidence, not posted to claims or billing autonomously.

## Frappe realization

- **DocTypes:** `OC AI Coding Suggestion` with source document/version Links, terminology, code, citation offsets, artifact, reviewer disposition, and export status.
- **Workflow:** Generated → Pending Review → Accepted/Modified/Rejected → Exported/Stale.
- **Roles/permissions:** `OC Clinical Coder` and authorized clinicians review; source record permissions are enforced on citations.
- **Hooks/API/surfaces:** source amendment hook stales suggestions; rq extraction job; Query Report and side-by-side citation review form; guarded export API emits reviewed evidence.

## Boundaries

Owns: source-cited code candidates and review. Consumes: accepted documentation and terminology. Emits: human-reviewed coding evidence. Does not own: claims, billing, reimbursement policy, or source-document alteration.

## Open questions

- Should modified code choices require a new citation or permit reviewer-authored rationale alone?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Documentation-Gap Nudges](openchart-feature-catalog-aic-015-documentation-gap-nudges.md)
