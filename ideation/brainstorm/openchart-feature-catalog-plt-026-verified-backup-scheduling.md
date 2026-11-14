# Verified Backup Scheduling — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Schedules site backups and verifies completeness, encryption, retention, and restorability evidence after every run.
Topics: openchart-feature-catalog, platform, frappe, backup-verification
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-026 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Recovery-point compliance dashboard** — Compare actual verified backups with site recovery objectives.

## Focus

This feature isolates backup policy and integrity verification around Frappe sites without treating file creation as proof of recoverability.

## Behavior

- Platform operators configure site scope, database and file coverage, cadence, destination, encryption key reference, and retention.
- Policies move through Draft, Active, Paused, Failed, Retired, and Superseded states.
- Each run records start and finish, component sizes, manifest digest, encryption result, upload result, and verification checks.
- Missing private files, incomplete database dumps, checksum mismatch, or destination failure marks the run failed.
- Failures alert the site and platform owner and retry only within configured concurrency and retention safeguards.
- Backup artifacts are never downloadable through ordinary Desk file access and contain no embedded credentials.

## Frappe realization

- **DocTypes:** `OC Backup Policy` stores site, coverage, cadence, destination credential reference, encryption policy, and retention; `OC Backup Run` stores manifests and results.
- **Automation:** `scheduler_events` launch controlled bench backup jobs through RQ; verification reads manifests and checks encrypted object existence.
- **Permissions:** Backup Operator manages runs; Backup Approver changes policy; Audit Reviewer sees evidence but not artifacts or secrets.
- **Surface:** dashboard charts show verified recovery points, age, duration, size trends, and failures by site.

## Boundaries

Owns: backup policy, orchestration, integrity checks, and evidence. Consumes: site data, storage binding, and encryption key reference. Emits: protected backup artifacts and verification results. Does not own: storage infrastructure or disaster declaration.

## Open questions

- How frequently must a verified artifact undergo a full restore drill to remain trusted?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Restore Drill Orchestration](openchart-feature-catalog-plt-027-restore-drill-orchestration.md)
