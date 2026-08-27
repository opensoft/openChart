# Patient Engagement And Telehealth — Brainstorm

Status: brainstorm
Kind: report
Summary: openChart should ship a consent-governed portal with granular proxy/guardian rules, omnichannel two-way communication, integrated video visits, and an assistant layer — matching MyChart-class engagement while making patient-controlled permissions a first-party feature OpenEMR lacks.
Topics: openchart-feature-list, patient-engagement, competitive-research
Repository context: openChart — Frappe-native EMR foundation; feature research versus the OpenEMR baseline and the enterprise big-3 (Epic, Oracle Health, MEDITECH Expanse)
Captured: 2026-08-23

## Possible feats

- **Granular proxy/guardian model** — family/caregiver access with age-based transitions, adolescent confidentiality rules, scope limits, and self-service revocation (Sharing Hub depth).
- **Omnichannel messaging** — secure inbox plus conversational SMS/email/voice threads routed to staff work queues, including patients without accounts.
- **Integrated video visits** — scheduled and on-demand virtual care launched from portal/app without leaving the chart context; e-visits as structured questionnaires.
- **Patient-facing assistant** — chart-question, scheduling, and bill-explanation chatbot in the Emmie/MyHealth Assistant pattern, with strict scope guardrails.
- **Consumer health integrations** — Apple Health Records, wearable/device data ingestion into the record.
- **Digital intake** — previsit forms, consents, insurance capture, and payments completed remotely.

## Focus

What engagement surface makes patients prefer openChart clinics, and what governance makes that surface safe for minors, proxies, and sensitive data?

## Current state: OpenEMR baseline

OpenEMR ships an onsite portal (login, demographics, appointments, secure messaging/chat, online payments, med/allergy/problem/result viewing, CCDA access, refill requests, custom forms) plus offsite/third-party portal APIs. Direct Messaging is core. Telehealth arrives via the Comlink module or third-party platforms (Jitsi/WebRTC integrations); video infrastructure, consent, and identity verification are deployment-dependent. Proxy access exists but lacks the mature policy model of enterprise portals; no patient-facing AI assistant; no native consumer-device pipeline.

Sources: open-emr.org Patient Portal wiki; API README; Modules catalog (Comlink); Release Features wiki.

## Enterprise gap candidates

- Epic MyChart: results/notes/scheduling/messaging/payments at scale; Sharing Hub proxy management with minor-to-adult permission transitions; Emmie conversational assistant handling scheduling and billing questions; Video Visits for All (no existing account needed).
- Oracle HealtheLife-lineage portal with Unified Consumer Communications (portal + SMS keyword automation + routing), scheduled native video visits from the portal, Amwell on-demand partner option.
- MEDITECH MHealth app, Expanse Patient Connect bidirectional multilingual SMS with registry-driven outreach, Virtual On Demand Care, MyHealth Assistant chatbot, Health Records on iPhone.
- Cross-organization identity portability (MyChart Central passkeys/single ID) remains an ecosystem moat openChart can counter only with standards.

## Proposed feature set for openChart

Parity floor: portal with records/appointments/messaging/payments/forms, refill requests, education. Adopted gaps: first-party video visit service with encounter-linked documentation and identity assurance; asynchronous e-visit questionnaire flows; proxy/adolescent permission engine with time-boxed delegation and revocation audit; two-way SMS thread infrastructure with staff assignment; device-data ingestion (Apple Health/GFIT-class); scoped patient assistant answering record/scheduling/billing questions with citation to source data. Twist: every portal action lands in the same clinical audit trail; consent changes take effect immediately across sharing surfaces.

## Interfaces and boundaries

Consumes: schedule slots from scheduling-and-access, statement balances from revenue-cycle, released results/orders data, FHIR APIs from interoperability. Emits: intake data to clinical-documentation, messages/tasks to staff queues, patient-reported observations to analytics-and-population-health. Owns the patient-facing contract and consent state; does not own clinician workflow queues.

## Alternatives and tensions

White-labeling an external engagement suite is faster but splits the audit trail and margin. Adolescent confidentiality rules interact with state law variability — configuration burden is real. A patient chatbot raises hallucination/overreach risk requiring hard scope fences and human escalation. On-demand video (Telehealth Anywhere pattern) may conflict with licensure boundaries.

## Open questions

- Build vs buy the video stack (WebRTC infra vs embedded vendor)?
- Which jurisdictions' minor-consent matrices launch first?
- Does the assistant read live FHIR data or a curated summary index?

## Relationships

Clustered in [Synthesis: Access And Engagement](openchart-feature-list-synthesis-access-and-engagement.md). Adjacent: [Interoperability And Exchange](openchart-feature-list-interoperability.md), [Clinical AI And Governance](openchart-feature-list-clinical-ai.md).
