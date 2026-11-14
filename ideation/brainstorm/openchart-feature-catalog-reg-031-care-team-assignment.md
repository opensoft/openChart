# Care Team Assignment — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Assigns accountable practitioners and teams to a patient by role, scope, facility, and effective period.
Topics: openchart-feature-catalog, registration, frappe, care-team
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-031 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Assignment gap detection** — Flag patients missing a required accountable role under clinic policy.

## Focus

Represent operational care-team responsibility separately from patient provider preference.

## Behavior

- Authorized staff assign practitioner, team, role, facility scope, and effective dates.
- Roles distinguish primary clinician, care coordinator, nurse, and other configured responsibilities.
- Overlapping primary assignments warn and require a documented shared-care or replacement decision.
- Ending an assignment preserves history and future-dated assignments activate at their start time.
- Assignment changes notify affected users but do not create autonomous clinical tasks.
- Cross-facility users see assignments only when site permissions and patient authority permit.

## Frappe realization

- **DocTypes:** `OC Patient Care Team Member` with practitioner/team link, role, facility, responsibility, rank, validity, and source.
- **Workflow:** Proposed → Active → Ended or Superseded, with supervisor review for primary-role conflicts.
- **Roles/permissions:** `OC Registration Supervisor` and `OC Care Coordinator` assign; clinical users read within User Permissions.
- **API/surfaces:** `open_chart.api.v1.registration.assign_care_team`; patient team panel, practitioner patient list, and assignment-gap Query Report.

## Boundaries

Owns: patient-level care-team assignment. Consumes: practitioner and facility directories. Emits: accountable-team roster and change events. Does not own: schedules, orders, or provider preference.

## Open questions

- Which roles may self-assign, and which require supervisor approval?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
