# L03 — Telemetry producers and visibility

**Stage:** original reference design. **Proposed accountable role:** Source-system owners and telemetry engineering.

**Inputs:** Endpoint, network, identity, cloud, SaaS, application, AI and OT events.

**Outputs:** Source contracts and observable coverage.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L03-C01 | Inventory each producer, required event class and accountable owner. | Agent installation is mistaken for collection of required events. | Source-by-event coverage matrix and deliberately missing-source test. |
| L03-C02 | Specify required fields, event time, observation time and uncertainty. | Incomplete identity or time data produces misleading correlations. | Representative records, missing-field handling and time-quality cases. |
| L03-C03 | Define source permissions, collection scope and sensitive-field handling. | Logging grants excessive access or captures secrets and unnecessary content. | Permission review and synthetic secret/privacy handling cases. |
| L03-C04 | Distinguish healthy source, silent source, blocked source and unknown visibility. | No events is interpreted as no threats. | Independent health signal and silence/permission-failure exercise. |
| L03-C05 | Authorize collection changes on production and safety-sensitive systems. | Sensor deployment or active polling disrupts essential operations. | Owner-approved change window and OT-safe collection review. |
| L03-C06 | Protect telemetry ingestion as an attacker-controlled input boundary. | Events trigger parser execution, unsafe rendering or agent instructions. | Malformed/oversized/adversarial records handled without privileged action. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[nist-controls](https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json) · [otel](https://opentelemetry.io/docs/specs/otel/logs/data-model/)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
