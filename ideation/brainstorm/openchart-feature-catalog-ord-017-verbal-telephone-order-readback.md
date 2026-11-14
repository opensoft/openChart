# Verbal And Telephone Order Read-Back — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records verbal or telephone orders with receiver transcription, mandatory read-back evidence, and timely prescriber authentication.
Topics: openchart-feature-catalog, cpoe, frappe, verbal-orders
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-017 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Read-back phrase checklist** — Prompt the receiver through high-risk fields without recording audio.

## Focus

This feature isolates accountable entry of orders communicated outside direct prescriber entry.

## Behavior

- An authorized receiver identifies the prescriber, communication mode, time, order details, and clinical urgency.
- Submission requires the receiver to attest that the complete order was read back and confirmed.
- The order is visibly marked verbal or telephone and enters a pending-authentication state.
- CDS and privilege checks run before activation; hard policy failures prevent activation and trigger escalation.
- The named prescriber reviews, authenticates, corrects by succession, or rejects within a configured deadline.
- Identity, timestamps, read-back attestation, and all later actions remain immutable evidence.

## Frappe realization

- **DocTypes:** submittable `OC Clinical Order` includes communication_mode, received_by, ordered_by, read_back_confirmed, read_back_at, auth_due_at, and provenance.
- **Workflow:** Draft → Read-Back Confirmed → Active Pending Authentication → Authenticated or Rejected/Escalated.
- **Roles/permissions:** `OC Verbal Order Receiver` enters; named `OC Prescriber` authenticates; sensitive evidence is permlevel 2 read-only after submit.
- **Hooks/API/surface:** `validate` enforces read-back fields, `on_submit` runs CDS, and hourly scheduler events escalate overdue authentication through a filtered worklist.

## Boundaries

Owns: communication and read-back evidence. Consumes: prescriber identity, receiver authority, and order schema. Emits: active pending-authentication order. Does not own: communication systems or audio recording.

## Open questions

- Which order classes may activate before prescriber authentication?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Ordering Role Cosign Requirements](openchart-feature-catalog-ord-030-ordering-role-cosign-requirements.md)
