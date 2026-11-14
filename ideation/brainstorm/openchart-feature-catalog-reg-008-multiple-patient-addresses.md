# Multiple Patient Addresses — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Maintains purpose-specific patient addresses with validity periods so care and communication use the right location at the right time.
Topics: openchart-feature-catalog, registration, frappe, patient-addresses
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-008 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Seasonal address activation** — Select an address automatically within recorded seasonal intervals.

## Focus

Represent multiple current and historical addresses without flattening them into one mailing field.

## Behavior

- Staff add home, mailing, temporary, previous, billing-contact, or confidential addresses.
- Each address records use, effective dates, preferred flag, and whether mail is permitted.
- Only one preferred address per use can be active at a time.
- Overlapping temporary and home addresses are allowed when their uses differ.
- Ending an address preserves it for historical document interpretation.
- Address selection surfaces show purpose and confidentiality before a user confirms use.

## Frappe realization

- **DocTypes:** `OC Patient Address` linked to `OC Patient`, with use, lines, locality, region, postal_code, country, validity, preferred, and confidential.
- **Workflow:** Draft → Active → Inactive or Superseded, with validation preventing duplicate preferred uses.
- **Roles/permissions:** `OC Registration Clerk` maintains; `OC Privacy Officer` controls confidential addresses at permlevel 2.
- **API/surfaces:** `open_chart.api.v1.registration.upsert_address`; patient address grid, purpose-aware selector, and address-history report.

## Boundaries

Owns: patient address facts and usage metadata. Consumes: patient-reported locations. Emits: purpose-qualified addresses. Does not own: postal standardization or geocoding.

## Open questions

- Should confidential addresses be omitted or redacted on all default print formats?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
