# Waived Test Compliance Records — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Maintains competency, procedure, lot, environment, maintenance, and review evidence for waived testing programs.
Topics: openchart-feature-catalog, laboratory, frappe, waived-testing
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-045 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Waived Test Compliance Records assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates waived-testing evidence inventory and expiry monitoring as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC POCT Coordinator supplies site, assay, certificate reference, procedure version, staff competency, training, maintenance, lot checks, and review dates.
- The system produces a time-bounded compliance evidence set with visible gaps and exposes its current state to permitted users.
- The governed lifecycle is Draft → Reviewed → Active → Expiring → Expired or Renewed; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Expired competency, missing procedure acknowledgment, or overdue review produces a hold or exception according to local policy.

## Frappe realization

- **DocTypes:** `OC Waived Test Compliance Record` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Draft → Reviewed → Active → Expiring → Expired or Renewed; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC POCT Coordinator` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.waived_test_compliance_records` is the supported write method, with allowlisted `/api/resource/OC%20Waived%20Test%20Compliance%20Record` reads and a Desk worklist or report.

## Boundaries

Owns: waived-testing evidence inventory and expiry monitoring. Consumes: POCT operations, staff credentials, documents, lots, and site policy. Emits: a time-bounded compliance evidence set with visible gaps. Does not own: legal certification, regulator submission, or concealing noncompliance.

## Open questions

- Which organization-level policy values and exception thresholds for waived test compliance records must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
