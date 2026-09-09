# Browser-Based Patient Video — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Enables patients to participate in an encrypted virtual visit in a supported browser without installing an application.
Topics: openchart-feature-catalog, telehealth, frappe, browser-video
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-003 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Accessible media controls** — Add keyboard, screen-reader, caption, and high-contrast adaptations to the patient client.

## Focus

This feature isolates the install-free patient media experience after authorization, independent of booking and encounter documentation.

## Behavior

- The client checks browser support and secure-context requirements before requesting camera or microphone access.
- Patients may choose camera and microphone devices and preview them before entering the waiting room.
- Permission denial produces device-specific guidance and preserves a path to audio-only or staff assistance.
- The client displays participant identity labels, local mute state, network state, and an unambiguous Leave action.
- Refresh or brief browser suspension attempts a controlled rejoin with the same authorized participant identity.
- Unsupported browsers receive a minimum-disclosure message and approved alternatives rather than a broken media page.

## Frappe realization

- **DocTypes:** `OC Telehealth Client Policy` stores supported-browser rules and fallback options; `OC Virtual Participant` records selected modality and lifecycle timestamps, not raw media.
- **Client/API:** a portal JavaScript client exchanges short-lived room credentials through `open_chart.api.v1.telehealth`; WebRTC signaling or partner SDK calls remain behind an adapter boundary.
- **Audit/security:** CSP, feature permissions, token expiry, and no-cache headers protect the portal route; technical events redact SDP, IP detail, and device labels from ordinary logs.

## Boundaries

Owns: browser media participation and user-facing controls. Consumes: authorized session grant and media adapter. Emits: presence and technical-state events. Does not own: appointment eligibility or clinical documentation.

## Open questions

- Which browser matrix is supportable for a custom WebRTC build, and when should a partner embed be offered instead?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
