# Order Hold And Resume — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Temporarily suspends and explicitly resumes order fulfillment with reasons, timing, authority, and preserved lifecycle evidence.
Topics: openchart-feature-catalog, cpoe, frappe, order-holds
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-025 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Timed hold review** — Require reassessment before a hold reaches its configured review deadline.

## Focus

This feature isolates reversible suspension of an order without rewriting or discontinuing it.

## Behavior

- Authorized users place an active order on hold with coded reason, effective time, expected review time, and optional conditions for resume.
- Fulfillment already underway is displayed and may require an exception acknowledgment.
- A held order is excluded from ordinary actionable queues but remains visible in held-order views.
- Resume requires a qualified user to review current safety, expiry, and privilege context.
- Expiration while held does not silently resume or renew the order.
- Every hold, extension, and resume is an immutable lifecycle event.

## Frappe realization

- **DocTypes:** submitted `OC Order Lifecycle Event` records Hold, Extend Hold, or Resume with reason, effective_at, review_at, and provenance.
- **Workflow:** Active → Held → Active or Discontinued/Stopped, with role-gated transitions.
- **Roles/permissions:** class policy defines hold and resume authority; fulfillment roles receive read-only status notifications.
- **Hooks/API/surface:** guarded hold/resume methods use row locks and revalidation; scheduler events create overdue-hold assignments; REST filters expose held orders.

## Boundaries

Owns: temporary suspension and resume evidence. Consumes: order state, expiry, and current safety context. Emits: queue eligibility changes. Does not own: fulfillment reversal.

## Open questions

- Should some hold reasons require the original orderer's resume approval?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Order Discontinuation With Reason](openchart-feature-catalog-ord-024-order-discontinuation-with-reason.md)
