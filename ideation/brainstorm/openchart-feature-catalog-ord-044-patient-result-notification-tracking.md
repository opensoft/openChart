# Patient Result Notification Tracking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Documents whether, when, how, and by whom result information and follow-up instructions were communicated to the patient or proxy.
Topics: openchart-feature-catalog, cpoe, frappe, result-notification
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD-044 (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Communication preference routing** — Present permitted channels and accessibility needs before staff contacts the patient.

## Focus

This feature isolates evidence of patient-facing result communication as part of follow-up accountability.

## Behavior

- Staff record recipient, proxy authority when applicable, channel, language or accommodation, time, content scope, and instructions.
- Automated portal release is distinguishable from confirmed communication and does not imply understanding.
- Unsuccessful attempts record outcome and next action without marking communication complete.
- Sensitive-result policies constrain recipient, channel, and visible content.
- The accountable clinician determines message content or approves a governed template before sending.
- Notification evidence links to the result version and follow-up plan.

## Frappe realization

- **DocTypes:** submitted `OC Result Communication` with accountability, result_version, recipient type, proxy reference, channel, outcome, template version, actor, and timestamp.
- **Workflow:** Planned → Attempted → Delivered/Confirmed or Failed/Escalated.
- **Roles/permissions:** `OC Clinical Communicator` records within consent and proxy permissions; sensitive fields use permlevel 1-2.
- **Hooks/API/surface:** guarded communication methods validate authority; Notifications may deliver approved content; REST filters expose failed and pending attempts.

## Boundaries

Owns: result-communication evidence. Consumes: approved message, consent, proxy authority, and follow-up plan. Emits: contact outcome and escalation. Does not own: portal release policy or clinical acknowledgment.

## Open questions

- When does delivery evidence count as communication versus requiring recipient confirmation?

## Relationships

[Synthesis: Orders CPOE And Decision Support](openchart-feature-catalog-synthesis-ord.md) · [Result Acknowledgment State](openchart-feature-catalog-ord-037-result-acknowledgment-state.md)
