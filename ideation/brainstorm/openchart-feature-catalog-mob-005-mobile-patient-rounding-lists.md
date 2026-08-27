# Mobile Patient Rounding Lists — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Gives clinicians a permission-filtered, offline-capable patient list for preparing, conducting, and handing off rounds.
Topics: openchart-feature-catalog, mobile-devices, frappe, rounding-lists
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-005 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Round progress handoff** — Share completion and unresolved-item status among an authorized rounding team.

## Focus

This entry isolates the compact list and sequence clinicians use to move through an assigned census.

## Behavior

- A clinician selects an authorized service, unit, care team, or personal list.
- Each row shows minimum-necessary identity, location, attending team, precautions, and unresolved-work indicators.
- Users can sort or manually sequence a personal round without changing bed or care-team authority.
- Opening a row rechecks access and loads a bounded chart-review card set.
- Offline lists retain their server-generated scope and display a prominent as-of time.
- Admission, transfer, discharge, or access changes invalidate affected rows when connectivity returns.
- A removed patient leaves no readable residual row after cache reconciliation.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Rounding List` and child `OC Rounding List Entry` with owner, source scope, patient link, encounter link, sequence, snapshot version, and cache expiry.
- **Roles and permissions:** `OC Clinician` and `OC Nurse` access lists only through patient, facility, and care-team user permissions; personal ordering is owner-only.
- **API and auth:** Expose token-authenticated `open_chart.api.v1.mobile.rounding_list` and `resequence`; guarded server methods resolve scope instead of trusting client patient IDs.
- **Realtime and jobs:** Websocket events invalidate changed census entries; server-side RQ jobs build scoped list snapshots and purge expired ones.
- **Files and surfaces:** No attachments are copied into lists; authorized chart files remain retrievable through Frappe private file attachment APIs after a fresh permission check.

## Boundaries

Owns: rounding-list membership snapshots and personal sequence. Consumes: census, location, care-team, precautions, and assignments. Emits: list views and progress signals. Does not own: admission state, patient identity, or clinical task disposition.

## Open questions

- Which patient indicators are minimum necessary on the list before the chart is opened?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
