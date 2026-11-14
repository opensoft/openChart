# Consent to Treat Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures a versioned consent-to-treat decision with signer authority, scope, evidence, dates, and withdrawal handling.
Topics: openchart-feature-catalog, registration, frappe, consent-to-treat
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-049 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Context-specific consent bundles** — Assemble reviewed forms by facility and service while preserving each consent as a distinct decision.

## Focus

Record the registration consent artifact and authority chain without implying consent for unspecified services.

## Behavior

- Staff present the current approved document version in the patient's preferred available language.
- The signer is identified as patient or authorized representative with linked authority determination.
- The record captures scope, effective dates, presentation method, questions answered, signature evidence, and witness if required.
- Decline or inability to consent routes to an authorized reviewer and does not fabricate acceptance.
- Withdrawal creates a dated successor state and does not erase prior lawful reliance.
- Consumers must check scope and validity for the requested context rather than only a yes/no field.

## Frappe realization

- **DocTypes:** submittable `OC Consent To Treat` with template_version, signer, authority, scope, validity, decision, private signature, and supersedes.
- **Workflow:** Draft → Presented → Accepted, Declined, or Review Required → Withdrawn or Expired.
- **Roles/permissions:** `OC Registration Clerk` presents; `OC Authority Reviewer` resolves signer issues; `OC Privacy Officer` audits at permlevel 2.
- **API/surfaces:** `open_chart.api.v1.registration.record_consent_to_treat`; signature surface, patient consent timeline, and Jinja print format.

## Boundaries

Owns: consent-to-treat artifact and lifecycle. Consumes: approved template, signer identity, and authority. Emits: scope-qualified consent decision. Does not own: treatment plan or procedure-specific consent.

## Open questions

- Which service contexts require separate treatment-consent scopes instead of one registration consent?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
