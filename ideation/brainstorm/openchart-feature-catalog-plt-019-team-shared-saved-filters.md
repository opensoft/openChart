# Team-shared Saved Filters — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets teams publish permission-safe list-view filters with ownership, versioning, and controlled defaults.
Topics: openchart-feature-catalog, platform, frappe, shared-filters
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-019 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Operational filter packs** — Bundle reviewed filters with a role workspace and onboarding template.

## Focus

This feature isolates reusable team views on Frappe List data without turning a filter into an access-control mechanism.

## Behavior

- Users save personal filters from an eligible List view and may submit them for team publication.
- A team owner chooses title, description, roles, site scope, sort order, columns, and optional default behavior.
- Publication rejects unknown fields, unsafe operators, role-inaccessible columns, and hard-coded patient identifiers.
- Shared filters move through Draft, Published, Retired, and Superseded states while personal copies remain user-owned.
- Running a filter always applies current Frappe permissions; zero visible rows is valid and does not reveal hidden counts.
- If schema changes invalidate a clause, the filter is disabled with an actionable owner notification.

## Frappe realization

- **DocTypes:** `OC Shared List Filter` stores reference DocType, filters JSON, columns, roles, team, site scope, version, and state.
- **Surface:** List View actions support Save Personal and Submit for Team; workspace shortcuts link published filter IDs.
- **Hooks:** validation resolves field metadata and permissions; scheduled checks detect schema drift after migrations.
- **Permissions:** Team Filter Publisher manages team assets; all execution still uses the reader's DocPerms and User Permissions.

## Boundaries

Owns: publication and lifecycle of shared list configurations. Consumes: DocType fields, roles, team identity, and list-view settings. Emits: permission-safe reusable views. Does not own: row authorization or source data.

## Open questions

- May a team owner force a default filter, or should users always be able to opt out?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Global Search Configuration](openchart-feature-catalog-plt-018-global-search-configuration.md) · [Role-specific Desk Workspace Builder](openchart-feature-catalog-plt-020-role-specific-desk-workspace-builder.md)
