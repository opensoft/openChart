# Referral Order Entry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures referrals with specialty, reason, urgency, destination constraints, and expected clinical response.
Topics: openchart-feature-catalog, cpoe, frappe, referral-orders
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-005 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Referral question templates** — Offer specialty-specific questions that remain editable before signature.

## Focus

This feature isolates the clinical request that initiates a referral.

## Behavior

- Clinicians specify specialty or service, reason, urgency, clinical question, destination preference, and requested completion window.
- Required supporting documents are listed and attached by reference rather than copied into the order.
- Internal and external destinations use the same clinical order state model.
- The signer can identify whether advice, consultation, transfer of care, or procedure is expected.
- An incomplete external destination routes to referral coordination after signature.
- Referral suggestions never select or transmit to a destination without human confirmation.

## Frappe realization

- **DocTypes:** submittable `OC Clinical Order` with order_class `Referral`; child `OC Referral Instruction` stores service, request type, destination, and attachment references.
- **Workflow:** Draft → Pending Signature → Active → Coordination → Sent → Response Received or Closed.
- **Roles/permissions:** `OC Ordering Clinician` submits; `OC Referral Coordinator` manages routing; patient-sensitive attachments obey source permissions.
- **Hooks/API/surface:** `on_submit` creates a coordinator assignment, guarded v1 methods manage transmission state, and REST filters expose overdue referral orders.

## Boundaries

Owns: referral intent and requested response. Consumes: patient context, directory choices, and referenced records. Emits: coordinatable referral request. Does not own: provider directory or referral scheduling.

## Open questions

- Which referral response types qualify the order as completed?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Result Follow-Up Deadline](openchart-feature-catalog-ord-039-result-follow-up-deadline.md)
