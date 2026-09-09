# AI Incident Response Workflow — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Coordinates detection, containment, impact review, correction, notification, recovery, and learning for AI safety and governance incidents.
Topics: openchart-feature-catalog, clinical-ai, frappe, incident-response
Repository context: openChart — Frappe v15 native EMR; catalog entry AIC-046 (Clinical AI And Governance)
Captured: 2026-08-24

## Possible feats

- **Affected-artifact tracing** — Enumerate outputs, reviewers, destinations, and unresolved follow-up associated with an incident scope.

## Focus

This feature isolates the full lifecycle after an AI concern is reported or detected.

## Behavior

- Staff, patients, monitors, or integrations can report an incident with capability, artifact, harm concern, urgency, and evidence.
- An incident commander classifies scope, invokes containment, assigns clinical, privacy, security, technical, and communications workstreams.
- Impact analysis traces affected invocations and accepted destinations without altering those records silently.
- Corrections use ordinary amendment, retraction, patient-communication, and follow-up authorities with accountable humans.
- Recovery requires root-cause evidence, validation, fairness review as applicable, staged enablement, and monitoring.
- Closure records lessons, outstanding obligations, and whether evaluation cases or policies must be updated.

## Frappe realization

- **DocTypes:** `OC AI Incident`, child workstreams, `OC AI Impact Item`, and `OC AI Corrective Action` store scope, severity, artifacts, owners, deadlines, decisions, and evidence.
- **Workflow:** Reported → Triaged → Contained → Investigating → Correcting → Recovery Review → Closed.
- **Roles/permissions:** incident commander controls coordination; clinical/privacy/security roles see need-to-know fields by permlevel.
- **Hooks/jobs/surfaces:** kill-switch API links containment; rq traces artifacts; scheduler escalates overdue actions; incident Workspace, Kanban, Notifications, and print format support response.

## Boundaries

Owns: AI incident coordination and evidence. Consumes: reports, telemetry, artifacts, policies, and impact findings. Emits: containment, human corrective work, recovery decision, and lessons. Does not own: autonomous clinical correction or legal conclusions.

## Open questions

- Which severity classes require patient notification review or external reporting assessment?

## Relationships

[Synthesis: Clinical AI And Governance](openchart-feature-catalog-synthesis-aic.md) · [AI Kill Switch And Incident Log](openchart-feature-catalog-aic-028-ai-kill-switch-and-incident-log.md)
