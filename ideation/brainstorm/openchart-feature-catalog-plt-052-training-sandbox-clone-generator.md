# Training Sandbox Clone Generator — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Creates time-limited training sites from approved baselines with synthetic data, isolated integrations, and automatic cleanup.
Topics: openchart-feature-catalog, platform, frappe, training-sandbox
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-052 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Scenario reset checkpoints** — Return a training site to a known synthetic starting state between classes.

## Focus

This feature isolates safe training environment generation and prohibits ordinary cloning of production patient data.

## Behavior

- Training administrators select an approved configuration baseline, synthetic dataset, app version, region, class owner, users, and expiry.
- Requests move through Draft, Approved, Provisioning, Seeding, Verifying, Ready, Failed, Expired, Cleaning, and Closed states.
- Provisioning creates an isolated bench site with outbound integrations disabled or bound to synthetic test endpoints.
- Seed fixtures use `SYN-` identifiers and validation rejects records or files that resemble real protected data.
- Verification confirms training banner, synthetic-only guard, disabled production credentials, mail sink, and scheduled cleanup.
- Expiry disables login before cleanup and retains only non-sensitive provisioning and completion evidence.

## Frappe realization

- **DocTypes:** `OC Training Sandbox Request` stores baseline, dataset, version, region, owner, users, expiry, state, and bench job; checks are child rows.
- **Automation:** controlled bench multi-site jobs create the site, install apps, load synthetic fixtures, run patches, and verify isolation.
- **Permissions:** Training Administrator requests; Platform Operator approves and remediates; trainees receive only sandbox User accounts.
- **Surface:** sandbox dashboard shows readiness, expiry, synthetic checks, active users, and cleanup state.

## Boundaries

Owns: training site lifecycle, synthetic seeding, isolation verification, and cleanup. Consumes: approved baseline and synthetic fixtures. Emits: isolated training site and evidence. Does not own: production cloning, curriculum, or user competency certification.

## Open questions

- Which realistic workflows require generated synthetic longitudinal histories rather than fixed fixtures?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Synthetic-only Training Mode](openchart-feature-catalog-plt-053-synthetic-only-training-mode.md) · [Restore Drill Orchestration](openchart-feature-catalog-plt-027-restore-drill-orchestration.md)
