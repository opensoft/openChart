## 1. Coordinated Contract Dependency (openxFactory)

- [ ] 1.1 Pin the openXwallet neutral-core contract version openChart extends (contract-v1.31) and record the pinned digest in this change.
- [ ] 1.2 Author the specialty/expertise attestation contract over the neutral core and open it for openxFactory ratification.
- [ ] 1.3 Author the state-license-number binding contract, including the append-only covered-hash set and the major/minor reissue classification.
- [ ] 1.4 Author the zone model declaration contract (act and object classes, license level, boundary reference).
- [ ] 1.5 Author the co-signature record-kind contract carrying one exercise and N role-qualified signatures.
- [ ] 1.6 Record the coordination state for all four contracts (proposed / under review / ratified) so openChart work proceeds against the shape without waiting on ratification.

## 2. Registries And Legal Research

- [ ] 2.1 Create the named ongoing legal-research work item that maintains jurisdiction data, with its owner and cadence.
- [ ] 2.2 Define the versioned Scope Registry schema: act and object classes, license boundaries, license-level and per-jurisdiction calibration, whole-registry versioning.
- [ ] 2.3 Define the versioned Jurisdiction Registry schema: AI-disclosure obligations, pre-licensure supervision requirements, license-boundary calibration.
- [ ] 2.4 Seed the first version of both registries for the first jurisdiction and license level, from the legal-research work item.
- [ ] 2.5 Verify a jurisdiction requiring per-encounter AI disclosure is representable as registry data without changing the general one-time consent rule.

## 3. Practitioner And Credential Records

- [ ] 3.1 Add the Practitioner DocType with holder class from the openXwallet vocabulary, specialty attestation, lifecycle state, audit provenance and migrations.
- [ ] 3.2 Add the optional credential-binding reference (holder identifier, holder class, wallet state, provenance) and enforce that the wallet identifier is never a subject key or a resolution path.
- [ ] 3.3 Add the License Binding DocType with license number, jurisdiction, license level, environment, effective interval, state and append-only covered-hash set.
- [ ] 3.4 Implement composition-hash computation over the six declared components and the major/minor classification.
- [ ] 3.5 Implement strict revoke on any composition change, automatic reissue for minor changes, and the attestation record naming component, prior hash and new hash.
- [ ] 3.6 Enforce that the covered-hash set is append-only — no removal, no in-place overwrite.
- [ ] 3.7 Add permissions, audit behavior and synthetic fixtures for practitioner, binding, license and attestation records.

## 4. Scope Grants, Zones And Exercise Records

- [ ] 4.1 Add the Scope Grant DocType with act classes, object classes, authority tier, expiry and derivation lineage.
- [ ] 4.2 Implement monotonic narrowing as a pure function: a derivation may never widen classes, tier or expiry.
- [ ] 4.3 Implement revocation through derivation so revoking a parent invalidates every descendant without individual revocation.
- [ ] 4.4 Implement the zone calculator as a pure function returning green / yellow / red / black from scope-registry data, distance measured from the license boundary.
- [ ] 4.5 Implement zone enforcement semantics: soft block with notification on yellow, escalation on red, authority shutdown on black, and refusal rather than annotation in every case.
- [ ] 4.6 Route jurisdiction-registry disclosure and supervision obligations through the zone calculator as conditions on the act.
- [ ] 4.7 Add the Exercise DocType carrying practitioner, act and object classes, presenting key, composition hash, grant reference, both registry versions, computed zone and timestamp.
- [ ] 4.8 Implement the continuity join — act hash present in the license's covered set at the act's timestamp — and its query surface.

## 5. Supervision, Co-Signature And Environment Split

- [ ] 5.1 Cap pre-licensure grants at authority tier `act` and stage orders so they take no effect before co-signature.
- [ ] 5.2 Add the Co-Signature DocType holding one exercise and N signatures, each role-qualified as performer, supervisor, council member or dissenting member.
- [ ] 5.3 Reject a second co-signature record for an exercise that already has one; additional signatures append to the existing record.
- [ ] 5.4 Implement the medical-director / managing-physician co-signature path that makes a staged order effective.
- [ ] 5.5 Implement the environment split: QA runs `act_unsupervised` against synthetic data only under a simulated license with no co-signature requirement.
- [ ] 5.6 Make a simulated license structurally incapable of authorizing a write against non-synthetic data.
- [ ] 5.7 Implement the production flip as a recorded act requiring a real license number bound to a named MedxFactory major release.

## 6. Consent And Transfer Of Care

- [ ] 6.1 Add the one-time revocable AI-treatment consent record on the patient with consenting party, time, scope and state.
- [ ] 6.2 Refuse AI clinical authority for a patient with no active consent.
- [ ] 6.3 Add the Transfer of Care record with opening trigger, named accepting practitioner and completion state.
- [ ] 6.4 On revocation, stop the AI practitioner's authority to initiate new acts while leaving active orders and the treatment plan in force.
- [ ] 6.5 Guarantee exactly one accountable practitioner of record at every moment, and make an unaccepted transfer a visible open state.

## 7. Exercise-Time Enforcement In The Guarded Surface

- [ ] 7.1 Extend `open_chart.api.v1` so a clinical write resolves the acting practitioner and validates its credential binding before touching data, alongside the existing subject/tenant/purpose/role context check.
- [ ] 7.2 Check the scope grant with proof of possession and call the zone calculator inside the same guarded write.
- [ ] 7.3 Write the exercise record as part of the guarded write, and make the controller guards refuse a clinical write that carries no exercise record.
- [ ] 7.4 Keep every decision (narrowing, zone computation, continuity join, consent state) in pure functions the bench-free validator can exercise without a Frappe site.
- [ ] 7.5 Verify the wallet-free path: practitioner modelling, ordering and signing operate with no wallet binding anywhere, under the conventional human gate.

## 8. Catalog Human-Gate Restatement (Documentation)

- [ ] 8.1 Restate aic-036 from `human` to `accountable credentialed practitioner`, keeping the prohibition on ungoverned autonomous action intact.
- [ ] 8.2 Restate aic-034 so an AI practitioner on the care team accesses PHI under treatment purpose rather than as egress to an outside party.
- [ ] 8.3 Restate aic-042's blanket "cannot diagnose, order, treat" so it forbids the ungoverned case without forbidding the credentialed one.
- [ ] 8.4 Restate plt-004 (provider master) and plt-005 (human licenses only) to admit non-human practitioner types and license holders.
- [ ] 8.5 Restate plt-043/044 (e-signature authority and delegation registries), phr-011/013 (credential-bound signing ceremony), ord-030–034 (order signature gates) and doc-023/027 (documentation signature gates) against the new predicate.
- [ ] 8.6 Sweep the remaining autonomous-clinical-action boilerplate entries and record which were restated, which were left unchanged and why.
- [ ] 8.7 Record the MedxFactory cross-repository flag: its wallet brainstorms forbid agent-owned order signing and need the same restatement, which this change cannot make.

## 9. Validation And Evidence

- [ ] 9.1 Add bench-free tests for narrowing, major/minor classification, append-only coverage, zone computation, registry-version reproducibility and the continuity join; keep `make validate` green.
- [ ] 9.2 Add Docker-gated bench tests under `make validate-docker` for migrations, permissions, guarded-surface refusals and the staged-order co-signature path.
- [ ] 9.3 Add negative tests for every refusal in the spec: wallet identifier as subject key, unrecognised holder class, widened derivation, act outside grant, black zone, simulated license against real data, production flip without a real license, act without consent, second co-signature record, service-account clinical write.
- [ ] 9.4 Add the nurse-level versus physician-level scenario proving one calculator returns different zones for the same act at different license levels.
- [ ] 9.5 Publish the QA evidence bundle: synthetic-only fixtures, simulated-license boundary, wallet-free operation, and confirmation that no real license number and no production authority exist in this change.
- [ ] 9.6 Run `openspec validate add-practitioner-identity` and confirm every applyRequires artifact reports done.
