# Technical Failure To Phone Conversion — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Documents a failed video attempt and governed conversion to a telephone encounter with linked technical evidence.
Topics: openchart-feature-catalog, telehealth, frappe, phone-conversion
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-021 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Failure pattern review** — Aggregate redacted conversion reasons to prioritize support and platform improvements.

## Focus

This feature isolates the operational and encounter documentation required when technical failure forces a phone continuation.

## Behavior

- A clinician selects Convert to Phone from an interrupted or failed video visit and confirms the technical reason.
- The system records attempted connection intervals, recovery actions, patient agreement, callback number source, and conversion time.
- Eligibility is rechecked for the service and jurisdiction before the telephone encounter continues.
- The phone leg receives its own participant and start/end evidence linked to the same encounter lineage.
- If conversion is not eligible or contact fails, staff choose another disposition and assign follow-up responsibility.
- Completion distinguishes video attempted from phone delivered and prompts reconciliation with the clinical note.

## Frappe realization

- **DocTypes:** `OC Technical Conversion` links virtual visit, diagnostic intervals, from/to channel, reason, patient agreement, eligibility result, and phone-leg timestamps.
- **API/hooks:** `open_chart.api.v1.telehealth.convert_after_failure` atomically closes media grants and opens the approved phone state; completion validates modality facts.
- **Reports/roles:** Clinician initiates, Telehealth Support may classify technical cause, and a Script Report summarizes de-identified failure categories.

## Boundaries

Owns: technical conversion evidence and linked phone state. Consumes: diagnostic, eligibility, and patient agreement. Emits: corrected modality history. Does not own: telephony service or billing claims.

## Open questions

- Should custom WebRTC and partner failures use one normalized cause taxonomy or retain adapter-specific secondary codes?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
