# Cancer Screening Outreach Tracking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Tracks supervised mammography, colorectal, cervical, and other cancer-screening outreach from care gap through response and completion.
Topics: openchart-feature-catalog, public-health, frappe, cancer-screening-outreach
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-029 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Multilingual campaign variants** — Govern language-appropriate messages and response paths by screening program.

## Focus

Accountable outreach episodes linked to a reviewed cancer-screening gap, not automated clinical determination.

## Behavior

- Program staff enroll an eligible reviewed gap into a campaign with consent and channel preferences.
- Attempts record date, channel, template version, sender, delivery result, and patient response.
- Outcomes include scheduled, externally-completed, declined, deferred, unreachable, ineligible, and closed.
- External completion requires source evidence and clinical reconciliation before closing the care gap.
- Suppression preferences and sensitive communication restrictions apply before every attempt.
- Failed deliveries and overdue responses route assignments without endless unbounded messaging.

## Frappe realization

- **DocTypes:** Add `OC Screening Outreach Episode`, child attempt rows, and `OC Screening Campaign` with bounded cadence and templates.
- **Workflow:** Use eligible, enrolled, active, awaiting-response, resolved, suppressed, and closed states.
- **Permissions:** Restrict campaigns to `OC Population Health User`; clinical closure requires `OC Clinician` review.
- **Surfaces:** Use Notifications/SMS integration points, Kanban worklists, campaign Dashboard Charts, and audited patient-chart history.

## Boundaries

Owns: outreach campaign and response history. Consumes: reviewed care gaps, consent, communication preferences, and results. Emits: contacts, tasks, and dispositions. Does not own: screening eligibility rules or appointment scheduling.

## Open questions

- What cadence caps should apply across concurrent outreach programs?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
