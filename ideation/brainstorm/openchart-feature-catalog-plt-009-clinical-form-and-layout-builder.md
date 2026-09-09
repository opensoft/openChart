# Clinical Form And Layout Builder — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Composes role-aware clinical capture screens from approved fields and sections with preview, versioning, and publication controls.
Topics: openchart-feature-catalog, platform, frappe, form-layout-builder
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-009 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Specialty layout packs** — Distribute vetted screen arrangements as installable configuration fixtures.

## Focus

This feature isolates low-code layout composition for clinical screens without allowing local layouts to redefine clinical data meaning.

## Behavior

- Form designers arrange approved fields into sections, columns, tabs, and child tables for a selected DocType and audience.
- Mandatory, read-only, depends-on, and role visibility expressions are validated against an allowlist.
- Desktop and narrow-screen previews display representative synthetic values and permission variants.
- Layouts move through Draft, Clinical Review, Published, Retired, and Superseded states.
- Publishing pins a version by site and role; users cannot select an unreviewed draft in clinical work.
- Missing fields or conflicting customizations block publication and identify the affected component.

## Frappe realization

- **DocTypes:** `OC Form Layout Profile` stores target DocType, audience roles, version, field arrangement JSON, conditions, and state.
- **Surface:** extend Customize Form and Form Builder metadata through a guarded Desk page with synthetic preview and diff panels.
- **Client scripts:** generated layout behavior uses reviewed depends-on/read-only expressions; arbitrary JavaScript is not accepted.
- **Promotion:** published profiles serialize as fixtures and are installed through reviewed patches where metadata migration is required.

## Boundaries

Owns: approved presentation layouts and audience binding. Consumes: standard and approved custom fields, roles, and synthetic preview data. Emits: versioned form metadata. Does not own: field semantics, clinical validation, or record authority.

## Open questions

- Should users be allowed personal section collapse preferences on top of a governed layout?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Custom Field Administration](openchart-feature-catalog-plt-008-custom-field-administration.md) · [Quick Entry Form Customization](openchart-feature-catalog-plt-021-quick-entry-form-customization.md)
