# Synthesis: Mobile Offline And Device Integration — Brainstorm

Status: brainstorm
Kind: reference
Summary: Combines a governed native app, offline continuity, bedside capture, field mobility, connected devices, shared displays, and fleet controls into one Frappe-native mobile clinical surface.
Topics: openchart-feature-catalog, mobile-devices, frappe, synthesis
Repository context: openChart — Frappe v15 native EMR; Mobile Offline And Device Integration domain synthesis
Captured: 2026-08-24

## Possible feats

- **Governed mobile capability program** — Release role-specific journeys against shared identity, offline, device, accessibility, observability, and fleet acceptance contracts.

## Focus

This synthesis relates 40 Mobile Offline And Device Integration capabilities into a mobile architecture that remains independently usable by openChart and preserves server authority, provenance, consent, audit, and human clinical control.

## Members and their joints

### Native foundation, identity, and role-oriented work

- [Native Clinician App Shell](openchart-feature-catalog-mob-001-native-clinician-app-shell.md), [Mobile Device Enrollment And Session](openchart-feature-catalog-mob-002-mobile-device-enrollment-and-session.md), and [Biometric App Unlock](openchart-feature-catalog-mob-003-biometric-app-unlock.md) separate signed application distribution, server authentication, device-bound grants, and local convenience unlock.
- [Role-Based Mobile Home Screens](openchart-feature-catalog-mob-004-role-based-mobile-home-screens.md), [Mobile Patient Rounding Lists](openchart-feature-catalog-mob-005-mobile-patient-rounding-lists.md), [Quick Chart Review Cards](openchart-feature-catalog-mob-006-quick-chart-review-cards.md), and [Mobile Clinical Task Inbox](openchart-feature-catalog-mob-007-mobile-clinical-task-inbox.md) turn those grants into physician, nurse, and home-care work surfaces without creating a second authorization system.

The joint is progressive narrowing: the signed build discovers site capabilities, enrollment binds an installation, authentication establishes a user, the active role and assignment select work, and each patient route rechecks current Frappe permissions. Biometric unlock can release a protected local key but never substitutes for these server decisions.

### Offline authority, authorship, conflict, and synchronization

- [Encrypted Offline Chart Cache](openchart-feature-catalog-mob-008-encrypted-offline-chart-cache.md) provides bounded read continuity, while [Offline Documentation Queue](openchart-feature-catalog-mob-009-offline-documentation-queue.md) keeps authored work in a separate encrypted, attributable intent store.
- [Offline Sync Conflict Resolution](openchart-feature-catalog-mob-010-offline-sync-conflict-resolution.md) compares base, current, and authored versions; [Sync Status And Retry Transparency](openchart-feature-catalog-mob-011-sync-status-and-retry-transparency.md) exposes acceptance truth and recovery; [Battery And Network-Aware Sync](openchart-feature-catalog-mob-038-battery-and-network-aware-sync.md) schedules transfer without hiding clinically important delay.

The joint is explicit provisionality: cached facts are snapshots, authored changes are intents, transmitted bytes are attempts, and only a server receipt identifies acceptance. Version checks and succession-based amendments prevent offline convenience from becoming silent last-write-wins chart mutation.

### Communication, capture, and virtual participation

- [Urgency-Routed Push Notifications](openchart-feature-catalog-mob-012-urgency-routed-push-notifications.md), [Secure In-App Clinical Messaging](openchart-feature-catalog-mob-021-secure-in-app-clinical-messaging.md), and [Chart-Launched Masked Calling](openchart-feature-catalog-mob-022-chart-launched-masked-calling.md) compose minimum-necessary alerting, protected conversation, and privacy-preserving voice contact.
- [Direct-To-Chart Clinical Photo Capture](openchart-feature-catalog-mob-016-direct-to-chart-clinical-photo-capture.md), [Mobile Document Scanning](openchart-feature-catalog-mob-017-mobile-document-scanning.md), and [On-Device E-Signature Capture](openchart-feature-catalog-mob-018-on-device-e-signature-capture.md) bind media and signature evidence to patient, encounter, purpose, consent, and immutable digests without device-gallery retention.
- [Mobile Voice Dictation](openchart-feature-catalog-mob-019-mobile-voice-dictation.md) handles deliberate field input; [Consented Mobile Ambient Capture](openchart-feature-catalog-mob-020-consented-mobile-ambient-capture.md) adds participant-aware encounter sessions and clinician-reviewed drafts; [In-App Telehealth Join](openchart-feature-catalog-mob-023-in-app-telehealth-join.md) adds short-lived virtual-room participation.

The joint is a common protected-artifact lifecycle: explicit context and consent precede capture, transient files use private attachment APIs, server-side RQ jobs scan or process them, websocket receipts expose state, and a human accepts any clinical text or consequence. Push and telecom adapters carry opaque routing identifiers rather than chart payloads.

### Bedside identity and closed-loop collection

- [Phone Camera Wristband Verification](openchart-feature-catalog-mob-013-phone-camera-wristband-verification.md) establishes the patient-context check reused by [Bedside Medication Administration Scanning](openchart-feature-catalog-mob-014-bedside-medication-administration-scanning.md) and [Specimen Collection Label Scanning](openchart-feature-catalog-mob-015-specimen-collection-label-scanning.md).
- [Smart Pump Data Hooks](openchart-feature-catalog-mob-030-smart-pump-data-hooks.md) brings device events back for order and administration reconciliation without granting the phone pump-control authority.

The joint is closed-loop evidence rather than barcode determinism: identity, active order, product or container, timing, location, user authority, and current state are checked together. Mismatches, overrides, provisional offline checks, and delayed device events remain visible to accountable humans.

### Home, community, and connected-device mobility

- [Offline Home-Care Visit Checklists](openchart-feature-catalog-mob-024-offline-home-care-visit-checklists.md), [Geofenced Field Visit Check-In](openchart-feature-catalog-mob-025-geofenced-field-visit-check-in.md), [Community Staff Mileage And Route Log](openchart-feature-catalog-mob-026-community-staff-mileage-and-route-log.md), and [Offline Visit Route Optimization](openchart-feature-catalog-mob-027-offline-visit-route-optimization.md) compose an assigned field journey while separating care evidence, point-in-time location verification, route advice, and reimbursement facts.
- [Bluetooth Vitals Device Pairing](openchart-feature-catalog-mob-028-bluetooth-vitals-device-pairing.md) handles clinician-present transfer; [Patient Home Device Feeds](openchart-feature-catalog-mob-029-patient-home-device-feeds.md) handles longitudinal weight and glucose connections; [Wearable Data Pipeline Management](openchart-feature-catalog-mob-031-wearable-data-pipeline-management.md) governs higher-volume consumer streams.

The joint is source-aware intake: visit plans and device profiles can travel offline, but every checklist response, location point, route change, and measurement carries its actor, device, time quality, consent, parser, and sync state. Device data enters reviewable intake before promotion to authoritative observations, and route tools remain advisory rather than autonomous staffing or clinical systems.

### Shared surfaces, fleet governance, and release safety

- [Kiosk Tablet Check-In Mode](openchart-feature-catalog-mob-032-kiosk-tablet-check-in-mode.md), [Bedside Patient Engagement Display](openchart-feature-catalog-mob-033-bedside-patient-engagement-display.md), and [Shared Device Session Hygiene](openchart-feature-catalog-mob-034-shared-device-session-hygiene.md) enforce narrow sessions, rapid unbinding, and next-user isolation on patient-facing and pooled hardware.
- [Mobile Device Management Profiles](openchart-feature-catalog-mob-035-mobile-device-management-profiles.md), [Minimum Mobile App Version Enforcement](openchart-feature-catalog-mob-036-minimum-mobile-app-version-enforcement.md), [PHI-Safe Mobile Crash Diagnostics](openchart-feature-catalog-mob-037-phi-safe-mobile-crash-diagnostics.md), [Mobile Accessibility Parity](openchart-feature-catalog-mob-039-mobile-accessibility-parity.md), and [Lost Device Remote Wipe](openchart-feature-catalog-mob-040-lost-device-remote-wipe.md) create the management, compatibility, support, inclusive-use, and incident-response envelope around every mobile surface.

The joint is lifecycle evidence from deployment to retirement: configuration declares expected posture, releases declare compatibility, accessibility tests gate critical flows, scrubbed diagnostics explain failures, and remote wipe revokes server grants even when local destruction cannot yet be confirmed. Shared and patient-facing modes add stricter session reset and content-release contracts on top of the same fleet identities.

## Frappe realization

- **Core model:** OC-prefixed app release, enrollment, session, cache manifest, documentation intent, receipt, capture, device intake, display, policy, diagnostic, and wipe DocTypes use Links, Dynamic Links, child tables, private Files, immutable provenance, and succession-based correction for accepted records.
- **Workflow and permissions:** Frappe Workflows encode enrollment, queue, conflict, capture, intake, review, release, and wipe transitions; named mobile, clinical, support, privacy, security, device-integration, and supervisor roles combine DocPerms with patient, facility, care-team, assignment, device, and owner user permissions.
- **API and authentication:** Guarded `open_chart.api.v1.mobile` and `open_chart.api.v1.devices` whitelisted methods are the supported write surfaces; TLS REST token or OAuth2 authentication is device- and user-scoped, while `/api/resource/...` remains read-only only where permission-query rules are sufficient.
- **Realtime and background work:** Frappe websocket events carry opaque IDs and minimum-necessary state invalidations; server-side RQ jobs perform manifest assembly, retries, media scanning, transcription, adapter ingestion, aggregation, expiry, purge, diagnostics, and reconciliation without autonomous clinical disposition.
- **Files and surfaces:** Frappe private file attachment APIs provide staged upload, content digests, malware scanning, versioning, short-lived grants, and retention for clinical media, scans, signatures, device batches, and diagnostics; native screens pair with permission-aware Desk workspaces, Query/Script Reports, dashboards, assignments, and portal or kiosk pages.

## Boundaries

Owns: openChart mobile app contracts, device/session lifecycle, bounded offline state, synchronization evidence, mobile capture, connected-device intake, shared-surface projections, and fleet policy records. Consumes: Frappe identity and permissions, clinical source records, consent, assignments, orders, appointments, device and telecom adapters, MDM assertions, mobile operating systems, and managed distribution channels. Emits: guarded clinical intents, source-labeled observations, private attachments, communication and workflow events, review tasks, receipts, posture decisions, and append-only audit evidence. Does not own: mobile operating systems, app stores, carrier or media networks, MDM products, medical-device calibration, pump control, payroll or reimbursement, autonomous clinical decisions, or physical device recovery.

## Emergent behavior

Together, the features produce a mobile clinical environment in which the phone is neither a thin browser nor an independent chart authority. A signed and enrolled app can orient each role, stage minimum-necessary work, operate through a network interruption, capture bedside and field evidence, communicate securely, pair with approved devices, and return attributable intents to guarded Frappe APIs. Shared receipts, versions, correlation IDs, private-file digests, device identities, and websocket state transitions let users distinguish local, transmitted, accepted, conflicted, reviewed, and revoked states across every workflow. Fleet controls and accessibility evidence make safe operation a continuous release property rather than an afterthought.

## Tensions to hold

- Rich offline capability improves continuity but increases lost-device exposure, stale-data risk, conflict complexity, key-recovery pressure, and the need for defensible purge evidence.
- Biometric convenience and shared-device speed must not blur which authenticated person authored, viewed, scanned, signed, or synchronized an action.
- Push, background sync, location, diagnostics, and wearable feeds improve timeliness and support while creating surveillance and metadata risks unless collection is minimized.
- Direct capture and device automation reduce transcription burden, yet every photo, transcript, scan, barcode, pump event, and reading still needs context, provenance, and human accountability.
- Hard version and posture controls reduce security risk but can strand clinicians or unsynced work when app stores, MDM services, networks, or devices fail.
- Cross-platform consistency supports governance, while iOS and Android background, biometric, camera, Bluetooth, accessibility, and managed-device behavior differ materially.
- Enterprise mobile breadth must remain an original openChart implementation and cannot make external vendor infrastructure the clinical source of truth.

## Recombination opportunities

- Combine rounding lists, review cards, task inbox, push routing, dictation, and secure messaging into a physician and nurse mobile shift workspace with one authorization model.
- Combine wristband verification, medication scanning, specimen collection, Bluetooth vitals, and smart-pump reconciliation into a bedside device journey that preserves separate clinical authorities.
- Combine route planning, geofenced check-in, offline checklists, photo capture, signatures, connected readings, and sync transparency into a complete home-care visit pack.
- Combine enrollment, MDM posture, version policy, accessibility tests, crash diagnostics, adaptive sync, and remote wipe into a fleet release gate with measurable safety evidence.
- Combine kiosk and bedside displays with shared-device hygiene to define one reusable ephemeral-session contract for every nonpersonal tablet.
- Combine cache manifests, documentation intents, conflict records, receipts, file digests, and wipe generations into a formal offline protocol test harness using only synthetic `SYN-` fixtures.

## Open questions

- Which initial workflows justify native implementation before a broader mobile shell, and which must remain online-only at launch?
- What common signed envelope should represent cache grants, offline schemas, base versions, attachments, device evidence, idempotency, and server receipts?
- How should openChart recover pending authored work after device loss without creating a key escrow that weakens confidentiality?
- Which iOS and Android versions, hardware classes, assistive technologies, Bluetooth profiles, MDM products, and distribution channels form the supported matrix?
- What minimum adapter evidence is required for telecom, telehealth, transcription, ambient, routing, wearable, home-device, smart-pump, push, and crash providers?
- Which operational metadata may be retained for support and safety, and which should be aggregated or deleted to prevent workforce or patient surveillance?

## Relationships

[openChart Feature Catalog](openchart-feature-catalog-overview.md)
