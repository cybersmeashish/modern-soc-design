# L05 — Ingestion and streaming

**Stage:** original reference design. **Proposed accountable role:** Platform and telemetry engineering.

**Inputs:** Authenticated batches, event streams and source metadata.

**Outputs:** Durable queues, quarantine and delivery accounting.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L05-C01 | Specify acknowledgement, durability and end-to-end delivery semantics. | Broker acknowledgement is presented as durable searchable evidence. | Crash/replay tests across acknowledgement and downstream checkpoint boundaries. |
| L05-C02 | Choose partition keys and make ordering scope explicit. | Cross-partition or cross-source records are given a false total order. | Tenant/resource partition review and out-of-order event cases. |
| L05-C03 | Apply quotas, backpressure and priority with explicit loss policies. | Bursts overload the platform or silently discard critical sources. | Burst/backlog exercise, priority decisions and loss accounting. |
| L05-C04 | Quarantine malformed, unauthorized or incompatible records. | Bad events poison processing or vanish without trace. | Dead-letter reason, protected raw sample and reprocessing workflow. |
| L05-C05 | Isolate tenants and regions in queues, credentials and routing. | Routing mistakes mix customers or violate placement constraints. | Cross-tenant/region negative cases at ingestion and storage. |
| L05-C06 | Authenticate callbacks and constrain retry loops and billing exposure. | Forged callbacks or infinite retries create work, cost or duplicate actions. | Callback authenticity tests, finite retries and cost/queue alerts. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[otel](https://opentelemetry.io/docs/specs/otel/logs/data-model/) · [nist-controls](https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
