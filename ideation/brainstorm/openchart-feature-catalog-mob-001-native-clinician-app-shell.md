# Native Clinician App Shell — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides a shared iOS and Android application shell for secure chart workflows, offline storage, device integrations, and governed release channels.
Topics: openchart-feature-catalog, mobile-devices, frappe, native-app-shell
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-001 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Capability plug-in registry** — Let governed mobile modules declare routes, permissions, offline needs, and device dependencies.

## Focus

This entry isolates the native application foundation rather than any one clinical workflow.

## Behavior

- Clinicians install a signed iOS or Android build from an approved distribution channel.
- The shell presents only capabilities enabled for the site, app version, role, and device posture.
- Deep links resolve to permission-checked in-app routes and never carry reusable credentials or clinical payloads.
- Local navigation remains usable during transient network loss and labels server-dependent actions clearly.
- Environment, tenant, build, and policy identities are visible in a support screen without exposing PHI.
- Unsupported operating systems or compromised builds enter a restricted state with a clear remediation path.
- Sign-out removes account-bound keys, cached records, pending notification details, and device session state.

## Frappe realization

- **DocTypes:** Create `OC Mobile App Release` and `OC Mobile Capability` with platform, semantic version, build digest, channel, minimum OS, feature flag, and effective dates.
- **Roles and workflow:** `OC Mobile Administrator` submits releases through Draft → Approved → Retired; Role Permission Manager and site user permissions filter capabilities.
- **API and auth:** Expose guarded `open_chart.api.v1.mobile.bootstrap` and read-only `/api/resource/OC%20Mobile%20App%20Release` through TLS REST token or OAuth2 auth; reject direct clinical writes.
- **Realtime and jobs:** Publish minimum-necessary release and policy changes with Frappe websocket events; use server-side RQ jobs for manifest generation and distribution reconciliation.
- **Files and surfaces:** Store signed manifests and non-PHI release artifacts through Frappe private file attachment APIs; add a Mobile Administration Desk workspace and Script Report.

## Boundaries

Owns: native shell contracts, release metadata, and capability discovery. Consumes: identity, permissions, site policy, and app-store distribution. Emits: build posture and capability availability. Does not own: clinical workflow semantics, mobile OS security, or app-store approval.

## Open questions

- Should the first release use one cross-platform UI runtime or separate native presentation layers over a shared protocol library?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
