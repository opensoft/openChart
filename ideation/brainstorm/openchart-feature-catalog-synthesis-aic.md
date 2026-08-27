# Synthesis: Clinical AI And Governance — Brainstorm

Status: brainstorm
Kind: reference
Summary: Connects useful clinical AI drafting, retrieval, scoring, and back-office assistance to provenance, evaluation, privacy, operational control, and non-bypassable human authority.
Topics: openchart-feature-catalog, clinical-ai, frappe, synthesis, ai-governance
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC synthesis (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Governed clinical AI control plane** — Combine artifact lineage, model evidence, deployment controls, human gates, monitoring, incident response, and transparent change communication without granting AI autonomous clinical authority.

## Focus

This synthesis relates the AIC catalog into a Frappe-native operating model where AI may summarize, draft, classify, retrieve, or score, but every consequential transition remains an attributable human decision under ordinary clinical authority.

## Members and their joints

### Artifact, invocation, model, and evidence foundation

- [AI Artifact Registry](openchart-feature-catalog-aic-001-ai-artifact-registry.md), [Pluggable Model Adapter Contract](openchart-feature-catalog-aic-002-pluggable-model-adapter-contract.md), and [Prompt And Context Audit Capture](openchart-feature-catalog-aic-021-prompt-context-audit-capture.md) create the shared output, provider-neutral invocation, and replay evidence envelope for every capability.
- [Explainability And Input Panel](openchart-feature-catalog-aic-038-explainability-and-input-panel.md) presents that evidence to authorized reviewers, while [AI Artifact Amendment And Retraction](openchart-feature-catalog-aic-049-ai-artifact-amendment-retraction.md) preserves corrections and routes downstream impact without rewriting history.

### Ambient, documentation, and clinician drafting

- [Consent-Gated Ambient Capture](openchart-feature-catalog-aic-003-consent-gated-ambient-capture.md), [Ambient Note Review Queue](openchart-feature-catalog-aic-004-ambient-note-review-queue.md), and [Sentence-Level Transcript Provenance](openchart-feature-catalog-aic-005-sentence-level-transcript-provenance.md) form a consent-first path from visible capture to source-verifiable note draft and clinician signature.
- [Specialty Summarization Profiles](openchart-feature-catalog-aic-006-specialty-summarization-profiles.md), [Pre-Visit Chart Summary](openchart-feature-catalog-aic-007-pre-visit-chart-summary.md), [Abnormal Results Narrative](openchart-feature-catalog-aic-010-abnormal-results-narrative.md), [Hospital Course And Discharge Draft](openchart-feature-catalog-aic-011-hospital-course-discharge-draft.md), and [Nursing SBAR Handoff Draft](openchart-feature-catalog-aic-012-nursing-sbar-handoff-draft.md) use versioned profiles, freshness, citations, and role-specific review rather than a universal opaque summarizer.
- [Human-Approved Order Suggestions](openchart-feature-catalog-aic-013-human-approved-order-suggestions.md), [Coding Suggestions With Citations](openchart-feature-catalog-aic-014-coding-suggestions-with-citations.md), [Documentation-Gap Nudges](openchart-feature-catalog-aic-015-documentation-gap-nudges.md), and [AI-Assisted Chart-Prep Checklist](openchart-feature-catalog-aic-016-ai-assisted-chart-prep-checklist.md) accelerate preparation and candidate generation while preserving distinct order, coding, signature, and task authorities.

### Patient, inbox, analytics, and back-office assistance

- [Patient-Friendly Explanation Drafts](openchart-feature-catalog-aic-008-patient-friendly-explanation-drafts.md), [In Basket Reply Drafting](openchart-feature-catalog-aic-009-in-basket-reply-drafting.md), [Patient-Facing Record Assistant](openchart-feature-catalog-aic-019-patient-facing-record-assistant.md), and [Assistant Escalation Triggers](openchart-feature-catalog-aic-020-assistant-escalation-triggers.md) connect source-cited communication with separate send, release, transaction, and escalation controls.
- [Duplicate-Record Detection Assist](openchart-feature-catalog-aic-017-duplicate-record-detection-assist.md) and [Natural-Language Report Drafting](openchart-feature-catalog-aic-018-natural-language-report-drafting.md) support reconciliation candidates and bounded analytics without silent merges, unrestricted SQL, or automatic publication.
- [Scanned-Document Indexing Review](openchart-feature-catalog-aic-040-scanned-document-indexing-review.md) and [Imported-Data Normalization Review](openchart-feature-catalog-aic-041-imported-data-normalization-review.md) place extraction and normalization into back-office queues where raw imports remain immutable and humans approve searchable or normalized projections.

### Evaluation, feedback, fairness, and clinical model evidence

- [Model Evaluation Case Registry](openchart-feature-catalog-aic-022-model-evaluation-case-registry.md), [Model Regression Scoring Runs](openchart-feature-catalog-aic-023-model-regression-scoring-runs.md), and [Correction Feedback For Evaluation](openchart-feature-catalog-aic-037-correction-feedback-for-evaluation.md) create a controlled loop from synthetic or de-identified golden cases through repeatable scoring and curated corrections, explicitly excluding silent retraining.
- [Shadow-Mode Deployment](openchart-feature-catalog-aic-024-shadow-mode-deployment.md) gathers non-user-facing production evidence before activation, while [AI Drift Monitoring](openchart-feature-catalog-aic-026-ai-drift-monitoring.md), [Stratified Bias Monitoring](openchart-feature-catalog-aic-027-stratified-bias-monitoring.md), and [Clinician Acceptance And Edit Analytics](openchart-feature-catalog-aic-050-clinician-acceptance-edit-analytics.md) monitor quality proxies, disparities, and workflow burden without confusing adoption with safety.
- [Clinical Risk Model Serving](openchart-feature-catalog-aic-042-clinical-risk-model-serving.md), [Clinical Model Validation Evidence](openchart-feature-catalog-aic-043-clinical-model-validation-evidence.md), and [Fairness Review Release Gate](openchart-feature-catalog-aic-044-fairness-review-release-gate.md) bind each score to exact intended-use, population, validation, equity, and human-response evidence.

### Privacy, deployment, enablement, and runtime operations

- [Per-Site And Per-Role Enablement](openchart-feature-catalog-aic-025-per-site-per-role-enablement.md), [PHI Boundary Controls](openchart-feature-catalog-aic-034-phi-boundary-controls.md), [Transcript And Audio Retention Policy](openchart-feature-catalog-aic-035-transcript-audio-retention-policy.md), and [Structural Human-Review Gates](openchart-feature-catalog-aic-036-structural-human-review-gates.md) jointly resolve who may invoke a capability, what data may cross the boundary, how long sensitive media remains, and which promotions are impossible without humans.
- [Bring-Your-Own-Model Onboarding](openchart-feature-catalog-aic-031-bring-your-own-model-onboarding.md), [Self-Hosted Open-Weights Profile](openchart-feature-catalog-aic-032-self-hosted-open-weights-profile.md), and [Vendor Model Certification Registry](openchart-feature-catalog-aic-033-vendor-model-certification-registry.md) support deployment choice while demanding exact-version validation and evidence rather than trusting hosting mode or vendor brand.
- [Model Endpoint Credential Health](openchart-feature-catalog-aic-047-model-endpoint-credential-health.md) and [Inference Latency And Fallback Policy](openchart-feature-catalog-aic-048-inference-latency-and-fallback-policy.md) keep endpoint identity, credentials, queues, timeouts, and substitutions observable and unable to weaken clinical gates.

### Accountability, containment, cost, and change

- [AI Kill Switch And Incident Log](openchart-feature-catalog-aic-028-ai-kill-switch-and-incident-log.md) supplies immediate fail-closed containment, while [AI Incident Response Workflow](openchart-feature-catalog-aic-046-ai-incident-response-workflow.md) traces impacts and coordinates human correction, recovery validation, and learning.
- [AI Interaction Export Feed](openchart-feature-catalog-aic-029-ai-interaction-export-feed.md) provides machine-readable oversight evidence and [AI Cost And Usage Metering](openchart-feature-catalog-aic-030-ai-cost-and-usage-metering.md) makes resource consumption accountable without exposing clinical payloads.
- [Confidence-Threshold Routing](openchart-feature-catalog-aic-039-confidence-threshold-routing.md) sends uncertain outputs to stricter review, and [Clinician AI Change Newsletter](openchart-feature-catalog-aic-045-clinician-ai-change-newsletter.md) makes model, prompt, policy, evidence, and fallback changes visible to affected users.

## Emergent behavior

Together these features create an evidence-bearing clinical AI control plane rather than a collection of privileged agents. A capability begins with exact-version model, adapter, profile, data-boundary, evaluation, fairness, and enablement evidence; produces an immutable artifact with prompt/context provenance; enters a confidence-aware human workflow; and generates review, cost, drift, bias, correction, export, and incident signals. Clinical value comes from reducing synthesis and preparation burden while the hard differentiator remains structural: models cannot sign, send, order, merge, diagnose, reconcile, discharge, or otherwise perform consequential clinical actions autonomously.

## Tensions to hold

- Rich prompt and source retention improves replay and incident analysis but increases PHI exposure and conflicts with media minimization and jurisdictional disposal duties.
- More citations and explanation can improve reviewer verification while also adding cognitive load and risking false confidence in model-generated rationales.
- Shadow evidence and acceptance analytics improve local understanding, yet production outcomes are confounded and adoption is not correctness.
- Per-site customization supports local law and workflow but can fragment safety baselines, validation scope, and clinician expectations.
- Fallback models improve availability but may change quality, bias, cost, and data residency; manual completion is often the safer fallback.
- Strong human gates prevent autonomous harm but poorly designed review can become ceremonial automation bias rather than meaningful judgment.

## Recombination opportunities

- Combine artifact lineage, sentence evidence, explanation, corrections, interaction export, and incident tracing into a single reviewer-to-auditor provenance graph.
- Join golden cases, correction curation, regression runs, shadow deployment, drift, equity, and acceptance analytics into a release evidence dossier with separately accountable approvals.
- Reuse enablement, PHI boundary, retention, endpoint health, runtime fallback, and kill-switch decisions as a common invocation policy pipeline across every model adapter.
- Pair profile governance, source freshness, confidence routing, and human-review policies to create role-specific drafting experiences without duplicating safety logic.
- Connect change newsletters, evidence expiry, incident lessons, and monitored fairness conditions into a clinician-visible AI change management calendar.

## Frappe realization

- **Core DocTypes:** use submittable `OC AI Artifact`, immutable `OC AI Invocation`, versioned model/adapter/profile/policy/evidence registries, and separate review, correction, evaluation, monitoring, export, and incident DocTypes with succession links.
- **Workflows:** separate model/content/policy approval, generated-artifact review, fairness and validation release gates, shadow-to-active enablement, escalation, incident recovery, and media disposal; no AI service role receives submit authority on consequential clinical DocTypes.
- **Hooks:** central server-side invocation hooks resolve kill switch → enablement → source permission → PHI boundary → model eligibility → runtime policy, while destination `validate/on_submit` enforces human decisions and current artifact digests.
- **Background jobs:** dedicated rq queues handle ambient processing, summaries, evaluations, shadow runs, indexing, normalization, exports, monitoring, retention, health probes, and impact tracing with idempotency, bounded retries, and visible dead-letter reports.
- **Server scripts and registries:** allow governed Server Scripts only for bounded local deterministic checks and routing; model, prompt, adapter, certification, validation, fairness, confidence, retention, and runtime rules remain versioned DocType registries rather than hidden code or vendor configuration.
- **Surfaces:** permission-aware Desk Workspaces, Kanban review queues, Assignments, Notifications, Script/Query Reports, Dashboard Charts, Number Cards, print-format evidence dossiers, portal citation panels, and websocket job status make governance operationally visible.

## Boundaries

Owns: AI artifacts, invocation provenance, model and policy registries, evaluation evidence, deployment controls, human-review enforcement, monitoring, audit export, and incident coordination. Consumes: permissioned clinical records, encounter and communication context, consent and authority, terminology, demographics under approved purpose, site/role policy, provider evidence, and human decisions. Emits: cited drafts, informational scores, review and escalation work, normalized back-office candidates, evaluation and monitoring evidence, usage records, audit feeds, and incident actions. Does not own: autonomous clinical action, diagnosis, treatment, ordering authority, signature, discharge, patient communication delivery, identity merge, billing, claims, or silent retraining.

## Open questions

- Which baseline human-gate, privacy, evaluation, fairness, and incident controls must remain nonconfigurable across every openChart site?
- How should shared artifact and invocation schemas support generative text, extraction, classification, and numerical risk scores without erasing their distinct uncertainty semantics?
- What independent evidence is sufficient to advance each capability class from shadow to pilot and from pilot to active?

## Relationships

[OpenChart Feature Catalog](https://github.com/opensoft/openChart/tree/main/ideation/brainstorm)
