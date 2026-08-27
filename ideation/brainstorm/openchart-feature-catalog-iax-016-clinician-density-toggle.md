# Clinician Density Toggle — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets clinicians switch supported grids and worklists between compact and comfortable density without losing content or accessibility.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, interface-density
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-016 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Task-specific density defaults** — Recommend comfortable density on touch devices and compact density on reviewed high-volume workstations.

## Focus

This feature isolates spacing density for repeated clinical rows, forms, and queues while preserving identical information and actions.

## Behavior

- Clinicians select Compact or Comfortable density from the user preference panel and may reset to site default.
- Both modes expose the same labels, values, actions, status text, keyboard order, and error messages.
- Compact mode reduces whitespace but never drops below approved target, focus, text, or row-height constraints.
- Comfortable mode expands controls and row separation without forcing horizontal scrolling for ordinary forms.
- A route may declare one mode unsupported only with a visible explanation and documented conformance reason.
- Changes apply immediately and persist across sessions and supported devices.
- Patient portal surfaces use their own reviewed default and do not inherit a clinician-only compact preference.

## Frappe realization

- **Preferences:** Frappe user preferences store `desk_density`; bootinfo resolves user, role, and site defaults before workspace render.
- **Themes:** Desk themes expose compact and comfortable spacing tokens for forms, list views, grids, Kanban cards, and dialogs.
- **Configuration:** `OC Surface Density Policy` stores route support, minimum dimensions, role default, and exception rationale.
- **Quality:** Synthetic layout and keyboard tests compare content and actions across both modes and supported text scales.

## Boundaries

Owns: supported spacing density and preference resolution. Consumes: route policy, role, device context, and accessibility constraints. Emits: equivalent compact or comfortable views. Does not own: field-level authorization or clinical summarization.

## Open questions

- Should density vary by workspace or remain one global Desk preference to reduce surprise?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Shared-device Touch-target Standards](openchart-feature-catalog-iax-015-shared-device-touch-target-standards.md)
