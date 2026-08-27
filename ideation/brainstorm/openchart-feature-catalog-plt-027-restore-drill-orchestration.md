# Restore Drill Orchestration — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Runs isolated, auditable restore drills that prove selected backups can recover within approved objectives.
Topics: openchart-feature-catalog, platform, frappe, restore-drills
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-027 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Scenario-based recovery exercises** — Add timed infrastructure and operator failure injects to a non-production drill.

## Focus

This feature isolates recovery proof in a quarantined environment and never permits accidental restore over a live clinic site.

## Behavior

- Recovery operators select a verified backup, isolated target, drill purpose, expected recovery point, and cleanup deadline.
- Approval checks environment separation, capacity, encryption access, and prohibition against production hostnames.
- Drills move through Planned, Approved, Restoring, Validating, Passed, Failed, Cleaning, and Closed states.
- Validation checks site boot, schema, app versions, record counts, files, background jobs, and synthetic smoke workflows.
- Any real identifiers visible to drill operators remain protected; training access requires de-identification or approved restricted handling.
- Closure requires cleanup evidence, measured recovery time and point, exceptions, and assigned remediation.

## Frappe realization

- **DocTypes:** `OC Restore Drill` links Backup Run and stores target, objectives, state, timings, validation rows, and cleanup evidence.
- **Workflow:** Recovery Operator plans; Recovery Approver authorizes; automated transitions reflect restore and validation jobs.
- **Automation:** controlled external bench commands run through queued jobs; fixtures supply synthetic validation probes after restore.
- **Surface:** Gantt view shows drill phases; Script Report compares achieved RTO/RPO and unresolved remediation.

## Boundaries

Owns: drill authorization, validation, measurements, and cleanup evidence. Consumes: verified backup and isolated infrastructure. Emits: recovery proof and remediation tasks. Does not own: live disaster recovery invocation or backup creation.

## Open questions

- Which validations are mandatory for every drill versus workload-specific extensions?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Verified Backup Scheduling](openchart-feature-catalog-plt-026-verified-backup-scheduling.md) · [Training Sandbox Clone Generator](openchart-feature-catalog-plt-052-training-sandbox-clone-generator.md)
