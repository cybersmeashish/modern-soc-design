# L04 — Edge collection and buffering

**Stage:** original reference design. **Proposed accountable role:** Telemetry engineering and site operator.

**Inputs:** Source events, connectivity state and local policies.

**Outputs:** Bounded durable buffers and attributable forwarding.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L04-C01 | Define buffer durability, capacity, priority and maximum outage assumptions. | An apparently resilient collector loses events on restart or disk exhaustion. | Restart, full-buffer and outage-duration observations. |
| L04-C02 | Declare duplicate/replay behavior and stable event identifiers. | Reconnect duplicates inflate alerts or repeat response actions. | Replay/dedup cases with preserved evidence lineage. |
| L04-C03 | Keep local identity, configuration, time and licensing dependencies visible. | A disconnected collector cannot authenticate, timestamp or operate. | Dependency inventory and local-operation failure exercise. |
| L04-C04 | Encrypt buffered data and separate key custody from routine operations. | Lost edge devices expose evidence or make recovery impossible. | Key/owner map, authorized recovery and denied-read checks. |
| L04-C05 | Control offline updates and imports with independent verification inputs. | A compromised or stale bundle becomes an authorized configuration. | Signer/digest/target/version checks and failed-admission cases. |
| L04-C06 | Expose backlog, dropped records, clock uncertainty and resynchronization status. | Central reporting silently treats an isolated site as current. | Local health report and freshness-aware central evidence view. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[nist-controls](https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json) · [otel](https://opentelemetry.io/docs/specs/otel/logs/data-model/)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
