# Workflow Configuration Studio — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets authorized designers configure, simulate, review, and publish document workflows with explicit states, transitions, and authority.
Topics: openchart-feature-catalog, platform, frappe, workflow-configuration
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-010 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Workflow simulation cases** — Replay synthetic records and actors through a proposed transition graph before publication.

## Focus

This feature isolates a governed UI around Frappe Workflow Manager and Workflow Builder as a first-class low-code advantage.

## Behavior

- Workflow designers select an allowlisted DocType and define states, document states, actions, roles, conditions, and optional Workflow Actions.
- The studio rejects unreachable states, ambiguous transitions, missing terminal outcomes, and unsafe condition expressions.
- A simulator tests actors, fields, and transitions using synthetic cases without mutating production records.
- Definitions move through Draft, Review, Published, Retired, and Superseded states.
- Publication shows records currently in affected states and requires an explicit migration mapping when state names change.
- Runtime transition failures leave the document unchanged and return a user-facing reason and correlation ID.

## Frappe realization

- **DocTypes:** `OC Workflow Package` wraps target DocType, version, Workflow/Workflow State/Workflow Action references, simulation cases, and migration map.
- **Surface:** extend Frappe Workflow Manager and Workflow Builder with graph linting, role matrix, diff, and synthetic simulation.
- **Permissions:** Workflow Designer authors; Workflow Approver publishes; clinical roles only execute permitted transitions.
- **Promotion:** published Workflow metadata exports as fixtures; state migrations run through idempotent patches with preflight reports.

## Boundaries

Owns: workflow definition lifecycle, simulation, and publication. Consumes: DocType metadata, roles, and approved expressions. Emits: native Frappe Workflow configuration and migration evidence. Does not own: domain decisions encoded by workflow actors.

## Open questions

- Which workflow changes require domain-owner approval in addition to platform approval?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Declarative Business Rule Builder](openchart-feature-catalog-plt-011-declarative-business-rule-builder.md)
