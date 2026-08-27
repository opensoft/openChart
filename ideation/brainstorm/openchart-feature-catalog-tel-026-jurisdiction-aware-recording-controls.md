# Jurisdiction-Aware Recording Controls — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Keeps virtual-visit recording off by default and permits it only through explicit jurisdiction, policy, consent, and retention controls.
Topics: openchart-feature-catalog, telehealth, frappe, recording-governance
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-026 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Recording prohibition signal** — Surface a signed no-recording policy to every participant at join and after late admission.

## Focus

This feature isolates whether a virtual session may be recorded, who authorizes it, and how any resulting artifact is governed.

## Behavior

- New virtual rooms have recording disabled regardless of media-platform defaults.
- A recording request evaluates patient location, provider location, service, organization policy, participant roles, and effective law configuration.
- Every required participant receives a distinct disclosure and must give affirmative agreement before recording can start.
- Joiners arriving after consent stop or pause recording until their required decision is resolved.
- Start, pause, resume, stop, refusal, and failure events are visibly announced and recorded in the audit trail.
- An approved artifact is private, encrypted, retention-classified, access-logged, and never attached as an ordinary public File.

## Frappe realization

- **DocTypes:** `OC Recording Policy`, `OC Recording Authorization`, child `OC Participant Recording Decision`, and `OC Recording Artifact` store jurisdictions, consent, adapter reference, retention, checksum, and access state.
- **API/adapters:** guarded recording controls call a custom WebRTC recorder or partner API only after server authorization; adapter callbacks reconcile actual state.
- **Permissions:** Recording Officer governs policy, Clinician requests, participants decide, Records Custodian controls artifacts, and default DocPerms deny download.

## Boundaries

Owns: recording authorization, control state, and artifact governance. Consumes: location, policy, and participant consent. Emits: recording events and protected artifact. Does not own: legal interpretation or media-platform storage internals.

## Open questions

- Can partner embeds prove recording is disabled and honor openChart's per-participant consent state as strictly as a custom build?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
