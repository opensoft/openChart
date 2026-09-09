# Outbreak Response Mode — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Activates time-bounded outbreak protocols, rapid documentation surfaces, cohorts, and reporting queues under explicit incident governance.
Topics: openchart-feature-catalog, public-health, frappe, outbreak-response
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-037 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Incident command dashboard** — Combine aggregate throughput, resource, reporting, and unresolved-exception indicators.

## Focus

A temporary governed operating mode that changes workflow configuration without weakening clinical authority or audit.

## Behavior

- Incident leaders activate a protocol with condition/event scope, facilities, start/end time, roles, forms, and escalation rules.
- Users see only incident-specific shortcuts and defaults relevant to their assigned facility and role.
- Rapid forms retain patient identity, source, performer, timestamps, consent, and required safety fields.
- Protocol changes are versioned, approved, and effective-dated; prior event records retain their version.
- Expiry removes special defaults and permissions while leaving open tasks in a controlled closeout queue.
- The mode never bypasses guarded clinical writes, disclosure authority, or human review requirements.

## Frappe realization

- **DocTypes:** Add `OC Public Health Incident`, versioned `OC Outbreak Protocol`, child facility/role assignments, and protocol-event links.
- **Workflow:** Use draft, approved, active, suspended, closing, and closed incident states with dual authorization for activation.
- **Permissions:** Apply incident-scoped User Permissions and temporary roles managed through controlled hooks and expiry jobs.
- **Surfaces:** Deliver a dedicated Desk workspace, Quick Entry forms, realtime aggregate dashboard, and closeout Query Reports.

## Boundaries

Owns: temporary protocol activation and incident workflow context. Consumes: governed forms, roles, facilities, and reporting profiles. Emits: incident-tagged records and metrics. Does not own: emergency legal authority, diagnosis, or relaxed safety controls.

## Open questions

- Which protocol changes require two-person approval during urgent activation?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
