# Synthesis: Scheduling And Patient Access — Brainstorm

Status: brainstorm
Kind: reference
Summary: Connects schedule supply, governed booking, demand recovery, communication, patient flow, and access measurement into one Frappe-native patient-access system.
Topics: openchart-feature-catalog, scheduling, frappe, synthesis
Repository context: openChart — Frappe v15 native EMR; Scheduling And Patient Access domain synthesis
Captured: 2026-08-24

## Possible feats

- **Closed-loop access operations** — Combine capacity, request, booking, communication, and flow signals into reviewable improvement cycles without autonomous clinical action.

## Focus

This synthesis relates the 55 Scheduling And Patient Access capabilities and identifies the authority, state, and information seams that let them operate as a coherent domain.

## Members and their joints

### Calendar and capacity foundations

- [Provider Calendar](openchart-feature-catalog-sch-001-provider-calendar.md), [Facility Calendar](openchart-feature-catalog-sch-002-facility-calendar.md), and [Resource Calendar](openchart-feature-catalog-sch-003-resource-calendar.md) provide role-specific projections over shared capacity.
- [Appointment Type Catalog](openchart-feature-catalog-sch-004-appointment-type-catalog.md) supplies duration, modality, color, buffers, and resource defaults consumed by those projections.
- [Day Template Patterns](openchart-feature-catalog-sch-021-day-template-patterns.md) and [Location Schedule Templates](openchart-feature-catalog-sch-034-location-schedule-templates.md) create the baseline; [Provider Availability Exceptions](openchart-feature-catalog-sch-022-provider-availability-exceptions.md) and [Holiday Closure Management](openchart-feature-catalog-sch-023-holiday-closure-management.md) supersede it for bounded intervals.

The joint is a versioned effective-capacity projection: templates establish supply, exceptions remove or add it, and Frappe's native Calendar view per DocType renders the same accepted intervals through provider, facility, and resource lenses.

### Search, access, and capacity control

- [Open-slot Search](openchart-feature-catalog-sch-006-open-slot-search.md), [Rule-based Booking Constraints](openchart-feature-catalog-sch-007-rule-based-booking-constraints.md), and [Patient Self-scheduling](openchart-feature-catalog-sch-008-patient-self-scheduling.md) separate candidate discovery from transactional confirmation.
- [Overbooking Controls](openchart-feature-catalog-sch-024-overbooking-controls.md), [Double-booking Warnings](openchart-feature-catalog-sch-025-double-booking-warnings.md), and [Multi-resource Appointment Booking](openchart-feature-catalog-sch-032-multi-resource-appointment-booking.md) defend capacity integrity at confirmation time.
- [Scheduling Holds](openchart-feature-catalog-sch-044-scheduling-holds.md), [Slot Release Windows](openchart-feature-catalog-sch-045-slot-release-windows.md), and [Booking Horizon Rules](openchart-feature-catalog-sch-046-booking-horizon-rules.md) govern when inventory becomes available and to whom.
- [Time-zone-safe Scheduling](openchart-feature-catalog-sch-047-time-zone-safe-scheduling.md), [Patient Preference Matching](openchart-feature-catalog-sch-048-patient-preference-matching.md), and [Accessibility Accommodation Scheduling](openchart-feature-catalog-sch-049-accessibility-accommodation-scheduling.md) keep valid results understandable, practical, and equitable.

The joint is revalidation: search results and holds are provisional, while one guarded `open_chart.api.v1.scheduling` transaction resolves effective policy, time, permissions, and all required resources before confirmation.

### Appointment lifecycle and complex itineraries

- [Recurring Appointment Series](openchart-feature-catalog-sch-005-recurring-appointment-series.md), [Group and Class Appointments](openchart-feature-catalog-sch-018-group-and-class-appointments.md), and [Sequential Care Pathway Booking](openchart-feature-catalog-sch-019-sequential-care-pathway-booking.md) compose appointments without erasing each occurrence's independent state.
- [Patient Rescheduling](openchart-feature-catalog-sch-009-patient-rescheduling.md) and [Appointment Cancellation Policies](openchart-feature-catalog-sch-010-appointment-cancellation-policies.md) preserve lineage as bookings move or release capacity.
- [Late-cancellation Fee Hooks](openchart-feature-catalog-sch-016-late-cancellation-fee-hooks.md) and [Prepayment-required Booking Rules](openchart-feature-catalog-sch-040-prepayment-required-booking-rules.md) expose bounded financial integration states without moving billing or payment ownership into openChart.
- [Procedure Scheduling](openchart-feature-catalog-sch-038-procedure-scheduling.md) coordinates the most demanding resource and readiness case.

The joint is explicit scope: every series, itinerary, group, procedure, reschedule, and cancellation operation states which appointments change, and Frappe auto-repeat may seed bounded patterns without replacing per-occurrence audit and validation.

### Demand intake, recovery, and backfill

- [Appointment Request Triage](openchart-feature-catalog-sch-043-appointment-request-triage.md), [Referral-driven Scheduling Queue](openchart-feature-catalog-sch-037-referral-driven-scheduling-queue.md), and [Recall-driven Scheduling](openchart-feature-catalog-sch-017-recall-driven-scheduling.md) turn authorized demand into accountable scheduling work.
- [Waitlist Management](openchart-feature-catalog-sch-011-waitlist-management.md), [Standby List](openchart-feature-catalog-sch-041-standby-list.md), and [Automated Waitlist Offer Cascade](openchart-feature-catalog-sch-012-automated-waitlist-offer-cascade.md) distinguish durable preference, immediate readiness, and time-bounded offers.
- [Cancellation Backfill Analytics](openchart-feature-catalog-sch-051-cancellation-backfill-analytics.md) closes the operational feedback loop by attributing whether released capacity was recovered.

The joint is provenance-preserving demand state: clinical urgency and referral authority remain upstream, while scheduling owns queue state, consented outreach, offer deadlines, and the final link to a booking.

### Communication and readiness

- [Appointment Reminder Cadence](openchart-feature-catalog-sch-013-appointment-reminder-cadence.md) and [Two-way SMS Appointment Confirmation](openchart-feature-catalog-sch-014-two-way-sms-appointment-confirmation.md) create a closed reminder-response loop.
- [Interpreter Scheduling](openchart-feature-catalog-sch-030-interpreter-scheduling.md), [Telehealth Slot Types](openchart-feature-catalog-sch-031-telehealth-slot-types.md), and [Transportation-aware Scheduling](openchart-feature-catalog-sch-050-transportation-aware-scheduling.md) coordinate support dependencies that determine practical access.
- [Procedure Preparation Instructions](openchart-feature-catalog-sch-039-procedure-preparation-instructions.md) and [Appointment Arrival Instructions](openchart-feature-catalog-sch-054-appointment-arrival-instructions.md) distinguish clinical preparation content from operational wayfinding.
- [Schedule Change Broadcasts](openchart-feature-catalog-sch-055-schedule-change-broadcasts.md) provides the many-recipient disruption path.

The joint is consent-aware delivery: Frappe Notification doctypes, Notification Log, email, SMS settings, push adapters, print formats, and portal pages use the same versioned scheduling event while recording channel-specific outcomes.

### Day-of operations and disruption resolution

- [Appointment Check-in Statuses](openchart-feature-catalog-sch-026-appointment-check-in-statuses.md), [Real-time Patient Flow Board](openchart-feature-catalog-sch-027-real-time-patient-flow-board.md), and [Wait-time Tracking](openchart-feature-catalog-sch-028-wait-time-tracking.md) connect accepted flow transitions to live coordination and derived measures.
- [Room Assignment](openchart-feature-catalog-sch-029-room-assignment.md) binds current flow to safe physical occupancy.
- [Provider Substitution Workflow](openchart-feature-catalog-sch-052-provider-substitution-workflow.md) and [Schedule Conflict Resolution](openchart-feature-catalog-sch-053-schedule-conflict-resolution.md) turn disruptions into reviewable human decisions.

The joint is append-only operational state: websocket events update boards quickly, but accepted server transitions remain authoritative and corrected events supersede rather than rewrite history.

### Oversight, interoperability, and improvement

- [No-show Risk Scoring](openchart-feature-catalog-sch-015-no-show-risk-scoring.md) supplies advisory outreach prioritization under explicit non-action safeguards.
- [Block and Bulk Scheduling](openchart-feature-catalog-sch-020-block-and-bulk-scheduling.md) applies reviewed high-volume operations with per-item outcomes.
- [iCalendar Feed Export](openchart-feature-catalog-sch-033-ical-calendar-feed-export.md) projects privacy-minimized appointments to external calendars through revocable tokens.
- [Scheduling Capacity Dashboard](openchart-feature-catalog-sch-035-scheduling-capacity-dashboard.md) and [Third-next-available Metric](openchart-feature-catalog-sch-036-third-next-available-metric.md) make supply, utilization, and prospective access measurable.
- [Schedule Audit History](openchart-feature-catalog-sch-042-schedule-audit-history.md) provides the common evidence spine for changes, overrides, jobs, and integrations.

The joint is explainable automation: `scheduler_events` and background jobs may materialize templates, expire holds, send due communications, and calculate metrics, but every action is idempotent, permission-aware, and attributable.

## Frappe realization

- **Core model:** OC-prefixed schedule, appointment, request, policy, reservation, event, communication, and metric DocTypes use Links, child tables, explicit effective versions, and succession-based corrections where accepted history matters.
- **Views:** Frappe's native Calendar view per DocType anchors provider, facility, and resource time; Gantt, Kanban, List, Query/Script Reports, Number Cards, Dashboard Charts, portal pages, and a websocket flow board provide task-specific projections.
- **Workflow and permissions:** Frappe Workflows govern multi-state records; Scheduler, Scheduling Manager, Scheduling Outreach, Scheduling Rule Manager, Front Desk, Clinical Operations, Audit Reviewer, and Patient roles combine DocPerms with facility and provider user permissions.
- **Automation and communication:** Frappe auto-repeat supports reviewed bounded patterns; `scheduler_events`, RQ background jobs, Notification doctypes, Notification Log, `frappe.email`, SMS settings, and push adapters execute due work with consent and idempotency checks.
- **API:** guarded `open_chart.api.v1.scheduling` methods are the supported mutation surface; whitelisted search, portal, webhook, and feed methods enforce row-level authority and structured errors.
- **Audit and safety:** canonical append-only scheduling events record actor, source, reason, policy version, and correlation ID; no risk score, free-text interpretation, or missing clinical input triggers autonomous clinical action.

## Boundaries

Owns: scheduling supply, operational access requests, booking state, resource reservations, scheduling communications, patient flow, and access measures. Consumes: patient identity, consent, authorized clinical need, provider authority, facility/resource master data, and external delivery or payment outcomes. Emits: appointments, operational tasks, notifications, audit evidence, and capacity metrics. Does not own: clinical orders, clinical triage, encounter documentation, credentialing, billing, claims, payment processing, transportation fulfillment, or telehealth media.

## Emergent behavior

Together, the features form a closed but human-governed access loop: versioned templates create supply; requests, rules, preferences, and accommodations discover feasible options; transactional booking commits resources; communications and day-of flow carry appointments through completion; cancellations and disruptions return capacity to demand queues; and audited metrics reveal where policy or supply merits review. Shared event identity lets a cancellation update calendars, stop reminders, release resources, start a waitlist cascade, open a recovery episode, and notify affected actors without any one feature silently owning the others' decisions.

## Tensions to hold

- Fast self-service and automated backfill must not bypass clinical authorization, consent, protected-access policy, or resource safety.
- Rich preference and risk signals can improve service, but can also encode inequity or expose sensitive facts if used as hidden hard constraints.
- Materialized slots simplify operations, while projection from templates reduces stale data; the system needs an explicit horizon and reconciliation model.
- Realtime boards favor immediacy, while audit, permission checks, and transactional conflict detection require the server to remain authoritative.
- Patient-friendly communications need useful detail, but external channels and shared displays demand strict minimum-necessary disclosure.

## Recombination opportunities

- Combine third-next-available trends, protected slot release, and request queue age into a human-reviewed access policy cockpit.
- Combine cancellation backfill, waitlist cascades, standby readiness, and communication outcomes to test refill strategies without changing priority automatically.
- Combine accommodations, interpreters, transportation, arrival guidance, and multi-resource booking into a patient-specific readiness itinerary.
- Combine provider exceptions, substitution, conflict cases, and broadcasts into a disruption command workflow with one audited resolution graph.

## Open questions

- What is the authoritative representation of future capacity: materialized slot records, an effective projection, or a governed hybrid?
- Which scheduling policies are global defaults versus facility-owned versions, and how is precedence explained?
- Which patient-access protections require clinical or compliance review before activation?
- What minimum event contract lets independent scheduling features react without creating circular side effects?

## Relationships

[openChart Feature Catalog](openchart-feature-catalog-overview.md)
