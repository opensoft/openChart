# Human-Approved Order Suggestions — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Drafts contextual order candidates with rationale and evidence while structurally requiring a qualified clinician to select, edit, and sign.
Topics: openchart-feature-catalog, clinical-ai, frappe, order-suggestions
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-013 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Suggestion comparison** — Show alternatives, contraindication checks, and source evidence side by side before selection.

## Focus

This feature isolates generative order suggestion drafting; it never grants a model ordering authority.

## Behavior

- A qualified clinician requests suggestions from an encounter, transcript, or accepted note context.
- Each candidate includes order class, parameters, rationale, cited inputs, confidence, and model evidence.
- Candidates remain non-orders until the clinician selects and edits one into the ordinary order composer.
- Composer validation, privileges, interaction checks, and signature run exactly as for manually entered orders.
- Low-confidence, unsupported, restricted, or conflicting candidates are withheld or routed to human-only review.
- Rejection and edits are recorded for evaluation, not silent retraining.

## Frappe realization

- **DocTypes:** `OC AI Order Suggestion` stores artifact, encounter, candidate schema, citations, disposition, and resulting draft-order Link.
- **Workflow:** Generated → In Review → Accepted To Draft/Rejected/Expired; no Submitted clinical state exists.
- **Roles/permissions:** only users already permitted for the order class may convert a candidate; model service role has read-limited context and no order create permission.
- **Hooks/API/surfaces:** whitelisted suggestion and convert methods; server-side conversion copies into an unsigned draft; order `validate/on_submit` reruns all safeguards.

## Boundaries

Owns: contextual candidate generation and disposition. Consumes: approved patient context and order schemas. Emits: optional unsigned draft input. Does not own: ordering authority, signature, fulfillment, diagnosis, or autonomous action.

## Open questions

- Which order classes should be categorically excluded from generative suggestions?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Structural Human-Review Gates](openchart-feature-catalog-aic-036-structural-human-review-gates.md)
