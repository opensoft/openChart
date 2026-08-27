# Diagnosis-Driven Order Suggestions — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents governed order candidates associated with encounter diagnoses while requiring clinician selection and approval.
Topics: openchart-feature-catalog, cpoe, frappe, diagnosis-suggestions
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-012 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Rationale comparison** — Show why multiple eligible suggestion bundles differ for the same diagnosis.

## Focus

This feature isolates diagnosis-contextual order suggestions that never become autonomous actions.

## Behavior

- When a clinician selects an encounter diagnosis, the composer displays eligible suggestions with rationale, evidence, rule version, and owner.
- Suggestions are ordered by governed priority, not hidden predictive ranking.
- The clinician may accept, edit, dismiss, or ignore each candidate.
- Acceptance creates an ordinary draft order that must pass all checks and be signed.
- Dismissal reasons are optional unless a rule explicitly requires acknowledgment.
- Missing or uncertain diagnosis coding produces no inferred diagnosis and no automatic orders.

## Frappe realization

- **DocTypes:** `OC Diagnosis Order Suggestion Rule` links diagnosis concepts to order templates and mandatory provenance fields; `OC CDS Evaluation` records de-identified outcome metadata.
- **Workflow:** rule Draft → Testing → Approved → Active → Retired; suggestions themselves are ephemeral until accepted.
- **Roles/permissions:** `OC CDS Author` drafts, `OC CDS Reviewer` approves, and ordering clinicians consume active rules.
- **Hooks/API/surface:** a whitelisted preview method evaluates encounter context; accepted items use v1 order APIs and `on_submit` re-evaluation.

## Boundaries

Owns: diagnosis-to-order suggestion mapping. Consumes: clinician-selected diagnoses and active rules. Emits: reviewable candidates and evaluation evidence. Does not own: diagnosis inference or order submission.

## Open questions

- Which suggestion exposures and dismissals should be retained for analytics?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [CDS Rule Registry](openchart-feature-catalog-ord-045-cds-rule-registry.md)
