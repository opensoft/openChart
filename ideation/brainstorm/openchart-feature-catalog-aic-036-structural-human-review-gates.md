# Structural Human-Review Gates — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enforces server-side state and permission barriers so consequential AI outputs cannot bypass qualified human review.
Topics: openchart-feature-catalog, clinical-ai, frappe, human-review-gates
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-036 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Gate conformance test suite** — Prove every consequential destination rejects direct AI-service submission and forged client approval.

## Focus

This feature isolates the hard architectural doctrine that AI may draft or suggest but cannot take consequential clinical action.

## Behavior

- Each consequential capability declares destination type, qualified reviewer roles, required attestations, freshness, and separation-of-duty rules.
- AI outputs enter nonclinical draft states with no submit, send, sign, merge, reconcile, or order authority.
- Promotion requires an authenticated human action, current permission, artifact review, and destination-specific server validation.
- Client-side flags, service-account identity, background jobs, and provider callbacks cannot satisfy a human gate.
- Rejection, expiry, revocation, and stale source state prevent promotion.
- Every attempt and decision records actor, inputs, policy version, and outcome.

## Frappe realization

- **DocTypes:** `OC AI Human Review Policy` defines destination, roles, attestations, freshness, and gate version; `OC AI Review Decision` records immutable outcomes.
- **Roles/permissions:** AI service role has zero submit permission on clinical DocTypes; custom DocPerms separate draft review from destination authority.
- **Hooks/API:** destination `validate/on_submit` rejects missing human decision and mismatched artifact digest; guarded v1 promotion methods require session user, never API service token alone.
- **Tests/surfaces:** fixtures register policies; Desk forms show unmet gates; Script Report surfaces bypass attempts.

## Boundaries

Owns: mandatory human promotion controls and evidence. Consumes: artifact, destination, permissions, and policy. Emits: allowed or denied promotion decision. Does not own: the human's clinical judgment or destination workflow semantics.

## Open questions

- Which low-consequence administrative outputs can use single-click confirmation rather than formal attestations?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Human-Approved Order Suggestions](openchart-feature-catalog-aic-013-human-approved-order-suggestions.md)
