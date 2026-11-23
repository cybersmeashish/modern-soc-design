# L09 — Detection engineering and content lifecycle

**Stage:** original reference design. **Proposed accountable role:** Detection engineering and domain owners.

**Inputs:** Threat hypotheses, telemetry contracts and backend semantics.

**Outputs:** Versioned rules, evaluation evidence and known gaps.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L09-C01 | Define each detection as a falsifiable hypothesis with required data and expected behavior. | A technique label is mistaken for operational coverage. | Required source/field list, positive cases and limitations. |
| L09-C02 | Keep content, dependencies, schemas and backend versions under reviewable change control. | A parser or rule update silently changes protection. | Versioned change, reviewer, regression results and rollback artifact. |
| L09-C03 | Test benign cases, missing data, time boundaries and duplicates alongside attack cases. | A detector fires only on its authored example or floods analysts. | Held-out/benign cases, missed cases and correctly scoped rates. |
| L09-C04 | Translate and verify Sigma or other portable logic on the actual target backend. | A portable syntax file is assumed to have identical query semantics. | Backend-specific output and expected match/no-match evidence. |
| L09-C05 | Measure rule ownership, health, drift and retirement conditions. | Broken, stale or duplicate detections remain enabled without accountability. | Detection health report and owner-approved tuning/deprecation. |
| L09-C06 | Separate rule promotion from changing response authority. | A signed rule bundle indirectly authorizes destructive tool actions. | Independent response policy review and denied authority-expansion case. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[sigma](https://raw.githubusercontent.com/SigmaHQ/sigma-specification/main/README.md) · [mitre-attack](https://attack.mitre.org/resources/working-with-attack/) · [nist-controls](https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
