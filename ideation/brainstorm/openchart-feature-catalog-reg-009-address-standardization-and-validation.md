# Address Standardization and Validation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Validates and optionally standardizes entered addresses while preserving the patient's original wording and user control.
Topics: openchart-feature-catalog, registration, frappe, address-validation
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-009 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Pluggable postal providers** — Configure country-specific validators without coupling records to one vendor.

## Focus

Separate address-quality evidence from the authoritative patient-reported address.

## Behavior

- Validation runs on demand or before an address becomes preferred.
- The user sees entered, standardized, and provider-returned components side by side.
- Staff may accept the suggestion, retain the entered form with reason, or mark validation unavailable.
- Apartment and rural-route details cannot be dropped silently by normalization.
- Each result records provider, timestamp, confidence, and response code.
- Provider failure does not erase input or block urgent registration unless clinic policy requires it.

## Frappe realization

- **DocTypes:** `OC Address Validation` linked to `OC Patient Address`, with original_json, suggestion_json, provider, confidence, and disposition.
- **Workflow:** Requested → Suggested → Accepted, Retained as Entered, or Unavailable.
- **Roles/permissions:** `OC Registration Clerk` requests and decides; `OC Registration Supervisor` configures required thresholds.
- **API/surfaces:** `open_chart.api.v1.registration.validate_address` queues provider calls; address comparison dialog and validation exception report.

## Boundaries

Owns: validation evidence and standardization choice. Consumes: an entered address and configured provider. Emits: qualified normalized components. Does not own: patient address lifecycle.

## Open questions

- Which validation providers can support offline or low-connectivity clinics?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
