# Non-Interruptive CDS Advisory Feed — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents relevant low-urgency guidance in a persistent advisory feed without blocking order composition or signature.
Topics: openchart-feature-catalog, cpoe, frappe, cds-advisories
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-053 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Advisory pinning** — Let clinicians retain selected guidance through encounter completion.

## Focus

This feature isolates visible but non-interruptive decision support.

## Behavior

- Advisories appear beside the order basket with title, rationale, evidence, owner, version, and relevance trigger.
- Clinicians may expand, pin, dismiss, or act by creating a reviewable draft.
- Advisories never prevent signing and never execute their suggested action.
- Dismissed items remain accessible for the encounter and may record optional feedback.
- Material context changes reevaluate the feed and label stale advisories.
- Critical or blocking rules cannot be downgraded into this feed by user preference.

## Frappe realization

- **DocTypes:** `OC CDS Evaluation` outcome Advisory and optional `OC Advisory Interaction` with action, actor, time, and evaluation link.
- **Roles/permissions:** patient-context users see scoped advisories; preferences affect presentation only, not rule severity.
- **Hooks/API/surface:** whitelisted preview endpoint returns active advisories; client component refreshes on basket change; accepted actions create ordinary drafts.
- **Reports:** aggregate advisory interactions use minimum necessary data and governance-approved retention.

## Boundaries

Owns: advisory presentation and interactions. Consumes: non-interruptive evaluations. Emits: visibility, feedback, or draft initiation. Does not own: rule severity or autonomous action.

## Open questions

- Which advisory interactions are clinically useful enough to retain?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Order-Time Alert Orchestration](openchart-feature-catalog-ord-048-order-time-alert-orchestration.md)
