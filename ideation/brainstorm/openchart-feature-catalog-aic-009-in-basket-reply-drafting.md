# In Basket Reply Drafting — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Drafts source-cited replies to inbound clinical messages while measuring human acceptance and edits before any send action.
Topics: openchart-feature-catalog, clinical-ai, frappe, reply-drafting
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-009 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Draft pattern library** — Promote repeatedly useful, reviewed response structures into governed templates rather than retraining silently.

## Focus

This feature isolates message reply assistance with explicit human send authority.

## Behavior

- An authorized inbox user requests a draft for one inbound thread and selected chart context.
- The draft identifies source records, uncertainty, and any question it could not answer.
- Users may edit, accept, reject, or regenerate and may record a rejection reason.
- Send remains a separate user action under ordinary messaging permissions and recipient checks.
- Emergency language, medication change requests, and configured high-risk topics route to human-only handling without a send-ready draft.
- Acceptance, edit distance, elapsed review time, and disposition are recorded without treating acceptance as clinical correctness.

## Frappe realization

- **DocTypes:** `OC AI Message Draft` links communication thread, selected context, artifact, reviewer, disposition, edit metrics, and final message reference.
- **Workflow:** Requested → Ready → In Review → Accepted/Rejected; Accepted does not equal Sent.
- **Roles/permissions:** inbox assignment and patient user permissions govern access; AI service role cannot create outbound messages.
- **Hooks/API/surfaces:** whitelisted request method; message composer client script displays citations and risk flags; `on_submit` of outbound message records final comparison.

## Boundaries

Owns: reply draft, review disposition, and acceptance analytics. Consumes: inbound message and permissioned context. Emits: reviewer-approved candidate text and metrics. Does not own: message delivery, triage authority, or clinical decisions.

## Open questions

- Which high-risk intents should suppress drafting entirely versus allow a non-sendable summary for staff?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Assistant Escalation Triggers](openchart-feature-catalog-aic-020-assistant-escalation-triggers.md)
