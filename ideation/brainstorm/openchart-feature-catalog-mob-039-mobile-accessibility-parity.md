# Mobile Accessibility Parity — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Establishes tested VoiceOver and TalkBack parity for critical mobile workflows, including scanning, offline states, signatures, messaging, and device readings.
Topics: openchart-feature-catalog, mobile-devices, frappe, mobile-accessibility
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-039 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Accessible workflow evidence pack** — Publish repeatable test scripts and results for each supported mobile release.

## Focus

This entry isolates accessibility as a release-gated functional contract rather than visual polish.

## Behavior

- Every critical workflow has keyboard, switch-control, VoiceOver, and TalkBack navigation expectations.
- Controls expose meaningful names, roles, values, errors, progress, and state changes in logical focus order.
- Dynamic sync, scan, recording, waiting-room, and conflict states announce changes without trapping focus.
- Text scales without loss of actions, clipping, or forced orientation; contrast and target size meet adopted criteria.
- Camera-dependent workflows offer equivalent manual or assisted paths when clinically safe.
- Accessibility settings persist per user without weakening authorization or shared-device cleanup.
- A release cannot claim parity when a documented critical flow fails on a supported OS and assistive technology version.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Mobile Accessibility Flow`, `OC Accessibility Test Run`, and child results with platform, OS, app build, assistive technology, steps, outcome, and evidence.
- **Workflow and roles:** Draft → Tested → Passed/Failed/Waived → Superseded; `OC Accessibility Tester` records evidence and `OC Release Approver` accepts time-limited waivers.
- **API and auth:** Token-authenticated test-fixture methods under `open_chart.api.v1.mobile.accessibility` provide synthetic data only; production auto-REST remains permission-bound.
- **Realtime and jobs:** Websocket announcements follow an accessible event schema; server-side RQ jobs aggregate release coverage and expire waivers.
- **Files and surfaces:** Test recordings and reports use private Frappe file attachment APIs with synthetic fixtures; Desk dashboards gate releases by critical-flow status.

## Boundaries

Owns: mobile accessibility contract, test evidence, and release status. Consumes: workflow definitions, supported platforms, and assistive technologies. Emits: pass, fail, or governed waiver. Does not own: OS accessibility implementation or clinical workflow semantics.

## Open questions

- Which flows are release-blocking on day one, and what evidence is required for a temporary waiver?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
