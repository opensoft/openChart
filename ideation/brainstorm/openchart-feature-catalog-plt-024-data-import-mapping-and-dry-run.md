# Data Import Mapping And Dry Run — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Imports governed catalog and configuration data through reusable mappings, validation previews, and per-row reconciliation.
Topics: openchart-feature-catalog, platform, frappe, data-import
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-024 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Source-specific mapping library** — Share vetted mappings for common administrative datasets without bundling source data.

## Focus

This feature isolates safe use of Frappe Data Import for administrative and catalog data, not unreviewed clinical ingestion.

## Behavior

- Data stewards upload CSV or spreadsheet input, select an allowlisted DocType, and map columns to approved fields.
- Mapping templates define transforms, defaults, key matching, duplicate policy, and expected code sets.
- Dry run parses every row and reports creates, updates, no-ops, duplicates, missing Links, and validation failures.
- Imports move through Uploaded, Mapped, Dry-run Complete, Approved, Running, Completed, Partially Failed, and Rejected states.
- Execution pins the source digest and mapping version; changed files require a new dry run and approval.
- Row outcomes are downloadable, while uploaded files follow retention policy and reject formulas, macros, and unsafe content.

## Frappe realization

- **DocTypes:** `OC Import Mapping Template` stores target, column map, transforms, keys, and version; `OC Governed Data Import` wraps native Data Import evidence.
- **Surface:** extend Frappe Data Import with mapping templates, full dry-run reconciliation, and approval summary.
- **Automation:** RQ workers process approved imports in bounded batches through DocType validation and supported APIs.
- **Permissions:** Data Steward prepares; Data Approver authorizes by target class; attachments use restricted File permissions.

## Boundaries

Owns: administrative import mapping, preview, approval, and row outcomes. Consumes: source file, DocType schema, and code sets. Emits: validated records and reconciliation evidence. Does not own: general clinical migration or direct table writes.

## Open questions

- Which transform functions are sufficiently deterministic and safe for reusable mapping templates?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Previewed Bulk Data Update](openchart-feature-catalog-plt-023-previewed-bulk-data-update.md) · [Terminology And Code-set Updates](openchart-feature-catalog-plt-038-terminology-and-code-set-updates.md)
