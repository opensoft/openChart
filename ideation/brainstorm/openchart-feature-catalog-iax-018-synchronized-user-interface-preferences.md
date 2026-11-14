# Synchronized User Interface Preferences — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Resolves, validates, and synchronizes per-user interface preferences across Desk and portal sessions with clear site-default precedence.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, user-preferences
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-018 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Preference portability** — Export and import non-sensitive presentation settings between authorized openChart sites.

## Focus

This feature isolates the preference spine used by language, accessibility, appearance, density, and navigation capabilities.

## Behavior

- Authenticated users edit supported preferences from one accessible panel with descriptions, previews, and reset controls.
- Effective values resolve from mandatory accessibility behavior, user choice, role or surface default, site default, then safe product fallback.
- Changes save optimistically only after server validation and synchronize to new sessions and supported devices.
- Conflicting simultaneous edits produce a clear latest-version choice rather than silently overwriting another session.
- Device-local choices are explicitly labeled and never mistaken for synchronized account preferences.
- Administrators may set defaults and allowed values but cannot weaken mandatory accessibility contracts.
- Preference history excludes patient data and records actor, source session, changed keys, and timestamp.

## Frappe realization

- **DocTypes:** `OC UX Preference Policy` defines keys, types, allowed values, scope, defaults, and mandatory constraints; values use Frappe User preferences where supported.
- **Bootinfo:** A boot hook resolves effective preferences and version into bootinfo; portal context uses the same resolver to prevent Desk/portal drift.
- **API:** Guarded `open_chart.api.v1.ux.preferences` methods parse a typed allowlist, use version checks, and publish realtime updates to other sessions.
- **Surfaces and roles:** A Desk/portal preference panel serves all users; UX Administrator manages policies through permlevel-protected fields and a change report.

## Boundaries

Owns: preference definitions, precedence, synchronization, and non-PHI change history. Consumes: user, role, site, device, and browser signals. Emits: typed effective preference sets in bootinfo. Does not own: clinical defaults, access control, or device security.

## Open questions

- Which preferences should remain device-local because synchronizing them would create poor behavior on dissimilar screens?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Dark Mode](openchart-feature-catalog-iax-017-dark-mode.md)
