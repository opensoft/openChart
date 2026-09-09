# Standing Order Expiry Control — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enforces effective dates, maximum uses, renewal review, and expiry for standing orders and protocols.
Topics: openchart-feature-catalog, cpoe, frappe, standing-order-expiry
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-019 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Utilization-based review** — Prompt early review when use patterns exceed governed expectations.

## Focus

This feature isolates temporal and utilization limits on reusable ordering authority.

## Behavior

- Every standing order or protocol has effective_from, expires_at, use limits, owner, and renewal policy.
- Activators see remaining validity and uses before applying it.
- Expired, exhausted, withdrawn, or not-yet-effective artifacts cannot create orders.
- Owners receive advance renewal tasks and may author a successor for independent approval.
- Expiry does not discontinue already accepted patient orders unless their own duration says so.
- Manual exceptions require explicit authority, rationale, and an auditable successor action.

## Frappe realization

- **DocTypes:** expiry and utilization fields live on `OC Standing Protocol`; `OC Protocol Activation` provides immutable use counts.
- **Workflow:** Active → Expiring → Expired, with Renewal Draft creating a successor rather than editing active authority.
- **Roles/permissions:** activators read validity; owners initiate renewal; publishers approve successors.
- **Scheduler/API/surface:** daily scheduler events mark due states and assignments; activation API uses row locking to enforce use limits; REST filters expose expiring artifacts.

## Boundaries

Owns: reusable-authority validity and use enforcement. Consumes: activation history and governance dates. Emits: expiry states and renewal tasks. Does not own: individual order auto-stop.

## Open questions

- Should maximum-use counters apply globally, per location, or per patient?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Order Duration And Auto-Stop](openchart-feature-catalog-ord-022-order-duration-and-auto-stop.md)
