# Contextual Tooltip Documentation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Links concise accessible field help to versioned documentation while keeping essential instructions visible outside hover-only tooltips.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, contextual-help
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-029 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Help-gap report** — Identify high-use controls with no maintained explanation or broken documentation target.

## Focus

This feature isolates layered contextual help: brief control guidance plus a stable handoff to fuller documentation.

## Behavior

- Authors attach a concise help entry and optional documentation target to stable fields, controls, statuses, or actions.
- Essential instructions and errors remain visible in the interface rather than existing only in a tooltip.
- Help opens by keyboard, focus, touch, and pointer; it stays available long enough to read and can be dismissed without losing focus.
- Screen readers associate concise help with the control and expose the full documentation link with an informative label.
- Entries are localized, versioned, assigned an owner, and marked stale when their target component changes.
- Links resolve through an approved documentation registry and report missing or unauthorized targets without opening arbitrary URLs.
- Help content never includes patient-specific values or substitutes for clinical policy at the point of care.

## Frappe realization

- **DocTypes:** `OC Contextual Help Entry` stores target key, locale, concise text, documentation Link, owner, release, review date, and state.
- **Translation system:** Frappe translation keys cover concise help; longer approved content may render from versioned documentation records.
- **Surfaces:** Shared Frappe form controls, dialogs, lists, and portal components use one Website Theme-compatible popover with ARIA relationships.
- **Automation:** A release hook checks target keys and links; a Query Report assigns stale and missing help entries to UX Documentation Maintainers.

## Boundaries

Owns: contextual help mapping, concise content, accessible disclosure, and documentation linkage. Consumes: stable UI targets, locale, and approved docs. Emits: help popovers, links, and maintenance findings. Does not own: source documentation, clinical policy, or required instructions.

## Open questions

- Should longer help content be stored in Frappe records or generated from repository-managed documentation at release time?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Role-based Guided Tours](openchart-feature-catalog-iax-028-role-based-guided-tours.md)
