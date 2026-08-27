# Pre-Visit Technology Check — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets patients test browser, devices, permissions, and connectivity before a virtual appointment without entering its clinical room.
Topics: openchart-feature-catalog, telehealth, frappe, previsit-tech-check
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-022 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Assisted test call** — Schedule a staff-led practice session that contains no clinical encounter content.

## Focus

This feature isolates reusable technical readiness testing before the appointment's arrival window.

## Behavior

- An authorized portal user can start a test from appointment instructions without receiving a clinical-room credential.
- The test checks secure browser support, camera preview, microphone loopback, speaker output, permissions, and connection quality.
- Each check returns pass, warning, fail, or skipped with plain-language remediation.
- The patient can repeat checks, change devices, or request assistance without altering appointment state.
- The appointment stores only readiness status, policy version, completion time, and redacted failure categories.
- Passing never guarantees clinical eligibility, while failure never cancels the appointment automatically.

## Frappe realization

- **DocTypes:** `OC Technology Check` and child `OC Technology Check Result` store appointment link, client policy, check type, normalized outcome, support request, and expiry.
- **Portal/API:** `www/telehealth/test` runs local checks and submits redacted outcomes through a guarded method; no room grant or chart data is exposed.
- **Automation/surfaces:** Notifications invite testing, Telehealth Support receives assignments for requested help, and appointment badges show fresh, stale, or incomplete readiness.

## Boundaries

Owns: nonclinical readiness assessment and support handoff. Consumes: browser/device signals and client policy. Emits: redacted readiness status. Does not own: media session or appointment cancellation.

## Open questions

- How far before a visit does a successful test remain meaningful across browser, network, and platform changes?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
