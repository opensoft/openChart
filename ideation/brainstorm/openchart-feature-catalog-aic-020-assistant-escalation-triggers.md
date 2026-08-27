# Assistant Escalation Triggers — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies versioned rules that stop assistant automation and route risky, uncertain, or requested interactions to accountable humans.
Topics: openchart-feature-catalog, clinical-ai, frappe, assistant-escalation
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-020 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Escalation coverage simulation** — Replay synthetic conversations to reveal missed and excessive routes before rule activation.

## Focus

This feature isolates deterministic and model-assisted escalation decisions across clinician and patient assistants.

## Behavior

- Governed triggers cover emergency language, self-harm, abuse, medication change, identity uncertainty, repeated failure, low confidence, and explicit human requests.
- A matching trigger stops generation or marks the draft non-actionable and creates an escalation with reason and priority.
- The user receives clear next-step language appropriate to the channel without claims that a clinician has reviewed it.
- Assignment follows configured human pools and deadlines; technical delivery is distinct from acknowledgment.
- Reviewers resolve false positives and missed-trigger reports for evaluation.
- No model can override a deterministic mandatory trigger.

## Frappe realization

- **DocTypes:** `OC AI Escalation Rule` and `OC AI Escalation` store versioned criteria, priority, destination pool, deadlines, source interaction, assignments, and resolution.
- **Workflow:** rule Draft → Tested → Approved → Active → Retired; escalation New → Assigned → Acknowledged → Resolved.
- **Roles/permissions:** `OC AI Safety Reviewer` governs rules; destination teams see only authorized source context.
- **Hooks/jobs/surfaces:** pre/post-generation hooks evaluate rules; Assignment Rules and Notifications route work; scheduler_events escalate overdue items; Kanban supports resolution.

## Boundaries

Owns: escalation policy evaluation and accountable work routing. Consumes: interaction signals, confidence, and site rules. Emits: stopped automation and human tasks. Does not own: emergency services, clinical triage, or resolution content.

## Open questions

- Which escalation classes require synchronous acknowledgment before the user session can close?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [Structural Human-Review Gates](openchart-feature-catalog-aic-036-structural-human-review-gates.md)
