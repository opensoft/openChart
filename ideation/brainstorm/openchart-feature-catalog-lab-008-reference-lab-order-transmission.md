# Reference Lab Order Transmission — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Transmits signed laboratory orders and required demographics electronically to external reference laboratories with message-level delivery evidence.
Topics: openchart-feature-catalog, laboratory, frappe, outbound-interface
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-008 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Reference Lab Order Transmission assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates outbound payload generation and transport state as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Interface Operator supplies signed order, destination profile, patient identifiers, ordered tests, diagnosis links, specimen data, and protocol credentials.
- The system produces a version-pinned outbound payload and transport acknowledgment and exposes its current state to permitted users.
- The governed lifecycle is Queued → Sending → Acknowledged, Rejected, or Reconciliation Required; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Timeouts and negative acknowledgments retry only under configured idempotency rules and otherwise enter reconciliation.

## Frappe realization

- **DocTypes:** `OC Lab Outbound Transaction` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Queued → Sending → Acknowledged, Rejected, or Reconciliation Required; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Interface Operator` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.reference_lab_order_transmission` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Outbound%20Transaction` reads and a Desk worklist or report.

## Boundaries

Owns: outbound payload generation and transport state. Consumes: lab orders, connector profiles, patient identity, and consent policy. Emits: a version-pinned outbound payload and transport acknowledgment. Does not own: the external laboratory's order acceptance or test performance.

## Open questions

- Which organization-level policy values and exception thresholds for reference lab order transmission must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
