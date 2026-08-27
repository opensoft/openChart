# Stuck Transaction Reconciliation Queue — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Queues laboratory transactions whose expected acknowledgment or downstream state has not arrived for accountable investigation and replay.
Topics: openchart-feature-catalog, laboratory, frappe, transaction-reconciliation
Repository context: openChart — Frappe v15 native EMR; catalog entry LAB-039 (Labs And Diagnostics)
Captured: 2026-08-24

## Possible feats

- **Stuck Transaction Reconciliation Queue assurance view** — Combine adoption, exception, and completion signals into a permission-aware operational view without automating clinical decisions.

## Focus

This feature isolates technical transaction recovery and evidence as one traceable laboratory capability with explicit clinical, operational, and technical boundaries.

## Behavior

- The OC Interface Operator supplies transaction, expected response, last known state, payload digest, retry history, external inquiry reference, and assignee.
- The system produces a resolved, replayed, cancelled, or externally confirmed reconciliation case and exposes its current state to permitted users.
- The governed lifecycle is Detected → Assigned → Investigating → Replayed, Resolved, or Escalated; each transition records actor, time, reason, and provenance.
- Draft data may be corrected before acceptance; accepted clinical evidence is immutable and later corrections use linked succession.
- Role and patient-context permissions apply to API, Desk, report, export, and notification surfaces consistently.
- Replay requires idempotency evidence and never creates a new clinical record merely to move a technical queue.

## Frappe realization

- **DocTypes:** `OC Lab Reconciliation Case` with naming series `LAB-.YYYY.-`, patient or order links as applicable, status, source identifiers, provenance, effective time, and `supersedes`; child tables hold repeating details without flattening source structure.
- **Workflow:** Frappe Workflow implements Detected → Assigned → Investigating → Replayed, Resolved, or Escalated; submitted clinical records use succession rather than in-place amendment.
- **Roles/permissions:** `OC Interface Operator` receives task-specific create or transition rights; `OC Lab Result Reviewer`, `OC Lab Administrator`, and patient-context User Permissions constrain review and configuration, with provenance fields at permlevel 1.
- **Hooks/API/surfaces:** server-side `validate` and `on_submit` enforce invariants; guarded `open_chart.api.v1.labs.stuck_transaction_reconciliation` is the supported write method, with allowlisted `/api/resource/OC%20Lab%20Reconciliation%20Case` reads and a Desk worklist or report.

## Boundaries

Owns: technical transaction recovery and evidence. Consumes: interface transactions, connector policies, acknowledgments, and external confirmations. Emits: a resolved, replayed, cancelled, or externally confirmed reconciliation case. Does not own: altering signed orders or filed results without clinical correction workflows.

## Open questions

- Which organization-level policy values and exception thresholds for stuck transaction reconciliation queue must be mandatory, and which may remain configurable?

## Relationships

[Synthesis: Labs And Diagnostics](openchart-feature-catalog-synthesis-lab.md)
