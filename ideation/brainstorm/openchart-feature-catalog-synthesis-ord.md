# Synthesis: Orders CPOE And Decision Support — Brainstorm

Status: brainstorm
Kind: reference
Summary: Connects governed order entry, lifecycle authority, fulfillment, result accountability, and provenance-bearing human-approved decision support into a closed-loop clinical ordering domain.
Topics: openchart-feature-catalog, cpoe, frappe, synthesis, order-governance
Repository context: openChart — Frappe v15 native EMR; catalog entry ORD synthesis (Orders CPOE And Clinical Decision Support)
Captured: 2026-08-24

## Possible feats

- **Closed-loop order safety cockpit** — Combine order, fulfillment, result, follow-up, and CDS-governance signals without allowing the cockpit to take clinical action autonomously.

## Focus

This synthesis relates the ORD catalog's atomic capabilities into a Frappe-native clinical ordering system in which signed intent, fulfillment state, result responsibility, and decision-support evidence remain distinct but traceable.

## Members and their joints

### Order composition across fulfillment classes

- [Medication Order Entry](openchart-feature-catalog-ord-001-medication-order-entry.md), [Laboratory Order Entry](openchart-feature-catalog-ord-002-laboratory-order-entry.md), [Imaging Order Entry](openchart-feature-catalog-ord-003-imaging-order-entry.md), [Procedure Order Entry](openchart-feature-catalog-ord-004-procedure-order-entry.md), [Referral Order Entry](openchart-feature-catalog-ord-005-referral-order-entry.md), [Nursing Order Entry](openchart-feature-catalog-ord-006-nursing-order-entry.md), and [Diet Order Entry](openchart-feature-catalog-ord-007-diet-order-entry.md) share a submittable order envelope while retaining class-specific instructions.
- [Unified Multi-Class Order Composer](openchart-feature-catalog-ord-008-unified-multi-class-order-composer.md), [Batch Panel Order Entry](openchart-feature-catalog-ord-009-batch-panel-order-entry.md), [Order Search With Synonyms](openchart-feature-catalog-ord-010-order-search-with-synonyms.md), [Personal Order Favorites](openchart-feature-catalog-ord-011-personal-order-favorites.md), and [Diagnosis-Driven Order Suggestions](openchart-feature-catalog-ord-012-diagnosis-driven-order-suggestions.md) accelerate composition, but every generated item remains a reviewable draft requiring human approval.

### Organization content and reusable authority

- [Organization Order Set Library](openchart-feature-catalog-ord-013-organization-order-set-library.md), [Order Set Version Authoring](openchart-feature-catalog-ord-014-order-set-version-authoring.md), [Order Set Approval And Publishing](openchart-feature-catalog-ord-015-order-set-approval-and-publishing.md), and [Order Set Review Reminders](openchart-feature-catalog-ord-016-order-set-review-reminders.md) form a succession-based content lifecycle from authored draft through accountable retirement.
- [Verbal And Telephone Order Read-Back](openchart-feature-catalog-ord-017-verbal-telephone-order-readback.md), [Standing Protocol Activation](openchart-feature-catalog-ord-018-standing-protocol-activation.md), and [Standing Order Expiry Control](openchart-feature-catalog-ord-019-standing-order-expiry-control.md) make exceptional or reusable ordering authority explicit, time-bounded, and auditable.

### Order instructions and lifecycle control

- [PRN Order Capture](openchart-feature-catalog-ord-020-prn-order-capture.md), [Titration Order Instructions](openchart-feature-catalog-ord-021-titration-order-instructions.md), and [Order Duration And Auto-Stop](openchart-feature-catalog-ord-022-order-duration-and-auto-stop.md) convert discretionary, adjustable, and time-bounded instructions into structured constraints.
- [Order Renewal And Reorder](openchart-feature-catalog-ord-023-order-renewal-and-reorder.md), [Order Discontinuation With Reason](openchart-feature-catalog-ord-024-order-discontinuation-with-reason.md), and [Order Hold And Resume](openchart-feature-catalog-ord-025-order-hold-and-resume.md) preserve immutable accepted intent while lifecycle events or successors change operational eligibility.
- [Order Clarification Thread](openchart-feature-catalog-ord-026-order-clarification-thread.md), [External Order Import Reconciliation](openchart-feature-catalog-ord-027-external-order-import-reconciliation.md), [Fulfillment-Class Order Queues](openchart-feature-catalog-ord-028-fulfillment-class-order-queues.md), and [Order Dispatch Status Tracking](openchart-feature-catalog-ord-029-order-dispatch-status-tracking.md) connect signed intent to human and technical fulfillment without conflating transport, task, and clinical states.

### Ordering authority and accountability

- [Ordering Role Cosign Requirements](openchart-feature-catalog-ord-030-ordering-role-cosign-requirements.md), [Restricted Order Privileges](openchart-feature-catalog-ord-031-restricted-order-privileges.md), [Credential Expiry Ordering Guard](openchart-feature-catalog-ord-032-credential-expiry-ordering-guard.md), [High-Risk Order Dual Authorization](openchart-feature-catalog-ord-033-high-risk-order-dual-authorization.md), and [Delegated Order Attribution](openchart-feature-catalog-ord-034-delegated-order-attribution.md) distinguish entry, ordering, supervision, credential, and independent authorization roles.

### Closed-loop result responsibility

- [Result Accountability Record](openchart-feature-catalog-ord-035-result-accountability-record.md), [Result Owner Assignment And Transfer](openchart-feature-catalog-ord-036-result-owner-assignment-and-transfer.md), [Result Acknowledgment State](openchart-feature-catalog-ord-037-result-acknowledgment-state.md), [Result Escalation Ladder](openchart-feature-catalog-ord-038-result-escalation-ladder.md), and [Result Follow-Up Deadline](openchart-feature-catalog-ord-039-result-follow-up-deadline.md) make ownership, review, escalation, and completion separate explicit states.
- [Critical Result Acknowledgment Evidence](openchart-feature-catalog-ord-040-critical-result-acknowledgment-evidence.md), [Abnormal Result Worklists](openchart-feature-catalog-ord-041-abnormal-result-worklists.md), [On-Call Result Routing Pools](openchart-feature-catalog-ord-042-on-call-result-routing-pools.md), [Incidental Finding Follow-Up](openchart-feature-catalog-ord-043-incidental-finding-follow-up.md), and [Patient Result Notification Tracking](openchart-feature-catalog-ord-044-patient-result-notification-tracking.md) add urgency, coverage, longitudinal obligation, and communication evidence without treating inbox opening as clinical acknowledgment.

### CDS governance and runtime resolution

- [CDS Rule Registry](openchart-feature-catalog-ord-045-cds-rule-registry.md), [CDS Rule Version And Provenance](openchart-feature-catalog-ord-046-cds-rule-version-and-provenance.md), and [CDS Ownership And Review Lifecycle](openchart-feature-catalog-ord-047-cds-ownership-and-review-lifecycle.md) establish the provenance, succession, and accountable stewardship required before a rule can run.
- [Order-Time Alert Orchestration](openchart-feature-catalog-ord-048-order-time-alert-orchestration.md), [Drug-Drug Interaction Alerts](openchart-feature-catalog-ord-049-drug-drug-interaction-alerts.md), [Drug-Allergy Order Alerts](openchart-feature-catalog-ord-050-drug-allergy-order-alerts.md), [Duplicate Therapy Alerts](openchart-feature-catalog-ord-051-duplicate-therapy-alerts.md), and [Dose Range Checking](openchart-feature-catalog-ord-052-dose-range-checking.md) evaluate signed-intent candidates against active rules and exact patient context.
- [Non-Interruptive CDS Advisory Feed](openchart-feature-catalog-ord-053-non-interruptive-cds-advisory-feed.md), [Coded Alert Override Reasons](openchart-feature-catalog-ord-054-coded-alert-override-reasons.md), [CDS Override Analytics](openchart-feature-catalog-ord-055-cds-override-analytics.md), and [Allergy Override Documentation](openchart-feature-catalog-ord-056-allergy-override-documentation.md) separate non-blocking guidance, clinician resolution evidence, and governance feedback.

### Contextual guidance, evidence, and surveillance

- [Age Pregnancy And Lactation Safety Checks](openchart-feature-catalog-ord-057-age-pregnancy-lactation-safety-checks.md), [Renal Dose Adjustment Guidance](openchart-feature-catalog-ord-058-renal-dose-adjustment-guidance.md), [Formulary Checks At Order Time](openchart-feature-catalog-ord-059-formulary-checks-at-order-time.md), and [Order Selection Cost Transparency](openchart-feature-catalog-ord-060-order-selection-cost-transparency.md) present contextual facts and options without replacing prescriber judgment.
- [Evidence Citations For CDS Rules](openchart-feature-catalog-ord-061-evidence-citations-for-cds-rules.md) and [CDS Rule Testing Sandbox](openchart-feature-catalog-ord-062-cds-rule-testing-sandbox.md) make active guidance explainable and testable against synthetic cases.
- [Point-Of-Care Quality Gap Prompts](openchart-feature-catalog-ord-063-point-of-care-quality-gap-prompts.md), [Visit-Due Preventive Care Prompts](openchart-feature-catalog-ord-064-visit-due-preventive-care-prompts.md), and [Sepsis And Deterioration Surveillance Worklists](openchart-feature-catalog-ord-065-sepsis-deterioration-surveillance-worklists.md) turn registered rules into human-review work without autonomous diagnosis, ordering, outreach, or treatment.

## Emergent behavior

Together these features produce a closed-loop path from discoverable orderable content through attributed signature, permissioned fulfillment, result ownership, acknowledgment, follow-up, and rule-governance feedback. The loop is safer because clinical intent remains immutable, every rule firing pins provenance, technical delivery does not masquerade as completion, and every suggestion or surveillance signal terminates in a qualified human decision.

## Tensions to hold

- Fast order entry must not collapse the distinct validation, privilege, signature, and fulfillment semantics of each order class.
- Interruptive CDS can prevent harm but excessive or poorly targeted alerts create override fatigue; analytics inform human governance rather than automatic tuning.
- Coverage-aware result routing improves continuity, yet transfers must not create gaps where every pool assumes another owns the result.
- Cost and formulary context can support feasible care but must never suppress safety evidence or coerce clinical choice.
- Scheduled surveillance offers earlier visibility but must not be represented as real-time monitoring or autonomous clinical assessment.

## Recombination opportunities

- Combine order-set governance, rule citations, and synthetic testing into a single clinical-content release train with separate approval authorities.
- Join fulfillment queues, dispatch evidence, result accountability, and incidental-finding follow-up into service-line closed-loop dashboards.
- Reuse the same ownership, deadline, transfer, and escalation primitives for cosign, content review, result follow-up, and surveillance worklists while preserving their distinct permissions.
- Pair diagnosis suggestions, quality gaps, preventive prompts, and surveillance signals with the unified composer so accepted recommendations become ordinary drafts rather than privileged actions.

## Frappe realization

- **Core DocTypes:** use submittable `OC Clinical Order` and submitted lifecycle/evidence records; govern `OC Order Set`, `OC CDS Rule`, `OC Result Accountability`, and related child and event DocTypes with mandatory provenance and succession links.
- **Workflows:** separate Draft/Review/Approved/Active content lifecycles from Draft/Pending Signature/Active/Fulfillment/Completed order states and Assigned/Reviewed/Follow-Up/Completed accountability states.
- **Hooks:** `doc_events.validate/on_submit` on orders rerun privilege and active-rule checks; result `on_submit/on_update` creates or reopens accountability; no client-only check is authoritative.
- **Schedulers:** `scheduler_events` handle auto-stop, overdue cosign, result escalation, content review, credential expiry, evidence freshness, and surveillance scans idempotently, with visible exception reports.
- **APIs/worklists:** guarded `open_chart.api.v1.orders` methods are the supported write surface; allowlisted `/api/resource/...` filters for class, state, owner, pool, priority, and due range back permission-aware Desk worklists.
- **Roles/surfaces:** distinct prescriber, fulfillment, reviewer, publisher, credentialing, result-oversight, and surveillance roles use Frappe Workspaces, Query/Script Reports, Dashboard Charts, Notifications, Assignments, and websocket refresh events.

## Boundaries

Owns: clinical order intent, ordering authority evidence, order lifecycle, CDS artifacts and evaluations, fulfillment routing projections, and result accountability. Consumes: patient and encounter context, clinical statements, terminology, credentials, schedules, consent, results, formulary, and cost sources. Emits: signed orders, fulfillment work, alerts, human-approved drafts, acknowledgment evidence, escalation events, and governance analytics. Does not own: autonomous clinical action, dispensing, administration, diagnostic interpretation, staffing schedules, billing, claims, or external-system authority.

## Open questions

- Which shared event and provenance schema can support orders, results, rules, and accountability without flattening their distinct clinical meanings?
- Which safety failures must fail closed at signature, and which should produce explicit uncertainty plus an operational exception?
- How should organizations calibrate interruptive severity, overrideability, escalation timing, and surveillance cadence without weakening immutable baseline safeguards?

## Relationships

[OpenChart Feature Catalog](openchart-feature-catalog-overview.md)
