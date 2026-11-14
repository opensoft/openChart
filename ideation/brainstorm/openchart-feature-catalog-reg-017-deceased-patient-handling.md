# Deceased Patient Handling — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Applies a verified deceased status with provenance and safeguards so workflows stop inappropriate outreach without erasing the chart.
Topics: openchart-feature-catalog, registration, frappe, deceased-status
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-017 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Downstream suppression registry** — Publish a controlled event for portals, reminders, and integrations to stop routine contact.

## Focus

Govern the transition to deceased status, including correction of erroneous reports.

## Behavior

- Authorized staff record date, precision, source, place, and verification status of death.
- An unverified report places a visible warning but does not finalize the deceased state.
- Verification disables routine portal invitations, reminders, and registration intake while preserving authorized chart access.
- Conflicting dates or an active encounter create a supervisor task before finalization.
- Incorrect deceased status is corrected through a documented reversal, never field deletion.
- Surviving-family contact and disclosure remain separate from the patient's prior communication preferences.

## Frappe realization

- **DocTypes:** `OC Deceased Status` linked to `OC Patient`, with date, precision, source, evidence, verified_by, and reversal_of.
- **Workflow:** Reported → Verification Pending → Confirmed or Rejected; Confirmed → Reversal Review → Reversed.
- **Roles/permissions:** `OC Registration Clerk` reports; `OC Identity Reviewer` confirms; `OC Privacy Officer` reviews disclosures.
- **API/surfaces:** `open_chart.api.v1.registration.report_death` and `.resolve_death_report`; patient banner, verification queue, and suppression hook events.

## Boundaries

Owns: patient deceased-state lifecycle. Consumes: reported or verified death evidence. Emits: confirmed-status and reversal events. Does not own: estate authority or bereavement communication.

## Open questions

- Which external sources qualify for automatic evidence ingestion but still require human confirmation?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
