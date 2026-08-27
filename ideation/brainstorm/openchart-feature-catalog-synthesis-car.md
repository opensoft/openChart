# Synthesis: Care Plans Coordination Referrals And Transitions — Brainstorm

Status: brainstorm
Kind: reference
Summary: Connects shared care plans, longitudinal programs, referral closure, transition handoffs, access support, and coordinator work into one human-governed continuity system.
Topics: openchart-feature-catalog, care-coordination, frappe, synthesis
Repository context: openChart — Frappe v15 native EMR; Care Plans Coordination Referrals And Transitions domain synthesis
Captured: 2026-08-24

## Possible feats

- **Continuity command workspace** — Combine accepted plan, referral, transition, barrier, and workload signals into a permission-filtered workspace for human review and accountable action.

## Focus

This synthesis relates all 55 CAR capabilities and identifies their state, authority, consent, provenance, assignment, and closure seams. It describes a coordination graph, not an autonomous care manager or a replacement for discipline-specific clinical judgment.

## Members and their joints

### Shared care-plan foundations

- [Problem And Goal Template Care Plans](openchart-feature-catalog-car-001-problem-goal-template-care-plans.md), [Measurable Goals And Target Dates](openchart-feature-catalog-car-002-measurable-goals-and-target-dates.md), [Care Intervention Task Assignment](openchart-feature-catalog-car-003-care-intervention-task-assignment.md), [Plan Of Care Version Approvals](openchart-feature-catalog-car-004-plan-of-care-version-approvals.md), [Interdisciplinary Shared Care Plans](openchart-feature-catalog-car-005-interdisciplinary-shared-care-plans.md), [Patient Portal Care Plan View](openchart-feature-catalog-car-006-patient-portal-care-plan-view.md), [Caregiver Task Access](openchart-feature-catalog-car-007-caregiver-task-access.md), [Education Material Assignment And Completion](openchart-feature-catalog-car-008-education-material-assignment.md), [Teach Back Documentation](openchart-feature-catalog-car-009-teach-back-documentation.md).

The joint is governed decomposition: an approved plan version publishes patient-readable goals and education while producing role-owned interventions, caregiver grants, and teach-back follow-up that retain their source plan identity.

### Longitudinal programs and preventive pathways

- [Chronic Condition Program Enrollment](openchart-feature-catalog-car-010-chronic-program-enrollment.md), [Program Enrollment Dashboard](openchart-feature-catalog-car-011-program-enrollment-dashboard.md), [Program Milestone Tracking](openchart-feature-catalog-car-012-program-milestone-tracking.md), [Diabetes Management Program](openchart-feature-catalog-car-013-diabetes-management-program.md), [Heart Failure Management Program](openchart-feature-catalog-car-014-heart-failure-management-program.md), [COPD Management Program](openchart-feature-catalog-car-015-copd-management-program.md), [Wound Care Program Pathway](openchart-feature-catalog-car-016-wound-care-pathway.md), [Anticoagulation Program INR And Dosing Logs](openchart-feature-catalog-car-017-anticoagulation-program-inr-logs.md), [MAT Buprenorphine Program Tracking](openchart-feature-catalog-car-018-mat-buprenorphine-program-tracking.md), [Trimester Based Pregnancy Care Plans](openchart-feature-catalog-car-019-trimester-based-pregnancy-care-plans.md), [Postpartum Follow Up Scheduling Automation](openchart-feature-catalog-car-020-postpartum-follow-up-automation.md), [Pediatric Medical Home Complexity Tiering](openchart-feature-catalog-car-021-pediatric-medical-home-complexity-tiering.md), [Annual Wellness Visit Preparation Assembly](openchart-feature-catalog-car-022-annual-wellness-visit-preparation.md).

The joint is enrollment context: one accepted enrollment selects a reviewed pathway, materializes dated milestones through bounded auto-repeat, and lets specialty episodes report progress without silently changing goals or treatment.

### Referral exchange and loop closure

- [Referral Order With Clinical Summary](openchart-feature-catalog-car-023-referral-order-with-clinical-summary.md), [Internal And External Referral Routing](openchart-feature-catalog-car-024-internal-external-referral-routing.md), [Referral Directory With Specialty And Insurance](openchart-feature-catalog-car-025-referral-directory-specialty-insurance.md), [Referral Status Lifecycle](openchart-feature-catalog-car-026-referral-status-lifecycle.md), [Referral Loop Closure And Aging Alerts](openchart-feature-catalog-car-027-referral-loop-closure-aging-alerts.md), [Asynchronous E Consults](openchart-feature-catalog-car-028-asynchronous-e-consults.md), [Incoming Referral Intake And Triage Queue](openchart-feature-catalog-car-029-incoming-referral-intake-triage.md), [Referral Authorization Required Flags](openchart-feature-catalog-car-030-referral-authorization-required-flags.md), [Consult Report Ingestion And Referral Linkage](openchart-feature-catalog-car-031-consult-report-ingestion-linkage.md).

The joint is correlation across organizational boundaries: the signed referral, route attempts, destination identity, acknowledgements, authorization evidence, consult advice, and returned report share one referral identifier while each actor retains authority over its own state.

### Transitions and destination coordination

- [Transition Of Care Document Generation](openchart-feature-catalog-car-032-transition-of-care-document-generation.md), [Discharge Planning Checklists](openchart-feature-catalog-car-033-discharge-planning-checklists.md), [Post Discharge Follow Up Call Tasks](openchart-feature-catalog-car-034-post-discharge-follow-up-calls.md), [Readmission Risk Stratification For Outreach](openchart-feature-catalog-car-035-readmission-risk-outreach.md), [Home Health Agency Coordination Records](openchart-feature-catalog-car-036-home-health-coordination-records.md), [Durable Medical Equipment Order Coordination](openchart-feature-catalog-car-037-dme-order-coordination.md), [Community Resource Closed Loop Referrals](openchart-feature-catalog-car-038-community-resource-closed-loop-referrals.md), [Behavioral Health Crisis Safety Plans](openchart-feature-catalog-car-039-behavioral-health-crisis-safety-plans.md), [Shared Decision Aid Delivery And Recording](openchart-feature-catalog-car-040-shared-decision-aid-delivery.md).

The joint is discharge readiness and follow-through: a reviewed transition document and checklist establish the handoff package, parallel home-health, equipment, social-care, safety-plan, and decision-aid work resolve destination needs, and follow-up evidence returns after departure.

### Coordination workforce and population work

- [Care Team Role Based Task Views](openchart-feature-catalog-car-041-care-team-role-task-views.md), [Unassigned Task Escalation](openchart-feature-catalog-car-042-unassigned-task-escalation.md), [Coordinator Caseload Management Views](openchart-feature-catalog-car-043-coordinator-caseload-management.md), [Panel Management Intervention Worklists](openchart-feature-catalog-car-044-panel-intervention-worklists.md), [Cohort Outreach Campaign Creation](openchart-feature-catalog-car-045-cohort-outreach-campaigns.md), [Campaign Communication Preference Enforcement](openchart-feature-catalog-car-046-campaign-communication-preferences.md).

The joint is accountable workload shaping: reproducible panel criteria create frozen campaign candidates, communication preferences suppress unsafe contact, role queues assign permitted work, and caseload and exception views reveal capacity without changing clinical priority automatically.

### Access barriers and serious-illness handoffs

- [Interpreter Inclusive Referral Coordination](openchart-feature-catalog-car-047-interpreter-inclusive-referral-coordination.md), [Transportation Barrier And Ride Arrangement Tracking](openchart-feature-catalog-car-048-transportation-barrier-ride-tracking.md), [High Cost Care Benefits Investigation](openchart-feature-catalog-car-049-high-cost-care-benefits-investigation.md), [Palliative Care Consult Coordination](openchart-feature-catalog-car-050-palliative-care-consult-coordination.md), [Hospice Election Tracking Handoff](openchart-feature-catalog-car-051-hospice-election-handoff.md).

The joint is patient-authorized practical access: interpreter, ride, and benefit work proceeds beside the referral, while palliative and hospice coordination adds sensitive preference and election evidence under tighter disclosure and acknowledgement controls.

### Continuity evidence and shared accountability

- [Transition Medication Reconciliation Tasks](openchart-feature-catalog-car-052-transition-medication-reconciliation-tasks.md), [Receiving Provider Handoff Acknowledgment](openchart-feature-catalog-car-053-receiving-provider-handoff-acknowledgment.md), [Care Conference Coordination And Decisions](openchart-feature-catalog-car-054-care-conference-coordination.md), [Longitudinal Care Coordination Timeline](openchart-feature-catalog-car-055-longitudinal-coordination-timeline.md).

The joint is a closed evidence spine: medication-review discrepancies, receiving-provider responses, and care-conference decisions emit correlated events that the longitudinal timeline can project without becoming the editable source of any member record.

## Frappe realization

- **Core model:** OC-prefixed plan, goal, task, program, referral, transition, barrier, acknowledgement, and event DocTypes use explicit links, child evidence tables, effective versions, and succession-based amendments.
- **Workflow and assignment:** Frappe Workflows enforce accountable state changes; Assignment Rules route eligible work, unassigned exceptions escalate visibly, and Notification Log records review and delivery notices.
- **Operational views:** Kanban boards expose referral, discharge, task, milestone, and barrier queues; Calendar and Gantt views show conferences, targets, and pathways; Query/Script Reports and Dashboard Charts reveal age, capacity, and closure.
- **Recurring and portal work:** Frappe auto-repeat seeds reviewed recurring milestones and follow-ups without replacing occurrence records; Web Forms and portal pages support bounded patient, caregiver, destination, and community-partner participation.
- **API and events:** guarded `open_chart.api.v1.care_coordination` methods are the supported mutation surface; idempotent background jobs and canonical `OC Coordination Event` records connect features without circular ownership.
- **Safety and permissions:** Care Coordinator, Clinician, Program Coordinator, Referral Coordinator, Transition Nurse, Social Worker, Patient, Caregiver, and external-partner roles combine DocPerms with patient, facility, program, and assignee user permissions; no score or automation performs autonomous clinical action.

## Boundaries

Owns: care-plan coordination, longitudinal program participation, referral and handoff state, coordination tasks, barrier follow-up, acknowledgements, and closure evidence. Consumes: patient identity, consent, accepted clinical records, clinical orders, provider authority, coverage facts, scheduling outcomes, and external responses. Emits: human work items, summaries, coordination events, notifications, status evidence, and oversight measures. Does not own: diagnosis, prescribing, scheduling capacity, payer adjudication, billing, claims, transportation or vendor fulfillment, or autonomous clinical decisions.

## Emergent behavior

Together the members create a continuity loop: accepted problems and goals become a versioned shared plan; interventions become accountable role work; programs add recurring milestones; referrals move through routing, acknowledgement, scheduling, results, and closure; discharge and serious-illness handoffs assemble destination-ready evidence; barriers create parallel support work; and acknowledgements return proof to the longitudinal timeline. Because every seam carries patient identity, consent, provenance, authority, predecessor, and correlation identifiers, staff can distinguish a delayed service from a missing handoff, a declined offer, an authorization barrier, or a true clinical review need.

## Tensions to hold

- Shared visibility improves continuity but must respect behavioral-health sensitivity, proxy scope, minimum-necessary disclosure, and patient choices about caregiver participation.
- Assignment Rules and auto-repeat reduce dropped work but can create unsafe confidence unless unassigned, stale, duplicate, and failed-delivery states stay conspicuous.
- Standard pathways improve consistency while individualized plans must preserve patient goals, clinician judgment, exceptions, and version history.
- External partners need low-friction Web Forms and acknowledgements, but identity, consent, attachment safety, and replay protection remain mandatory.
- Risk, complexity, and panel signals can prioritize review, but they must remain explainable advisory inputs and must never autonomously reduce access or initiate clinical action.

## Recombination opportunities

- Combine plan goals, program milestones, referral outcomes, and teach-back evidence into a clinician-reviewed continuity progress view.
- Combine loop-closure aging, unassigned-task escalation, coordinator caseload, and destination acknowledgements into a capacity-aware exception cockpit.
- Combine interpreter, transportation, benefits, caregiver, and communication-preference records into a patient-approved access support itinerary.
- Combine transition summaries, medication-review tasks, home-health and DME coordination, follow-up calls, and receiving-provider acknowledgement into one discharge readiness graph.

## Open questions

- Which event identifiers and state vocabulary are stable enough to connect every CAR workflow without forcing one giant DocType?
- Which external participants may update state directly through Web Forms, and which responses require staff verification before acceptance?
- How should assignment precedence balance care-team ownership, facility coverage, program responsibility, and patient continuity?
- Which coordination evidence belongs in the legal clinical record versus an operational log with shorter retention?

## Relationships

[openChart Feature Catalog](openchart-feature-catalog-overview.md)
