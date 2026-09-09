# Emergency Contact Management — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Records ranked emergency contacts with relationship, reachability, and disclosure constraints for safe use during urgent events.
Topics: openchart-feature-catalog, registration, frappe, emergency-contacts
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-012 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Emergency contact drill** — Periodically prompt patients to confirm that priority and contact details remain current.

## Focus

Maintain contacts for urgent notification without treating them automatically as guardians or proxies.

## Behavior

- Staff record contact identity, relationship, priority, endpoints, language, and effective dates.
- The patient specifies whether the contact may receive location, condition, or no clinical detail.
- At least one reachable endpoint is required before a contact becomes active.
- Staff can record unsuccessful attempts without changing the underlying contact point.
- Expired or withdrawn contacts remain in history and are excluded from current emergency lists.
- The UI states clearly that emergency-contact status grants no consent or decision authority.

## Frappe realization

- **DocTypes:** `OC Emergency Contact` linked to `OC Patient` and optionally `OC Related Person`, with priority, disclosure_scope, and contact rows.
- **Workflow:** Draft → Active → Inactive or Withdrawn, with succession history.
- **Roles/permissions:** `OC Registration Clerk` maintains; `OC Clinical User` reads active contacts; disclosure scope is permlevel 1.
- **API/surfaces:** `open_chart.api.v1.registration.update_emergency_contact`; patient emergency panel, printable emergency list, and stale-contact report.

## Boundaries

Owns: emergency notification contacts and allowed disclosure scope. Consumes: relationship and endpoint facts. Emits: ranked urgent-contact instructions. Does not own: guardianship, proxy access, or consent authority.

## Open questions

- Should emergency contacts require periodic reconfirmation at every registration encounter?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
