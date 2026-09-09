# Patient Home Device Feeds — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Ingests patient-home weight-scale and glucometer feeds through governed account linking, provenance, deduplication, and clinical review queues.
Topics: openchart-feature-catalog, mobile-devices, frappe, home-device-feeds
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-029 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Measurement-plan adherence view** — Compare expected and received readings without autonomously changing care.

## Focus

This entry isolates longitudinal home-device ingestion and keeps consumer-platform identity separate from patient matching.

## Behavior

- Staff or patients link an approved vendor account through explicit consent and patient matching.
- The connection declares device types, measurement scope, start date, sharing status, and revocation path.
- Each reading preserves vendor, device, source identifier, measured time, received time, raw unit, and transformations.
- Duplicate readings are idempotently recognized; corrected or deleted vendor records create provenance events.
- Unassigned, impossible, stale, or unit-ambiguous readings enter review and never silently attach to a patient.
- Patients can see connection and last-received state and revoke future import.
- Thresholds may create human review tasks but do not autonomously diagnose or alter treatment.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Home Device Connection` and `OC Home Device Reading Intake` with patient, vendor subject hash, consent, scopes, device, values, provenance, and state.
- **Workflow and roles:** Pending Link → Active → Suspended/Revoked; readings use Received → Matched → Accepted/Needs Review/Rejected.
- **API and auth:** Patient/app setup uses OAuth2 or token-authenticated `open_chart.api.v1.mobile.home_devices`; vendor webhooks use signed whitelisted endpoints and idempotency keys.
- **Realtime and jobs:** Websocket events update connection and review status; server-side RQ jobs poll adapters, normalize, deduplicate, route review, and retry safely.
- **Files and surfaces:** Vendor exports and consent evidence use private Frappe file attachment APIs; portal/mobile connection views and Desk intake reports enforce patient permissions.

## Boundaries

Owns: connection, feed provenance, match, and review intake. Consumes: patient consent, vendor identity, and observations. Emits: accepted source-labeled observations. Does not own: vendor devices, calibration, clinical interpretation, or autonomous alerts.

## Open questions

- Should weight and glucose feeds share one consent scope or require measurement-specific authorization?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
