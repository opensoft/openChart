# Patient-Facing Record Assistant — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Answers authenticated patient questions about authorized records, scheduling, and billing references with citations and bounded scope.
Topics: openchart-feature-catalog, clinical-ai, frappe, patient-assistant
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-019 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Proxy-aware conversation mode** — Explain whose record and authority scope govern each cited answer in a proxy session.

## Focus

This feature isolates a patient-facing retrieval assistant that explains existing information rather than practicing medicine.

## Behavior

- An authenticated patient or proxy asks a question within records, scheduling, or linked billing-reference scope.
- Answers cite portal-visible sources and identify source dates, missing information, and uncertainty.
- The assistant refuses diagnosis, treatment changes, emergency triage, unauthorized proxy data, and unsupported actions.
- Configured intents offer a human contact or create a reviewable escalation request.
- Conversation history follows consent and retention policy and is visible to the user where required.
- The assistant cannot schedule, cancel, pay, message clinicians, or change records without a separate confirmed workflow.

## Frappe realization

- **DocTypes:** `OC Patient Assistant Session` and child turns store actor, proxy authority, scope, citations, policy decisions, artifact Links, and escalation state.
- **Roles/permissions:** portal user and proxy user permissions filter retrieval; assistant service account cannot bypass portal-visible rules.
- **Hooks/API/surfaces:** portal page calls whitelisted scoped retrieval and response methods; Server Script policy checks precede adapter invocation; audit events record refusals.
- **Workflow:** Active → Escalated/Closed/Expired; each external action remains a separate confirmation flow.

## Boundaries

Owns: cited conversational answers and escalation initiation. Consumes: portal-authorized records and reference APIs. Emits: bounded answers or human-review requests. Does not own: clinical advice, scheduling transactions, billing, or record changes.

## Open questions

- Which patient questions should always escalate rather than receive a cited informational answer?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Assistant Escalation Triggers](openchart-feature-catalog-aic-020-assistant-escalation-triggers.md)
