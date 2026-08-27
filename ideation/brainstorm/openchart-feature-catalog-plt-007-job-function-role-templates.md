# Job-function Role Templates — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Packages reviewed roles, user permissions, workspaces, and access constraints into reusable job-function templates.
Topics: openchart-feature-catalog, platform, frappe, role-templates
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-007 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Least-privilege diff review** — Explain how a proposed template version changes effective access.

## Focus

This feature isolates governed access bundles while keeping Frappe Role Permission Manager and DocPerms authoritative.

## Behavior

- Security administrators define a job function, included roles, required site or facility scopes, workspace, and incompatible roles.
- Templates move through Draft, Review, Published, Retired, and Superseded states.
- Publishing validates that referenced roles and workspace assets exist and shows the effective permission delta.
- User lifecycle requests pin the published template version used for approval.
- Updating a template does not silently modify existing users; administrators choose reconcile, grandfather, or revoke actions.
- Conflicting or missing scopes block application with a precise remediation message.

## Frappe realization

- **DocTypes:** `OC Role Template` with version, status, Role Table MultiSelect, scope rules, workspace Link, and incompatible-role child rows.
- **Workflow:** Security Administrator authors; Security Approver publishes or retires.
- **Permissions:** custom DocPerms protect template mutation while Role Permission Manager remains the source for per-DocType rights.
- **Surface/API:** a Script Report previews effective grants; `open_chart.api.v1.platform.apply_role_template` requires an approved lifecycle request.

## Boundaries

Owns: versioned job-function bundles and reconciliation intent. Consumes: Frappe Roles, DocPerms, workspaces, and scopes. Emits: reviewed grant plans. Does not own: authentication or direct clinical authority.

## Open questions

- Should published templates be immutable or allow corrected metadata without a new version?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Staff User Lifecycle Provisioning](openchart-feature-catalog-plt-006-staff-user-lifecycle-provisioning.md) · [Role-specific Desk Workspace Builder](openchart-feature-catalog-plt-020-role-specific-desk-workspace-builder.md)
