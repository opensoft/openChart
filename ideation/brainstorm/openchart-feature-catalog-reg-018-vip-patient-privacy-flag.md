# VIP Patient Privacy Flag — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies time-bounded enhanced access controls to designated patient charts without exposing the reason to unauthorized users.
Topics: openchart-feature-catalog, registration, frappe, vip-privacy
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-018 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Break-glass review queue** — Route every emergency override on a VIP chart to immediate privacy review.

## Focus

Treat VIP as a privacy-control profile, not a decorative demographic label.

## Behavior

- Privacy Officer applies the flag with reason category, scope, start, expiry, and approving authority.
- Unauthorized users learn only that access is restricted, not why the patient is designated.
- Authorized users encounter an access acknowledgment and purpose capture before chart opening.
- Emergency break-glass access is time-limited, logged, and notifies privacy reviewers.
- Expiry removes enhanced controls only after configured review or explicit approval.
- VIP designation never changes clinical prioritization, care eligibility, or display prominence.

## Frappe realization

- **DocTypes:** `OC Patient Privacy Flag` with type, scope, reason_category, validity, approver, and break_glass_policy.
- **Workflow:** Draft → Approved → Active → Expiry Review → Closed or Renewed.
- **Roles/permissions:** `OC Privacy Officer` controls at permlevel 2; other roles receive permission-query filtering and guarded access checks.
- **API/surfaces:** `open_chart.api.v1.registration.authorize_restricted_chart`; restricted banner, access-reason dialog, and privacy audit Script Report.

## Boundaries

Owns: enhanced VIP access policy and lifecycle. Consumes: approved privacy designation. Emits: access decisions and review events. Does not own: clinical triage or public-relations handling.

## Open questions

- Should VIP access require named-user allowlists or role plus purpose checks?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
