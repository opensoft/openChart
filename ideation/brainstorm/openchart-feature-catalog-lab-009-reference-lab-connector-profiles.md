# Reference Lab Connector Profiles — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Maintains versioned Quest-, Labcorp-, and peer-class connector mappings without embedding vendor-specific assumptions in core laboratory records.
Topics: openchart-feature-catalog, laboratory, frappe, connector-profiles
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-009 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Reference Lab Connector Profiles assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates external-lab transport and mapping configuration as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Interface Administrator supplies endpoint, protocol, credentials reference, identifier namespaces, code maps, acknowledgment rules, and activation dates.
- The system produces an approved connector version used by inbound and outbound transactions and exposes its current state to permitted users.
- The governed lifecycle is Draft → Tested → Approved → Active → Retired; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Credential or mapping changes create successors; active transactions remain pinned to the version that processed them.

## Frappe realization

- **DocTypes:** `OC Lab Connector Profile` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Draft → Tested → Approved → Active → Retired; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Interface Administrator` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.reference_lab_connector_profiles` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Connector%20Profile` reads and a Desk worklist or report.

## Boundaries

Owns: external-lab transport and mapping configuration. Consumes: organization secrets management, terminology maps, and interface policy. Emits: an approved connector version used by inbound and outbound transactions. Does not own: vendor contracts, vendor code, or external system authority.

## Open questions

- Which organization-level policy values and exception thresholds for reference lab connector profiles must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
