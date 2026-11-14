# Upgrade Channel And Preflight Manager — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Assigns sites to supported release channels and blocks upgrades until compatibility, backup, capacity, and migration checks pass.
Topics: openchart-feature-catalog, platform, frappe, upgrade-management
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-028 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Fleet upgrade waves** — Promote a release through canary, cohort, and broad site groups with pause criteria.

## Focus

This feature isolates LTS-versus-current channel policy and pre-upgrade evidence for Frappe v15 sites.

## Behavior

- Platform operators assign each site to an approved release channel, maintenance window, and upgrade cohort.
- Preflight checks current app versions, database compatibility, pending patches, custom metadata conflicts, backup recency, disk, and worker health.
- Upgrade plans move through Draft, Preflight Failed, Ready, Approved, Running, Verifying, Completed, Rolled Back, and Failed states.
- Blocking findings require remediation or a separately authorized exception with expiry.
- Execution records package digests, bench commands, migrations, patch outcomes, downtime, and post-upgrade checks.
- Cohort failure can pause later waves automatically but cannot trigger clinical changes or hidden rollback.

## Frappe realization

- **DocTypes:** `OC Upgrade Channel`, `OC Site Upgrade Plan`, and child `OC Upgrade Preflight Check` capture versions, cohorts, windows, findings, and outcomes.
- **Automation:** queued deployment-controller calls run bench update/migrate and registered patches; callbacks update evidence and websocket progress.
- **Permissions:** Platform Release Manager plans; Release Approver authorizes; Site Administrator reads site-specific status.
- **Surface:** fleet dashboard shows channel distribution, blockers, wave progress, and version drift.

## Boundaries

Owns: channel assignment, preflight, upgrade authorization, and evidence. Consumes: release manifests, site inventory, backups, and compatibility rules. Emits: controlled upgrade jobs and status. Does not own: release engineering or infrastructure rollback mechanics.

## Open questions

- How long may a clinic remain on an older LTS release after security support ends?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [In-app Patch Notes](openchart-feature-catalog-plt-029-in-app-patch-notes.md) · [Configuration Promotion Pipeline](openchart-feature-catalog-plt-030-configuration-promotion-pipeline.md)
