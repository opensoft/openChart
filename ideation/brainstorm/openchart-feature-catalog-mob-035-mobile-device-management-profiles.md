# Mobile Device Management Profiles — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Publishes app configuration and compliance expectations for managed deployment while reconciling MDM posture into openChart access decisions.
Topics: openchart-feature-catalog, mobile-devices, frappe, mdm-profiles
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-035 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Configuration conformance preview** — Compare a proposed app profile with required openChart controls before rollout.

## Focus

This entry isolates the contract between openChart and organization-selected MDM platforms.

## Behavior

- Administrators define environment URL, tenant, certificate expectations, managed app settings, sharing restrictions, and compliance requirements.
- Versioned profiles are exported in vendor-neutral form and optionally adapted for selected MDM products.
- Enrolled apps report applied profile version and bounded compliance claims, not full personal device inventory.
- Compliant, unknown, stale, noncompliant, exempted, and retired states are explicit.
- Policy can restrict offline cache, attachments, notifications, or login while retaining a clear remediation route.
- Personally owned devices receive only declared app-level checks unless enrollment policy says otherwise.
- MDM failure never silently grants broader access or collects unrelated device data.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Mobile Management Profile`, `OC Device Compliance Report`, and `OC MDM Adapter` with version, controls, claims, effective dates, state, and exception.
- **Workflow and roles:** Draft → Approved → Active → Retired; `OC Mobile Administrator` authors and `OC Security Administrator` approves policy and exceptions.
- **API and auth:** Token-authenticated `open_chart.api.v1.mobile.management_profile` and signed MDM callbacks exchange scoped posture; profile auto-REST is read-only.
- **Realtime and jobs:** Websocket events invalidate changed profiles; server-side RQ jobs reconcile MDM inventories, expire stale claims, and generate adapter exports.
- **Files and surfaces:** Configuration profiles and vendor evidence use private or non-PHI public Frappe file attachment APIs as appropriate; Desk fleet and compliance reports are restricted.

## Boundaries

Owns: openChart app-configuration contract and received posture. Consumes: MDM assertions, enrollment, and security policy. Emits: scoped access posture and configuration exports. Does not own: MDM vendor, OS enforcement, or personal device inventory.

## Open questions

- Which controls are mandatory for personally owned devices versus organization-owned shared devices?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
