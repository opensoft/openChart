# Connection Diagnostics And Reconnect — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Detects virtual-visit connection problems, guides recovery, and preserves an auditable reconnect history.
Topics: openchart-feature-catalog, telehealth, frappe, connection-recovery
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-004 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Support-ready diagnostic bundle** — Generate a patient-approved, redacted snapshot for technical assistance.

## Focus

This feature isolates quality measurement and bounded recovery during an authorized media session.

## Behavior

- The client classifies connectivity as good, degraded, interrupted, or failed using adapter-normalized signals.
- Degradation presents plain-language actions such as stopping video, changing networks, or checking device permissions.
- An interruption starts bounded reconnect attempts with visible progress and a cancel option.
- Successful recovery retains participant identity and records a new connection interval rather than a second visit.
- Exhausted attempts offer staff contact and approved modality conversion without silently ending the clinical encounter.
- Diagnostic details visible to support exclude media payload, clinical content, and unnecessary network identifiers.

## Frappe realization

- **DocTypes:** child `OC Connection Interval` stores normalized state, timestamps, quality bands, recovery action, and adapter code on `OC Virtual Visit`.
- **Client/hooks:** browser listeners publish rate-limited telemetry; RQ jobs aggregate quality bands while websocket events notify the clinician console.
- **Permissions/reports:** Patient sees guidance, Telehealth Support sees redacted diagnostics, and Audit Reviewer sees transition provenance through a Script Report.

## Boundaries

Owns: normalized quality state and reconnect orchestration. Consumes: media-adapter telemetry. Emits: recovery events and redacted diagnostics. Does not own: network service or encounter disposition.

## Open questions

- What quality measurements can be normalized consistently across custom WebRTC and partner-embedded sessions?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
