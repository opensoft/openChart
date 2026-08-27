# Cross-site Shared Services — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets independently isolated clinic sites consume explicitly approved shared operational services without sharing clinical tables.
Topics: openchart-feature-catalog, platform, frappe, shared-services
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-002 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Regional service pools** — Route sites to compliant shared services by residency and capacity policy.

## Focus

This feature isolates the contract by which bench multi-site tenants share gateways, terminology feeds, or operational workers while preserving site authority.

## Behavior

- Platform operators register a shared service with endpoint class, supported regions, health state, and data-handling policy.
- Site administrators request a service binding and see which data categories and operations the binding permits.
- Approval creates a site-scoped binding with revocable credentials and no direct database access between sites.
- Requests include site identity and correlation IDs; responses return per-site outcomes and never aggregate clinical payloads by default.
- Health degradation can fail over only to a compatible approved endpoint and records the routing decision.
- Revocation blocks new calls immediately while retaining redacted operational evidence for audit.

## Frappe realization

- **DocTypes:** `OC Shared Service` defines class, endpoint, region, policy, and health; `OC Site Service Binding` stores site, scope, credential reference, and status.
- **Permissions:** Platform Operator manages services; Site Administrator may request and inspect only bindings for permitted sites via User Permissions.
- **Hooks/API:** `validate` enforces region and scope compatibility; `open_chart.api.v1.platform.invoke_shared_service` injects site identity and checks the binding.
- **Surface:** a Script Report shows binding health, failovers, request counts, and errors without payload content.

## Boundaries

Owns: shared-service registry and site bindings. Consumes: site identity, service health, and credential references. Emits: authorized service routes and operational evidence. Does not own: service implementation or cross-site clinical exchange.

## Open questions

- Which service classes may receive identifiable data, and under what site-level agreement?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Clinic Site Provisioning](openchart-feature-catalog-plt-001-clinic-site-provisioning.md)
