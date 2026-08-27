# Specimen Container And Handling Rules — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Resolves container, minimum volume, temperature, light protection, transport, processing, and stability requirements for each ordered test.
Topics: openchart-feature-catalog, laboratory, frappe, specimen-handling
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-049 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Specimen Container And Handling Rules assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates preanalytic specimen requirement content as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Catalog Manager supplies test, specimen, container, minimum volume, additives, handling steps, transport limits, stability, processing site, and effective dates.
- The system produces a versioned requirement set consumed at ordering, collection, routing, and accessioning and exposes its current state to permitted users.
- The governed lifecycle is Draft → Reviewed → Approved → Active → Retired; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Conflicting panel requirements identify required separate containers or route to review instead of merging unsafe instructions.

## Frappe realization

- **DocTypes:** `OC Specimen Requirement` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Draft → Reviewed → Approved → Active → Retired; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Catalog Manager` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.specimen_container_handling_rules` is the supported write method, with allowlisted `/api/resource/OC%20Specimen%20Requirement` reads and a Desk worklist or report.

## Boundaries

Owns: preanalytic specimen requirement content. Consumes: test catalog, laboratory methods, destination capabilities, and governance approvals. Emits: a versioned requirement set consumed at ordering, collection, routing, and accessioning. Does not own: collector performance assessment or external-lab acceptance decisions.

## Open questions

- Which organization-level policy values and exception thresholds for specimen container and handling rules must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
