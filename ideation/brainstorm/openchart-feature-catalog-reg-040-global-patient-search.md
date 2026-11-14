# Global Patient Search — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides fast, privacy-aware patient discovery across names, identifiers, demographics, contacts, and historical identity facts.
Topics: openchart-feature-catalog, registration, frappe, patient-search
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-040 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Search explanation panel** — Show authorized users which normalized fields produced each candidate.

## Focus

Make finding the correct patient a deliberate identification workflow rather than an unrestricted text lookup.

## Behavior

- Users search by name, date of birth, MRN, external identifier, phone, email, or configured combinations.
- Results show enough distinguishing facts to select safely while masking sensitive values.
- Prior-name and normalized-contact matches are labeled so users understand why the record appeared.
- Confidential and VIP policies hide, mask, or acknowledgment-gate results consistently.
- Ambiguous searches encourage additional criteria and never auto-open the top result.
- Every sensitive identifier lookup records actor, purpose, query type, and result count without logging raw secrets.

## Frappe realization

- **DocTypes:** search projections from `OC Patient`, names, contacts, addresses, and identifiers; `OC Patient Search Audit` stores redacted metadata.
- **Workflow:** no document workflow; guarded permission and purpose checks execute for every query and selection.
- **Roles/permissions:** `OC Registration Clerk` and clinical roles receive scope-specific result fields through User Permissions and privacy flags.
- **API/surfaces:** `open_chart.api.v1.registration.patient_search`; custom Desk search page, Quick Entry precheck, and keyboard-accessible result list.

## Boundaries

Owns: patient discovery query and safe result presentation. Consumes: indexed identity facts and access policy. Emits: selected patient reference and search audit. Does not own: duplicate adjudication or chart access authorization after selection.

## Open questions

- Which minimum criteria should be required for broad-name searches in large sites?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
