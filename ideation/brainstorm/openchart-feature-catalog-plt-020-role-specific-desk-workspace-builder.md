# Role-specific Desk Workspace Builder — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Composes governed Desk home screens with role-appropriate shortcuts, charts, queues, and explanatory content.
Topics: openchart-feature-catalog, platform, frappe, desk-workspaces
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-020 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Workspace adoption review** — Compare assigned workspaces with privacy-safe navigation signals to find ineffective layouts.

## Focus

This feature isolates administration of Frappe desk workspaces as job-centered navigation, not as a substitute for permissions.

## Behavior

- Workspace designers arrange approved Shortcuts, Links, Number Cards, Dashboard Charts, queues, and instructional blocks.
- Each workspace targets roles, optional job-function templates, sites, and an effective date.
- Preview simulates each target role and flags cards or links the role cannot read.
- Workspaces move through Draft, Review, Published, Retired, and Superseded states.
- Publication preserves user personalization allowed by policy while replacing governed sections atomically.
- Missing assets are omitted with an administrator warning and never expose inaccessible record counts.

## Frappe realization

- **DocTypes:** `OC Workspace Release` wraps native Workspace metadata with audience roles, template Links, version, sections JSON, and state.
- **Surface:** extend Frappe Workspace Builder with role simulation, responsive preview, and a release diff.
- **Permissions:** Workspace Designer authors; Workspace Approver publishes; runtime cards retain source report permissions.
- **Promotion:** Workspace, Number Card, and Dashboard Chart records export as fixtures and activate through the configuration pipeline.

## Boundaries

Owns: role-specific Desk composition and publication. Consumes: roles, reports, filters, charts, and shortcuts. Emits: native Workspace configuration. Does not own: underlying capabilities, permissions, or personal task priority.

## Open questions

- Which workspace elements may users personalize without losing supportability?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Job-function Role Templates](openchart-feature-catalog-plt-007-job-function-role-templates.md) · [Team-shared Saved Filters](openchart-feature-catalog-plt-019-team-shared-saved-filters.md)
