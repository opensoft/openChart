# Licensure And Patient Location Check — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Checks the patient's declared care location against provider authority and service rules before booking and again at arrival.
Topics: openchart-feature-catalog, telehealth, frappe, jurisdiction-eligibility
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-007 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Coverage gap routing** — Offer human-reviewed alternatives when no eligible virtual provider is available.

## Focus

This feature isolates jurisdiction eligibility for virtual care; it does not grant or adjudicate professional licensure.

## Behavior

- Booking asks the patient for the physical location where care will be received and explains why it matters.
- Eligibility uses effective-dated provider authority, facility policy, service type, and declared jurisdiction.
- Unknown, unsupported, or expiring authority blocks confirmation and creates a staff-reviewable reason code.
- At join, the patient reconfirms location; a changed jurisdiction triggers re-evaluation before admission.
- Browser geolocation may corroborate only with explicit permission and never silently overrides the declaration.
- Overrides require an authorized reviewer, reason, evidence reference, and expiry; they cannot fabricate provider authority.

## Frappe realization

- **DocTypes:** `OC Telehealth Jurisdiction Policy`, `OC Provider Authority Evidence`, and `OC Visit Location Attestation` store effective dates, regions, service constraints, source, and review state.
- **API/hooks:** booking and arrival call one versioned eligibility method; `validate` prevents confirmation or admission when the accepted result is ineligible.
- **Roles/reports:** Credentialing Reviewer maintains evidence, Scheduler sees actionable eligibility only, and Audit Reviewer can run an effective-date Script Report.

## Boundaries

Owns: location declaration and policy evaluation. Consumes: provider authority evidence and service policy. Emits: eligible, ineligible, or review-required result. Does not own: credential issuance or legal interpretation.

## Open questions

- What authoritative sources and refresh cadence are required for provider authority evidence?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
