# openChart Feature List Overview — Brainstorm

Status: brainstorm
Kind: reference
Summary: research across Epic, Oracle Health, and MEDITECH Expanse against the OpenEMR baseline yields twelve feature domains where openChart can match enterprise capability while differentiating on governed AI, closed-loop accountability, turnkey exchange, and open analytics — an EMR built to beat OpenEMR on workflow, trust, and total cost.
Topics: openchart-feature-list, emr-strategy, competitive-research, feature-roadmap
Repository context: openChart — Frappe-native EMR foundation; feature research versus the OpenEMR baseline and the enterprise big-3 (Epic, Oracle Health, MEDITECH Expanse)
Captured: 2026-08-23

## Possible feats

- **Beat OpenEMR where it is weakest** — clinician UX/mobile, analytics depth, turnkey interoperability, native revenue-cycle operations, governed AI, and implementation burden.
- **Match the big-3 where it matters** — ambient documentation, CPOE/CDS breadth, e-prescribing with EPCS/benefit/ePA, registry-driven population health, national exchange participation, cloud delivery.
- **Differentiate where nobody stands** — pluggable model layer with artifact-level provenance, reproducible open metric semantics, financial provenance as API, consent-governed engagement as first-party feature.

## Motivation

OpenEMR proves open-source clinical software can reach ONC certification and global adoption, but its 2022 usability report (SUS 55), module-dependent prescribing/telehealth/AI, clearinghouse-assembled revenue cycle, SQL-only analytics, recurring security-advisory burden, and self-managed operations leave a large gap between "capable" and "preferred". The enterprise leaders (Epic, Oracle Health, MEDITECH) define that preferred standard — integrated suites with embedded AI (Epic Art, Oracle Clinical AI Agent, MEDITECH Navigator), network effects (Care Everywhere, QHINs, Traverse), and operational depth — at proprietary prices with proprietary lock-in. openChart exists in that gap: Frappe-native, independently usable, original implementation.

## Goals

Observable outcomes rather than activity: a clinic documents a complete encounter with ambient assistance faster than in OpenEMR; every abnormal result has a provable owner and resolution; prescriptions flow electronically without per-vendor subscription assembly; denial appeals assemble their own evidence; patients self-schedule into constraint-safe slots; outside records arrive reconciled; metrics reproduce across versions; clinics choose AI models without switching EHRs.

## Non-goals

Not a fork or code copy of OpenEMR, Marley, or any incumbent. Not a PACS, LIS bench system, or billing bureau replacement. Not autonomous clinical action — every consequential step keeps human gates by default. Not hospital-inpatient completeness at launch (BCMA/smart-pump-class capabilities enter via roadmap, not v1 promise). Not competing on Cosmos-style data-moat economics; openness is the strategy, not a concession.

## What the system delivers

Twelve domains organized as four clusters: a closed-loop clinical core (documentation through imaging), an access-and-engagement funnel (intelligent scheduling plus consent-governed portal/telehealth), a business-and-exchange spine (provenance-linked revenue cycle riding managed interoperability), and an intelligence platform (governed pluggable AI, open semantic analytics, hardened mobile-first platform with managed-cloud delivery). Each atomic document states the OpenEMR parity floor, the enterprise gap candidates with sources, and the proposed openChart feature set with its twist.

## System model

```text
patients ──▶ ACCESS FUNNEL ──▶ CLINICAL CORE ──▶ BUSINESS & EXCHANGE ──▶ payers/networks
             scheduling          documentation        revenue cycle
             portal/video        orders + CDS         FHIR/X12/Direct/QHIN-path
             omnichannel         pharmacy · labs      public health
                    │           imaging                   │
                    │                │                    │
                    └──── INTELLIGENCE PLATFORM ─────────┘
                     governed AI · open analytics · mobile/cloud platform
```

Value flows left to right (access feeds care, care generates business events, events reach payers/networks); intelligence and platform underlie all four surfaces reading and writing every domain through governed contracts.

## Cluster map

- [Synthesis: Clinical Core](openchart-feature-list-synthesis-clinical-core.md) — the point-of-care circuit where accountability loops and ambient-to-action pipelines live.
- [Synthesis: Access And Engagement](openchart-feature-list-synthesis-access-and-engagement.md) — demand-shaping funnel from prediction to consent-governed patient surfaces.
- [Synthesis: Business And Exchange](openchart-feature-list-synthesis-business-and-exchange.md) — one managed pipeline carrying money and data flows with observability.
- [Synthesis: Intelligence Platform](openchart-feature-list-synthesis-intelligence-platform.md) — the trust-and-openness wedge amplifying every other cluster.

## How it fits

openChart's existing foundation (OC DocTypes, versioned idempotent intake API, guarded controllers, synthetic-fixture discipline, provenance-first record design) already embodies several packet themes — amendments, succession, identity-conflict routing — so this feature list extends an architecture that anticipated it rather than bolting governance onto legacy behavior. Enterprise patterns inform targets; no incumbent implementation code is consulted or copied. Frappe-native extensibility supplies the app-market path incumbents gatekeep.

## Key decisions and open questions

Load-bearing tensions preserved across the packet: structured capture vs clinician speed (resolved only jointly with ambient AI); partner-first vs first-party for ambient, e-Rx networks, exchange aggregators, and video; open-core boundaries before managed-cloud pricing; evaluation infrastructure before third-party models; jurisdiction-aware consent defaults before convenience automation. Each domain document carries its own open questions; none are settled here.

## Document map

Overview:
- this document

Syntheses:
- [Synthesis: Clinical Core](openchart-feature-list-synthesis-clinical-core.md)
- [Synthesis: Access And Engagement](openchart-feature-list-synthesis-access-and-engagement.md)
- [Synthesis: Business And Exchange](openchart-feature-list-synthesis-business-and-exchange.md)
- [Synthesis: Intelligence Platform](openchart-feature-list-synthesis-intelligence-platform.md)

Atomics — clinical core:
- [Clinical Documentation And Ambient Capture](openchart-feature-list-clinical-documentation.md)
- [Clinical Orders And Decision Support](openchart-feature-list-orders-and-cds.md)
- [Pharmacy And E-Prescribing](openchart-feature-list-pharmacy-and-eprescribing.md)
- [Labs And Diagnostics](openchart-feature-list-labs-and-diagnostics.md)
- [Imaging Workflows](openchart-feature-list-imaging-workflows.md)

Atomics — access and engagement:
- [Scheduling And Patient Access](openchart-feature-list-scheduling-and-access.md)
- [Patient Engagement And Telehealth](openchart-feature-list-patient-engagement.md)

Atomics — business and exchange:
- [Revenue Cycle](openchart-feature-list-revenue-cycle.md)
- [Interoperability And Exchange](openchart-feature-list-interoperability.md)

Atomics — intelligence platform:
- [Analytics And Population Health](openchart-feature-list-analytics-and-population-health.md)
- [Clinical AI And Governance](openchart-feature-list-clinical-ai.md)
- [Platform Security And Deployment](openchart-feature-list-platform-and-security.md)
