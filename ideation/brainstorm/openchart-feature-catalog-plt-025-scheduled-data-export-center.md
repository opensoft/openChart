# Scheduled Data Export Center — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates authorized one-time and recurring exports with scoped datasets, encryption, expiry, and delivery evidence.
Topics: openchart-feature-catalog, platform, frappe, data-export
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-025 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Catalog snapshot manifests** — Produce signed inventories of exported configuration versions for reproducibility.

## Focus

This feature isolates platform and catalog export operations while making sensitive clinical export require its own authority path.

## Behavior

- Data administrators choose an approved export definition, scope, format, destination, schedule, retention, and purpose.
- Preview reports record classes, estimated volume, sensitive categories, and permission or consent gates before approval.
- Definitions move through Draft, Review, Scheduled, Running, Available, Failed, Expired, and Retired states.
- Each run rechecks authority, pins schema and definition versions, encrypts output, and records a digest.
- Download links are short-lived, recipient-scoped, and revocable; destinations receive only the approved artifact.
- Partial generation or delivery failure never marks the run complete and supports idempotent retry.

## Frappe realization

- **DocTypes:** `OC Export Definition` stores dataset, fields, filters, format, schedule, destination, and policy; `OC Export Run` stores state, File, digest, and delivery evidence.
- **Automation:** `scheduler_events` enqueue RQ export runs; background generation uses permission-aware Query/Script Reports or registered exporters.
- **Permissions:** Data Export Administrator designs; Data Export Approver authorizes sensitive scopes; recipients receive artifact-specific access.
- **API:** guarded methods create, approve, download, revoke, and verify exports with audit correlation IDs.

## Boundaries

Owns: export orchestration, artifact protection, and delivery evidence. Consumes: approved dataset definitions, authority, and storage destination. Emits: encrypted export artifacts and manifests. Does not own: source data semantics or unrestricted EHI disclosure.

## Open questions

- Which export classes may be scheduled without per-run approval?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Verified Backup Scheduling](openchart-feature-catalog-plt-026-verified-backup-scheduling.md)
