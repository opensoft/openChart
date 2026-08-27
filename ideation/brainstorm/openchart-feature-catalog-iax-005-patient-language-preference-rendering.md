# Patient Language Preference Rendering — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Selects patient-facing content by recorded language preference with explicit fallback and provenance at every delivery surface.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, patient-language
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-005 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Preference confirmation prompt** — Periodically ask patients to confirm spoken and written language choices separately.

## Focus

This feature isolates language selection for patient-facing content without inferring comprehension or consent.

## Behavior

- Registration staff or patients record preferred spoken language, preferred written language, and whether an interpreter is requested.
- Portal pages, notifications, instructions, and print outputs resolve content against the written-language preference at delivery time.
- If no validated translation exists, the surface identifies the fallback language before display or send.
- Staff may choose another available language for a single artifact with a reason, without rewriting the patient's preference.
- Preference changes affect future rendering and retain effective-dated history for prior delivery evidence.
- Proxy viewers use the patient's content preference unless a clearly labeled proxy-only interface setting applies.
- The system never treats a selected language as proof of literacy, understanding, or informed consent.

## Frappe realization

- **DocTypes:** `OC Patient Language Preference` stores patient, spoken and written locales, interpreter request, effective dates, source, and successor link.
- **Translation system:** Frappe translations and validated patient-content variants resolve through a shared server service with explicit fallback metadata.
- **Roles and permissions:** Patient, Proxy User, Registration Staff, and Clinical Staff receive scoped access; preference changes use guarded `open_chart.api.v1.ux.language_preference` methods.
- **Surfaces:** Website Theme exposes the current content language and fallback banner consistently across portal, Notification, Print Format, and Web Form surfaces.

## Boundaries

Owns: patient language preferences and content-resolution metadata. Consumes: patient identity, validated translations, proxy scope, and channel context. Emits: selected content locale and fallback evidence. Does not own: interpreter fulfillment, literacy assessment, or consent validity.

## Open questions

- Which patient communications should be blocked rather than sent in a fallback language?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Translated Patient Instructions Library](openchart-feature-catalog-iax-007-translated-patient-instructions-library.md)
