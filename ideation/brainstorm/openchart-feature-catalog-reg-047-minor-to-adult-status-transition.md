# Minor to Adult Status Transition — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates review of authority, access, contact, consent, and privacy when a patient reaches the site's age-of-majority policy.
Topics: openchart-feature-catalog, registration, frappe, age-transition
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-047 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Pre-transition patient campaign** — Invite the patient to establish independent access and preferences before the effective date.

## Focus

Treat adulthood as a governed relationship transition rather than an automatic deletion of guardian access.

## Behavior

- A scheduled rule creates a review before the configured age-of-majority date using jurisdiction and patient context.
- The review inventories guardian authority, proxy access dependencies, communication endpoints, guarantors, and active consents.
- Patient and staff confirm independent contact, portal, privacy, and consent preferences where applicable.
- Authority records end or continue according to evidence and policy, never from age alone when exceptions apply.
- Unresolved items escalate and remain visible after the transition date without blocking urgent care.
- Completion records every continued, ended, or newly established relationship with effective time.

## Frappe realization

- **DocTypes:** `OC Age Transition Review` and child `OC Transition Decision` with policy, milestone_date, subject, prior link, action, and outcome.
- **Workflow:** Upcoming → Outreach → In Review → Completed, Exception, or Escalated.
- **Roles/permissions:** `OC Registration Clerk` coordinates; `OC Authority Reviewer` resolves continued authority; patient portal user confirms own preferences.
- **API/surfaces:** scheduler event creates reviews; `open_chart.api.v1.registration.complete_age_transition`; transition worklist and upcoming Number Card.

## Boundaries

Owns: registration-level age transition coordination. Consumes: birth-date precision, authority, access, consent, and policy. Emits: effective relationship changes. Does not own: jurisdictional legal interpretation.

## Open questions

- How should uncertain birth dates affect transition timing and outreach?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
