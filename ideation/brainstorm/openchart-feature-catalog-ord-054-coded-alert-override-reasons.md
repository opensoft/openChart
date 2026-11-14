# Coded Alert Override Reasons — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Requires policy-appropriate coded rationale and optional narrative when a clinician proceeds despite an interruptive CDS alert.
Topics: openchart-feature-catalog, cpoe, frappe, alert-overrides
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-054 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Rule-specific reason sets** — Tailor allowed reasons and required supporting fields to each alert class.

## Focus

This feature isolates accountable resolution of overrideable interruptive alerts.

## Behavior

- The clinician chooses from an approved reason set and enters narrative when the selected reason requires it.
- Available reasons depend on rule type, severity, role, and care setting.
- Non-overrideable policy blocks have no override control and provide an escalation route.
- Override confirmation repeats the alert, intended order, and accountable signer.
- Changing the draft after override reruns CDS and invalidates stale override evidence.
- The final order links the exact evaluation, rule version, reason code, narrative, identity, and time.

## Frappe realization

- **DocTypes:** `OC CDS Override Reason` governs code, label, applicability, narrative_required, and status; submitted `OC CDS Override` links evaluation and order.
- **Workflow:** reason Draft → Approved → Active → Retired; override is submitted evidence, not editable state.
- **Roles/permissions:** `OC CDS Governance` manages reasons; only the signing clinician records their override.
- **Hooks/API/surface:** guarded override method validates current order digest and reason applicability; `on_submit` rejects missing or stale required evidence.

## Boundaries

Owns: override rationale vocabulary and evidence. Consumes: current alert, order, clinician, and policy. Emits: valid override token for signature. Does not own: alert logic or appropriateness judgment.

## Open questions

- Which override reasons should always require narrative or second review?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [CDS Override Analytics](openchart-feature-catalog-ord-055-cds-override-analytics.md)
