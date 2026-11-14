# Standing Protocol Activation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets authorized staff activate predefined orders under a published protocol when documented eligibility criteria are met.
Topics: openchart-feature-catalog, cpoe, frappe, standing-protocols
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-018 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Protocol eligibility preview** — Show unmet criteria before staff begins activation.

## Focus

This feature isolates human-authorized use of standing protocols without autonomous order placement.

## Behavior

- Authorized staff select an active protocol and document each eligibility and exclusion criterion.
- The system expands proposed orders with protocol version, accountable owner, and evidence provenance.
- Staff review and explicitly activate eligible orders; no rule or AI service submits them automatically.
- Failed criteria block activation and show the governing clause.
- A clinician cosign is requested when protocol or staff role requires it.
- Protocol withdrawal prevents new activations but does not erase prior order provenance.

## Frappe realization

- **DocTypes:** `OC Standing Protocol` with owner, criteria, exclusions, order templates, effective dates, version, and provenance; `OC Protocol Activation` records patient-scoped answers and actor.
- **Workflow:** protocol Draft → Review → Published → Retired/Withdrawn; activation Draft → Eligible → Activated or Ineligible.
- **Roles/permissions:** `OC Protocol Activator` uses published protocols; `OC Clinical Reviewer` and `OC Protocol Publisher` govern definitions.
- **Hooks/API/surface:** whitelisted preview and activate methods evaluate criteria server-side; resulting orders submit through v1 and fire `doc_events.on_submit` rules.

## Boundaries

Owns: protocol eligibility evidence and activation provenance. Consumes: published protocol, patient facts, and staff privileges. Emits: explicitly activated orders. Does not own: autonomous surveillance or fulfillment.

## Open questions

- Which patient facts may be accepted automatically versus requiring staff confirmation?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Standing Order Expiry Control](openchart-feature-catalog-ord-019-standing-order-expiry-control.md)
