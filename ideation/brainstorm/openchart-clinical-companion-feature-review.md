# Clinical Companion Feature Review — Brainstorm

Status: brainstorm
Kind: report
Summary: the 1,115-feature catalog and twelve strategy documents reviewed against the clinical-companion vision's eight pillars — strong provenance and governance substrate, an assisted-human worldview that contradicts credentialed AI practitioners, two pillars with zero coverage, and roughly a quarter of the corpus sitting outside the clinical boundary.
Topics: openchart-clinical-companion, gap-analysis, feature-catalog-review, ai-practitioner, scope-boundary
Repository context: openChart — Frappe v15 native EMR; review of the existing brainstorm corpus (1,115 catalog features across 22 domains, 12 feature-list strategy documents) against the product-owner vision stated 2026-08-25
Captured: 2026-08-25

## Verdict

The catalog is a well-built record-and-fulfillment EMR substrate,
benchmarked against OpenEMR, Epic, Oracle Health, and MEDITECH Expanse,
with genuinely strong provenance, governance, and auditability — the
audit, consent, retention, and AI-artifact machinery is better than most
of what it was benchmarked against. It was designed, however, around an
assisted human clinician in a conventional practice, not around the
vision's always-on companion serving human and AI physicians alike.
Measured against the eight pillars, P1, P2, and P6 have real substrate;
P3 and P4 have excellent raw material but no assembled use case; P5 and
P7 are entirely absent, with zero features addressing them and, in P7's
case, a structural contradiction to resolve first. P8 exists as a
half-built portal rather than a companion loop. Roughly a quarter of the
corpus — about 250 of 1,115 features — sits in billing, scheduling, HR,
and practice-operations territory the vision excludes to openPractice.
None of this is wasted work: the substrate is sound, the gaps are
nameable, and the boundary problem is a question of ownership rather than
of quality.

## Coverage by pillar

### P1 — Pre-visit preparation: adequate substrate

Present and usable largely as-is. aic-007 pre-visit chart summary and
aic-016 AI-assisted chart-prep checklist do the assembly; doc-037
contextual timeline, doc-038 cited chart summary, and doc-040 semantic
chart search supply retrieval; pmr-050 record summary workspace and
pmr-049 timeline give the clinical picture; pub-005 vaccines-due-today
and car-022 annual wellness visit prep add protocol-driven prompts;
car-055 longitudinal timeline, mob-006 quick chart review cards, and
eng-027 previsit forms round out mobile and patient-supplied inputs.

Missing: on-demand targeted retrieval of outside records — "query the
network for this patient before the 2pm visit". Every inbound path in
`int` is push or scheduled (int-025, int-036 through int-038); there is
no record-locator or patient-discovery query anywhere, despite the
interoperability strategy document naming MEDITECH Traverse as the model.
Preparation that cannot reach outward is preparation over a partial
chart.

### P2 — Always-on in-visit companion: partial, episodic rather than always-on

Substantial capture machinery exists. aic-003 consent-gated ambient
capture, aic-004 ambient note review queue, and aic-005 sentence-level
transcript provenance define the governed pipeline; doc-039 ambient visit
capture draft is its documentation-side counterpart; mob-020 consented
mobile ambient capture is the single best P2 asset in the corpus, with
mob-019 dictation beside it, and tel-002 clinician video console with
chart context covers the remote room. In-visit assistance appears as
ord-008 unified order composer, aic-013 human-approved order suggestions,
aic-015 documentation-gap nudges, and iax-022 key-phrase expander.

Missing: the always-on part. Everything is capture-then-queue. doc-039 is
explicitly a batch lifecycle — Recording, then Processing, then Draft
Ready — and aic-048's latency and fallback policy assumes asynchronous
jobs. There is no streaming live-transcript surface, no mid-visit
retrieval or prompting tied to what is being said in the room, no
room-resident session that stays open, no session resume across
interruptions, and no dual-operator UX contract for a human and an AI
editing the same note concurrently — `iax` contains nothing of the kind.
mob-020, tel-002, and doc-039 are three good components never wired
together into one continuous loop.

### P3 — Case collaboration: thin, right seeds, no assembly

The seeds are correct. car-054 care conference coordination is
structurally the right record — agenda, attendance, decisions, dissent
captured as clinical content. car-023 referral order with clinical
summary and car-028 e-consults open outbound paths; car-031 consult
report ingestion closes one; car-053 handoff acknowledgment and msg-028
rapid clinician consult chat carry the fast lane. img-040 multi-reader
consensus and tel-014 store-and-forward specialist review are the two
genuine multi-reader patterns.

Missing: assembly. Nothing packages a case — imaging, timeline, the
specific question, prior workup — for a meeting. There is no
second-opinion request flow distinct from a referral; img-040's consensus
pattern is trapped inside radiology and never generalized
cross-specialty; consult-package exchange has no representation in `int`,
leaving the `car` and `msg` collaboration features unlinked to
interoperability entirely; and AI practitioners appear nowhere as
conference or thread participants.

### P4 — Medico-legal support: strong substrate, no use case

The strongest substrate in the corpus, and the one least shaped for its
purpose. The evidentiary spine is sec-022 append-only hash-chained audit
ledger, sec-021 clinical record audit including reads, sec-023 audit
search, sec-028 disclosure accounting, and sec-046 fail-closed retention
and legal hold. dms-040 chain-of-custody legal export is the closest
single feature to the pillar — sealed, dual-reviewer, with a
verification-breaking manifest — but covers documents only; dms-016
per-document disclosure log and dms-018 legal-hold override sit beside
it. Chart history reconstructs through doc-069 full view and edit audit,
doc-028 and doc-029 section provenance and diff, and reg-044 merge audit.
The failure-to-notify defense trio is msg-005 escalation ladders, msg-006
acknowledgment tracking, and msg-023 unread-critical phone fallback, with
msg-037's unified communication attempt log beneath them. anl-060 execution provenance and
qme-034 auditor evidence package show the regulator-facing pattern
already exists.

Missing: everything defense-shaped. No matter or case workspace binding a
patient, a date range, and an allegation. No cross-domain sealed evidence
package — dms-040 generalized past documents to chart facts, orders,
result acknowledgments, messages, AI interactions, and access history. No
who-knew-what-when timeline reconstruction: no "what did the chart look
like on date X", no result-acknowledgment-to-action latency. No
standard-of-care rationale captured as such. No redaction for production
(dms-038 watermarks only), no privileged attorney-work-product scoping,
and no AI-attribution audit class linking `aic`'s invocation provenance
into the legal record — precisely what a plaintiff will ask for first
once AI practitioners exist.

### P5 — Patient diagnostic research: absent, zero features

Nothing in the corpus addresses this pillar. No differential-diagnosis
workspace anywhere. No hypothesis or working-diagnosis object carrying
uncertainty and competing candidates — `pmr`'s problem list holds
conclusions only, never the reasoning that produced them. No
workup-strategy comparison: lab-027 suggests screening tests from
guidelines and ord-012 suggests orders from an already-chosen diagnosis,
and neither reasons over a differential to ask which test discriminates
between hypotheses.

Most tellingly, no external knowledge connectors of any kind — a grep
across all 1,115 documents finds zero literature, guideline,
drug-reference, or clinical-trial-matching integrations. Point-of-care
similar-patient evidence, the Cosmos analog, is named in the competitive
scan and implemented by no feature; anl-032 de-identified extract
generation and anl-033 governed research cohort release are the honest
path toward it. aic-042 clinical risk model serving is operational risk
(no-show, readmission), not diagnostic reasoning, and aic-010's stated
boundary explicitly excludes interpretation.

### P6 — Treatment plan research and creation: authoring spine exists, research absent

The authoring half is well built. car-001 through car-005 give versioned
care-plan templates, measurable goals, intervention tasks, version
approvals, and interdisciplinary authorship. ord-013 through ord-016
govern order sets. tel-030 hybrid follow-up ordering, pmr-024 monitoring
plans, and sch-019 sequential care-pathway booking (clinical residue
misfiled in scheduling) complete the execution edge.

Missing: the research half the pillar names. Nothing retrieves evidence
or compares therapeutic options for this patient and feeds car-001. There
is no treatment-response tracking against the plan, no outcome feedback
from `anl` back into plan authoring, and no connection between plan
versions and the patient-side adherence loop of P8. The plan can be
written and approved; it cannot be researched, measured, or revised on
evidence.

### P7 — AI practitioner and openXwallet: absent, structurally contradicted, substrate transfers

Zero occurrences of openXwallet or any AI-practitioner concept across all
1,115 documents. Around 575 entries carry the boilerplate boundary that
the feature "does not own … autonomous clinical action". The load-bearing
conflict is aic-036 structural human-review gates, which states that the
AI service role has zero submit permission on clinical DocTypes and that
a service-account identity cannot satisfy a human gate — restated in the
`aic` synthesis as "no AI service role receives submit authority on
consequential clinical DocTypes". Every signature, credential, and
delegation feature assumes a human: doc-023 and doc-027, ord-030 through
ord-034, phr-011 through phr-013 credential-bound signing, plt-004
provider master with no non-human provider type, plt-005 human licenses
only, plt-045 human-only routing.

What transfers almost intact into a credentialed-AI-practitioner model is
considerable. aic-033 vendor model certification registry becomes the
openXwallet credential registry. aic-043 validation evidence plus aic-044
fairness release gate become the scope-of-practice dossier. aic-022
evaluation case registry and aic-023 regression scoring runs become
competency examination and recertification. aic-028 kill switch and
aic-046 incident response become license suspension and adverse-event
review. aic-026, aic-027, and aic-050 drift, bias, and acceptance
monitoring become ongoing practice monitoring. aic-039 confidence
threshold routing becomes supervision escalation. aic-025 per-site and
per-role enablement becomes privileging. plt-005, plt-043, and plt-044 —
credentials, e-signature authority, delegation registries — are the
authority triad. phr-011 and phr-013 signing ceremony is the natural seam
for credential-bound AI prescribing.

Genuinely new, covered by no entry: verifiable-credential presentation
and revocation checking (aic-047 handles API-key rotation only); the AI
practitioner as a clinical actor with identity, signature authority, and
attributable liability; per-credential scope-of-practice enforcement;
supervision topology, including who supervises which AI, co-signature,
and mid-encounter handoff; AI-to-human consult and disagreement
adjudication; liability attribution when a credentialed AI errs; and
patient consent to and disclosure of AI treatment.

### P8 — Patient app loop: half-built portal, not a companion

The parts exist. eng-036 portal care plan view, eng-037 patient task
lists, eng-038 remote monitoring submission, eng-039 wearable
connections, and eng-071 patient uploads cover the portal surface;
mob-029 patient home device feeds and mob-031 wearable pipeline carry
device data; pmr-021 medication adherence capture and pmr-033, pmr-034,
pmr-035 device and home vitals give the clinical return path; phr-046
adherence follow-up tasks and msg-034 chronic-care check-ins close some
loops manually; int-004 patient-standalone SMART launch, int-056 device
gateway vitals ingest, and tel-031 remote-monitoring review encounters
supply the transport and review edges.

Missing: the app and the loop. There is no patient-side app anywhere in
the catalog — `mob` is clinician-only, and the "patient app" is a browser
portal. eng-037 tasks carry no link to a care-plan version, no adherence
measurement, no medication-taking loop, no symptom diary, no
plan-deviation signal back to the doctor. `int` has neither a care-plan
push contract to a patient app nor an adherence and PRO ingest contract.
The pieces — eng-036, eng-037, eng-038, mob-029, pmr-021, phr-046 — are
never composed into one loop.

## The AI-practitioner tension

This is the deepest finding of the review. The catalog encodes `human` as
the gate predicate wherever authority is exercised; the vision needs
*accountable credentialed practitioner* as the predicate, with humanity
as one way to qualify. aic-036 is the sharpest statement of the current
position, restated as policy in the `aic` synthesis: no AI service role
receives submit authority on consequential clinical DocTypes.

The reframing is not a demolition. The governance machinery already in
the catalog — artifact-level provenance, evaluation registries and
regression runs, drift and bias monitoring, kill switches and incident
workflow, per-site enablement — is precisely what makes a credentialed AI
practitioner defensible in the first place, and none of it is discarded.
What changes is where authority comes from: a validated openXwallet
credential, bound to a model version, scoped and revocable, rather than
the fact of being human. An ungoverned AI acting autonomously is what
aic-036 rightly forbids; a credentialed practitioner acting within a
verified scope is a different object, and the catalog has no name for it.

Two further assumptions need restating. aic-034 PHI boundary controls
treat every inference as PHI egress to an outside party; under the
vision, an AI practitioner on the care team accesses PHI under treatment
purpose — a different legal and architectural posture, with different
logging and consent obligations. And aic-042's blanket "cannot diagnose,
order, treat" is written actor-independently: it constrains the
capability rather than the credential, so it forbids the credentialed
case along with the ungoverned one.

Separately, an AI practitioner needs longitudinal reasoning state across
encounters — an evolving understanding of a patient, carried forward.
Every `aic` artifact today is per-invocation and expiring; aic-007's
pre-visit summary literally ends in an Expired state. There is nowhere in
the record model to put a practitioner's continuity of thought.

## Boundary findings

Roughly 250 of 1,115 features — 22 to 25 percent — sit in territory the
vision excludes: billing, scheduling, HR and workforce, practice
operations, and supply chain.

The largest blocks: `sch`, where about 47 of 55 features are pure
practice-access operations, with clinical residue in sch-017, sch-019,
sch-026, sch-030, sch-031, sch-037, sch-039, sch-043, and sch-049 that
should re-home to `car` or `tel`; `anl`, where about 35 of 60 are revenue
(anl-015, anl-019, anl-026, anl-050 through anl-053), scheduling
(anl-013, anl-018, anl-021, anl-045, anl-056), or workforce (anl-016,
anl-017, anl-020, anl-039, anl-044); `qme`, where about 28 of 35 are MIPS
scoring and payment (qme-007, qme-009, qme-012, qme-020, qme-021,
qme-025, qme-026, qme-035); and `phr`, with roughly 20 in benefit and
prior-authorization (phr-017, phr-018, phr-021 through phr-025) and
inventory and supply (phr-037 through phr-041, phr-048).

Smaller blocks run across the corpus: the `eng` financial features
(eng-011 through eng-015, eng-054, eng-055) and front-desk surfaces; the
`reg` insurance and guarantor block (reg-013, reg-014, reg-023 through
reg-027, reg-051); the workforce and fleet half of `mob` (mob-025,
mob-026, mob-027, mob-032 through mob-038, mob-040); payer transports in
`int` (int-050 through int-054); plt-033, plt-039, plt-041, plt-046;
dms-025 through dms-028; doc-041 through doc-043 (E/M coding evidence);
ord-059 and ord-060; img-005, img-006, img-032, img-033; the `car` payer,
logistics, and workforce entries (car-025, car-030, car-036, car-037,
car-043, car-048, car-049); and pub-016, pub-017, pub-036, pub-038 —
including occupational health, which is HR territory.

At the strategy-document level, [Revenue Cycle](openchart-feature-list-revenue-cycle.md)
is a direct boundary violation serving no pillar: excise it to
openPractice and rewrite
[Synthesis: Business And Exchange](openchart-feature-list-synthesis-business-and-exchange.md)
around clinical exchange only — that synthesis already flags the
ownership question itself.

The disposition for the features, though, is not deletion. Mark excluded
features as openPractice-owned integration points and keep the ideation:
the research is sound and the interfaces still matter to openChart. What
moves is ownership, not knowledge.

## Domain disposition

| Domain | Features | Vision role | Pillars served | Out-of-boundary (approx) |
| --- | --- | --- | --- | --- |
| doc | 70 | Core enabler | P1, P2, P4 | ~6 |
| ord | 65 | Core enabler | P2, P6 | ~3 |
| pmr | 50 | Core enabler | P1, P2, P8 | 0 |
| lab | 50 | Supporting | P2, P5 | ~7 |
| img | 40 | Supporting | P2, P3, P5 | ~6 |
| phr | 55 | Mixed | P2, P6 | ~20 |
| qme | 35 | Mostly out of scope | — | ~28 |
| pub | 40 | Peripheral, P1 pocket | P1 | ~7 |
| reg | 55 | Supporting | P1, P4 | ~10 |
| sch | 55 | Mostly out of scope | — | ~47 |
| eng | 75 | Supporting, P8 slice | P8 | ~15 |
| tel | 35 | Core enabler (remote) | P2 | ~7 |
| msg | 40 | Supporting | P3, P4, P8 | ~10 |
| mob | 40 | Core enabler (capture half) | P1, P2, P8 | ~13 |
| car | 55 | Core enabler | P3, P6 | ~10 |
| aic | 50 | Core enabler + P7 substrate | P1, P2, P7 | ~8 |
| anl | 60 | Low, P5 substrate | P5 | ~35 |
| plt | 55 | Enabling, P7 skeleton | P7 | ~5 |
| sec | 55 | Strong P4 substrate | P4 | 0 |
| dms | 40 | Moderate, best P4 feature | P4 | ~4 |
| iax | 30 | Quality layer | all | ~1 |
| int | 65 | Moderate-strong transport | P1, P8 | ~5 |

## Recommended new packets

The forward agenda. Each is a new brainstorm packet, not an edit to the
existing ones.

**R1 — Practitioner identity and openXwallet credentialing.** A new
domain. The AI practitioner as clinical actor; verifiable-credential
presentation, verification, and revocation; scope-of-practice enforcement
per credential; model-version binding; supervision topology and
co-signature; per-action authority provenance; patient consent to and
disclosure of AI treatment. Restates aic-036's gate predicate from
"human" to "accountable credentialed practitioner". Builds on plt-005,
plt-043, plt-044, aic-033, aic-043, aic-044, phr-011, phr-013.

**R2 — Live visit companion.** Streaming transcript surface, mid-visit
retrieval and prompting, a room-resident always-on session with resume,
wiring doc-039, mob-020, tel-002, aic-003, aic-004, and aic-005 into one
continuous loop. Includes the dual-operator UX contract that `iax` lacks.

**R3 — Diagnostic reasoning workspace.** A working-diagnosis and
hypothesis object carrying uncertainty (extending `pmr`), a differential
builder, workup-strategy comparison bridging ord-012 and lab-027, and
similar-patient evidence built over anl-032 and anl-033.

**R4 — External knowledge connectors.** Governed literature, guideline,
drug-reference, and trial-matching integrations with citation provenance
— a new class within `int`, feeding R3 and R5.

**R5 — Treatment-plan research bench.** Evidence retrieval and
therapeutic-option comparison feeding car-001 through car-005;
plan-response tracking; outcome feedback loop from `anl`.

**R6 — Case collaboration packet.** Case-presentation assembly; a
conference workspace extending car-054; a second-opinion flow distinct
from referral; cross-specialty review generalizing img-040;
consult-package exchange in `int`; AI participants throughout.

**R7 — Medico-legal matter workspace.** A matter object; a cross-domain
sealed evidence package generalizing dms-040; who-knew-what-when timeline
reconstruction over sec-021, sec-022, sec-023, doc-069, and msg-037;
redaction for production; privileged counsel scoping.

**R8 — Patient companion app and adherence loop.** A native patient app;
a care-plan push contract; a plan-to-action-to-measurement-to-deviation
loop binding eng-036, eng-037, eng-038, mob-029, pmr-021, and phr-046; an
adherence and PRO ingest contract in `int`.

Alongside these, boundary cleanup: excise the revenue-cycle strategy
document to openPractice, and re-home the `sch` clinical residue to `car`
and `tel`.

## Relationships

The owner's issue-by-issue direction on these findings — which revises R7
(matter workspace to openPractice) and R8 (the patient app is HealthLinc) —
is recorded in
[Clinical Companion Phase Decisions](openchart-clinical-companion-phase-decisions.md).
Reviews the vision stated in
[openChart Clinical Companion Vision](openchart-clinical-companion-vision.md)
against
[openChart Feature Catalog Overview](openchart-feature-catalog-overview.md)
and
[openChart Feature List Overview](openchart-feature-list-overview.md).
Load-bearing syntheses:
[Synthesis: aic](openchart-feature-catalog-synthesis-aic.md) (the
human-gate stance and AI governance substrate),
[Synthesis: car](openchart-feature-catalog-synthesis-car.md) (care plans
and collaboration),
[Synthesis: sec](openchart-feature-catalog-synthesis-sec.md) (audit and
retention spine), and
[Synthesis: dms](openchart-feature-catalog-synthesis-dms.md)
(chain-of-custody export).
