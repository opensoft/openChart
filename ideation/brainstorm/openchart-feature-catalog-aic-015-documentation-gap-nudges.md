# Documentation-Gap Nudges — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Surfaces explainable missing-documentation prompts before signature without inventing content or blocking care by default.
Topics: openchart-feature-catalog, clinical-ai, frappe, documentation-gaps
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-015 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Nudge burden dashboard** — Compare useful corrections, dismissals, and repeated low-value prompts by note type.

## Focus

This feature isolates pre-signature prompts for incomplete, inconsistent, or unsupported documentation.

## Behavior

- Before signature, a clinician may run or automatically receive an approved gap check against the current draft.
- Each nudge identifies the exact section, governing rule or model evidence, and a suggested question rather than fabricated prose.
- The clinician can address, dismiss with optional reason, or defer a nonmandatory nudge.
- Only explicitly governed hard requirements can block signature; model confidence alone never creates a blocker.
- Prompts are recalculated after material edits and prior outcomes remain auditable.
- Service failure leaves manual signing rules intact and reports the unavailable check.

## Frappe realization

- **DocTypes:** `OC Documentation Gap Evaluation` stores note version, finding type, evidence, severity, disposition, model/rule versions, and resolved field.
- **Roles/permissions:** note authors resolve findings; `OC Documentation Governance Reviewer` authors blocking policy separately.
- **Hooks/API/surfaces:** note `validate` calls deterministic mandatory checks and schedules optional AI review; client script shows anchored nudges; Script Report tracks dispositions.
- **Server scripts:** approved Server Scripts may express local deterministic requirements but cannot call unrestricted external inference endpoints.

## Boundaries

Owns: gap findings and clinician resolution evidence. Consumes: current draft and approved policies. Emits: prompts or governed blockers. Does not own: clinical content, coding authority, or automatic note completion.

## Open questions

- Which gaps are suitable for noninterruptive prompts versus policy-backed signature blockers?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Coding Suggestions With Citations](openchart-feature-catalog-aic-014-coding-suggestions-with-citations.md)
