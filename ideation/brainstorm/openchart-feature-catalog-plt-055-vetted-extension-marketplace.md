# Vetted Extension Marketplace — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets administrators discover, review, install, upgrade, disable, and remove approved Frappe apps under explicit compatibility and trust policy.
Topics: openchart-feature-catalog, platform, frappe, extension-marketplace
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-055 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Extension conformance lab** — Run synthetic install, migration, permission, API, and uninstall tests before catalog approval.

## Focus

This feature isolates a client for vetted extensions and never treats marketplace listing as permission to execute unreviewed code.

## Behavior

- Site administrators browse extensions with publisher, license, source, version, compatibility, permissions, data access, support, and review status.
- Installation requests show app dependencies, DocTypes, hooks, scheduled jobs, migrations, outbound services, and requested roles before approval.
- Requests move through Requested, Security Review, Approved, Installing, Verifying, Active, Disabled, Upgrade Available, Failed, and Removed states.
- Installation requires a verified artifact digest, compatible Frappe/openChart versions, current backup, and approved maintenance window.
- Post-install verification uses synthetic checks; failure pauses activation and exposes rollback or remediation choices.
- Removal preserves governed records and audit evidence and refuses destructive uninstall without an approved data disposition plan.

## Frappe realization

- **DocTypes:** `OC Extension Catalog Entry`, `OC Site Extension`, and `OC Extension Operation` store manifest, digest, permissions, compatibility, site, state, and outcomes.
- **Automation:** an external deployment controller runs controlled `bench get-app`, install-app, migrate, patches, disable, and uninstall operations through queued requests.
- **Permissions:** Extension Reviewer curates; Security Approver and Site Approver authorize; Platform Operator executes signed catalog artifacts.
- **Surface:** marketplace Desk page, dependency diff, permission manifest, operation progress, and installed-extension health report.

## Boundaries

Owns: vetted catalog consumption, installation governance, compatibility evidence, and extension lifecycle. Consumes: signed manifests, artifacts, compatibility data, backups, and site approval. Emits: controlled app operations and health status. Does not own: third-party code quality, publisher support, or arbitrary package execution.

## Open questions

- What minimum conformance and security evidence must an extension provide before public listing?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Upgrade Channel And Preflight Manager](openchart-feature-catalog-plt-028-upgrade-channel-and-preflight-manager.md) · [Configuration Promotion Pipeline](openchart-feature-catalog-plt-030-configuration-promotion-pipeline.md)
