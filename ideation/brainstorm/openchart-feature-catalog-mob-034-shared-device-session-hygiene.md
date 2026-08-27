# Shared Device Session Hygiene — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enforces fast user switching, local data separation, idle lock, and verified cleanup on shared clinical phones and tablets.
Topics: openchart-feature-catalog, mobile-devices, frappe, shared-device-hygiene
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-034 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Shift custody handoff** — Record accountable transfer of a shared device between units or users.

## Focus

This capability isolates identity and data hygiene on nursing-station and pooled devices.

## Behavior

- A shared-device profile disables personal backups, consumer sharing, remembered patient state, and ungoverned biometric enrollment.
- Each user selects identity and authenticates before a separate encrypted session container is opened.
- Idle timeout locks immediately; user switch closes views, cancels previews, clears clipboard, and removes notification details.
- Pending offline work remains bound to its author and is inaccessible to the next user.
- Sign-out reports cleanup success, pending-work disposition, and any policy exception before the device becomes available.
- Lost network does not permit a user to inherit another person's offline grant.
- Failed cleanup quarantines the app until an administrator resolves or wipes the affected container.

## Frappe realization

- **DocTypes:** Create `OC Shared Mobile Device`, `OC Device Custody Event`, and `OC Session Cleanup Receipt` with facility, profile, user, times, pending counts, outcome, and quarantine reason.
- **Roles and permissions:** Users see only their active container metadata; `OC Mobile Device Custodian` manages custody and `OC Security Administrator` handles quarantine.
- **API and auth:** Device-bound plus user TLS REST token auth calls `open_chart.api.v1.mobile.shared_device.switch` and `cleanup_receipt`; server revokes prior user grants atomically.
- **Realtime and jobs:** Websocket events signal lock, revocation, and quarantine; server-side RQ jobs detect abandoned sessions and route unresolved pending-work cases.
- **Files and surfaces:** Private Frappe attachments remain author-scoped and are purged locally after transfer; a Desk fleet report tracks cleanup without clinical payloads.

## Boundaries

Owns: shared profile, user-session separation, custody, and cleanup proof. Consumes: identity, enrollment, offline queue, and device policy. Emits: revocation and quarantine state. Does not own: operating-system multiuser implementation or physical device custody enforcement.

## Open questions

- How can pending authored work be recovered without exposing it to the next shared-device user?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
