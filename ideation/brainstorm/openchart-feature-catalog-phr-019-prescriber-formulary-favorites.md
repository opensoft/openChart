# Prescriber Formulary Favorites — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets each prescriber maintain frequently used medication choices with contextual formulary cues while requiring patient-specific review.
Topics: openchart-feature-catalog, eprescribing, frappe, formulary-favorites
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-019 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Team-curated starter sets** — Organizations could publish reviewable favorite templates that users explicitly adopt.

## Focus

This feature isolates personal medication shortcuts without turning them into order defaults. Favorites accelerate search but never carry patient-specific safety approval forward.

## Behavior

- A prescriber can pin a medication, form, common SIG template, indication, and optional formulary context.
- Favorites are private by default and can be reordered, annotated, retired, or copied from a governed organization set.
- The composer shows whether stored formulary context is current, stale, or unrelated to the patient's coverage.
- Choosing a favorite creates editable draft fields and triggers all current patient-specific checks.
- Changes to terminology, schedule, product availability, or policy can mark a favorite stale without deleting it.
- No favorite can submit, sign, or transmit a prescription automatically.

## Frappe realization

- **DocTypes:** `OC Prescriber Medication Favorite` links User, medication code, optional SIG template, indication, rank, and context snapshot.
- **Permissions/API:** Owner-only DocPerms govern personal entries; formulary stewards publish separate `OC Medication Favorite Set` templates.
- **Hooks:** Terminology and policy updates flag affected favorites for review through background jobs.
- **Surfaces:** Composer shortcut palette and stale-favorites report support selection and maintenance.

## Boundaries

Owns: user shortcut configuration and freshness markers. Consumes: medication terminology, SIG templates, and formulary metadata. Emits: editable draft values. Does not own: clinical suitability, coverage determination, or automatic ordering.

## Open questions

- Which organization-curated fields should remain locked versus editable after adoption?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Therapeutic Alternative Suggestion Hooks](openchart-feature-catalog-phr-020-therapeutic-alternative-suggestion-hooks.md)
