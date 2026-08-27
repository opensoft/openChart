# Chart Transfer Between Facilities — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates an authorized patient-chart responsibility transfer between facilities while preserving identifiers, provenance, and access boundaries.
Topics: openchart-feature-catalog, registration, frappe, facility-transfer
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-045 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Transfer readiness preview** — Inventory identity, consent, restriction, and external-link blockers before approval.

## Focus

Move or extend registration authority across facility boundaries without treating bench multi-site databases as one unrestricted chart.

## Behavior

- Authorized staff request transfer with source facility, destination, reason, scope, requested date, and patient authority basis.
- The system inventories identifiers, privacy flags, active care responsibility, and records eligible for transfer or reference.
- Source and destination reviewers approve independently before any access or identifier changes.
- Conflicting destination identity candidates block execution and route to identity review.
- Completion records retained source authority, destination authority, aliases, and every transferred or excluded artifact.
- Failure leaves both facility records in their prior state and creates a reconciliation work item.

## Frappe realization

- **DocTypes:** `OC Chart Transfer Request` and child `OC Transfer Artifact Decision` with source_site, destination_site, authority, scope, and outcomes.
- **Workflow:** Draft → Source Review → Destination Review → Approved → Executing → Completed, Failed, or Rejected.
- **Roles/permissions:** `OC Facility Registrar` approves locally; `OC Privacy Officer` clears restrictions; cross-site service identity has narrow API permission.
- **API/surfaces:** signed `open_chart.api.v1.registration.export_transfer_package` and `.accept_transfer`; transfer workspace and reconciliation report.

## Boundaries

Owns: facility transfer request, approvals, and registration-level reconciliation. Consumes: patient authority, restrictions, and artifact inventory. Emits: signed transfer package and audit. Does not own: universal cross-site data replication.

## Open questions

- When should facilities share one patient identity versus maintain linked local records?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
