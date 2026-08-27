# Patient Photo Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures a consented patient identity photo with quality, provenance, expiry, and restricted display controls.
Topics: openchart-feature-catalog, registration, frappe, patient-photo
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-020 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Photo refresh prompts** — Flag stale photos by age or material appearance-change report.

## Focus

Use a patient photo as a human identification aid without making facial recognition an implicit capability.

## Behavior

- Registration staff request consent before camera capture or file upload.
- The UI shows framing, lighting, and image-quality guidance and allows retake before save.
- The patient may decline without blocking registration unless a documented policy exception applies.
- Every image records capture source, actor, consent, timestamp, and replacement reason.
- Replaced photos remain secured in history and are not shown in routine chart surfaces.
- No biometric template, face matching, or automated identity conclusion is generated.

## Frappe realization

- **DocTypes:** `OC Patient Photo` with Image attachment, captured_on, source, consent_reference, active, quality_status, and supersedes.
- **Workflow:** Draft → Consented → Active → Superseded or Withdrawn.
- **Roles/permissions:** `OC Registration Clerk` captures; `OC Clinical User` sees active image; historical files use permlevel 2.
- **API/surfaces:** `open_chart.api.v1.registration.capture_patient_photo`; camera dialog, patient header thumbnail, and stale-photo report.

## Boundaries

Owns: patient identity-photo lifecycle. Consumes: consent and captured image. Emits: active display image with provenance. Does not own: biometrics, surveillance, or diagnostic imaging.

## Open questions

- What retention rule applies when a patient withdraws photo-display consent?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
