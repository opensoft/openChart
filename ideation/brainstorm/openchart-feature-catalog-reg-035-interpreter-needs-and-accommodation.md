# Interpreter Needs and Accommodation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Assesses and tracks interpreter modality, accommodation, and fulfillment needs so communication support is explicit and reviewable.
Topics: openchart-feature-catalog, registration, frappe, interpreter-accommodation
Repository context: openChart — Frappe v15 native EMR; catalog entry REG-035 (Registration Identity And Demographics)
Captured: 2026-08-24

## Possible feats

- **Encounter accommodation handoff** — Emit a request to scheduling or care workflows with patient-approved modality details.

## Focus

Capture the need and preferred form of language assistance without treating family interpretation as a default.

## Behavior

- Staff ask whether an interpreter is needed and for which language, modality, and interaction types.
- Options include in-person, video, audio, sign-language, communication aid, declined, and patient-provided support.
- The record distinguishes assessed need, patient preference, requested accommodation, and fulfilled accommodation.
- Use of a minor or unqualified companion requires an exception reason and does not satisfy future needs automatically.
- Changes retain source, assessor, date, and patient confirmation.
- Unfulfilled urgent needs surface visibly and require escalation, not silent closure.

## Frappe realization

- **DocTypes:** `OC Communication Accommodation` with language link, need, modality, contexts, status, source, validity, and exception reason.
- **Workflow:** Assessed → Requested → Arranged → Fulfilled, Declined, Unavailable, or Escalated.
- **Roles/permissions:** `OC Registration Clerk` assesses; `OC Accommodation Coordinator` arranges; clinical users read current requirements.
- **API/surfaces:** `open_chart.api.v1.registration.assess_interpreter_need` and `.update_accommodation`; patient banner and accommodation worklist.

## Boundaries

Owns: interpreter need and accommodation lifecycle. Consumes: patient language and interaction context. Emits: explicit support requirements and status. Does not own: vendor staffing or translation quality certification.

## Open questions

- Should fulfillment be tracked per visit, per care episode, or both?

## Relationships

[Synthesis: Registration Identity And Demographics](openchart-feature-catalog-synthesis-reg.md)
