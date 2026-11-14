# Clinic Site Provisioning — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provisions an isolated Frappe site for each clinic with repeatable configuration, health checks, and ownership records.
Topics: openchart-feature-catalog, platform, frappe, clinic-site-provisioning
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-001 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Guided clinic launch checklist** — Turn an approved site request into a tracked readiness sequence.

## Focus

This feature isolates site-per-clinic tenancy through Frappe bench multi-site rather than mixing clinic records in one database.

## Behavior

- Platform operators submit a clinic code, host name, region, initial administrator, and approved baseline profile.
- Requests move through Draft, Approved, Provisioning, Verifying, Active, Failed, and Retired states.
- Provisioning creates an isolated site and installs only the approved openChart app set and fixtures.
- Verification checks schema level, required roles, synthetic smoke data, background workers, and outbound service reachability.
- A failed step records a redacted error and supports idempotent retry without creating a second site.
- Retiring a site requires backup evidence, retention approval, and explicit confirmation; it never silently deletes clinical data.

## Frappe realization

- **DocTypes:** `OC Clinic Site Request` stores clinic_code, hostname, region, baseline_profile, state, and bench_job_id; `OC Site Verification` stores check outcomes.
- **Workflow:** Frappe Workflow gates Draft → Approved → Provisioning → Verifying → Active, with Platform Operator and Platform Approver actions.
- **Automation:** a whitelisted `open_chart.api.v1.platform.provision_site` method enqueues an RQ job that invokes controlled bench multi-site operations outside the request transaction.
- **Surface:** a Platform Operations Desk workspace shows request Kanban, failed checks, and active-site health.

## Boundaries

Owns: tenant site lifecycle orchestration. Consumes: approved clinic identity, deployment region, app baseline, and infrastructure credentials. Emits: isolated site and verification evidence. Does not own: infrastructure procurement or clinical data migration.

## Open questions

- Which bench operations require an external deployment controller rather than a Frappe worker?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Cross-site Shared Services](openchart-feature-catalog-plt-002-cross-site-shared-services.md)
