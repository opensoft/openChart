# Per-Site And Per-Role Enablement — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Controls each AI capability by tenant site, care location, role, workflow, and deployment state with fail-closed defaults.
Topics: openchart-feature-catalog, clinical-ai, frappe, capability-enablement
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-025 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Policy inheritance preview** — Show the effective enablement decision for a user and workflow before publishing changes.

## Focus

This feature isolates fine-grained activation policy from model configuration and user permissions.

## Behavior

- Site administrators view capabilities as Disabled, Shadow, Pilot, Active, Suspended, or Retired.
- Policies constrain care location, role, user cohort, workflow, hours, profile, model deployment, and maximum data classification.
- Effective policy is evaluated server-side on every invocation and displayed to authorized operators.
- Deny and kill-switch states override narrower allows; missing policy means Disabled.
- Policy edits require reason, effective time, approver, and immutable history.
- Enablement never grants source-data permission or clinical authority the user does not already hold.

## Frappe realization

- **DocTypes:** `OC AI Capability Policy` with capability, site, locations, roles, cohort, mode, component Links, data class, effective dates, and precedence.
- **Workflow:** Draft → Review → Approved → Scheduled/Active → Suspended/Retired.
- **Roles/permissions:** `OC Site AI Administrator` proposes; `OC AI Governor` approves Pilot or Active; bench multi-site keeps tenant policies isolated.
- **Hooks/API/surfaces:** invoke hook resolves effective policy; cache invalidates on update; Workspace matrix and Script Report explain policy decisions.

## Boundaries

Owns: capability activation and effective-policy resolution. Consumes: site, role, workflow, deployment, and kill-switch state. Emits: allow, shadow, or deny decisions. Does not own: underlying RBAC or clinical privileges.

## Open questions

- Which capabilities require dual approval before moving from Pilot to Active?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [AI Kill Switch And Incident Log](openchart-feature-catalog-aic-028-ai-kill-switch-and-incident-log.md)
