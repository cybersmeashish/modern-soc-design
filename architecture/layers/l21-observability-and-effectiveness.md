# L21 — Observability and effectiveness measures

**Stage:** original reference design. **Proposed accountable role:** SRE, detection and SOC service owners.

**Inputs:** Pipeline/source health, cases, decisions and workload measurements.

**Outputs:** Freshness-aware service reporting and operational alerts.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L21-C01 | Measure source completeness, pipeline loss, delay and schema quality separately. | A healthy platform is reported while required sources are absent. | Independent health/coverage signals and deliberately missing-source exercise. |
| L21-C02 | Track current, delayed, missing and unverified evidence states. | A disconnected or failed site appears green centrally. | Freshness thresholds and reports aged beyond each threshold. |
| L21-C03 | Define detection, acknowledgement, investigation and containment timing precisely. | MTTD/MTTR combine incompatible start/end events or ignore censored cases. | Metric dictionary with known origin, uncertainty and excluded/missing events. |
| L21-C04 | Include alert burden, valid-case preservation and known misses in performance review. | Low alert volume is claimed as improved detection quality. | Benign/adversarial evaluation with sample and base-rate limitations. |
| L21-C05 | Protect health and audit signals from the same privileges that run the platform. | An attacker disables monitoring and also suppresses the evidence of failure. | Independent visibility path and privileged-disable investigation. |
| L21-C06 | Tie executive reports to scope, decisions and dated evidence. | Activity and technique totals are mistaken for reduced business risk. | Traceable board scorecard and unresolved-risk/visibility decisions. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[nist-controls](https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json) · [nist-csf](https://www.nist.gov/cyberframework) · [otel](https://opentelemetry.io/docs/specs/otel/logs/data-model/)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
