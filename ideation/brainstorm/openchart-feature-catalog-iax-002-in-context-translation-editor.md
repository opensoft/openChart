# In-context Translation Editor — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets authorized administrators propose translations from the rendered interface while preserving review gates and source context.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, translation-editor
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-002 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Screenshot review evidence** — Attach de-identified viewport captures to translation proposals for layout review.

## Focus

This feature isolates safe, in-context translation authoring for administrators without making live interface text directly editable.

## Behavior

- A Localization Editor enables edit mode and selects a translatable label, message, help text, or portal phrase.
- The editor displays the source key, current translation, placeholders, nearby labels, locale, and originating app release.
- Saving creates a proposal rather than changing production text; patient-derived values are never copied into translation context.
- Placeholder removal, markup imbalance, duplicate keys, and length overflow produce actionable validation errors.
- Proposals move through Draft, Submitted, Changes Requested, Approved, and Superseded states.
- Approved proposals enter the target language-pack review queue and appear only after that pack is published.
- Users without translation permission see no edit affordance and cannot call proposal mutation methods.

## Frappe realization

- **DocTypes:** `OC Translation Proposal` stores message key, locale, source digest, proposed text, context route, placeholders, and state.
- **Client and translation system:** A Desk/portal client script maps rendered `__()` strings to keys; Frappe translation catalogs supply current values while proposals remain separate records.
- **Workflow and roles:** Frappe Workflow transitions are limited to Localization Editor and Localization Reviewer; Clinical Translation Reviewer approval is mandatory for marked clinical strings.
- **API and surfaces:** Guarded methods under `open_chart.api.v1.ux.translation` create proposals; a Desk workspace provides diff, assignment, and filtered review queues.

## Boundaries

Owns: contextual proposal capture and review handoff. Consumes: rendered translation keys, locale, route, and pack state. Emits: approved translation proposals. Does not own: source-string authoring, pack publication, or arbitrary page editing.

## Open questions

- How much non-PHI render context can be retained while still making ambiguous phrases reviewable?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Clinical Language Pack Governance](openchart-feature-catalog-iax-001-clinical-language-pack-governance.md)
