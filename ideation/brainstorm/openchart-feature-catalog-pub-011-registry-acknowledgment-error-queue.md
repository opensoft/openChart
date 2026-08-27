# Registry Acknowledgment And Error Queue — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Correlates registry acknowledgments with submissions and routes rejected or unconfirmed messages to an accountable remediation queue.
Topics: openchart-feature-catalog, public-health, frappe, registry-acknowledgment
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-011 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Error-pattern guidance** — Suggest profile-specific remediation from governed mappings without changing records automatically.

## Focus

Closed-loop operational handling of registry acceptance, rejection, and missing acknowledgment.

## Behavior

- Inbound acknowledgments correlate by destination, control ID, and submission correlation ID.
- Accepted, accepted-with-warning, rejected, unmatched, and timeout outcomes remain separately visible.
- Field-level errors identify the source value and profile rule without exposing full payloads broadly.
- Assigned users may retry, cancel, escalate, or request clinical correction with a reason.
- A clinical correction creates a successor record; exchange staff cannot edit accepted clinical content.
- Missing or duplicate acknowledgments create safe exceptions and never falsely mark delivery accepted.

## Frappe realization

- **DocTypes:** Add `OC Registry Acknowledgment` and `OC Registry Exchange Exception` linked to submission and protected response artifact.
- **Workflow:** Use open, assigned, awaiting-clinical-correction, retry-ready, resolved, and waived states with Assignment Rules and SLAs.
- **Permissions:** Restrict payloads to `OC Registry Exchange User`; let clinicians view only correction requests tied to their patients.
- **Hooks and surfaces:** Parse responses in background jobs, update submission state idempotently, and provide Kanban plus aging Query Reports.

## Boundaries

Owns: acknowledgment correlation and remediation state. Consumes: submissions and connector responses. Emits: accepted status, retries, and correction requests. Does not own: clinical corrections or external registry behavior.

## Open questions

- When may an accepted-with-warning result count as operationally complete?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
