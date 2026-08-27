# Late-cancellation Fee Hooks — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Emits policy-backed, reviewable fee events when a cancellation falls inside a configured late window.
Topics: openchart-feature-catalog, scheduling, frappe, fee-hooks
Repository context: openChart — Frappe v15 native EMR; catalog entry SCH-016 (Scheduling And Patient Access)
Captured: 2026-08-24

## Possible feats

- **Hardship waiver intake** — Capture structured waiver requests before downstream financial action.

## Focus

This feature isolates the scheduling evidence and integration hook for a possible fee, not billing itself.

## Behavior

- Cancellation evaluation compares the event timestamp with the effective late-window policy.
- A qualifying event records appointment, policy version, actor, reason, notice interval, and suggested amount code.
- Exempt reasons and approved waivers suppress or reverse the hook with provenance.
- Staff can review Pending, Emitted, Waived, Rejected, and Reversed states.
- Duplicate cancellation callbacks cannot create duplicate fee events.
- Patients see applicable policy and review status without implying that openChart collected payment.

## Frappe realization

- **DocTypes:** `OC Scheduling Fee Event` with appointment, cancellation, policy_snapshot, external_key, state, and waiver evidence.
- **Workflow/API:** Pending Review → Emitted/Waived/Rejected → Reversed; a guarded outbound integration reads accepted events idempotently.
- **Hooks:** cancellation `on_update` creates the event; Notifications assign review without embedding sensitive financial details.

## Boundaries

Owns: fee-trigger evidence and state. Consumes: cancellation policy outcome. Emits: idempotent downstream fee event. Does not own: invoices, payment, claims, or collections.

## Open questions

- Which exemptions may be applied automatically versus requiring review?

## Relationships

[Synthesis: Scheduling And Patient Access](openchart-feature-catalog-synthesis-sch.md) · [Appointment Cancellation Policies](openchart-feature-catalog-sch-010-appointment-cancellation-policies.md)
