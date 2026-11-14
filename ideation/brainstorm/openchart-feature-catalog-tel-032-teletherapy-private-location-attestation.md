# Teletherapy Private Location Attestation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Captures behavioral-health participants' location, privacy, emergency-contact, and interruption plans before teletherapy begins.
Topics: openchart-feature-catalog, telehealth, frappe, teletherapy-privacy
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-032 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Privacy recovery plan** — Offer clinician-reviewed responses for shared spaces, interruptions, or loss of confidentiality.

## Focus

This feature isolates teletherapy-specific readiness attestations that support privacy and emergency response for the session.

## Behavior

- Before admission, the patient confirms current physical location, callback number, privacy level, and whether others are present.
- The patient identifies an emergency contact and acknowledges the session's interruption and emergency plan where policy requires.
- A lack of privacy, unexpected participant, location change, or inability to speak safely is shown to the clinician before admission.
- The clinician may proceed with mitigations, request relocation, change modality, reschedule, or escalate based on judgment.
- Attestation is encounter-specific and may be reconfirmed after a disconnect or material location change.
- Sensitive answers use minimum-necessary display and are never included in waiting-room messages or general scheduling notifications.

## Frappe realization

- **DocTypes:** `OC Teletherapy Readiness Attestation` stores encounter, location, callback confirmation, privacy state, others present, emergency plan version, decision, and mitigation.
- **Workflow/API:** Patient submission creates Ready or Needs Clinician Review; guarded clinician disposition controls admission and appends changes rather than overwriting attestations.
- **Permissions:** Behavioral Health Clinician has encounter access, Telehealth Staff sees only actionable readiness state, and privacy fields use elevated permlevels.

## Boundaries

Owns: teletherapy readiness and privacy attestation. Consumes: identity, location, and emergency plan. Emits: admission readiness and mitigation record. Does not own: behavioral-health assessment or emergency dispatch.

## Open questions

- Which readiness details should remain segmented from ordinary telehealth operations staff?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
