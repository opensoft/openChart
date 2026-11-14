# Department And Division Hierarchy — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Models effective-dated organizational divisions and departments for ownership, routing, reporting, and scoped administration.
Topics: openchart-feature-catalog, platform, frappe, organization-hierarchy
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-040 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Reorganization planner** — Preview ownership, routing, and reporting effects before a hierarchy change becomes effective.

## Focus

This feature isolates the administrative organization tree from physical locations and provider identity.

## Behavior

- Organization administrators create divisions and departments with codes, parent, owner, cost reference, site scope, and effective dates.
- The hierarchy rejects cycles, duplicate effective codes, and parents that expire before children.
- Reorganization creates successor relationships and a future-effective tree rather than rewriting history.
- Published nodes may be used for assignment, ownership, report grouping, and user permissions.
- Inactivation requires reassignment of active owners, queues, and rules or a documented exception.
- Users see only nodes within permitted sites, while stable identifiers remain resolvable on historical records.

## Frappe realization

- **DocTypes:** tree DocType `OC Organization Unit` stores unit_type, code, parent, owner User, site, effective dates, and successor Link.
- **Workflow:** Organization Administrator drafts; Platform Approver publishes restructures and retirements.
- **Hooks:** `validate` checks tree and effective-date integrity; publication emits hierarchy-version events and refreshes User Permission caches.
- **Surface:** Tree view, effective-date preview, and Script Report show dependencies blocking retirement.

## Boundaries

Owns: division and department identities, hierarchy, and effective versions. Consumes: site and accountable owner identity. Emits: organization-unit Links and restructuring events. Does not own: physical locations, HR positions, or accounting ledgers.

## Open questions

- Can a department belong to multiple reporting hierarchies, or should alternate groupings use tags?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Facility And Location Master Registry](openchart-feature-catalog-plt-003-facility-and-location-master-registry.md) · [Skill-based Task Routing](openchart-feature-catalog-plt-045-skill-based-task-routing.md)
