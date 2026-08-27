# Virtual Visit Emergency Location And Escalation — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Keeps a verified current location and human-directed emergency escalation plan available during each virtual encounter.
Topics: openchart-feature-catalog, telehealth, frappe, emergency-escalation
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-035 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Local resource directory** — Present verified emergency and crisis contacts based on the attested visit location.

## Focus

This feature isolates current-location evidence and accountable escalation coordination when urgent safety concerns arise during remote care.

## Behavior

- The patient confirms current address or precise location and callback number before clinical admission.
- Staff can reconfirm or update location after movement, reconnect, or a concerning change in circumstances.
- A clinician initiating escalation selects reason, urgency, destination, contact method, and whether the patient remains connected.
- The system presents jurisdiction-appropriate emergency or crisis resources as decision support, not an autonomous dispatch.
- Contact attempts, handoff recipient, instructions, outcome, and accountable follow-up are recorded in sequence.
- Failed contact or uncertain location remains visibly unresolved until an authorized clinician records disposition.

## Frappe realization

- **DocTypes/workflow:** `OC Virtual Emergency Context` and child `OC Emergency Handoff Event` store attested location, source, callback, resource version, actions, outcome, and owner.
- **API/surfaces:** a prominent clinician-console action opens a guarded escalation workflow; portal reconfirmation appends location attestations with timestamp and actor.
- **Permissions/safety:** Clinician directs escalation, Telehealth Staff assists within policy, and sensitive location fields use elevated permlevels and access logging.

## Boundaries

Owns: encounter location evidence and escalation chronology. Consumes: patient attestation and reviewed resource directory. Emits: human-directed handoff and follow-up task. Does not own: emergency dispatch, crisis assessment, or legal authority.

## Open questions

- How should openChart maintain reliable local emergency resources without implying that the directory replaces clinician judgment or emergency services?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
