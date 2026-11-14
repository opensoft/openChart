# Custom Field Administration — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets authorized administrators extend approved DocTypes through governed custom fields without application code changes.
Topics: openchart-feature-catalog, platform, frappe, custom-fields
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-008 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Extension compatibility scan** — Warn when custom fields conflict with an incoming standard schema change.

## Focus

This feature isolates safe use of Frappe Customize Form for additive local data capture while protecting clinical invariants and supported APIs.

## Behavior

- Configuration administrators select an allowlisted DocType and propose a field label, type, placement, permissions, and display conditions.
- Protected core fields, unsupported names, unsafe field types, and edits to accepted-record semantics are rejected.
- A preview shows the form layout, API shape impact, report availability, and affected roles before publication.
- Changes move through Draft, Review, Published, Disabled, and Superseded states with reasons.
- Disabling hides capture but retains existing values and export visibility under permission control.
- Publication records a schema snapshot and requires a migration-safe rollback plan for destructive proposals.

## Frappe realization

- **DocTypes:** `OC Custom Field Change` stores target DocType, proposed Custom Field JSON, placement, risk class, state, and snapshot references.
- **Surface:** wrap Frappe Customize Form with allowlists, preview, and review workflow; generated Custom Field records remain native Frappe metadata.
- **Hooks:** `validate` enforces protected-field policy; `on_update` clears metadata caches and writes administrative audit evidence.
- **Promotion:** export reviewed Custom Fields as fixtures and apply schema changes through patches/migrations rather than ad hoc production edits.

## Boundaries

Owns: governed additive custom-field lifecycle. Consumes: DocType metadata, field policy, and roles. Emits: native Custom Field metadata and fixtures. Does not own: standard schema evolution or arbitrary server logic.

## Open questions

- Which clinical DocTypes are safe for local custom fields without breaking interoperability profiles?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Clinical Form And Layout Builder](openchart-feature-catalog-plt-009-clinical-form-and-layout-builder.md) · [Configuration Promotion Pipeline](openchart-feature-catalog-plt-030-configuration-promotion-pipeline.md)
