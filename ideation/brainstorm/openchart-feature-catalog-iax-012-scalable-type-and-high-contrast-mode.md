# Scalable Type And High-contrast Mode — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets users enlarge interface text and select a high-contrast presentation without clipping, lost content, or semantic changes.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, visual-accessibility
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-012 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Zoom resilience matrix** — Certify critical workflows at browser zoom and text-only scaling thresholds by release.

## Focus

This feature isolates user-controlled text scale and contrast modes across dense clinical and patient-facing surfaces.

## Behavior

- Users choose supported text scales and a high-contrast mode from an accessible preference panel.
- Layouts reflow without hiding labels, controls, error messages, or patient context at the declared scaling range.
- Tables offer horizontal navigation or responsive detail views rather than shrinking text below the selected size.
- High-contrast mode increases relevant foreground, border, focus, and control-state distinction without using color alone.
- Browser zoom and operating-system forced-colors settings remain functional and are not overridden.
- Changes preview immediately, persist per user, and can be reset without administrator help.
- Print outputs retain their governed print scale rather than inheriting an unsuitable interactive preference.

## Frappe realization

- **Preferences:** Frappe user preferences store `text_scale` and `high_contrast`; a boot hook adds effective values to bootinfo for first-render application.
- **Themes:** Website Theme and Desk themes use relative units, responsive grid rules, and contrast-token variants; client scripts set root data attributes.
- **Surfaces:** Shared forms, dialogs, lists, dashboards, portal pages, and error summaries consume the same tokens and reflow contracts.
- **Quality:** Synthetic browser tests cover supported scales, zoom, forced colors, and major locales; failures enter `OC Accessibility Defect`.

## Boundaries

Owns: interactive text scaling, high-contrast tokens, and reflow behavior. Consumes: user preferences, browser capabilities, and component layouts. Emits: adapted interfaces and conformance evidence. Does not own: clinical print typography or device display calibration.

## Open questions

- What maximum text scale can dense clinical grids support before switching to a card or detail projection?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Dyslexia-friendly Reading Mode](openchart-feature-catalog-iax-014-dyslexia-friendly-reading-mode.md)
