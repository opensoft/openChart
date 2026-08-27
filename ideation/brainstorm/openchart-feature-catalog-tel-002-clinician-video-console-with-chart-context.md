# Clinician Video Console With Chart Context — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Gives clinicians a secure video workspace beside the authorized encounter chart and visit actions.
Topics: openchart-feature-catalog, telehealth, frappe, clinician-video-console
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-002 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Context-preserving pop-out** — Move video to a compact window while retaining the same encounter and participant controls.

## Focus

This feature isolates the clinician workspace that combines live media controls with minimum-necessary chart context for one virtual encounter.

## Behavior

- An assigned clinician opens the console from a scheduled or accepted on-demand virtual visit.
- The console verifies encounter access before showing patient identity, reason for visit, allergies, medications, and recent results.
- Participant, mute, camera, interpreter, admit, and end controls remain bound to the active room and clinician role.
- Chart actions open the linked encounter without duplicating clinical facts into session records.
- A clinician can mark delayed, connected, disconnected, completed, or converted while media presence remains separately observed.
- Loss of chart authorization closes clinical context immediately and prevents further encounter actions even if media persists.

## Frappe realization

- **DocTypes:** `OC Virtual Visit` links `OC Patient` and the governed encounter; child `OC Virtual Participant` records role, invitation state, and presence timestamps without media content.
- **API/hooks:** whitelisted console bootstrap and control methods return permission-filtered context; realtime events update presence while accepted transitions persist through `open_chart.api.v1.telehealth`.
- **Surfaces/permissions:** a Telehealth workspace page serves Clinician and Telehealth Staff roles; sensitive chart panels rely on existing encounter DocPerms and patient user permissions.

## Boundaries

Owns: clinician virtual-visit coordination surface. Consumes: encounter authorization, chart projections, and room presence. Emits: governed visit transitions. Does not own: source clinical records or media infrastructure.

## Open questions

- Can a custom WebRTC console meet accessibility and support needs better than a partner embed without duplicating partner controls?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
