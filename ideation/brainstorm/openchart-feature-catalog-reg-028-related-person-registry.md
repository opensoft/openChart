# Related Person Registry — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Maintains people related to a patient with relationship type, dates, contact data, provenance, and no implied authority.
Topics: openchart-feature-catalog, registration, frappe, related-persons
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-028 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Household relationship map** — Visualize linked people while respecting confidential and disputed relationships.

## Focus

Create reusable related-person identities from which emergency, guardian, guarantor, or proxy roles may be explicitly granted.

## Behavior

- Staff record person name, relationship, contact points, addresses, effective dates, and source.
- A related person may link to another `OC Patient` without exposing that person's chart.
- Relationship type alone grants no access, consent, financial, or decision authority.
- Duplicate related-person candidates are shown before creation using limited identifying facts.
- Disputed or ended relationships remain historical and are excluded from active selectors.
- Confidential relationships are hidden from users without explicit permission.

## Frappe realization

- **DocTypes:** `OC Related Person` and `OC Patient Relationship` with optional patient link, type, validity, status, source, and confidentiality.
- **Workflow:** Draft → Active → Disputed, Ended, or Superseded.
- **Roles/permissions:** `OC Registration Clerk` maintains; `OC Privacy Officer` controls confidential rows at permlevel 2.
- **API/surfaces:** `open_chart.api.v1.registration.upsert_related_person`; patient relationship grid, quick-create dialog, and duplicate warning.

## Boundaries

Owns: related-person identity and descriptive relationship. Consumes: patient-reported relationship facts. Emits: reusable person link. Does not own: guardianship, proxy access, consent, or guarantor authority.

## Open questions

- When should a related person be promoted to a full patient identity rather than linked later?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
