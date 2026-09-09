# Prescription Status Tracking — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Presents a provenance-aware timeline of prescription transmission and pharmacy-reported states from signing through dispensing outcome.
Topics: openchart-feature-catalog, eprescribing, frappe, prescription-status
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-007 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Patient-safe status view** — Portal users could see selected operational states with uncertainty and contact guidance.

## Focus

This feature isolates status observation and reconciliation. It does not infer that a medication was taken merely because a pharmacy reports receipt or fill.

## Behavior

- Users see ordered, signed, queued, sent, received, rejected, cancelled, denied, ready, partially filled, filled, and unknown states when supported.
- Every state records source, source timestamp, receipt timestamp, correlation ID, and confidence.
- Out-of-order or conflicting updates remain visible and are reconciled by deterministic rules without deleting evidence.
- Transport acknowledgements are distinguished from pharmacy workflow and dispensing events.
- Prolonged unknown, rejected, or contradictory states create worklist exceptions for authorized staff.
- Portal rendering uses patient-safe labels and clearly states that fill status does not establish administration or adherence.

## Frappe realization

- **DocTypes:** Append-only `OC Prescription Status Event` links `OC Prescription`; a derived read model stores current operational state and reason.
- **Permissions/API:** Network callbacks use authenticated idempotent v1 methods; clinical and portal reads apply field-level permissions and consent checks.
- **Hooks:** `after_insert` recomputes the derived state, publishes websocket updates, and opens exceptions for configured conditions.
- **Surfaces:** Prescription timeline, list indicators, status Query Report, dashboard Number Cards, and portal component provide role-specific views.

## Boundaries

Owns: observed status events and derived operational state. Consumes: local workflow and authenticated network updates. Emits: timelines, exceptions, and patient-safe status. Does not own: adherence, administration, or pharmacy inventory truth.

## Open questions

- Which external status vocabularies can be normalized without losing network-specific meaning?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [NewRx Electronic Prescription Routing](openchart-feature-catalog-phr-001-newrx-electronic-prescription-routing.md)
