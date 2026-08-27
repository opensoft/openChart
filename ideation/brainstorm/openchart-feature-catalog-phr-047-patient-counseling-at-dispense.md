# Patient Counseling At Dispense — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Documents offered and delivered medication counseling, topics, language, materials, questions, and patient or caregiver participation at dispensing.
Topics: openchart-feature-catalog, eprescribing, frappe, patient-counseling
Repository context: openChart — Frappe v15 native EMR; catalog entry PHR-047 (Pharmacy And E-Prescribing)
Captured: 2026-08-24

## Possible feats

- **Teach-back prompt set** — Configurable prompts could help staff record understanding without reducing counseling to a checkbox.

## Focus

This feature isolates evidence of counseling around a dispense. It records what was offered and communicated without claiming comprehension solely from a signature.

## Behavior

- The pharmacist sees counseling requirements derived from medication, new-versus-refill status, patient needs, and site policy.
- The record identifies participant, interpreter, language, modality, materials, topics, and questions raised.
- Outcomes distinguish delivered, offered and declined, deferred, unable due to barrier, and not required by documented policy.
- Teach-back or understanding notes preserve the observer and patient wording rather than assigning an unsupported score.
- High-risk questions can pause handoff and create a prescriber clarification task.
- Submission links the counseling event to the exact dispense and material versions used.

## Frappe realization

- **DocTypes:** Submittable `OC Dispense Counseling` links dispense, participants, interpreter, topics, materials, outcome, questions, and acknowledgements.
- **Workflow:** Due → In Counseling → Completed/Declined/Deferred/Clarification Required.
- **Roles:** Pharmacists document counseling; interpreters and support staff receive limited participant permissions.
- **Surfaces:** Dispense checklist, counseling form, multilingual patient-material Print Formats, and incomplete-counseling report support use.

## Boundaries

Owns: counseling offer, delivery, content, and outcome evidence. Consumes: dispense, patient communication needs, materials, and policy. Emits: counseling record and clarification tasks. Does not own: guaranteed comprehension or clinical consent beyond its scope.

## Open questions

- Which counseling topics and acknowledgements are mandatory for specific medication categories?

## Relationships

[Synthesis: Pharmacy And E-Prescribing](openchart-feature-catalog-synthesis-phr.md) · [In-House Dispensary Dispensing Record](openchart-feature-catalog-phr-036-in-house-dispensary-dispensing-record.md)
