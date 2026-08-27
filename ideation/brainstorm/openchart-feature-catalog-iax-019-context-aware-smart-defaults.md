# Context-aware Smart Defaults — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Prefills eligible form values from explicit context and governed rules while keeping every default visible, editable, and attributable.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, smart-defaults
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-019 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Default effectiveness review** — Measure accepted, changed, and cleared defaults by rule without judging clinical correctness.

## Focus

This feature isolates transparent prefill from recommendations and autonomous clinical decisions.

## Behavior

- UX administrators define defaults for eligible non-consequential fields using role, facility, encounter type, device, and current workflow context.
- Prefilled values are visually identified and expose a plain-language explanation of their source.
- Users may accept, change, or clear a default before submission unless a separate authoritative policy makes the field read-only.
- Patient-specific clinical facts are never inferred solely from prior frequency or another patient's behavior.
- Rules are versioned, effective-dated, priority ordered, and tested against synthetic contexts before activation.
- Conflicting rules yield no value and show an administrator-visible conflict rather than choosing silently.
- Submitted records retain the rule version and whether the user accepted or changed the default.

## Frappe realization

- **DocTypes:** `OC Smart Default Rule` stores target DocType/field, typed value expression, context conditions, priority, effective dates, and state.
- **Workflow and roles:** Draft, Review, Active, Retired, and Superseded states separate UX Administrator approval from Clinical Safety Reviewer approval for clinical surfaces.
- **Hooks and API:** `before_load`/whitelisted preview methods evaluate rules server-side; `validate` records provenance and never bypasses mandatory or permission checks.
- **Surfaces:** Frappe form scripts mark defaulted controls and show source explanations; a Script Report lists conflicts and user-change rates.

## Boundaries

Owns: eligible prefill rules, explanation, and provenance. Consumes: authorized workflow context, policy versions, and field metadata. Emits: editable proposed values and audit metadata. Does not own: clinical recommendations, diagnosis, orders, or locked compliance values.

## Open questions

- Which field classes are too consequential to permit smart defaults even when users can edit them?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Form Autosave And Recovery](openchart-feature-catalog-iax-023-form-autosave-and-recovery.md)
