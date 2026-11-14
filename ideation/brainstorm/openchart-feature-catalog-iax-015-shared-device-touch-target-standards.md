# Shared-device Touch-target Standards — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enforces touch target size, spacing, and input safeguards for clinical workflows used on shared tablets and touch displays.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, touch-targets
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-015 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Glove-mode profile** — Offer larger controls for approved devices and workflows used with clinical gloves.

## Focus

This feature isolates safe touch interaction sizing and spacing without redefining shared-device authentication.

## Behavior

- Primary actions, row controls, dismiss buttons, checkboxes, and icon buttons meet the configured minimum target size and spacing.
- Dense tables expose a touch-friendly row action surface instead of requiring precise taps on small icons.
- Destructive and clinically consequential actions remain separated from common navigation targets.
- Touch use does not remove keyboard, pointer, or screen-reader operability.
- Device or user touch mode may increase control size but cannot hide required context or silently change workflow meaning.
- Repeated taps during slow responses are debounced and return one idempotent operation result.
- Automated checks flag undersized targets, overlaps, and controls reachable only by hover.

## Frappe realization

- **Themes:** Desk themes and Website Theme define touch target, spacing, and coarse-pointer tokens applied by shared controls and list views.
- **Preferences and bootinfo:** Frappe user preferences plus coarse-pointer detection resolve Auto, Standard, or Large touch mode in bootinfo.
- **Configuration:** `OC Interaction Size Standard` stores minimums, exceptions, rationale, route, and release status.
- **Hooks and API:** Client scripts debounce submissions while guarded server methods enforce idempotency keys for consequential actions.

## Boundaries

Owns: target sizing, spacing, touch alternatives, and duplicate-input suppression. Consumes: pointer capability, user preference, and action criticality. Emits: touch-safe controls and conformance findings. Does not own: device enrollment, session locking, or infection-control policy.

## Open questions

- Which shared-device profiles require larger minimum targets than the general WCAG-oriented baseline?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Clinician Density Toggle](openchart-feature-catalog-iax-016-clinician-density-toggle.md)
