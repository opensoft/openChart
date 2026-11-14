# Provider Modality Availability — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Lets providers divide working availability between in-person, video, audio, and asynchronous care with explicit conversion rules.
Topics: openchart-feature-catalog, telehealth, frappe, modality-availability
Repository context: openChart — Frappe v15 native EMR; catalog entry TEL-029 (Telehealth Virtual Care And E-Visits)
Captured: 2026-08-24

## Possible feats

- **Modality balance review** — Compare planned and delivered modality mix without changing provider schedules automatically.

## Focus

This feature isolates modality-specific provider supply and guarded substitution, leaving general schedule ownership to scheduling.

## Behavior

- A provider or authorized manager marks time bands as in-person, video, audio, asynchronous review, or approved combinations.
- Each band includes location, eligible services, jurisdiction constraints, concurrency, and conversion policy.
- Slot search returns only modalities compatible with patient need, location, room capacity, and provider authority.
- Converting a reserved slot revalidates all affected constraints and requires patient agreement when the experience changes.
- Asynchronous review capacity is measured in assignments or effort units and cannot be double-counted as synchronous time.
- Exceptions and overrides preserve actor, reason, previous modality, and affected appointments.

## Frappe realization

- **DocTypes:** `OC Provider Modality Availability` and child `OC Allowed Modality` link provider, interval, facility, service, jurisdiction, capacity, and conversion rule.
- **API/hooks:** scheduling reads a permission-filtered availability projection; guarded updates trigger conflict analysis and affected-booking review tasks.
- **Surfaces/permissions:** Calendar overlays and reports serve Provider and Scheduling Manager roles with facility-scoped user permissions.

## Boundaries

Owns: modality constraints on provider availability. Consumes: provider schedule, authority, and service policy. Emits: modality-qualified supply. Does not own: appointment booking or provider credentialing.

## Open questions

- How should asynchronous workload units translate into protected schedule capacity without encouraging unsafe volume?

## Relationships

[Synthesis: Telehealth Virtual Care And E-Visits](openchart-feature-catalog-synthesis-tel.md)
