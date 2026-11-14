# Guided Remote Exam Capture — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Guides patients or assistants through clinician-selected remote observation prompts and records the resulting evidence with provenance.
Topics: openchart-feature-catalog, telehealth, frappe, remote-exam-guidance
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-015 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Specialty prompt library** — Maintain governed capture sequences for range of motion, respiratory effort, gait, or wound review.

## Focus

This feature isolates structured remote-exam instructions and evidence capture without claiming equivalence to hands-on examination.

## Behavior

- A clinician selects an approved prompt sequence appropriate to the encounter and participant capability.
- The patient sees one clear instruction at a time with safety limits, stop guidance, and optional demonstration media.
- The clinician may skip, repeat, or stop a prompt and records who performed or observed the action.
- Responses distinguish patient report, clinician observation, uploaded media, and device measurement.
- Pain, instability, distress, or inability to perform stops the sequence and offers clinician-led escalation.
- The signed encounter shows completed, skipped, unsafe, and unavailable prompts without inferring findings automatically.

## Frappe realization

- **DocTypes:** `OC Remote Exam Template`, child `OC Remote Exam Prompt`, and `OC Remote Exam Capture` store version, instruction, safety text, evidence type, performer, and disposition.
- **Client/hooks:** the clinician console publishes selected prompts to the patient portal via realtime events; `validate` requires source and observer for each accepted capture.
- **Governance:** Clinical Content Reviewer controls template versions; Clinician initiates and signs captures; Patient can view instructions but cannot alter accepted observations.

## Boundaries

Owns: guided prompt execution and evidence provenance. Consumes: clinician selection and participant response. Emits: structured remote observation artifact. Does not own: diagnostic interpretation or device integration.

## Open questions

- Which prompts require a trained assistant rather than an unaccompanied patient?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
