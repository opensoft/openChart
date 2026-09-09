# Location Holiday Calendars — Brainstorm

Status: brainstorm
Kind: architecture
Summary: Publishes effective holiday and closure calendars by location with inheritance, exceptions, and downstream change signals.
Topics: openchart-feature-catalog, platform, frappe, holiday-calendars
Repository context: openChart — Frappe v15 native EMR; catalog entry PLT-041 (Platform Administration Configuration And Workflow Engine)
Captured: 2026-08-24

## Possible feats

- **Closure impact preview** — List future schedules, jobs, deadlines, and routing windows affected by a proposed date.

## Focus

This feature isolates location-specific non-working dates as reusable configuration rather than embedding them in each workflow.

## Behavior

- Facility administrators define named calendars with dates, partial-day windows, closure type, locale, and effective year.
- Locations inherit a site default and may add or override dates with an explicit reason.
- Publication detects duplicate intervals, impossible local times, and changes affecting active future commitments.
- Calendars move through Draft, Review, Published, Retired, and Superseded states.
- Consumers request working-time answers with location and timestamp and receive the calendar version used.
- Emergency closures append a high-priority exception and emit change events; they do not autonomously cancel appointments or deadlines.

## Frappe realization

- **DocTypes:** native Holiday List is wrapped by `OC Location Calendar Release`; child rows store date, time window, type, source, and override reason.
- **Permissions:** Facility Administrator authors local calendars; Operations Approver publishes; consumers have read-only access.
- **API/hooks:** `open_chart.api.v1.platform.is_working_time` resolves inheritance; publication emits realtime and background reconciliation events.
- **Surface:** Calendar view and impact Script Report show closures and dependent future records.

## Boundaries

Owns: published location working-day exceptions and version resolution. Consumes: location, locale, and operating policy. Emits: working-time decisions and closure events. Does not own: appointment cancellation, payroll, or staffing.

## Open questions

- How should overnight operations represent partial closures spanning local midnight?

## Relationships

[Synthesis: Platform Administration And Workflow Engine](openchart-feature-catalog-synthesis-plt.md) · [Facility And Location Master Registry](openchart-feature-catalog-plt-003-facility-and-location-master-registry.md) · [Operational Queue SLA Timers](openchart-feature-catalog-plt-046-operational-queue-sla-timers.md)
