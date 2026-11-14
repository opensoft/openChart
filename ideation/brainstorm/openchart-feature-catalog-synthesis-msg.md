# Synthesis: Messaging Tasks Notifications And Reminders — Brainstorm

Status: brainstorm
Kind: reference
Summary: Connects accountable staff work, closed-loop clinical messaging, consent-aware patient outreach, reminders, and communication governance into one Frappe-native coordination system.
Topics: openchart-feature-catalog, messaging-tasks, frappe, synthesis
Repository context: openChart — Frappe v15 native EMR; Messaging Tasks Notifications And Reminders domain synthesis
Captured: 2026-08-24

## Possible feats

- **Closed-loop coordination cockpit** — Combine queue age, acknowledgment, channel reach, escalation, and unresolved patient contact into a human-governed operations view.

## Focus

This synthesis relates all 40 Messaging Tasks Notifications And Reminders capabilities through shared custody, event identity, consent, delivery evidence, escalation, and lifecycle boundaries.

## Members and their joints

### Accountable staff intake and conversation

- [Staff Work-queue Inbox](openchart-feature-catalog-msg-001-staff-work-queue-inbox.md) gives personal and pooled work one accountable operational surface.
- [Clinical Message Routing Rules](openchart-feature-catalog-msg-002-clinical-message-routing-rules.md) supplies clinical destination policy, while [Patient-context Message Threads](openchart-feature-catalog-msg-003-patient-context-message-threads.md) preserves chart-linked conversation without copying clinical truth.
- [Internal Colleague Mentions](openchart-feature-catalog-msg-004-internal-colleague-mentions.md) signals attention without silently assigning responsibility.
- [Urgent Message Escalation Ladders](openchart-feature-catalog-msg-005-urgent-message-escalation-ladders.md) adds durable deadlines and qualified-recipient tiers for urgent work.

The joint is explicit custody: routing proposes a destination, the inbox exposes work, claiming establishes current responsibility, mentions attract attention, and escalation reacts to missing acknowledgment without pretending that delivery is clinical action.

### Task lifecycle and evidence

- [Recipient Read and Acknowledgment Tracking](openchart-feature-catalog-msg-006-recipient-read-and-acknowledgment-tracking.md) separates attempted delivery, read, acknowledgment, and later action.
- [Contextual Clinical Task Creation](openchart-feature-catalog-msg-007-contextual-clinical-task-creation.md) turns any authorized chart context into work without duplicating the source.
- [Task Delegation and Reassignment](openchart-feature-catalog-msg-008-task-delegation-and-reassignment.md) preserves custody transfer and acceptance history.
- [Task Due Dates and Recurrence](openchart-feature-catalog-msg-009-task-due-dates-and-recurrence.md) governs deadlines and per-occurrence accountability.
- [Task Completion Evidence Capture](openchart-feature-catalog-msg-010-task-completion-evidence-capture.md) makes selected completion states contingent on structured proof.

The joint is an evidence-bearing state machine: accepted context creates work, assignment identifies responsibility, temporal policy defines when action is due, and completion requires the proof declared by task type rather than a bare checkbox.

### Routing, coverage, and assignment

- [Assignment Rule Engine](openchart-feature-catalog-msg-011-assignment-rule-engine.md) evaluates constrained criteria and writes an explainable destination decision.
- [Coverage and Out-of-office Forwarding](openchart-feature-catalog-msg-012-coverage-and-out-of-office-forwarding.md) substitutes destinations for bounded absences while preserving original ownership.
- [On-call Coverage Calendar](openchart-feature-catalog-msg-013-on-call-coverage-calendar.md) resolves the effective primary and backup at an event timestamp.
- [Two-way Patient SMS Threads](openchart-feature-catalog-msg-014-two-way-patient-sms-threads.md) applies those assignment mechanics to inbound patient conversations.
- [SMS Template Library](openchart-feature-catalog-msg-015-sms-template-library.md) constrains what those and other SMS workflows may render.

The joint is decision provenance: domain policy supplies criteria, the generic engine applies them, coverage supplies time-sensitive destinations, and every resulting work item stores the facts and policy version that made routing explainable.

### Outbound channels and reminder programs

- [Broadcast Campaigns to Patient Cohorts](openchart-feature-catalog-msg-016-broadcast-campaigns-to-patient-cohorts.md) freezes an approved audience and executes governed high-volume outreach.
- [Email Templates and Delivery Events](openchart-feature-catalog-msg-017-email-templates-and-delivery-events.md) provides versioned composition and uncertain transport evidence.
- [Voice-call Tasks and Outcomes](openchart-feature-catalog-msg-018-voice-call-tasks-and-outcomes.md) represents human phone work and structured dispositions.
- [Reminder Cadence Engine](openchart-feature-catalog-msg-019-reminder-cadence-engine.md) creates purpose-specific planned touchpoints and stop conditions.
- [Reminder Effectiveness Analytics](openchart-feature-catalog-msg-020-reminder-effectiveness-analytics.md) links eligible populations through delivery to attributable action.

The joint is a common communication event identity across channels: cadence or campaign intent selects an approved template and channel, delivery creates evidence, human calls add attempt outcomes, and analytics retains denominator failures and attribution uncertainty.

### Recipient policy, critical fallback, and accessibility

- [Patient Notification Preference Resolution](openchart-feature-catalog-msg-021-patient-notification-preference-resolution.md) calculates allowed and suppressed channels with an explanation.
- [Quiet Hours and Notification Batching](openchart-feature-catalog-msg-022-quiet-hours-and-notification-batching.md) shifts noncritical timing without changing source deadlines.
- [Unread Critical Phone Fallback](openchart-feature-catalog-msg-023-unread-critical-phone-fallback.md) transitions failed digital acknowledgment into accountable call work.
- [Closed-loop Alert Effectiveness Metrics](openchart-feature-catalog-msg-024-closed-loop-alert-effectiveness-metrics.md) reveals acknowledgment performance and interruption burden for policy review.
- [Interpreter-included Outbound Communications](openchart-feature-catalog-msg-025-interpreter-included-outbound-communications.md) makes language support a planned and evidenced part of outreach.

The joint is bounded adaptation: recipient policy and accessibility affect channel and timing, criticality may invoke an approved bypass or fallback, and outcome metrics inform humans without automatically suppressing alerts or changing clinical urgency.

### Secure clinical coordination

- [Secure Staff Message Attachments](openchart-feature-catalog-msg-026-secure-staff-message-attachments.md) governs file provenance, scanning, and permission-checked access.
- [PHI-aware External Email Gateway](openchart-feature-catalog-msg-027-phi-aware-external-email-gateway.md) redirects sensitive email content into authenticated portal access.
- [Rapid Clinician Consult Chat](openchart-feature-catalog-msg-028-rapid-clinician-consult-chat.md) provides a bounded, time-sensitive consult disposition.
- [Order Clarification Threads](openchart-feature-catalog-msg-029-order-clarification-threads.md) preserves the authority boundary between conversation and an order amendment.
- [Prescription Renewal Request Inbox](openchart-feature-catalog-msg-030-prescription-renewal-request-inbox.md) separates renewal intake and review from prescribing authority.

The joint is source authority: secure conversation may contextualize, clarify, or request action, but accepted chart records change only through their owning APIs and workflows; attachments and external projections inherit current authorization rather than broadening it.

### Clinical and population follow-up

- [Abnormal-result Notification Composition](openchart-feature-catalog-msg-031-abnormal-result-notification-composition.md) supports clinician-authored plain-language result outreach.
- [Mass Recall and Disruption Notifications](openchart-feature-catalog-msg-032-mass-recall-and-disruption-notifications.md) governs urgent, versioned communication waves and unresolved exceptions.
- [New-patient Onboarding Checklists](openchart-feature-catalog-msg-033-new-patient-onboarding-checklists.md) coordinates role-assigned setup tasks and patient prompts.
- [Chronic-care Check-in Automation](openchart-feature-catalog-msg-034-chronic-care-check-in-automation.md) executes clinician-approved recurring outreach and routes responses.
- [Post-procedure Scripted Follow-up Calls](openchart-feature-catalog-msg-035-post-procedure-scripted-follow-up-calls.md) structures procedure-linked human calls and trigger escalation.

The joint is programmatic but non-autonomous follow-up: approved source events and protocols generate communications or work, structured responses feed accountable review queues, and no reply or script result independently changes diagnosis, medication, care plan, or order state.

### Reachability, compliance, and operational support

- [No-answer Cross-channel Retry Ladders](openchart-feature-catalog-msg-036-no-answer-cross-channel-retry-ladders.md) advances bounded attempts and stops on a qualifying response.
- [Unified Patient Communication Attempt Log](openchart-feature-catalog-msg-037-unified-patient-communication-attempt-log.md) normalizes channel evidence into one patient timeline.
- [Do-not-contact Registry Enforcement](openchart-feature-catalog-msg-038-do-not-contact-registry-enforcement.md) supplies a mandatory purpose-aware release gate for every outbound channel.
- [Communication Retention and Purge Schedules](openchart-feature-catalog-msg-039-communication-retention-and-purge-schedules.md) governs holds, archival, tombstones, and deletion evidence.
- [Internal Service-desk Ticketing](openchart-feature-catalog-msg-040-internal-service-desk-ticketing.md) reuses queue and assignment primitives for explicitly nonclinical support work.

The joint is end-to-end governance: attempts are checked before release, normalized after execution, stopped or retried by explicit policy, retained according to record class, and separated from nonclinical service work by clear type and authority boundaries.

## Frappe realization

- **Core model:** OC-prefixed message, receipt, work item, task, route decision, communication, campaign, reminder, escalation, attempt, preference, restriction, and retention DocTypes use Links/Dynamic Links, child tables, immutable events, and succession-based corrections.
- **Workflow and assignment:** Frappe Workflows govern multi-state records; native Assignment Rules plus clinically constrained adapters route to users and pools while preserving policy version, evaluated facts, and override evidence.
- **Channels:** Notification Log is the authoritative in-app event surface; Frappe Notification, Email Accounts, `frappe.email`, SMS settings, portal pages, voice-call tasks, and adapters project approved content to recipients.
- **Automation:** `scheduler_events` and RQ background jobs materialize recurrences, release batched events, process campaigns, run retry and escalation deadlines, refresh measures, and enforce retention through idempotent, bounded jobs.
- **Permissions:** Clinical Messaging User, Work Pool Manager, Task Supervisor, Communications Approver, Privacy Officer, Records Manager, and Audit Reviewer combine DocPerms, permlevels, participant checks, and facility/patient user permissions.
- **API and surfaces:** guarded `open_chart.api.v1.messaging` methods are the supported write surface; Desk workspaces, List/Kanban/Calendar/Gantt views, chart timelines, portal pages, Query/Script Reports, Number Cards, and Dashboard Charts expose role-specific projections.

## Boundaries

Owns: messaging and task custody, communication orchestration, delivery and acknowledgment evidence, reminder cadence, contact restrictions, and communication lifecycle. Consumes: patient identity, consent, proxy authority, chart permissions, source clinical events, clinician decisions, schedules, coverage, templates, and channel-provider outcomes. Emits: work assignments, messages, tasks, patient contact attempts, acknowledgments, escalations, exceptions, and aggregate measures. Does not own: clinical truth, orders, prescribing, diagnosis, emergency dispatch, workforce credentialing, billing, or carrier delivery.

## Emergent behavior

Together, the features form a closed-loop coordination fabric: source events enter an explainable route; personal and pooled queues establish custody; threads, tasks, and consults preserve context and evidence; preferences, restrictions, language support, and PHI policy shape delivery; receipt and retry events drive bounded escalation; and unified logs plus metrics expose whether the intended person was reached and accountable work completed. Shared event and policy identifiers let every transition remain auditable without collapsing communication receipt into clinical action.

## Tensions to hold

- Rapid clinical attention must coexist with explicit acknowledgment, recipient qualification, quiet hours, and reliable escalation under worker or gateway failure.
- Rich chart context improves coordination, but every message, attachment, digest, and external projection must remain minimum necessary and permission checked.
- Patient channel choice and do-not-contact restrictions may conflict with essential or critical communication obligations that require narrow, governed exceptions.
- Batching and multi-channel retries improve reach but can increase alarm fatigue, duplicate exposure, carrier cost, and opt-outs.
- Unified timelines and long-lived evidence support safety and audit, while retention minimization and legal holds pull in opposite directions.
- Automation may route, remind, and escalate, but must not interpret results, authorize prescriptions, or take autonomous clinical action.

## Recombination opportunities

- Combine work-queue age, current coverage, recipient acknowledgment, and phone fallback into a clinical operations command view.
- Combine preference resolution, no-contact enforcement, interpreter needs, quiet hours, and retry ladders into one explainable channel planner.
- Combine campaigns, reminders, communication attempts, and attributable actions into a governed outreach-learning loop with human policy review.
- Combine result notifications, order clarifications, renewal requests, and completion evidence into service-specific closed-loop safety bundles.
- Combine retention classes, secure attachments, portal redirects, and unified attempt logs into a communication records-management cockpit.

## Open questions

- What event contract lets independent DocTypes share custody, delivery, acknowledgment, response, and completion without circular updates?
- Which communications belong to the designated clinical record, and which remain operational evidence under separate retention?
- Which urgency and purpose policies may override quiet hours or channel restrictions, and what approval separation is required?
- How should pool accountability be measured when many members can read an item but only one person may acknowledge or complete it?
- Which delivery, read, and response signals are reliable enough for patient-safety metrics across gateways and clients?

## Relationships

[openChart Feature Catalog](openchart-feature-catalog-overview.md)
