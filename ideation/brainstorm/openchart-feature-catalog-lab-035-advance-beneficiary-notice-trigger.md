# Advance Beneficiary Notice Trigger — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Flags laboratory orders that may require an Advance Beneficiary Notice and records completion evidence before affected transmission.
Topics: openchart-feature-catalog, laboratory, frappe, abn
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-035 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Advance Beneficiary Notice Trigger assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates ABN trigger and evidence linkage as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Lab Coordinator supplies order items, diagnosis links, coverage rules, frequency limits, patient choice, notice version, signature, and completion time.
- The system produces a documented required, not-required, completed, declined, or exception outcome and exposes its current state to permitted users.
- The governed lifecycle is Evaluate → Not Required, Required, Completed, Declined, or Review; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Rule uncertainty routes to benefits review; the system does not infer waiver or consent from a generic signature.

## Frappe realization

- **DocTypes:** `OC Lab ABN Check` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Evaluate → Not Required, Required, Completed, Declined, or Review; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Lab Coordinator` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.advance_beneficiary_notice_trigger` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20ABN%20Check` reads and a Desk worklist or report.

## Boundaries

Owns: ABN trigger and evidence linkage. Consumes: lab orders, diagnosis links, coverage policy, and notice records. Emits: a documented required, not-required, completed, declined, or exception outcome. Does not own: coverage determination, claims, billing, or legal advice.

## Open questions

- Which organization-level policy values and exception thresholds for advance beneficiary notice trigger must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
