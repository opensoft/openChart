# Legal and Preferred Name Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Separates legal, preferred, and display names so staff can identify patients accurately while addressing them respectfully.
Topics: openchart-feature-catalog, registration, frappe, patient-names
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-002 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Context-aware display name** — Render legal or preferred names according to operational need and permission.

## Focus

Capture current legal and preferred names as distinct, validated identity facts.

## Behavior

- Registration Clerk records legal given, middle, family, suffix, and preferred names independently.
- The UI previews the formal label and patient-facing display label before save.
- Legal-name changes require effective date, source, and supporting-document status.
- Preferred-name changes do not overwrite legal-name history.
- Search indexes both legal and preferred names while labeling match context.
- Missing legal-name components require an explicit unknown or single-name reason rather than filler text.

## Frappe realization

- **DocTypes:** fields on `OC Patient` plus child `OC Patient Name` with use, components, effective dates, source, and active flag.
- **Workflow:** proposed legal change routes Pending Review → Accepted or Rejected; preferred-name updates may accept immediately by policy.
- **Roles/permissions:** `OC Registration Clerk` proposes; `OC Registration Supervisor` approves legal changes; restricted history at permlevel 1.
- **API/surfaces:** `open_chart.api.v1.registration.update_names`; patient Quick Entry, identity panel, global-search formatter, and label print format.

## Boundaries

Owns: current name uses and display derivation. Consumes: identity evidence and change authority. Emits: searchable name facts and audit events. Does not own: external identifier assignment.

## Open questions

- Should clinic policy choose preferred name or legal name as the default wristband label?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
