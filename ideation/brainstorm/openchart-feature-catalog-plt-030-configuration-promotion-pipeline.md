# Configuration Promotion Pipeline — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Packages reviewed Frappe configuration and promotes it from development through staging to production with diff, preflight, and rollback evidence.
Topics: openchart-feature-catalog, platform, frappe, configuration-promotion
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-030 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Configuration provenance graph** — Trace every production metadata value to its source release and approval.

## Focus

This feature isolates environment promotion for low-code assets so production configuration is reproducible rather than manually recreated.

## Behavior

- Configuration authors assemble approved Custom Fields, Workflows, Print Formats, Workspaces, rules, and related metadata into a release package.
- The pipeline computes dependency order, canonical digests, target diffs, required patches, and environment compatibility.
- Packages move through Draft, Built, Staging, Validated, Approved, Production, Failed, Rolled Back, and Superseded states.
- Staging validation uses synthetic fixtures and records test outcomes before production approval.
- Production application is idempotent, rejects untracked target drift, and retains a rollback snapshot for reversible metadata.
- Destructive schema or state changes require explicit patches/migrations and cannot masquerade as ordinary fixture synchronization.

## Frappe realization

- **DocTypes:** `OC Configuration Package`, child `OC Configuration Item`, and `OC Promotion Run` store assets, fixtures, patches, digests, environments, approvals, and outcomes.
- **Automation:** package build uses Frappe fixture export; deployment controller applies fixtures then idempotent patches in declared order and runs validation hooks.
- **Permissions:** Configuration Author builds; Environment Approver promotes; production service identity executes signed packages only.
- **Surface/API:** diff viewer, dependency graph, validation report, and guarded promote/rollback methods with correlation IDs.

## Boundaries

Owns: configuration packaging, environment promotion, drift checks, and evidence. Consumes: published metadata assets, fixtures, patches, and target inventory. Emits: reproducible configuration releases. Does not own: application binaries or unreviewed production edits.

## Open questions

- Which Frappe metadata types can be safely rolled back after users create records under the new configuration?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Custom Field Administration](openchart-feature-catalog-plt-008-custom-field-administration.md) · [Feature Flag Gradual Rollout](openchart-feature-catalog-plt-031-feature-flag-gradual-rollout.md)
