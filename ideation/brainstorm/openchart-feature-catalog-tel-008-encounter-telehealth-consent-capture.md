# Encounter Telehealth Consent Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures patient or authorized representative agreement to telehealth terms for the specific encounter.
Topics: openchart-feature-catalog, telehealth, frappe, encounter-consent
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-008 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Comprehension confirmation** — Add accessible teach-back prompts for policies that require more than acknowledgment.

## Focus

This feature isolates the consent ceremony and accepted artifact for one virtual encounter.

## Behavior

- The patient or validated representative receives the effective telehealth disclosure before joining clinical media.
- The presentation records language, format, policy version, and accessibility accommodation.
- The signer may agree, decline, or request staff explanation; no preselected acceptance is allowed.
- Agreement records signer identity, authority, timestamp, encounter, and attestation wording.
- Decline blocks video admission and offers approved alternatives without cancelling the encounter automatically.
- Material policy changes invalidate incomplete ceremonies but never rewrite an already accepted consent artifact.

## Frappe realization

- **DocTypes/workflow:** submittable `OC Telehealth Consent` links encounter, subject, representative authority, disclosure version, language, signature method, and decision; amendments use succession.
- **Surfaces/API:** a portal Web Form and assisted Desk form submit through `open_chart.api.v1.telehealth.record_consent`; Jinja Print Format renders the signed artifact.
- **Permissions:** Patient and Proxy roles act only within verified authority; Telehealth Staff may witness but not substitute consent; Audit Reviewer has immutable read access.

## Boundaries

Owns: encounter-level telehealth agreement or decline. Consumes: disclosure policy, identity, and representative authority. Emits: consent artifact and gate result. Does not own: general treatment consent.

## Open questions

- Which jurisdictions and services permit standing consent versus requiring encounter-by-encounter renewal?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
