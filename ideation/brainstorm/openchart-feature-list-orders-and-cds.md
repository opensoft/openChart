# Clinical Orders And Decision Support — Brainstorm

Status: brainstorm
Kind: report
Summary: openChart should make closed-loop order and result accountability — ownership, acknowledgment, escalation, follow-up evidence — its CPOE differentiator, since OpenEMR has order plumbing but no accountable loop and the big-3 only partially close it.
Topics: openchart-feature-list, cpoe, competitive-research
Repository context: openChart — Frappe-native EMR foundation; feature research versus the OpenEMR baseline and the enterprise big-3 (Epic, Oracle Health, MEDITECH Expanse)
Captured: 2026-08-23

## Possible feats

- **Closed-loop results** — every result has an owning clinician, acknowledgment state, escalation path, and follow-up deadline with audit evidence.
- **Explainable CDS** — Best Practice Advisory-style alerts that carry rule identity, version, trigger rationale, and override reasons.
- **Governed order-set library** — organization-level protocols plus personal favorites, with content lifecycle and review dates.
- **Predictive surveillance** — deterioration/medication-safety worklists in the Expanse Surveillance pattern, feeding task queues rather than passive alerts.
- **AI-assisted order drafting** — ambient-conversation-derived order suggestions requiring explicit approval (Oracle Clinical AI Agent pattern).

## Focus

Which order-entry and decision-support capabilities turn openChart from a charting app into a system clinicians and safety officers trust with consequential clinical actions?

## Current state: OpenEMR baseline

OpenEMR provides procedure-order forms, lab ordering with electronic result collection, CAMOS ordering, a Clinical Decision Rules engine with physician/patient reminders and dated reminders, recall boards, care-gap logic, and ONC decision-support interventions. Effective content requires local configuration and measure packages; there is no explicit result-ownership model, no acknowledgment/escalation workflow, and alert fatigue complaints appear in usability research. Community reviews flag ineffective alerts as a recurring pain.

Sources: open-emr.org Features wiki; CDR User Manual; Release Features wiki; 2024 usability study (Sage/HFES).

## Enterprise gap candidates

- Epic Orders and Results unifies labs/imaging/meds/procedures/referrals with BestPractice Advisories interruptive CDS, results routing into In Basket pools, and deficiency workflows.
- MEDITECH Expanse Surveillance productizes predictive surveillance (medication safety, deterioration tracking) across settings.
- Oracle embeds Discern-rules heritage with patient-specific alerts during ordering, plus Clinical AI Agent order creation from ambient conversation (announced Feb 2026).
- Epic supports precision/genomic ordering returning discrete results through Aura rather than PDFs.
- None of the three publicly expose a simple, auditable "who owns this abnormal result and when did they acknowledge it" model — the loop closure remains implicit in worklists.

## Proposed feature set for openChart

Parity floor: unified order entry across med/lab/imaging/procedure/referral classes, order sets and favorites, configurable CDS rules, result routing. Adopted gaps: first-class Result Accountability object (owner, ack timestamp, escalation ladder, deadline, resolution evidence); CDS rule registry with versioning, provenance, and override analytics; surveillance worklists driven by registered rules; genomic test ordering with discrete-result return. Twist: alerts explain themselves (rule id, why fired, what to do) and every override feeds a measurable feedback report.

## Interfaces and boundaries

Consumes: patient context, signed documentation facts from clinical-documentation, result payloads from labs-and-diagnostics and imaging-workflows, drug checks from pharmacy-and-eprescribing. Emits: orders to fulfillment domains, charge hints to revenue-cycle, outcome signals to analytics-and-population-health. Owns the order/result accountability state machine; does not own fulfillment execution.

## Alternatives and tensions

Interruptive advisories drive compliance but also alert fatigue; non-interruptive surveillance worklists reduce interruptions but lose urgency. A strict accountability loop adds clicks clinicians resent unless ambient/AI assistance absorbs them. Predictive surveillance needs validated models — shipping unvalidated scores contradicts openChart's governance stance.

## Open questions

- Which result classes get mandatory acknowledgment first (critical labs? imaging findings?)?
- Is surveillance rule content built in-house, licensed, or community-contributed?
- Can escalation ladders stay configurable enough for clinic-scale buyers without becoming an integration project?

## Relationships

Clustered in [Synthesis: Clinical Core](openchart-feature-list-synthesis-clinical-core.md). Adjacent: [Labs And Diagnostics](openchart-feature-list-labs-and-diagnostics.md), [Imaging Workflows](openchart-feature-list-imaging-workflows.md), [Clinical AI And Governance](openchart-feature-list-clinical-ai.md).
