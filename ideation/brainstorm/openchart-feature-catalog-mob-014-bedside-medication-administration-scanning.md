# Bedside Medication Administration Scanning — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Uses patient and medication barcode scans to support a closed-loop bedside administration check and attributable outcome documentation.
Topics: openchart-feature-catalog, mobile-devices, frappe, medication-scanning
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-014 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Multi-package dose assembly** — Track several scanned packages that together satisfy one scheduled dose.

## Focus

This feature isolates mobile scan orchestration around an existing medication order and administration authority.

## Behavior

- A nurse selects a due administration, scans the current wristband, then scans each medication package.
- The server compares patient, active order, product code, dose, route, time window, prior status, and package state.
- Match, caution, hard stop, unavailable, and override-required outcomes are explicit and source-linked.
- An authorized override requires reason, second check when configured, and post-event review.
- Administration, held, refused, omitted, partial, and not-given outcomes remain distinct.
- Offline operation requires a signed administration manifest and queues the result as pending server acceptance.
- Camera frames and full barcode strings are not retained beyond decoding and minimum audit need.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Medication Administration Check` with order, schedule, patient check, product identifiers, dose components, decision, override, and resulting administration link.
- **Workflow and roles:** Ready → Verified → Administered/Held/Refused/Omitted/Partial/Needs Review; `OC Nurse` acts and `OC Medication Safety Reviewer` reviews overrides.
- **API and auth:** Token-authenticated `open_chart.api.v1.mobile.medication_check` and `record_administration` call guarded medication APIs with idempotency and current-version checks.
- **Realtime and jobs:** Websocket updates refresh due-dose state; server-side RQ jobs reconcile offline results, route overrides, and detect duplicate pending submissions.
- **Files and surfaces:** Package photos are excluded by default; approved exception evidence uses private Frappe file attachment APIs, with a bedside mobile view and Desk review report.

## Boundaries

Owns: scan sequence, verification evidence, and mobile outcome handoff. Consumes: orders, schedules, patient check, formulary identifiers, and policy. Emits: administration intent or exception. Does not own: prescribing, pharmacy dispensing, or autonomous administration approval.

## Open questions

- Which mismatch classes are absolute stops versus reviewable overrides at each care setting?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
