# Delegated Order Attribution — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Separates the person entering an order from the accountable ordering clinician and verifies permitted delegation relationships.
Topics: openchart-feature-catalog, cpoe, frappe, order-delegation
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-034 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Delegation coverage calendar** — Make active supervisor-delegate relationships visible at order-entry time.

## Focus

This feature isolates provenance and authority when order entry is performed on another clinician's behalf.

## Behavior

- The entry actor selects an accountable clinician only from currently valid delegation relationships.
- The composer displays entered_by, ordered_by, relationship scope, and any cosign requirement before signature.
- Delegation scope is checked against order class, facility, care setting, and effective dates.
- The accountable clinician remains visible on all downstream order and result views.
- Invalid or expired delegation blocks submission rather than substituting another clinician.
- Every action preserves both identities and the delegation record version.

## Frappe realization

- **DocTypes:** `OC Ordering Delegation` with principal, delegate, order classes, facility, effective dates, status, and provenance; orders store both actors.
- **Workflow:** Proposed → Accepted → Active → Expired/Revoked.
- **Roles/permissions:** principals and credentialing roles govern relationships; delegates cannot broaden scope.
- **Hooks/API/surface:** server-side `validate` resolves active delegation; `on_submit` creates cosign if required; filtered APIs list only eligible principals.

## Boundaries

Owns: delegated-entry authority and attribution. Consumes: identities, scope, and effective dates. Emits: dual-identity order provenance. Does not own: provider credentialing or verbal-order read-back.

## Open questions

- Who may create delegation relationships in each care setting?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Ordering Role Cosign Requirements](openchart-feature-catalog-ord-030-ordering-role-cosign-requirements.md)
