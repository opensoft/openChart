# Ordering Role Cosign Requirements — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies policy-based cosign obligations to orders entered by trainees, delegates, or other conditionally authorized roles.
Topics: openchart-feature-catalog, cpoe, frappe, order-cosign
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-030 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Supervisor load balancing** — Route cosign requests among eligible supervisors while preserving responsibility rules.

## Focus

This feature isolates determination, routing, and evidence of order cosign requirements.

## Behavior

- At signature, policy evaluates actor role, order class, care setting, risk, supervisor relationship, and urgency.
- The order displays whether it may activate before cosign and the due deadline.
- Eligible cosigners review the complete signed order and accept, reject, or request a successor correction.
- A cosigner cannot silently edit the originator's order.
- Overdue cosigns escalate to an eligible pool and remain visible on accountability reports.
- Originator, cosigner identity, timestamps, policy version, and decision are retained.

## Frappe realization

- **DocTypes:** `OC Order Cosign Requirement` links order, policy, originator, eligible pool, due_at, decision, and evidence.
- **Workflow:** Required → Assigned → Cosigned, Rejected, or Escalated; order activation behavior is policy-driven.
- **Roles/permissions:** originators read their requirements; `OC Order Cosigner` acts only when credential and supervision checks pass.
- **Hooks/API/surface:** order `on_submit` creates requirements; hourly scheduler escalates overdue items; REST filters by cosigner/state/due_at feed a worklist.

## Boundaries

Owns: cosign obligation and attestation evidence. Consumes: role, supervision, risk, and policy context. Emits: cosign decisions and escalations. Does not own: credential issuance.

## Open questions

- Which orders may activate while cosign remains pending?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Restricted Order Privileges](openchart-feature-catalog-ord-031-restricted-order-privileges.md)
