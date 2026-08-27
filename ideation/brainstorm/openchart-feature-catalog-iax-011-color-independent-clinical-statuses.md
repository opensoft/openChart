# Color-independent Clinical Statuses — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Represents every clinical and operational status with text or shape in addition to color so meaning survives visual variation.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, color-independent-status
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-011 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Status semantics registry** — Detect inconsistent labels, icons, and urgency meanings across modules before release.

## Focus

This feature isolates non-color status semantics for badges, charts, alerts, queues, and printed artifacts.

## Behavior

- Every status indicator includes a localized text label or programmatically determinable equivalent alongside color.
- Icons and patterns may reinforce meaning but use a consistent legend and never replace the label.
- Clinical urgency, abnormality, completion, and availability use separate semantic categories rather than reusing one red-to-green scale.
- Charts provide data labels, table alternatives, or pattern encodings that remain interpretable in monochrome.
- Theme changes, high-contrast mode, grayscale printing, and common color-vision variations preserve status distinctions.
- Component tests reject status configurations that define only a color token.
- Unknown or unmapped values display as explicit Unknown text rather than inheriting a reassuring default color.

## Frappe realization

- **DocTypes:** `OC Status Presentation Rule` stores domain value, translation key, semantic category, icon, pattern, theme tokens, and effective release.
- **Surfaces:** Shared Frappe List indicators, Desk badges, Dashboard Charts, portal cards, and Print Formats resolve through one status renderer.
- **Translation and themes:** Frappe translations localize labels; Website Theme and Desk themes supply contrast-tested colors and non-color tokens.
- **Validation:** Fixtures register allowed statuses, and a build hook plus Script Report identifies raw color-only indicators and unmapped values.

## Boundaries

Owns: status presentation semantics and non-color equivalence. Consumes: authoritative status values, locale, and theme. Emits: consistent labels, icons, patterns, and test findings. Does not own: status computation or clinical urgency policy.

## Open questions

- Which status families require centrally governed vocabulary rather than module-owned labels?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Scalable Type And High-contrast Mode](openchart-feature-catalog-iax-012-scalable-type-and-high-contrast-mode.md)
