# Social Needs Screening at Registration — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Offers a consented, purpose-limited social-needs screening during registration and routes positive responses for human review without making diagnoses.
Topics: openchart-feature-catalog, registration, frappe, social-needs-screening
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-048 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Resource-navigation handoff** — Create a patient-approved referral request from a reviewed need.

## Focus

Capture optional registration-time screening responses while keeping clinical interpretation and intervention outside registration.

## Behavior

- The patient receives purpose, privacy, and voluntary-participation notice before the screening begins.
- Questions come from a versioned instrument and support patient, proxy, declined, and unable-to-answer states.
- Sensitive answers are stored separately from general demographics and excluded from routine registration printouts.
- Configured urgent responses create a high-priority human review task but never an autonomous intervention.
- Staff record whether the patient wants follow-up and the safest communication method.
- Amendments preserve the original accepted response set and create a successor submission.

## Frappe realization

- **DocTypes:** `OC Social Screening Submission` and child `OC Social Screening Response` with instrument_version, answer, source, consent, follow_up, and supersedes.
- **Workflow:** Draft → Submitted → Review Required, Reviewed, or Declined → Superseded.
- **Roles/permissions:** `OC Registration Clerk` offers; `OC Social Care Reviewer` reads sensitive responses at permlevel 2; patient sees own submission.
- **API/surfaces:** `open_chart.api.v1.registration.submit_social_screening`; portal/intake form, review worklist, and restricted Script Report.

## Boundaries

Owns: consented screening response and review routing. Consumes: versioned instrument and patient answers. Emits: human-review tasks and patient follow-up preference. Does not own: diagnosis, eligibility, or autonomous referral.

## Open questions

- Which instrument can be adopted without licensing constraints and with appropriate translations?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
