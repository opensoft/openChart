# Clinical AI And Governance — Brainstorm

Status: brainstorm
Kind: report
Summary: openChart's sharpest differentiation is governed, pluggable clinical AI — ambient notes, order/coding drafts, inbox triage, patient assistant — with model provenance, human-review gates, and auditable artifacts as product features, against OpenEMR's two paid add-ons and the big-3's proprietary embedded AI.
Topics: openchart-feature-list, clinical-ai, competitive-research
Repository context: openChart — Frappe-native EMR foundation; feature research versus the OpenEMR baseline and the enterprise big-3 (Epic, Oracle Health, MEDITECH Expanse)
Captured: 2026-08-23

## Possible feats

- **AI artifact registry** — every AI output (note draft, suggested order, code suggestion, summary) is a typed object carrying model id/version, prompt/context reference, confidence, reviewer, decision, and amendment chain.
- **Pluggable model layer** — ambient capture, summarization, and drafting behind a vendor-neutral interface; clinics choose models (first-party, partner like Suki/Dragon-class, or self-hosted open weights) without workflow rewrites.
- **Human-gate enforcement** — consequential actions (orders, coding, denials, patient communications) structurally require confirmation; no autonomous clinical action by default.
- **Inbox triage drafting** — message/result reply drafts in In Basket-assistant style with measured acceptance rates.
- **AI interaction export** — Epic-style machine-readable log of which AI touched which encounter for audit/research.
- **Monitoring and disablement** — per-capability quality dashboards, drift alerts, kill switches scoped by role/site.

## Focus

How does openChart ship clinically powerful AI while making governance so structural that regulators, malpractice insurers, and skeptical clinicians prefer it to incumbent offerings?

## Current state: OpenEMR baseline

No core AI subsystem exists in OpenEMR 7.x. The 2026 module catalog lists exactly two optional paid services (~$65/month each): AI Chart Summary (specialty-tailored summaries insertable into notes) and browser voice-to-text (Chrome-only). No ambient documentation, no AI orders/coding/inbox assistance, no governance surface.

Sources: open-emr.org Modules catalog; Release Features wiki.

## Enterprise gap candidates

- Epic: Art ambient charting extracting diagnoses/orders into draft notes; nursing end-of-shift drafts (85% faster note claims); In Basket generative reply drafts; Draft Hospital Course; Cosmos point-of-care insights; Curiosity foundation models; KLAS shows adoption/impact varies sharply by workflow.
- Oracle Clinical AI Agent: ambient notes spanning ED/inpatient contexts using triage/labs/imaging/overnight events; order creation from conversation; professional-fee coding suggestions; dictation; chart review; announced nursing agent; agents share context across workflows (Feb–Aug 2026 announcements).
- MEDITECH: Expanse Navigator Google Health-powered search/summarization across structured/unstructured/scanned/handwritten/faxed data; Hospital Course Summary drafts; AI Nursing Handoff SBAR generation; MyHealth Assistant patient chatbot; AI denial appeal planning; no-show prediction; Ask Expanse clinician chatbot announced at HIMSS26.
- Gap in all three: none market AI-artifact-level provenance or pluggability as buyer-facing controls — governance is internal, not contractual.

## Proposed feature set for openChart

Parity floor: exceed OpenEMR's nothing-native with at least ambient notes + chart summary + inbox drafts at launch. Adopted gaps: the full registry/gating/monitoring feature set above; specialty-aware summarization; patient-assistant integration from patient-engagement; coding suggestions from revenue-cycle; finding-extraction surfacing from imaging-workflows. Twist: the pluggable-model contract is itself published and open-source — clinics can swap models without swapping EHRs, directly attacking incumbent lock-in and OpenEMR's per-module subscription tax simultaneously.

## Interfaces and boundaries

Consumes: context from every domain (documentation, orders, labs, financial events), consent state, transcript/audio streams from capture clients. Emits: typed AI artifacts into owning domains' review queues, telemetry to analytics-and-population-health, audit records to platform-and-security. Owns model orchestration and the artifact registry; never owns final clinical decisions.

## Alternatives and tensions

First-party models vs pure orchestration changes capital needs and liability posture. Ambient audio retention conflicts with minimum-necessary data principles — retention policy must be configurable per jurisdiction. Over-gating frustrates power users; under-gating invites regulatory/malpractice exposure. Model churn makes evaluation infrastructure (golden sets, regression harnesses) mandatory before any third-party plug-in ships.

## Open questions

- Which three AI capabilities justify v1 given evaluation-infrastructure cost?
- Is the pluggable contract versioned publicly from day one or stabilized internally first?
- What evidence threshold must a partner model pass before listing?

## Relationships

Clustered in [Synthesis: Intelligence Platform](openchart-feature-list-synthesis-intelligence-platform.md). Adjacent: [Clinical Documentation And Ambient Capture](openchart-feature-list-clinical-documentation.md), [Analytics And Population Health](openchart-feature-list-analytics-and-population-health.md), [Platform Security And Deployment](openchart-feature-list-platform-and-security.md).
