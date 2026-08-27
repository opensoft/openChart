# Keyboard-only Navigation Completeness — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Ensures every supported Desk and portal workflow can be completed by keyboard with predictable order, shortcuts, and escape paths.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, keyboard-navigation
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-009 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Workflow keyboard certification** — Track end-to-end completion evidence for high-frequency clinical tasks by release.

## Focus

This feature isolates complete keyboard operability rather than isolated key handlers on individual controls.

## Behavior

- Users can reach, operate, and leave every interactive control without a pointer or touch input.
- Tab order follows reading and task order; composite controls use documented arrow-key patterns rather than excessive tab stops.
- Escape closes transient UI without discarding accepted work, and no route creates a keyboard trap.
- Shortcuts are discoverable, remappable where practical, and disabled in editable text contexts when they would capture typing.
- Data grids expose row, column, selection, edit, and paging operations with stable focus after refresh.
- Automated route tests detect unreachable controls, while manual scripts verify complete synthetic clinical workflows.
- A failed critical workflow is marked unsupported for release until fixed or given an equivalent accessible path.

## Frappe realization

- **Configuration:** `OC Keyboard Interaction Contract` stores route, workflow, expected focus sequence, shortcut map, and release status.
- **Client behavior:** Shared Frappe Desk and portal utilities implement roving tabindex, grid keys, dialog escape, and focus restoration without changing server authorization.
- **Preferences:** User-remapped non-reserved shortcuts load through bootinfo from Frappe user preferences and sync across sessions.
- **Quality surfaces:** Accessibility Tester and UX Maintainer roles review Script Reports generated from synthetic browser runs and manual evidence attachments.

## Boundaries

Owns: keyboard interaction contracts and workflow completion evidence. Consumes: routes, component semantics, and user shortcut preferences. Emits: consistent keyboard behavior and conformance results. Does not own: operating-system assistive shortcuts or voice control.

## Open questions

- Which clinical workflows must pass manual keyboard certification before every release?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Visible Focus And Skip Navigation](openchart-feature-catalog-iax-010-visible-focus-and-skip-navigation.md)
