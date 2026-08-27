# Visible Focus And Skip Navigation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Makes keyboard location unmistakable and provides stable skip targets for repeated clinical and portal page regions.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, focus-navigation
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-010 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Focus-path overlay** — Let testers visualize and export the focus sequence for a route using synthetic data.

## Focus

This feature isolates focus visibility, placement, and bypass navigation from general keyboard operability.

## Behavior

- Every keyboard-focusable control displays a high-contrast indicator that remains visible against all supported themes.
- Focus indicators are not clipped by scrolling containers, sticky headers, dialogs, or validation overlays.
- Desk and portal pages expose skip links to main content, patient context, primary form, messages, and navigation where present.
- Route changes and validation failures move focus to a meaningful heading or error summary only when that movement helps the user.
- After dialogs, drawers, and command surfaces close, focus returns to the invoking control or a documented fallback.
- Virtualized lists preserve the user's logical item or announce when it no longer exists.
- Pointer interaction does not permanently suppress focus visibility for later keyboard use.

## Frappe realization

- **Surfaces:** Website Theme and Desk theme tokens define focus ring color, width, offset, and forced-colors behavior; shared templates render skip targets.
- **Client behavior:** Frappe route hooks manage heading focus, error-summary focus, dialog restoration, and virtual-list fallback by stable element IDs.
- **Configuration:** `OC Focus Navigation Standard` stores required landmarks, route exceptions, test status, and approved rationale.
- **Quality hooks:** Browser tests evaluate focus visibility across themes and save failures to `OC Accessibility Defect` for assigned remediation.

## Boundaries

Owns: visible focus presentation, focus restoration, and repeated-region bypass. Consumes: route structure, theme tokens, and component lifecycle events. Emits: predictable focus location and conformance defects. Does not own: authorization or business workflow order.

## Open questions

- Which patient-context regions warrant first-class skip targets without making the skip menu itself burdensome?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Keyboard-only Navigation Completeness](openchart-feature-catalog-iax-009-keyboard-only-navigation-completeness.md)
