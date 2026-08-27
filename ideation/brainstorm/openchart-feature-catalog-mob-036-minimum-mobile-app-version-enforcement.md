# Minimum Mobile App Version Enforcement — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enforces platform- and site-specific minimum mobile versions with warning, restricted, and blocked states plus emergency-safe transition rules.
Topics: openchart-feature-catalog, mobile-devices, frappe, version-enforcement
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-036 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Phased rollout rings** — Evaluate a release with synthetic and pilot cohorts before raising the minimum.

## Focus

This capability isolates compatibility and security gating without making updates unexpectedly destroy unsynced work.

## Behavior

- Each authenticated bootstrap compares platform, app build, OS, site, and channel with an effective version policy.
- Supported, update available, update required soon, restricted, blocked, and exception states have distinct messages.
- Security-critical blocks include reason, effective time, approved update route, and support contact.
- Pending offline work is synchronized or placed in governed recovery before a hard block whenever safely possible.
- Restricted mode may allow status, export-to-recovery, sign-out, and emergency reference while denying incompatible writes.
- Administrators can grant expiring device-specific exceptions with rationale and audit.
- Store propagation delays and staged releases are represented explicitly rather than treated as user fault.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Mobile Version Policy` and `OC Mobile Version Exception` with platform, channel, minimum, deadlines, mode, reason, scope, and effective period.
- **Workflow and roles:** Draft → Scheduled → Active → Superseded; `OC Mobile Release Manager` proposes and `OC Security Administrator` approves critical blocks.
- **API and auth:** Bootstrap and token refresh call `open_chart.api.v1.mobile.version_decision`; read-only REST policy access exposes no internal vulnerability detail.
- **Realtime and jobs:** Websocket events announce policy changes to active apps; server-side RQ jobs activate schedules, monitor adoption, and expire exceptions.
- **Files and surfaces:** Release notes and signed manifests use Frappe file attachment APIs; mobile remediation and Desk adoption dashboards avoid patient data.

## Boundaries

Owns: minimum-version decision and exceptions. Consumes: release metadata, security policy, app posture, and pending-work state. Emits: supported, warned, restricted, or blocked result. Does not own: app-store timing or OS updates.

## Open questions

- What restricted capabilities must remain available when a hard security update meets unsynced clinical work?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
