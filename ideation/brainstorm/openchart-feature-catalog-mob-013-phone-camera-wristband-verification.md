# Phone Camera Wristband Verification — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Scans a patient wristband with the phone camera and verifies the encoded identity against the active workflow before bedside action.
Topics: openchart-feature-catalog, mobile-devices, frappe, wristband-scanning
Repository context: openChart — Frappe v15 native EMR; catalog entry MOB-013 (Mobile Offline And Device Integration)
Captured: 2026-08-24

## Possible feats

- **Dual-identifier prompt** — Require a second human-confirmed identifier for configured bedside workflows.

## Focus

This entry isolates patient-context verification and does not itself authorize medication, collection, or documentation.

## Behavior

- The user opens scanning from an active patient-sensitive workflow and grants camera access only while scanning.
- On-device decoding extracts an opaque wristband identifier without retaining frames.
- The server validates identifier status, patient, encounter, facility, location, and workflow context.
- Match shows minimum-necessary identity for human confirmation; mismatch blocks continuation and explains the next safe step.
- Duplicate, expired, replaced, malformed, or wrong-facility bands are distinct outcomes.
- Offline verification is allowed only against a signed, unexpired assignment manifest and remains visibly provisional.
- Every verification records actor, device, context, outcome, and time without storing barcode images.

## Frappe realization

- **Transport:** Require TLS REST token or OAuth2 authentication for mobile API calls and rotate revocable credentials through device enrollment.
- **DocTypes:** Create `OC Wristband Identifier` and `OC Bedside Identity Check` with patient, encounter, code hash, issue/expiry, replacement link, context, and outcome.
- **Roles and permissions:** `OC Nurse`, `OC Phlebotomist`, and configured bedside roles verify only within facility and patient user permissions; issuance is separately restricted.
- **API and auth:** Call token-authenticated `open_chart.api.v1.mobile.verify_wristband`; never expose barcode lookup through unrestricted auto-REST.
- **Realtime and jobs:** Websocket events invalidate replaced bands; server-side RQ jobs expire identifiers and reconcile provisional offline checks.
- **Files and surfaces:** Camera frames are not uploaded; if exception evidence is required, it uses explicit-consent private Frappe file attachment APIs and restricted retention.

## Boundaries

Owns: wristband identifier validation and check evidence. Consumes: patient, encounter, facility, and workflow context. Emits: matched, mismatched, provisional, or invalid result. Does not own: patient identity proofing or downstream clinical action.

## Open questions

- Which bedside actions may rely on provisional offline wristband verification?

## Relationships

[Synthesis: Mobile Offline And Device Integration](openchart-feature-catalog-synthesis-mob.md)
