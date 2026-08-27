# Quick Entry Form Customization — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Configures concise, role-aware Quick Entry forms for safe high-frequency creation of approved records.
Topics: openchart-feature-catalog, platform, frappe, quick-entry
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-021 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Task-context defaults** — Prefill safe values from the launching queue while preserving visible confirmation.

## Focus

This feature isolates Frappe Quick Entry configuration without weakening mandatory fields, validation, or API guardrails.

## Behavior

- Form designers choose an allowlisted createable DocType, visible fields, ordering, safe defaults, and target roles.
- Required source fields cannot be omitted unless a deterministic server default supplies them.
- Preview covers empty, defaulted, validation-error, and permission-limited states using synthetic data.
- Configurations move through Draft, Review, Published, Retired, and Superseded states.
- Users may expand to the full form before saving; partial Quick Entry records are never silently persisted.
- Save failures preserve entered values locally and show field-specific errors without bypassing guarded write APIs.

## Frappe realization

- **DocTypes:** `OC Quick Entry Profile` stores target DocType, roles, ordered field rows, defaults, version, and state.
- **Client scripts:** launch hooks select the effective profile and render native Quick Entry controls; server validation remains authoritative.
- **Permissions/API:** profile validation checks DocPerms and mandatory metadata; clinical writes continue through supported `open_chart.api.v1` methods.
- **Promotion:** reviewed profiles are fixtures and receive compatibility checks during patches/migrations.

## Boundaries

Owns: concise creation presentation and safe defaults. Consumes: DocType metadata, role permissions, and launch context. Emits: validated create requests. Does not own: source validation, record authority, or bulk entry.

## Open questions

- Which clinical record types are too consequential for Quick Entry even with full validation?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Clinical Form And Layout Builder](openchart-feature-catalog-plt-009-clinical-form-and-layout-builder.md) · [Keyboard Shortcut Scheme Editor](openchart-feature-catalog-plt-022-keyboard-shortcut-scheme-editor.md)
