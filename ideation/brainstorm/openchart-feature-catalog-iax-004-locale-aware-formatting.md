# Locale-aware Formatting — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Renders dates, times, numbers, and currency by locale while preserving canonical stored values and unambiguous clinical interpretation.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, locale-formatting
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-004 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Ambiguity linting** — Flag numeric date or decimal presentations that could be misread in clinical contexts.

## Focus

This feature isolates localized display and input parsing from canonical clinical value storage.

## Behavior

- Users see dates, times, decimal separators, digit grouping, and currency according to their effective locale and timezone.
- Clinical dates with ambiguity risk include an unambiguous month name or ISO companion according to surface policy.
- Input controls parse only documented locale formats and preview the canonical interpreted value before acceptance when ambiguity exists.
- Currency always displays its code or symbol under site policy and never changes value during localization.
- Exports and APIs use stable machine formats independent of the viewer's locale.
- Changing locale immediately reformats presentation but does not mutate stored values or accepted records.
- Invalid or mixed-locale input returns an example of the expected format without silently guessing.

## Frappe realization

- **Configuration:** `OC Locale Format Policy` stores locale, date/time patterns, number rules, currency display, timezone behavior, and ambiguity safeguards.
- **Client and server hooks:** Frappe formatters and controls are wrapped through app hooks; `validate` normalizes accepted inputs into Date, Datetime, Currency, or Decimal fields.
- **Preferences:** Effective locale and timezone are delivered in bootinfo from Frappe User and user defaults, with site policy supplying fallback values.
- **Surfaces:** Desk lists, Query Reports, portal pages, Jinja Print Formats, and REST serializers use shared format-policy helpers.

## Boundaries

Owns: human display formats and safe locale parsing. Consumes: canonical values, user locale, timezone, and site currency. Emits: localized presentations and structured validation errors. Does not own: exchange payload standards or financial conversion.

## Open questions

- Which clinical values should always show a canonical companion representation regardless of locale?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Right-to-left Layout Support](openchart-feature-catalog-iax-003-rtl-layout-support.md)
