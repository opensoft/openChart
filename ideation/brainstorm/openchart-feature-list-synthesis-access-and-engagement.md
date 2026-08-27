# Synthesis: Access And Engagement — Brainstorm

Status: brainstorm
Kind: architecture
Summary: scheduling and patient engagement fuse into one demand-shaping funnel in openChart — prediction, waitlist automation, omnichannel messaging, and consent-governed portal permissions convert OpenEMR's passive calendar-plus-portal into an access engine clinics compete on.
Topics: openchart-feature-list, access-engagement-synthesis, synthesis, scheduling, patient-engagement
Repository context: openChart — Frappe-native EMR foundation; feature research versus the OpenEMR baseline and the enterprise big-3 (Epic, Oracle Health, MEDITECH Expanse)
Captured: 2026-08-23

## Possible feats

- **Demand-shaping loop** — no-show prediction feeds reminder strategy feeds waitlist cascade feeds fill-rate metrics; every cancellation becomes an automatic recovery opportunity.
- **Consent-aware everything** — portal visibility, messaging channels, proxy scopes, and appointment communications all read one consent state; changes apply instantly everywhere.
- **Digital front door consolidation** — booking, intake, estimates, payments, video visits, and assistant conversations under one patient identity with one audit trail.
- **Channel-inclusive outreach** — registry cohorts trigger campaigns reaching patients with or without portal accounts (Hello World/Patient Connect pattern).

## Members and their joints

Atomic members: [Scheduling And Patient Access](openchart-feature-list-scheduling-and-access.md), [Patient Engagement And Telehealth](openchart-feature-list-patient-engagement.md).

### Scheduling ↔ Portal actions

Self-service booking writes constraint-checked slots directly; rescheduling/cancellation triggers the waitlist cascade automatically. The seam requires the scheduling engine's rule vocabulary to be readable by patient-facing flows — constraints evaluated identically whether staff or patient initiates.

### Messaging ↔ Prediction

No-show risk scores select message cadence/channel per patient; reply threads route back into staff queues with schedule context attached. Prediction without a messaging actuator is a dashboard toy; messaging without prediction spams uniformly.

### Consent ↔ Everything

Proxy/guardian/adolescent rules gate appointment visibility, message content, result release, and payment obligations. Epic's Sharing Hub shows the maturity bar; openChart's twist is making consent state a queryable service every surface consumes, not per-module settings.

### Video ↔ Encounter context

Virtual visits launched from portal/app must land in the same encounter/documentation pipeline as in-person care — identity assurance at join time, consent captured, documentation drafted into the standard chart.

## Emergent behavior

The pair produces capabilities neither owns alone: third-next-available appointments shrink because cancellations self-heal; engagement messages become clinically consequential because they carry schedule mutations; the clinic's front door stays open 24/7 without staffing. Access metrics (fill rate, recovery rate, time-to-appointment) emerge as first-class business KPIs exportable to [Analytics And Population Health](openchart-feature-list-analytics-and-population-health.md).

## Tensions to hold

Automation that reshuffles schedules can surprise patients — consent and notification design carries the ethical weight prediction enables. Omnichannel reach (SMS to non-portal patients) conflicts with identity-assurance rigor required for health content. Adolescent confidentiality law varies enough that default-on convenience features need jurisdiction-aware defaults.

## Recombination opportunities

Waitlist automation recombines with [Revenue Cycle](openchart-feature-list-revenue-cycle.md) when estimates gate self-service booking; assistant conversations recombine with [Clinical AI And Governance](openchart-feature-list-clinical-ai.md) as the highest-volume AI surface; registry-driven outreach recombines with population-health cohort definitions.

## Open questions

- Does consent state live in engagement domain or platform identity layer?
- What is the minimal rule vocabulary that makes patient self-scheduling safe without staff approval queues?
- Which virtual-care pattern launches first — scheduled visits, e-visits, or on-demand?

## Relationships

Owned by [Overview](openchart-feature-list-overview.md). Cross-cluster: [Synthesis: Business And Exchange](openchart-feature-list-synthesis-business-and-exchange.md).
