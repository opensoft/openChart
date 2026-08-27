# Personal Order Favorites — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets clinicians save personal shortcuts to active orderables and preferred defaults without bypassing current policy checks.
Topics: openchart-feature-catalog, cpoe, frappe, order-favorites
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-011 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Specialty starter pack** — Copy a governed favorite collection into a new user's personal list for later editing.

## Focus

This feature isolates clinician-owned order-entry shortcuts.

## Behavior

- Clinicians save an orderable with permitted default fields and a personal label.
- Invoking a favorite opens a fresh draft and reruns current catalog, privilege, formulary, and CDS checks.
- Patient-specific facts, indications, and prior signatures are never stored in a favorite.
- Retired or materially changed orderables mark favorites unavailable with an explanation.
- Users reorder, rename, and delete only their own favorites.
- A favorite cannot submit an order or accept a suggestion without explicit review and signature.

## Frappe realization

- **DocTypes:** `OC Order Favorite` with owner, orderable, order_class, label, defaults JSON, and last_validated_at.
- **Roles/permissions:** owner-only create/read/write; administrators may disable unsafe defaults but not inspect unrelated personal usage without audit authority.
- **Hooks/API/surface:** `validate` allowlists defaultable fields; a whitelisted method resolves each favorite against current policy before populating Quick Entry.
- **Reports:** a personal Desk shortcut lists active, changed, and unavailable favorites.

## Boundaries

Owns: personal shortcut configuration. Consumes: current orderable definitions and permissions. Emits: prefilled drafts. Does not own: organization order sets or accepted orders.

## Open questions

- Which defaults are safe to persist for medication favorites?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Order Search With Synonyms](openchart-feature-catalog-ord-010-order-search-with-synonyms.md)
