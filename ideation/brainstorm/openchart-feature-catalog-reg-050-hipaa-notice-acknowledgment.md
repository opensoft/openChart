# HIPAA Notice Acknowledgment — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records delivery and acknowledgment of the applicable privacy notice without misrepresenting acknowledgment as consent.
Topics: openchart-feature-catalog, registration, frappe, privacy-notice
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-050 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Notice-version renewal queue** — Identify patients whose next registration should present a materially revised notice.

## Focus

Prove which privacy notice was offered and what acknowledgment outcome occurred.

## Behavior

- Staff present the facility-approved notice version in an available preferred language and accessible format.
- The record captures delivery channel, time, recipient, signer relationship, version, and acknowledgment outcome.
- Refusal to sign records good-faith delivery steps and is not converted into acceptance.
- An authorized representative's acknowledgment links to the authority used at presentation time.
- Revised notices can trigger re-presentation according to policy without invalidating prior evidence.
- The UI and print format state that acknowledgment is not authorization for unrelated disclosure or treatment.

## Frappe realization

- **DocTypes:** submittable `OC Privacy Notice Acknowledgment` with notice version, recipient, authority, channel, outcome, evidence, and presented_on.
- **Workflow:** Due → Presented → Acknowledged, Refused, Unable, or Deferred.
- **Roles/permissions:** `OC Registration Clerk` presents; `OC Privacy Officer` manages templates and audits exceptions; patient can view own receipt.
- **API/surfaces:** `open_chart.api.v1.registration.record_privacy_notice`; registration prompt, portal acknowledgment, receipt print format, and due report.

## Boundaries

Owns: privacy-notice delivery and acknowledgment evidence. Consumes: approved notice version and recipient authority. Emits: presentation outcome and receipt. Does not own: privacy consent or disclosure authorization.

## Open questions

- What constitutes a material notice change requiring re-presentation?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
