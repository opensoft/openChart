# Scheduling And Patient Access — Brainstorm

Status: brainstorm
Kind: report
Summary: openChart should treat access as an intelligent, self-service funnel — rule-driven booking, waitlist automation, no-show prediction, and previsit completion — where OpenEMR offers a capable calendar but none of the demand-shaping intelligence the big-3 now standardize.
Topics: openchart-feature-list, scheduling, competitive-research
Repository context: openChart — Frappe-native EMR foundation; feature research versus the OpenEMR baseline and the enterprise big-3 (Epic, Oracle Health, MEDITECH Expanse)
Captured: 2026-08-23

## Possible feats

- **Intelligent scheduling rules** — visit-type sequencing, provider attributes, room/equipment constraints, and clinical needs guiding slot selection (Epic pattern).
- **Waitlist automation** — cancellations automatically offered to eligible waitlisted patients (Fast Pass analog).
- **No-show prediction** — risk-scored appointments driving targeted reminders or virtual-care conversion offers (Expanse pattern).
- **Sequential itinerary booking** — multi-step pathways (labs before visit, infusions series) booked as one flow.
- **Self-service everything** — patient-facing booking, rescheduling, cancellation, pre-registration, forms, consents, estimates, and payment before arrival.
- **Kiosk/contactless check-in** — arrival without front-desk intervention, feeding the flow board.

## Focus

Which scheduling capabilities convert openChart's calendar from a recording tool into a revenue-protecting access system?

## Current state: OpenEMR baseline

Core OpenEMR covers calendar-based scheduling, open-slot search, appointment categories/colors, recurring appointments, restrictions by type, multiple facilities, reminder/recall generation, email/SMS notifications (SMS via module), patient-flow/tracker boards, check-in/status workflows, and portal-based appointment requests. Kiosk/mobile check-in, two-way SMS, mass texting, and telehealth-linked scheduling are module/third-party dependent. There is no predictive intelligence, waitlist automation, or constrained sequential booking.

Sources: open-emr.org Features wiki; Patient Flow Board wiki; Modules catalog.

## Enterprise gap candidates

- Epic: intelligent scheduling using sequencing/clinical-needs rules; Fast Pass waitlist auto-offers; MyChart self-scheduling spanning procedures/imaging/therapy/infusions and sequential itineraries; Hello World centralized two-way SMS/voice/email including patients without portal accounts; Welcome kiosk self-service registration/payments.
- Oracle: Patient Administration self-service scheduling/preregistration with driver's-license and insurance-card capture automation; engagement roadmap adds waitlist coordination and preventive outreach.
- MEDITECH: contactless check-in via MHealth; no-show prediction guiding outreach or virtual-care offers; Expanse Patient Connect bidirectional SMS campaigns tied to registries.
- Common thread: access is a managed funnel with prediction and automation, not a calendar.

## Proposed feature set for openChart

Parity floor: multi-facility calendar, categories/recurring/rules, reminders/recalls, flow board, portal requests. Adopted gaps: constraint-based scheduling engine (rules as data, not code); automated waitlist offer cascade on cancellation; no-show risk scoring feeding reminder strategy and virtual-conversion offers; sequential pathway templates; kiosk + BYOD previsit flows writing discrete data (not PDFs); unified outbound messaging across SMS/email/voice with two-way replies. Twist: access metrics (fill rate, time-to-third-next-available, no-show rate by cohort) are first-class analytics-and-population-health exports.

## Interfaces and boundaries

Consumes: provider/facility configuration, visit types from clinical-documentation, eligibility signals from revenue-cycle, registry cohorts from analytics-and-population-health. Emits: arrivals to flow/check-in, completed intake to clinical-documentation, deposit/prepayments to revenue-cycle. Owns the schedule and access funnel; does not own clinical triage decisions.

## Alternatives and tensions

Predictive features need training data small clinics lack at go-live — ship rules-first, learn-from-data second. Aggressive automation (auto-offered slots) can annoy patients without careful consent and channel design. Deep Epic-style sequencing rules risk becoming a professional-services product; constrain the vocabulary instead.

## Open questions

- Is no-show prediction v1 (heuristic) or v2 (ML) given cold-start data reality?
- Does messaging infrastructure build on an open gateway standard or per-vendor connectors?
- Sequential pathways: which three pathways justify template investment at launch?

## Relationships

Clustered in [Synthesis: Access And Engagement](openchart-feature-list-synthesis-access-and-engagement.md). Adjacent: [Patient Engagement And Telehealth](openchart-feature-list-patient-engagement.md), [Revenue Cycle](openchart-feature-list-revenue-cycle.md).
