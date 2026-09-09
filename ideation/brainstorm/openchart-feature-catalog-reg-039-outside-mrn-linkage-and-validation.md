# Outside MRN Linkage and Validation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Validates and links outside medical record numbers to the correct facility authority before they become trusted exchange keys.
Topics: openchart-feature-catalog, registration, frappe, outside-mrn
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-039 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Source-system confirmation adapters** — Verify MRNs against authorized external directory or exchange endpoints.

## Focus

Apply MRN-specific validation, facility scoping, and review on top of the general external identifier registry.

## Behavior

- Staff select the outside facility and enter or import its MRN with source evidence.
- Format and checksum rules run for the selected assigning authority when configured.
- A matching MRN on another local patient creates a blocking identity-conflict case.
- Unreachable source systems leave the linkage Provisional rather than falsely verified.
- A reviewer can confirm, reject, or mark the MRN entered in error with reason.
- Consumers receive authority-qualified MRNs and cannot search by value without appropriate permission.

## Frappe realization

- **DocTypes:** `OC Outside MRN Validation` linked to `OC Patient External Identifier`, facility, evidence, validation_method, result, and checked_on.
- **Workflow:** Draft → Validation Pending → Verified, Provisional, Conflict, or Rejected.
- **Roles/permissions:** `OC Registration Clerk` submits; `OC Identity Reviewer` resolves; `OC Integration User` may report automated checks.
- **API/surfaces:** `open_chart.api.v1.registration.validate_outside_mrn`; facility-scoped entry dialog and MRN-conflict worklist.

## Boundaries

Owns: outside-MRN validation and facility qualification. Consumes: external identifier and authority rules. Emits: trusted or provisional MRN linkage. Does not own: cross-system patient matching or data exchange.

## Open questions

- When may a provisional MRN be used to request outside records?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
