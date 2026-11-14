# Universal Search Command Palette — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Gives authorized users a keyboard-first palette to find records, routes, actions, and help without bypassing Frappe permissions.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, command-palette
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-020 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Task aliases by role** — Let administrators publish localized synonyms for common destinations without exposing hidden commands.

## Focus

This feature isolates a permission-safe jump-to-anything interaction that unifies discovery without replacing domain search semantics.

## Behavior

- A documented keyboard shortcut opens the palette from any supported Desk route and returns focus when closed.
- Users search localized navigation labels, permitted record titles, saved reports, recent destinations, and allowed commands.
- Results are grouped by type, explain their destination, and support arrow-key and screen-reader navigation.
- Every query and command is permission-filtered server-side; hidden result counts and sensitive snippets are not disclosed.
- Consequential actions open their ordinary reviewed form or confirmation flow rather than executing immediately from search text.
- Empty, slow, offline, and error states explain what can still be searched and how to recover.
- Query history is private to the user, bounded, clearable, and excludes protected record content by default.

## Frappe realization

- **Search:** The palette composes Frappe global search, Desk workspace Shortcuts, whitelisted action providers, and permission-aware recent-item projections.
- **Configuration:** `OC Command Palette Provider` stores provider key, localized label, roles, route, shortcut, priority, and active state.
- **Client and bootinfo:** A Desk client hook registers the palette and loads only authorized providers and shortcut settings from bootinfo.
- **API:** `open_chart.api.v1.ux.palette.search` rechecks DocType, row, and command permissions and returns minimum-necessary result labels.

## Boundaries

Owns: unified discovery interaction, provider registration, and permission-safe result composition. Consumes: Frappe search, workspace routes, user permissions, and localized labels. Emits: navigations and ordinary action handoffs. Does not own: source records or autonomous command execution.

## Open questions

- Which record classes should be excluded from palette history even when the user can access them?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Recent And Pinned Navigation](openchart-feature-catalog-iax-021-recent-and-pinned-navigation.md)
