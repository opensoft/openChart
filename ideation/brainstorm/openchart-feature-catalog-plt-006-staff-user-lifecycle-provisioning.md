# Staff User Lifecycle Provisioning — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates approved staff onboarding, access changes, suspension, and deprovisioning with complete task evidence.
Topics: openchart-feature-catalog, platform, frappe, user-lifecycle
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-006 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Identity-provider reconciliation** — Compare approved access with external directory membership and open exceptions.

## Focus

This feature isolates the human-governed lifecycle around a Frappe User without replacing authentication or identity proofing.

## Behavior

- Managers request onboarding with identity, job function, sites, facilities, start date, and sponsor.
- Security administrators review proposed roles and user permissions before activation.
- Changes and transfers create a new reviewed access request rather than silently accumulating privileges.
- Suspension disables login and active API credentials while preserving assignments and audit evidence for reassignment.
- Deprovisioning inventories open work, delegations, ownership, tokens, and integration identities before closure.
- Partial failures remain visible as blocking checklist items and may be retried safely.

## Frappe realization

- **DocTypes:** `OC User Lifecycle Request` and child `OC Access Grant Request` track action, subject User, effective dates, requested roles, user permissions, tasks, and outcomes.
- **Workflow:** Manager → Security Review → Provisioning → Verification → Completed, with rejection and failed states.
- **Hooks/API:** whitelisted lifecycle methods call Frappe User and Role assignment services under a guard; `on_update` records per-step evidence.
- **Surface:** Security Administration workspace shows pending starts, transfers, suspensions, and incomplete deprovisioning.

## Boundaries

Owns: approval and execution record for staff access lifecycle. Consumes: identity, job function, site, and role templates. Emits: Frappe User changes and reassignment tasks. Does not own: HR employment records or external identity-provider accounts.

## Open questions

- Which emergency suspension actions may bypass normal approval and require retrospective review?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Job-function Role Templates](openchart-feature-catalog-plt-007-job-function-role-templates.md)
