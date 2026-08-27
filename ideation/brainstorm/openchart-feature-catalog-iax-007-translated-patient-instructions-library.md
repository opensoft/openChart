# Translated Patient Instructions Library — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Publishes versioned patient instructions in reviewed language variants with clinical and translation gates before use.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, translated-instructions
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-007 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Readability comparison** — Compare approved variants by reading level without automatically rewriting clinical instructions.

## Focus

This feature isolates reusable translated instruction content and its approval lineage from encounter-specific delivery.

## Behavior

- Clinical authors create a source instruction with purpose, audience, jurisdiction, effective dates, and safety-critical passages.
- Translators create locale variants tied to an exact source version and may not alter protected placeholders or coded references.
- Each variant moves through Draft, Translation Review, Clinical Review, Published, Withdrawn, and Superseded states.
- Clinicians can select only published variants and preview the exact language before attaching instructions to a patient interaction.
- A source amendment marks affected translations Stale and prevents silent reuse under the new version.
- If the preferred-language variant is absent, the chooser identifies available fallbacks and requires acknowledgment.
- Delivered copies retain source version, translation version, locale, actor, and timestamp.

## Frappe realization

- **DocTypes:** `OC Patient Instruction` stores source content and version; `OC Patient Instruction Translation` stores locale, translated HTML, source digest, review state, and effective dates.
- **Workflow and roles:** Frappe Workflows separate Clinical Author, Translator, Clinical Translation Reviewer, and Publisher actions with assignment notifications.
- **Translation system and surfaces:** Frappe's interface translation system labels controls; versioned instruction bodies render through Website Theme portal pages and Jinja Print Formats.
- **API and evidence:** `open_chart.api.v1.ux.instructions` resolves published variants and records immutable `OC Instruction Delivery` evidence; direct writes to published content are rejected.

## Boundaries

Owns: instruction versions, translated variants, review state, and delivery provenance. Consumes: author authority, locale preference, and clinical selection. Emits: exact reviewed instruction artifacts. Does not own: diagnosis, treatment choice, or proof of comprehension.

## Open questions

- Must every material source change force full clinical re-review of every translation, or can structured change classification narrow the scope?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Clinical Language Pack Governance](openchart-feature-catalog-iax-001-clinical-language-pack-governance.md)
