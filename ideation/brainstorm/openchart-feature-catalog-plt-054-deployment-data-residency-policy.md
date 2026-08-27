# Deployment Data Residency Policy — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records and enforces approved storage, processing, backup, support, and failover regions for each deployed site.
Topics: openchart-feature-catalog, platform, frappe, data-residency
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-054 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Residency dependency attestation** — Periodically certify every bound service and backup destination against site policy.

## Focus

This feature isolates deployment residency configuration and evidence; it does not claim that a selector alone establishes legal compliance.

## Behavior

- Compliance administrators define allowed and prohibited regions for primary data, files, backups, logs, processing, support, and failover.
- Each clinic site pins an approved policy version during provisioning and shows its effective deployment region.
- Service, gateway, vault, telemetry, export, and backup bindings validate their regions before activation.
- Policies move through Draft, Legal Review, Approved, Active, Retired, and Superseded states.
- A proposed region change produces a dependency and migration impact report and cannot be applied as a simple field edit.
- Detected drift opens a critical exception, blocks new noncompliant bindings, and preserves evidence for human remediation.

## Frappe realization

- **DocTypes:** `OC Data Residency Policy`, child `OC Residency Rule`, and `OC Residency Exception` store data class, operations, regions, version, approval, and expiry.
- **Hooks:** validation hooks on site service, gateway, backup, export, vault, and telemetry bindings call a central residency evaluator.
- **Permissions:** Compliance Administrator authors; Legal Approver activates; Site Administrator reads the effective policy and exceptions.
- **Surface:** dependency graph and compliance Script Report show bindings, declared regions, drift, exceptions, and expiry.

## Boundaries

Owns: residency policy versions, binding validation, and exception evidence. Consumes: declared service regions and site deployment inventory. Emits: allow, block, or exception decisions. Does not own: legal advice, physical infrastructure location, or data migration execution.

## Open questions

- How should transient support access and encrypted global control-plane metadata be classified?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Clinic Site Provisioning](openchart-feature-catalog-plt-001-clinic-site-provisioning.md) · [Cross-site Shared Services](openchart-feature-catalog-plt-002-cross-site-shared-services.md)
