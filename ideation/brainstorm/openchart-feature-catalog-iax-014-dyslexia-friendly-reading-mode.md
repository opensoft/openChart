# Dyslexia-friendly Reading Mode — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Offers an optional reading presentation with adjustable typography and spacing while preserving exact clinical wording and document provenance.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, dyslexia-reading-mode
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-014 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Reading ruler option** — Provide a movable line guide on long patient instructions without changing document content.

## Focus

This feature isolates an opt-in reading presentation; it does not claim one typeface benefits every person with dyslexia.

## Behavior

- Users may enable a reading mode that changes approved font, character spacing, line spacing, line length, and paragraph separation.
- The mode is optional, reversible, and labeled as a presentation preference rather than a diagnosis-specific treatment.
- Clinical wording, punctuation, dosage values, codes, and signed document content remain unchanged.
- Users can choose among approved settings instead of receiving a forced universal dyslexia font.
- Long content preserves headings, lists, tables, links, and screen-reader semantics under the alternate typography.
- Missing glyph coverage falls back to a locale-approved font without replacing characters.
- The mode applies to readable views and patient instructions but not to faithful source-document images.

## Frappe realization

- **Preferences:** Frappe user preferences store the reading profile; bootinfo applies it before first content paint for authenticated Desk and portal users.
- **Themes:** Website Theme and Desk theme variants expose approved font stacks and relative spacing tokens with locale-specific glyph coverage.
- **Configuration:** `OC Reading Presentation Profile` stores font stack, spacing, line width, supported scripts, and active status.
- **Surfaces:** Client scripts apply profile attributes to reading containers while Jinja templates retain source text and provenance markers.

## Boundaries

Owns: optional reading typography and spacing. Consumes: locale, user preference, approved font profiles, and source content. Emits: alternate faithful presentation. Does not own: content simplification, literacy assessment, diagnosis, or document transformation.

## Open questions

- Should patients be able to tune individual spacing controls or choose only tested profiles?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Scalable Type And High-contrast Mode](openchart-feature-catalog-iax-012-scalable-type-and-high-contrast-mode.md)
