# Synthesis: Telehealth Virtual Care And E-Visits — Brainstorm

Status: brainstorm
Kind: reference
Summary: Connects virtual-care readiness, secure participation, synchronous and asynchronous encounters, failure recovery, and follow-up into one governed Frappe-native care domain.
Topics: openchart-feature-catalog, telehealth, frappe, synthesis
Repository context: openChart — Frappe v15 native EMR; Telehealth Virtual Care And E-Visits domain synthesis
Captured: 2026-08-24

## Possible feats

- **Modality-neutral virtual care journey** — Let one governed encounter pathway move among video, audio, asynchronous review, monitoring, and in-person follow-up without losing authority or provenance.

## Focus

This synthesis relates 35 Telehealth Virtual Care And E-Visits capabilities through shared identity, consent, location, participant, encounter, and audit boundaries while preserving human clinical control.

## Members and their joints

### Planning, eligibility, consent, and readiness

- [Licensure And Patient Location Check](openchart-feature-catalog-tel-007-licensure-and-patient-location-check.md), [Encounter Telehealth Consent Capture](openchart-feature-catalog-tel-008-encounter-telehealth-consent-capture.md), and [Telehealth Consent Audit Trail](openchart-feature-catalog-tel-019-telehealth-consent-audit-trail.md) establish whether remote care may proceed and preserve the evidence behind that gate.
- [Pre-Visit Technology Check](openchart-feature-catalog-tel-022-pre-visit-technology-check.md) and [Telehealth-Specific Intake Forms](openchart-feature-catalog-tel-034-telehealth-specific-intake-forms.md) surface technical or clinical readiness needs before arrival without cancelling care autonomously.
- [Virtual Room Scheduling Templates](openchart-feature-catalog-tel-028-virtual-room-scheduling-templates.md) and [Provider Modality Availability](openchart-feature-catalog-tel-029-provider-modality-availability.md) align logical room supply with provider time, service, modality, jurisdiction, and adapter capacity.

The joint is effective-time revalidation: booking decisions remain provisional until location, authority, consent, intake, technology, provider, and room constraints are checked again at arrival. Accepted consent and policy evidence remain immutable even when a later check changes whether the visit can continue.

### Secure arrival and waiting-room operations

- [Portal Scheduled Video Launch](openchart-feature-catalog-tel-001-portal-scheduled-video-launch.md) turns a confirmed appointment into a short-lived arrival grant.
- [Join Identity Verification](openchart-feature-catalog-tel-006-join-identity-verification.md) binds that grant to the intended person, while [Secure Virtual Room Access](openchart-feature-catalog-tel-027-secure-virtual-room-access.md) prevents link replay, cross-room use, and admission-stage bypass.
- [Virtual Waiting Room And Staff Admit](openchart-feature-catalog-tel-005-virtual-waiting-room-and-staff-admit.md) keeps clinical-room admission human-controlled, and [Waiting Room Messaging](openchart-feature-catalog-tel-023-waiting-room-messaging.md) provides a room-scoped operational channel while the patient waits.

The joint is least-privilege progression: appointment access permits a portal arrival request, verified identity permits waiting-room presence, and an explicit staff action permits media admission. Each stage has a narrower credential, server-authoritative transition, and independently revocable state.

### Live room, media, participants, and capture

- [Clinician Video Console With Chart Context](openchart-feature-catalog-tel-002-clinician-video-console-with-chart-context.md) binds the active room to permission-filtered encounter context, while [Browser-Based Patient Video](openchart-feature-catalog-tel-003-browser-based-patient-video.md) supplies the install-free patient endpoint.
- [Connection Diagnostics And Reconnect](openchart-feature-catalog-tel-004-connection-diagnostics-and-reconnect.md) normalizes quality and recovery across media adapters; [Peripheral Exam Device Streaming Hooks](openchart-feature-catalog-tel-016-peripheral-exam-device-streaming-hooks.md) adds governed device channels without interpreting them.
- [Interpreter-Inclusive Video](openchart-feature-catalog-tel-009-interpreter-inclusive-video.md) and [Family And Proxy Video Participation](openchart-feature-catalog-tel-025-family-and-proxy-video-participation.md) give every additional person distinct authority and presence intervals.
- [Jurisdiction-Aware Recording Controls](openchart-feature-catalog-tel-026-jurisdiction-aware-recording-controls.md) keeps recording off by default and makes any exception dependent on current participants, locations, consent, and retention policy.

The joint is separation of planes: the media adapter carries streams, openChart carries identity, authority, participant state, encounter links, and audit evidence. That separation permits a custom WebRTC build or a partner embed only if each can satisfy the same server-enforced control contract.

### Alternative care formats and specialty workflows

- [Group Video Sessions](openchart-feature-catalog-tel-010-group-video-sessions.md) supports many patients with isolated individual charts, while [On-Demand Urgent Video Queue](openchart-feature-catalog-tel-011-on-demand-urgent-video-queue.md) creates unscheduled access through accountable human triage.
- [Structured E-Visit Questionnaire](openchart-feature-catalog-tel-012-structured-e-visit-questionnaire.md), [Patient Photo Attachments For Async Review](openchart-feature-catalog-tel-013-patient-photo-attachments-for-async-review.md), and [Store-And-Forward Specialist Review](openchart-feature-catalog-tel-014-store-and-forward-specialist-review.md) compose asynchronous intake, evidence, dialogue, and specialist response.
- [Guided Remote Exam Capture](openchart-feature-catalog-tel-015-guided-remote-exam-capture.md) distinguishes patient report, performed action, clinician observation, and device evidence rather than claiming a hands-on examination occurred.
- [Teletherapy Private Location Attestation](openchart-feature-catalog-tel-032-teletherapy-private-location-attestation.md) adds behavioral-health privacy, location, interruption, and emergency-plan gates before admission.

The joint is one evidence discipline across different tempos: group, urgent, asynchronous, specialist, guided-exam, and teletherapy workflows preserve who supplied each fact, which policy and template applied, who made the clinical decision, and what remains unresolved.

### Failure recovery and safety escalation

- [Audio-Only Visit Fallback](openchart-feature-catalog-tel-017-audio-only-visit-fallback.md) preserves a governed modality transition when video is unsuitable or fails.
- [Virtual Visit No-Show Workflow](openchart-feature-catalog-tel-020-virtual-visit-no-show-workflow.md) distinguishes absence from technical, identity, queue, and communication problems before final disposition.
- [Technical Failure To Phone Conversion](openchart-feature-catalog-tel-021-technical-failure-to-phone-conversion.md) links diagnostic evidence, eligibility, patient agreement, and the resulting phone leg.
- [Virtual Visit Emergency Location And Escalation](openchart-feature-catalog-tel-035-virtual-visit-emergency-location-and-escalation.md) keeps current location and human-directed handoff evidence available when remote care becomes unsafe.

The joint is explicit degradation rather than silent failure: every fallback or escalation preserves the attempted modality, reason, eligibility check, participant agreement, accountable actor, and final disposition. Technical and operational signals may prompt review but never make the clinical decision.

### Completion, documentation, and continuity

- [Telehealth Billing Equivalency Documentation](openchart-feature-catalog-tel-018-telehealth-billing-equivalency-documentation.md) packages factual modality and location evidence for external human coding without moving claims ownership into openChart.
- [Post-Visit Summary Delivery](openchart-feature-catalog-tel-024-post-visit-summary-delivery.md) waits for signed, releasable encounter content and tracks patient delivery separately from media end.
- [Hybrid Follow-Up Ordering](openchart-feature-catalog-tel-030-hybrid-follow-up-ordering.md) carries human-selected next steps into in-person, virtual, asynchronous, or monitoring workflows.
- [Remote Monitoring Review Encounters](openchart-feature-catalog-tel-031-remote-monitoring-review-encounters.md) turns bounded observation sets into accountable human review and disposition.
- [Virtual Encounter E-Prescribing Launch](openchart-feature-catalog-tel-033-virtual-encounter-e-prescribing-launch.md) transfers authorized encounter context to an external prescribing boundary and reconciles its outcome.

The joint is encounter closure without premature finality: media end, encounter signature, summary release, billing-fact handoff, follow-up fulfillment, monitoring review, and prescribing outcome are related but independently observable states. Corrections use succession and trigger targeted downstream updates instead of rewriting history.

## Frappe realization

- **Core model:** OC-prefixed virtual visit, participant, grant, room, policy, attestation, consent, intake, review, transition, release, and audit DocTypes use Links, child tables, private Files, effective versions, and succession-based correction for accepted records.
- **Workflow and permissions:** Frappe Workflows encode explicit arrival, review, admission, conversion, completion, and escalation transitions; Patient, Proxy, Clinician, Telehealth Staff, Telehealth Support, Triage, Credentialing Reviewer, Consent Auditor, Security Reviewer, and specialty roles combine DocPerms with patient, facility, service, and room user permissions.
- **API and adapters:** guarded `open_chart.api.v1.telehealth` methods are the supported mutation surface; custom WebRTC signaling, partner video embeds, peripheral devices, prescribing, communications, and billing handoffs sit behind scoped adapters with signed callbacks and normalized states.
- **Surfaces:** portal pages handle join, tests, intake, consent, waiting, and summaries; Desk workspaces use Calendar, Kanban, assignments, realtime events, Query/Script Reports, Number Cards, and permission-filtered clinician consoles.
- **Automation and audit:** scheduler events and RQ jobs may create readiness reminders, due reviews, retries, expirations, and aggregates, but accepted server transitions and human clinical dispositions remain authoritative and attributable.
- **Security:** short-lived hashed grants, CSP, secret isolation, private attachments, minimum-necessary realtime payloads, redacted diagnostics, access logging, and no recording by default protect virtual-care data and room entry.

## Boundaries

Owns: openChart's virtual-care encounter state, participant authority, consent and location evidence, operational room controls, asynchronous review artifacts, modality transitions, and clinical continuity handoffs. Consumes: scheduling, patient identity, proxy authority, provider credentials, clinical chart data, communications, media and device adapters, payer policy, and external prescribing outcomes. Emits: governed encounters, participant and audit events, signed responses, follow-up requests, summary releases, and bounded integration payloads. Does not own: telecom networks, emergency dispatch, professional licensure, media vendor infrastructure, device hardware, claims adjudication, payment processing, or prescribing networks.

## Emergent behavior

Together, the features create a modality-flexible care system in which scheduling supply becomes an eligible arrival, arrival progresses through identity and consent into controlled participation, live or asynchronous evidence enters an accountable encounter, and failure can degrade safely without erasing what occurred. Shared participant, policy-version, location, and event identities let staff explain why a person entered, what modality actually delivered care, which evidence supported clinical work, and how the encounter continued afterward. The same governed state model can support custom WebRTC, partner video, audio, e-visits, store-and-forward review, and remote monitoring without allowing any adapter to become the clinical source of truth.

## Tensions to hold

- A custom WebRTC stack offers control over waiting, grants, recording, and devices but creates substantial security, accessibility, reliability, support, and scaling obligations; a partner embed reduces media engineering but may weaken proof of server-enforced policy and increase dependency risk.
- Fast browser arrival must not bypass identity, location, consent, proxy authority, or staff admission, yet excessive gates can worsen access for patients with low bandwidth, limited devices, disabilities, or language needs.
- Detailed telemetry improves recovery and platform oversight, while network, device, participant, and location data can become unnecessary sensitive surveillance if not minimized.
- Flexible fallback protects continuity, but video, audio, asynchronous, and in-person care are not automatically clinically, legally, or financially equivalent.
- Rich asynchronous evidence can expand access, but template branching, quality flags, and queue rules must remain advisory and human-governed rather than becoming hidden autonomous triage.
- Recording, group care, family participation, behavioral health, and emergency response each increase the need for segmentable permissions and participant-aware consent.

## Recombination opportunities

- Combine technology checks, intake, consent, identity, location, and room readiness into a patient-visible preflight checklist with staff-owned exception resolution.
- Combine normalized connection diagnostics, modality transitions, no-show investigation, and adapter outcomes into a quality-improvement dashboard that does not expose clinical content.
- Combine remote exam prompts, photo attachments, peripheral streams, and store-and-forward review into specialty-specific evidence packs with explicit source and quality labels.
- Combine on-demand triage, provider modality availability, jurisdiction eligibility, and virtual-room capacity into a human-governed urgent-care command queue.
- Combine post-visit summaries, hybrid follow-up orders, monitoring reviews, and prescribing outcomes into a closed continuity workspace with accountable owners for every unresolved next step.
- Use the shared adapter contract to compare custom WebRTC and partner platforms against identical security, accessibility, recording, participant, and audit acceptance criteria.

## Open questions

- Which media capabilities must openChart own directly, and which may be delegated to a partner without surrendering encounter authority, privacy, or audit completeness?
- What minimum adapter contract proves waiting-room enforcement, participant identity, recording state, encryption, quality telemetry, callback integrity, and deletion behavior?
- Which policies vary by patient location, provider location, service, facility, payer, age, or participant role, and how should effective precedence be explained?
- What is the canonical relationship among appointment, virtual visit, clinical encounter, media room, asynchronous review, and phone conversion records?
- Which technical and operational events require long-term retention, and which should be aggregated or deleted after support and audit needs expire?

## Relationships

[openChart Feature Catalog](openchart-feature-catalog-overview.md)
