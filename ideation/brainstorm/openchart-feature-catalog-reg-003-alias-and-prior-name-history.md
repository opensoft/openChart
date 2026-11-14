# Alias and Prior Name History — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Preserves aliases and prior names with provenance so historical records and patient searches remain correctly attributable.
Topics: openchart-feature-catalog, registration, frappe, name-history
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-003 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Historical document reconciliation** — Suggest prior-name matches when imported documents cannot resolve the current name.

## Focus

Maintain append-only name history without treating every alias as a current display name.

## Behavior

- Authorized staff add maiden, former, alias, transliterated, or unknown-use names.
- Each entry records effective interval, source, verification level, and free-text rationale.
- Closing a current name creates succession history rather than mutating the accepted fact.
- Search results identify that a hit matched a prior name and still display the current identity.
- Conflicting overlapping legal-name intervals route to identity review.
- Users without sensitive-history permission see only current names and a generic match indicator.

## Frappe realization

- **DocTypes:** append-only `OC Patient Name` records linked to `OC Patient`, with name_use, valid_from, valid_to, evidence, and supersedes.
- **Workflow:** Proposed → Verified → Superseded or Rejected, with succession links and Version history.
- **Roles/permissions:** `OC Identity Reviewer` verifies; `OC Registration Clerk` proposes; sensitive aliases use permlevel 2.
- **API/surfaces:** `open_chart.api.v1.registration.add_name_history`; patient identity timeline and permission-aware global-search expansion.

## Boundaries

Owns: historical and alternate patient names. Consumes: verified name changes. Emits: search aliases and provenance links. Does not own: legal-document retention policy.

## Open questions

- Which alias categories require restricted visibility by default?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
