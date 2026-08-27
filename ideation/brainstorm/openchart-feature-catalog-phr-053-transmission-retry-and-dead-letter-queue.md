# Transmission Retry And Dead-Letter Queue — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Manages idempotent retry, reconciliation, escalation, and manual resolution for failed or indeterminate pharmacy-network messages.
Topics: openchart-feature-catalog, eprescribing, frappe, transmission-recovery
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-053 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Network health dashboard** — Operations could correlate failure classes and latency without exposing prescription content.

## Focus

This feature isolates transport recovery across NewRx, CancelRx, RxRenewal responses, ePA, and status messages. It prevents retries from creating duplicate clinical intent.

## Behavior

- Every outbound message receives an idempotency key, content digest, correlation ID, attempt count, and acknowledgement deadline.
- Transient failures retry under bounded backoff while permanent rejection enters staffed review immediately.
- Indeterminate outcomes require status inquiry or human reconciliation before a new message can be created.
- The queue distinguishes transport, authentication, schema, endpoint, network, and business rejection errors.
- Operations staff may retry the identical payload, reroute an operational task, or close with evidence but cannot edit signed content.
- Escalation thresholds notify accountable roles and preserve all attempts, responses, and manual actions.

## Frappe realization

- **DocTypes:** `OC Pharmacy Message` and child attempt events store direction, type, digest, keys, endpoint, state, errors, and correlation.
- **Jobs:** RQ background jobs implement bounded retries; `scheduler_events` detect acknowledgement timeouts and stale dead letters.
- **Roles/API:** `OC Pharmacy Integration Operator` manages transport actions; guarded methods enforce payload immutability and idempotency.
- **Surfaces:** Dead-letter worklist, network dashboard, retry action, and latency/error Script Reports expose operations.

## Boundaries

Owns: message transport state, retry policy, and exception reconciliation. Consumes: immutable payloads, adapters, and responses. Emits: attempts, alerts, and operational outcomes. Does not own: clinical content correction or external network availability.

## Open questions

- What message-specific acknowledgement deadlines and retry ceilings should ship as defaults?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [Prescription Status Tracking](openchart-feature-catalog-phr-007-prescription-status-tracking.md)
