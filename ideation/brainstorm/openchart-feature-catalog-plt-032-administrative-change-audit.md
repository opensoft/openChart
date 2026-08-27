# Administrative Change Audit — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures searchable, tamper-evident evidence for configuration, privilege, operational, and platform changes made by administrators.
Topics: openchart-feature-catalog, platform, frappe, admin-audit
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-032 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Change review campaigns** — Periodically certify high-risk administrative changes and unresolved exceptions.

## Focus

This feature isolates audit of administration itself, including before/after metadata and delegated automation identity.

## Behavior

- Every governed administrative action records actor, effective identity, site, timestamp, action, target, reason, source, correlation ID, and outcome.
- Field-level diffs redact credentials and sensitive values while preserving that a protected value changed.
- Events are classified by risk and link to approvals, jobs, packages, or emergency justification.
- Auditors search by time, actor, target type, site, risk, outcome, and correlation without gaining target-record access.
- Corrections append a new explanatory event; administrators cannot edit or delete prior evidence.
- Missing audit emission for a required action fails the administrative operation closed where transactionally possible.

## Frappe realization

- **DocTypes:** `OC Administrative Audit Event` is append-only with immutable metadata, diff JSON, protected-value markers, parent correlation, and digest.
- **Hooks:** centralized service records `doc_events`, whitelisted API, scheduler, patch, fixture, permission, and deployment actions.
- **Permissions:** Audit Reviewer has read/report rights; Platform Administrator can emit but not alter events; export requires separate approval.
- **Surface:** Query Reports and timeline views correlate an asset, approval, job, and resulting changes.

## Boundaries

Owns: administrative action evidence and searchable correlation. Consumes: actor context, diffs, approvals, and job outcomes. Emits: immutable audit events and exception alerts. Does not own: clinical access audit or security incident adjudication.

## Open questions

- Which high-volume metadata actions should aggregate children while retaining record-level proof?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [API Key Lifecycle Administration](openchart-feature-catalog-plt-034-api-key-lifecycle-administration.md) · [Redacted Log Viewer](openchart-feature-catalog-plt-051-redacted-log-viewer.md)
