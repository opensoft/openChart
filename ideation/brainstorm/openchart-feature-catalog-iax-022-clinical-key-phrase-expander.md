# Clinical Key-phrase Expander — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Expands clinician-owned abbreviations into reviewable text while preventing silent insertion, hidden automation, and unsafe context reuse.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, phrase-expander
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-022 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Team phrase review** — Publish shared, versioned phrases after clinical and terminology review while retaining personal variants.

## Focus

This feature isolates explicit text expansion for documentation efficiency; it is not ambient generation or autonomous clinical inference.

## Behavior

- Clinicians define a unique trigger, expansion text, language, allowed document contexts, and personal or governed team scope.
- Typing a trigger and deliberate activation previews or inserts the exact expansion at the cursor.
- Expansions never fire inside medication dose controls, codes, identifiers, passwords, or other excluded field classes.
- Placeholders require explicit completion and remain visibly unresolved until addressed.
- Users can undo an insertion as one action and inspect which phrase version produced it.
- Shared phrases move through Draft, Review, Published, Retired, and Superseded states; personal phrases cannot impersonate governed labels.
- Final document submission validates that no unresolved placeholders or hidden phrase markers remain.

## Frappe realization

- **DocTypes:** `OC Clinical Phrase` stores owner/team, trigger, locale, rich text, allowed DocTypes/fields, placeholders, version, and state.
- **Workflow and permissions:** Clinical Author owns personal phrases; Phrase Publisher and Clinical Reviewer govern shared phrases through Frappe Workflow and User Permissions.
- **Client and hooks:** Frappe form scripts detect deliberate activation in allowed text controls; document `validate` rejects unresolved placeholders.
- **API:** `open_chart.api.v1.ux.phrases.resolve` returns only authorized exact versions and records non-PHI usage counts without copying note text.

## Boundaries

Owns: phrase definitions, explicit expansion, placeholder checks, and version provenance. Consumes: user identity, field context, locale, and phrase scope. Emits: clinician-reviewable text. Does not own: clinical truth, note signing, diagnosis, orders, or generative drafting.

## Open questions

- Which phrase categories are too clinically consequential for personal, unreviewed definitions?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Form Autosave And Recovery](openchart-feature-catalog-iax-023-form-autosave-and-recovery.md)
