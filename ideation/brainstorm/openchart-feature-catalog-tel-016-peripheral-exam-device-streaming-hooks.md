# Peripheral Exam Device Streaming Hooks — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Provides governed adapter hooks for live digital stethoscope, otoscope, and similar peripheral streams during virtual care.
Topics: openchart-feature-catalog, telehealth, frappe, exam-device-streaming
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-016 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Device certification registry** — Track validated adapter, firmware, calibration, and service combinations.

## Focus

This feature isolates authorization, routing, and provenance for peripheral streams; it does not define device hardware or interpret signals.

## Behavior

- Staff register an approved device and adapter before it can be offered in a virtual room.
- A clinician explicitly requests a device stream and the local operator confirms device, patient, and capture site.
- The session labels stream source, operator, connection state, and whether data is live-only or eligible for retention.
- Connection loss stops the device channel independently of ordinary audio and video and records the interruption.
- Unsupported, uncalibrated, or mismatched devices are blocked with an actionable reason.
- Any retained sample requires explicit policy, consent, checksum, timestamps, and linkage to the encounter.

## Frappe realization

- **DocTypes:** `OC Exam Device`, `OC Device Adapter Policy`, and `OC Device Stream Session` store identifiers, model, validation status, calibration expiry, operator, channel, and retention decision.
- **API/adapters:** `open_chart.api.v1.telehealth.device` issues scoped channel grants; custom WebRTC tracks or partner device APIs implement a common adapter contract.
- **Permissions/reports:** Device Technician maintains inventory, Clinician authorizes use, and Compliance Reviewer audits retained samples and expired validations.

## Boundaries

Owns: device stream authorization and provenance. Consumes: approved device, operator, consent, and media adapter. Emits: stream state and optional governed sample. Does not own: hardware safety or automated interpretation.

## Open questions

- Can a common contract span custom WebRTC tracks and partner-specific peripheral SDKs without losing safety controls?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
