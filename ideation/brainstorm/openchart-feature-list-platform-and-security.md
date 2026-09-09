# Platform Security And Deployment — Brainstorm

Status: brainstorm
Kind: report
Summary: openChart should ship hardened-by-default security, native offline-capable mobile execution, closed-loop clinical messaging, turnkey managed cloud, and validated multilingual UX — converting OpenEMR's self-managed burden and patch-discipline history into openChart's trust story.
Topics: openchart-feature-list, emr-platform, competitive-research
Repository context: openChart — Frappe-native EMR foundation; feature research versus the OpenEMR baseline and the enterprise big-3 (Epic, Oracle Health, MEDITECH Expanse)
Captured: 2026-08-23

## Possible feats

- **Hardened by default** — secure baseline image, TLS verification everywhere, continuous dependency scanning, published hardening guide enforced by installer; security advisories handled with enterprise-grade SLAs.
- **Native clinician mobile apps** — role-specific iOS/Android (Haiku/Canto/Expanse Now class) with offline-capable documentation, push notifications, barcode scanning, and biometric auth.
- **Closed-loop clinical messaging** — staff/pool messaging with acknowledgment, escalation ladders, device/alarm integration surface (Oracle Health Messenger pattern), reducing alarm fatigue.
- **Operational boards** — clinical whiteboards, room/bed status, staffing and device assignment views auto-populated from the record.
- **Managed cloud offering** — MEDITECH-as-a-Service-style subscription: updates, backups, monitoring, compliance operations handled centrally.
- **Validated multilingual UX** — fewer languages than OpenEMR's 30+, but clinically reviewed translation coverage per release with RTL support.
- **Device integration surface** — barcode scanners, vitals devices, smart-pump data hooks (CareAware-direction) as documented extension points.

## Focus

Which platform capabilities make openChart feel enterprise-trustworthy on day one while staying cheaper to run than anything the big-3 or a self-hosted OpenEMR instance offers?

## Current state: OpenEMR baseline

OpenEMR core includes multisite/multi-facility support, role-based ACLs with fine-grained objects, emergency access, AD/LDAP, MFA (TOTP/U2F), Argon hashing, database/document encryption, session controls, brute-force protection, audit trails, Docker/Kubernetes deployment, REST/FHIR APIs, module manager, 30+ community languages (coverage uneven per reviews). Recurring 2025-era security advisories (broken access control, XSS, IDOR, disabled TLS certificate verification pre-7.0.4, logging defects) illustrate patch-discipline burden falling on self-hosters. No bundled native clinician mobile app (responsive web only); no managed-cloud tier from the project itself.

Sources: open-emr.org Features wiki; GitHub security advisories (GHSA-7qj6-jxfc-xw4v, GHSA-vjmv-cf46-gffq, GHSA-2g6h-725p-pqhp, GHSA-8gj5-r8vm-mghq); Modules catalog.

## Enterprise gap candidates

- Epic: Haiku/Canto/Rover native apps; enormous audit/EHI surface including AI-interaction records; break-glass/access-review patterns (largely UserWeb-documented).
- Oracle: Workflow Authentication integrating MFA into clinical flow; CareAware device connectivity; near-real-time vitals capture; Health Messenger closed-loop alerts; digital room signage; Clinical Operations Whiteboard; OCI-hosted SaaS posture.
- MEDITECH: Expanse Now physician smartphone app (orders, results, dictation, rounding lists); Point of Care bedside barcode workflows with mobile image capture; Home Care Mobile real-time remote documentation; Google Cloud-native platform; MaaS subscription model; High Availability Snapshot resilience.
- Common thread: platform qualities are sold as operational outcomes (uptime, speed, less typing), not feature checklists.

## Proposed feature set for openChart

Parity floor: match OpenEMR's ACL/MFA/encryption/multisite/Docker surface. Adopted gaps: security-hardened distribution with advisory SLA and automated patch channel; two native mobile apps at launch (clinician + home-care/caregiver pattern) with offline queueing; closed-loop messaging with escalation analytics; whiteboard/room-status boards; vendor-operated managed-cloud tier with published RTO/RPO; per-release clinically validated language packs (launch: English + Spanish, expanding); device-integration SDK. Twist: Frappe-native extensibility plus openness gives ISVs an app market path incumbents gatekeep — ecosystem without permission slips.

## Interfaces and boundaries

Consumes: identity providers, device/vendor APIs, cloud infrastructure, translation contributions. Emits: auth/session services to every domain, audit/event stream to all modules, mobile API surfaces, deployment artifacts. Owns tenancy, identity, audit chain, and operational tooling; does not own customer infrastructure in self-hosted mode.

## Alternatives and tensions

Native apps cost real money vs responsive web's reach — offline capability forces native anyway for home care. Managed cloud revenue conflicts with open-source ethos unless licensing stays clean (open core boundaries must be explicit early). Broad device integration is an endless compatibility treadmill; SDK-first limits liability. Fewer validated languages trades reach for honesty versus OpenEMR's breadth-with-caveats.

## Open questions

- Which mobile roles launch first — physician rounding, nurse bedside, or home-care clinician?
- What open-core boundary keeps managed cloud defensible without poisoning community trust?
- Break-glass and emergency-access UX: which incumbent pattern do we adopt versus improve?

## Relationships

Clustered in [Synthesis: Intelligence Platform](openchart-feature-list-synthesis-intelligence-platform.md). Adjacent: [Interoperability And Exchange](openchart-feature-list-interoperability.md), [Clinical AI And Governance](openchart-feature-list-clinical-ai.md).
