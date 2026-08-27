# Actionable Error Message Standard — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents errors in plain, localized language with the failed action, safe recovery, field context, and support correlation details.
Topics: openchart-feature-catalog, i18n-accessibility, frappe, error-messages
Repository context: openChart — Frappe v15 native EMR; catalog entry IAX-025 (Internationalization Accessibility And Clinician UX Platform)
Captured: 2026-08-24

## Possible feats

- **Error quality lint** — Reject raw exception text, jargon-only messages, missing recovery steps, and untranslated message keys.

## Focus

This feature isolates user-facing error contracts from logging, stack traces, and domain error ownership.

## Behavior

- Errors state what could not be completed, what remains safe, and the next action the user can take.
- Field errors appear beside the field and in a keyboard-focusable summary linked to every invalid control.
- System errors provide a correlation ID and retry guidance without exposing stack traces, secrets, query text, or protected data.
- Permission denials avoid confirming the existence or attributes of records the user cannot access.
- Repeated retries are disabled when unsafe and retain entered work where policy permits.
- Messages are translated through reviewed keys with placeholder validation and a clear fallback-language indicator.
- Screen readers receive one timely announcement while the full error remains available for review and copy.

## Frappe realization

- **DocTypes:** `OC User Error Definition` stores stable code, translation key, severity, safe summary, recovery action, field mapping, and support metadata policy.
- **Translation system:** Frappe `__()` catalogs provide reviewed localized messages; error definitions use named placeholders validated in tests.
- **API and logging:** Guarded APIs return typed error codes and correlation IDs; server logs retain technical detail separately with minimum-necessary structured context.
- **Surfaces:** Shared Frappe form, dialog, toast, portal, and error-summary components render definitions consistently and move focus appropriately.

## Boundaries

Owns: user-facing error structure, localization, accessibility, and correlation presentation. Consumes: typed domain errors, field paths, locale, and retry safety. Emits: actionable messages and support IDs. Does not own: root-cause resolution, technical logs, or domain transaction behavior.

## Open questions

- Which error definitions need clinical-safety review in addition to UX and localization review?

## Relationships

[Synthesis: Internationalization Accessibility And UX Platform](openchart-feature-catalog-synthesis-iax.md) · [Loading Offline And Stale-state Signals](openchart-feature-catalog-iax-026-loading-offline-and-stale-state-signals.md)
