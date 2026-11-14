# Patient Group Membership — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Places patients in explicit operational or care-program groups with criteria, authority, dates, and visibility controls.
Topics: openchart-feature-catalog, registration, frappe, patient-groups
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-032 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Group enrollment review** — Periodically confirm that time-limited or criteria-based memberships remain appropriate.

## Focus

Manage deliberate patient group membership without turning ad hoc tags into hidden clinical classifications.

## Behavior

- Authorized staff enroll a patient into a named group with purpose, criteria basis, source, and effective dates.
- Groups declare whether membership is operational, programmatic, research-screening, or another configured type.
- Sensitive group names and membership are hidden from unauthorized search and list views.
- Automatic suggestions may be shown but require human acceptance before enrollment.
- Withdrawal or expiry ends membership and records reason without deleting history.
- Group membership never creates clinical action, consent, or research participation by itself.

## Frappe realization

- **DocTypes:** `OC Patient Group` and `OC Patient Group Membership` with purpose, type, criteria_reference, validity, sensitivity, and source.
- **Workflow:** Proposed → Active → Ended, Withdrawn, or Rejected.
- **Roles/permissions:** group-specific Frappe Roles and User Permissions; `OC Registration Supervisor` enrolls operational groups; sensitive membership at permlevel 2.
- **API/surfaces:** `open_chart.api.v1.registration.manage_group_membership`; group roster, patient badge, Kanban, and membership audit report.

## Boundaries

Owns: explicit patient group enrollment lifecycle. Consumes: group definitions and authorized decisions. Emits: permission-aware membership facts. Does not own: cohort inference, research consent, or care-plan execution.

## Open questions

- Which group types belong in registration rather than population-health tooling?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
