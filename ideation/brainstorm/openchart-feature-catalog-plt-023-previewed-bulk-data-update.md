# Previewed Bulk Data Update — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Performs reviewed mass updates with a deterministic preview, per-record outcomes, rollback strategy, and strict exclusions.
Topics: openchart-feature-catalog, platform, frappe, bulk-update
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-023 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Change-window execution** — Schedule approved batches inside a maintenance window with capacity checks.

## Focus

This feature isolates safe administrative mass update rather than exposing unrestricted database mutation.

## Behavior

- Data stewards select an allowlisted DocType, permission-safe filter, approved fields, replacement values, and reason.
- A dry run snapshots matching identifiers, validates every proposed change, and reports successes, skips, conflicts, and blocked records.
- Accepted clinical records, signed artifacts, immutable audit evidence, and protected fields are excluded by policy.
- Requests move through Draft, Previewed, Approved, Running, Completed, Partially Failed, Failed, and Reversed states.
- Execution rechecks versions and permissions; changed records become conflicts instead of receiving stale updates.
- Per-record outcomes and a tested compensation plan remain available without storing unnecessary record content.

## Frappe realization

- **DocTypes:** `OC Bulk Update Request` stores target, filter JSON, changes JSON, snapshot digest, counts, and state; child outcomes hold record Links and status.
- **Workflow:** Data Steward previews; Data Approver authorizes; Bulk Operator executes through an RQ job.
- **API:** `open_chart.api.v1.platform.preview_bulk_update` and `execute_bulk_update` enforce allowlists, version checks, and idempotency.
- **Surface:** a wizard shows sample diffs, aggregate counts, conflicts, and downloadable synthetic-safe outcome report.

## Boundaries

Owns: reviewed administrative batch mutation and outcome evidence. Consumes: filters, current versions, field policy, and permissions. Emits: validated updates and audit events. Does not own: clinical amendment or raw SQL access.

## Open questions

- Which non-clinical fields permit automated compensation versus manual correction after partial failure?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Data Import Mapping And Dry Run](openchart-feature-catalog-plt-024-data-import-mapping-and-dry-run.md)
