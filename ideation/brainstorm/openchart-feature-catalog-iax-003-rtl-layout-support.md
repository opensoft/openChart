# Right-to-left Layout Support — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Mirrors navigation, reading order, controls, and mixed-direction content for right-to-left locales without altering clinical data meaning.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, rtl-layout
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-003 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Bidirectional content test corpus** — Exercise mixed Arabic or Hebrew text with identifiers, doses, and Latin abbreviations using synthetic fixtures.

## Focus

This feature isolates direction-aware presentation across Desk, portal, reports, and print while keeping stored values direction-neutral.

## Behavior

- Selecting an RTL locale sets page direction before first meaningful render to avoid a left-to-right flash.
- Navigation order, drawers, breadcrumb direction, icons with directional meaning, and form alignment mirror consistently.
- Identifiers, numeric doses, code values, email addresses, and URLs retain isolated left-to-right display where required.
- Screen-reader reading order follows semantic DOM order rather than visual CSS reversal.
- Tables preserve logical column labels, frozen columns, keyboard movement, and horizontal scroll behavior in RTL mode.
- Unsupported custom components show a detectable conformance warning in test mode rather than silently misaligning.
- PDFs and print formats use locale-capable fonts and retain correct text shaping.

## Frappe realization

- **Surfaces:** Website Theme and Desk theme styles use logical CSS properties and Frappe's locale direction signal across portal pages, workspaces, dialogs, and print formats.
- **Client behavior:** A boot hook places `text_direction` and locale in bootinfo; client utilities apply `dir`, isolate mixed-direction fields, and avoid DOM-order reversal.
- **Configuration:** `OC Locale Presentation Policy` records RTL status, approved fonts, icon overrides, and print support by locale.
- **Quality hooks:** Synthetic Playwright fixtures exercise keyboard, screen-reader structure, grids, and PDF rendering for each active RTL locale.

## Boundaries

Owns: direction-aware layout and rendering rules. Consumes: active locale, field semantics, and approved fonts. Emits: RTL-safe Desk, portal, and print views. Does not own: translation quality or source data normalization.

## Open questions

- Which third-party Frappe controls require wrappers before an RTL locale can be declared supported?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Locale-aware Formatting](openchart-feature-catalog-iax-004-locale-aware-formatting.md)
