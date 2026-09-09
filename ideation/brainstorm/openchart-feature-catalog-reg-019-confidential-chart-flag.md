# Confidential Chart Flag — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Restricts patient discovery and chart access for documented confidentiality needs while retaining safe emergency escalation.
Topics: openchart-feature-catalog, registration, frappe, confidential-chart
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-019 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Search shielding profiles** — Configure whether restricted records are hidden, masked, or acknowledgment-gated by context.

## Focus

Control confidentiality at chart discovery and access boundaries independently from VIP designation.

## Behavior

- Privacy Officer records restriction type, legal or safety basis, scope, effective dates, and review date.
- Global search hides or masks the patient for users outside the allowed access profile.
- Direct links perform the same permission check and cannot bypass search shielding.
- Authorized access requires purpose capture when the restriction profile demands it.
- Break-glass is unavailable for restrictions whose legal basis forbids it and clearly explains escalation.
- Changes and expiry decisions are succession-based and retain prior access policy.

## Frappe realization

- **DocTypes:** `OC Patient Privacy Flag` type Confidential with access_profile, search_behavior, basis, validity, and review_date.
- **Workflow:** Proposed → Privacy Review → Active → Review Due → Closed, Renewed, or Escalated.
- **Roles/permissions:** `OC Privacy Officer` administers; custom DocPerm and permission-query conditions restrict `OC Patient` discovery.
- **API/surfaces:** guarded `open_chart.api.v1.registration.patient_search` and `.authorize_restricted_chart`; masked search row and restriction worklist.

## Boundaries

Owns: confidentiality restriction and chart-discovery behavior. Consumes: approved legal or safety basis. Emits: permission decisions and access logs. Does not own: consent segmentation for individual clinical records.

## Open questions

- Which restriction profiles must remain discoverable to emergency registration staff?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
