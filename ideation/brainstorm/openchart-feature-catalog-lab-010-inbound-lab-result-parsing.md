# Inbound Lab Result Parsing — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Parses inbound laboratory messages into a quarantined canonical result envelope while preserving every source value and raw payload reference.
Topics: openchart-feature-catalog, laboratory, frappe, inbound-interface
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-010 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Inbound Lab Result Parsing assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates transport-to-canonical parsing and source preservation as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Interface Operator supplies source payload, connector profile, sending facility, message identifiers, patient identifiers, accession, observations, and attachments.
- The system produces a parsed canonical envelope or explicit parse exception and exposes its current state to permitted users.
- The governed lifecycle is Received → Parsed → Validated or Quarantined; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Malformed segments, unsupported units, and unknown message versions are quarantined without partial chart filing.

## Frappe realization

- **DocTypes:** `OC Lab Inbound Message` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Received → Parsed → Validated or Quarantined; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Interface Operator` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.inbound_lab_result_parsing` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Inbound%20Message` reads and a Desk worklist or report.

## Boundaries

Owns: transport-to-canonical parsing and source preservation. Consumes: inbound payloads, connector versions, and terminology maps. Emits: a parsed canonical envelope or explicit parse exception. Does not own: patient matching, duplicate adjudication, or clinical filing.

## Open questions

- Which organization-level policy values and exception thresholds for inbound lab result parsing must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
