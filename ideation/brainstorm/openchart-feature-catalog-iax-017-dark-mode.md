# Dark Mode — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides a contrast-tested dark presentation for Desk and portal surfaces without obscuring clinical status or document fidelity.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, dark-mode
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-017 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Scheduled appearance** — Follow operating-system light or dark preference while allowing an immediate user override.

## Focus

This feature isolates dark presentation tokens and asset adaptation from general branding and high-contrast mode.

## Behavior

- Users choose Light, Dark, or System mode and preview the change without reloading or losing form state.
- Text, controls, focus rings, disabled states, alerts, graphs, and status indicators meet the same semantic and contrast contracts in dark mode.
- Images, scanned documents, diagnostic media, and signatures retain faithful source appearance rather than being indiscriminately inverted.
- Rich-text content uses constrained theme-aware colors and warns authors about fixed colors that fail contrast.
- Print and exported artifacts use their governed output theme unless explicitly designed for dark output.
- The preference applies before first meaningful paint to avoid a bright flash during session start.
- Unknown custom surfaces fall back to the supported light theme rather than presenting unreadable mixed tokens.

## Frappe realization

- **Themes:** Desk themes and Website Theme share semantic light/dark token maps, chart palettes, focus styles, and controlled rich-text rules.
- **Preferences:** Frappe user preferences store appearance mode; bootinfo combines it with the browser system signal before Desk initialization.
- **Configuration:** `OC Theme Conformance Record` tracks route, theme, release, automated contrast result, manual review, and exceptions.
- **Surfaces:** Client scripts switch root theme attributes; Print Formats and file viewers explicitly opt into faithful light presentation.

## Boundaries

Owns: dark interactive presentation and theme conformance. Consumes: user/system preference, semantic tokens, and route support. Emits: readable dark surfaces and defects. Does not own: source media transformation or high-contrast accessibility mode.

## Open questions

- Which visualization palettes remain distinguishable across dark mode and common color-vision variations?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Synchronized User Interface Preferences](openchart-feature-catalog-iax-018-synchronized-user-interface-preferences.md)
