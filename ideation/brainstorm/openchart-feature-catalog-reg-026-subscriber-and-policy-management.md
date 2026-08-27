# Subscriber and Policy Management — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Associates coverage with the correct subscriber, policy relationship, and policy dates without granting unrelated chart authority.
Topics: openchart-feature-catalog, registration, frappe, subscriber-policy
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-026 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Dependent consistency checks** — Flag relationship or birth-date mismatches before coverage handoff.

## Focus

Represent the patient-to-subscriber relationship and policy facts as a distinct registration capability.

## Behavior

- Staff identify whether the patient is self, spouse, child, other dependent, or an allowed configured relationship.
- A subscriber may link to the patient, a related person, or a minimal external identity record.
- The policy stores member and group references, effective dates, and dependent sequence where known.
- Relationship conflicts or an underage self-subscriber warn and require confirmation or correction.
- Subscriber changes create a new effective record rather than rewriting historical coverage.
- Subscriber status grants no proxy access, consent authority, or guarantor status automatically.

## Frappe realization

- **DocTypes:** `OC Coverage Subscriber` with Dynamic Link identity, coverage, relationship, policy fields, validity, and provenance.
- **Workflow:** Draft → Confirmed → Superseded or Disputed.
- **Roles/permissions:** `OC Registration Clerk` records; `OC Coverage Reviewer` confirms conflicts; identifiers use permlevel 2.
- **API/surfaces:** `open_chart.api.v1.registration.set_coverage_subscriber`; coverage relationship panel and subscriber-conflict report.

## Boundaries

Owns: subscriber identity and policy relationship. Consumes: coverage and related-person identities. Emits: dated subscriber snapshot. Does not own: guardianship, guarantor responsibility, or payer adjudication.

## Open questions

- What minimum external-subscriber data may be retained when the subscriber is not a patient?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
