# Lab Catalog Import And Update Management — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Imports external laboratory catalogs into staged diffs for mapping, review, approval, activation, and retirement.
Topics: openchart-feature-catalog, laboratory, frappe, catalog-management
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-042 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Lab Catalog Import And Update Management assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates orderable catalog ingestion and version lifecycle as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Catalog Manager supplies source file or feed, connector, test codes, names, panels, specimens, methods, preparation, pricing metadata, and effective dates.
- The system produces a reviewed catalog version with accepted, rejected, and unresolved changes and exposes its current state to permitted users.
- The governed lifecycle is Uploaded → Parsed → Diff Review → Approved → Activated or Rejected; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Removed tests, code reuse, panel reshaping, and changed specimen requirements cannot silently alter signed historical orders.

## Frappe realization

- **DocTypes:** `OC Lab Catalog Import` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Uploaded → Parsed → Diff Review → Approved → Activated or Rejected; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Catalog Manager` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.lab_catalog_import_management` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Catalog%20Import` reads and a Desk worklist or report.

## Boundaries

Owns: orderable catalog ingestion and version lifecycle. Consumes: external catalogs, connector profiles, terminology maps, and governance approvals. Emits: a reviewed catalog version with accepted, rejected, and unresolved changes. Does not own: vendor contract interpretation or automatic clinical substitution.

## Open questions

- Which organization-level policy values and exception thresholds for lab catalog import and update management must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
