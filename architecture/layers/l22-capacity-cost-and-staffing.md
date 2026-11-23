# L22 — Capacity, cost and staffing

**Stage:** original reference design. **Proposed accountable role:** Platform economics and SOC workforce owners.

**Inputs:** EPS, event sizes, retention, workload, staffing and unit-cost assumptions.

**Outputs:** Planning estimates requiring measured validation.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L22-C01 | Model steady ingest, bursts, outages and catch-up margin explicitly. | Average EPS masks backlog growth or no drain headroom. | Input assumptions plus measured workload-specific capacity and failure trials. |
| L22-C02 | Separate raw bytes, index overhead, compression, replicas and tier duration. | Storage estimates double-count or omit required retained copies. | Tier model reconciled with representative measured data. |
| L22-C03 | Account for API/query/egress/model costs and licenses alongside storage. | An affordable ingest estimate hides query or AI operating cost. | Transparent unit assumptions, sensitivity and cost guardrails. |
| L22-C04 | Distinguish staffed-seat coverage from workload-driven capacity. | A 24/7 rota is assumed to absorb unlimited alert volume. | Coverage and handling-time model with utilization and leave assumptions. |
| L22-C05 | Use distributions, burst behavior and censored outcomes before promising response latency. | A mean handling-time estimate is presented as a p95 queue guarantee. | Observed distributions and validated queue/scheduling experiment. |
| L22-C06 | Make trade-offs explicit for sampling, tiers, source selection and outsourcing. | Cost reduction silently removes important evidence or ownership. | Business-owner decision, visibility impact and residual-risk acceptance. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[nist-csf](https://www.nist.gov/cyberframework) · [nist-controls](https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
