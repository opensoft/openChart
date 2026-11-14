# Registry Query At Patient Registration — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Queues a consent-aware immunization registry query during registration and routes identity or response exceptions for review.
Topics: openchart-feature-catalog, public-health, frappe, registry-query
Repository context: openChart — Frappe v15 native EMR; catalog entry PUB-009 (Immunizations Public Health Screenings And Registries)
Captured: 2026-08-24

## Possible feats

- **Previsit history readiness** — Complete registry retrieval before a scheduled vaccination visit.

## Focus

An asynchronous registration trigger for state registry retrieval without blocking patient creation.

## Behavior

- Registration staff see whether patient jurisdiction, consent, and minimum demographics permit a query.
- Eligible registration completion creates an idempotent queued request rather than making an inline network call.
- States are queued, sent, matched, no-match, ambiguous, failed, declined, and expired.
- Responses never write doses directly; candidates enter a reconciliation review with source provenance.
- Ambiguous identity matches expose minimum necessary comparison data only to authorized reviewers.
- Connector unavailability leaves registration complete and presents a retryable operational status.

## Frappe realization

- **DocTypes:** Add `OC Registry Query` with patient, jurisdiction, consent reference, idempotency key, request state, and connector correlation ID.
- **Hooks:** After accepted registration, enqueue an rq job when site policy permits; use retries with bounded backoff and no PHI in logs.
- **Permissions:** Restrict payload and match review to `OC Registry Exchange User`; registration users see only safe status fields.
- **API and surfaces:** Add connector-neutral `open_chart.api.v1.request_registry_query`, realtime status updates, and an exception Query Report.

## Boundaries

Owns: query orchestration and status. Consumes: registration, consent, jurisdiction, and connector profile. Emits: sourced response candidates. Does not own: patient registration, external matching, or reconciliation acceptance.

## Open questions

- Which jurisdictions require explicit opt-in rather than treatment-based query authority?

## Relationships

[Synthesis: Immunizations Public Health And Registries](openchart-feature-catalog-synthesis-pub.md)
