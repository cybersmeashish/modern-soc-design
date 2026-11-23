# L10 — Analytics, UEBA and model assurance

**Stage:** original reference design. **Proposed accountable role:** Analytics owners and privacy reviewers.

**Inputs:** Scoped behavioral features, labels and evaluation data.

**Outputs:** Risk signals with explanations and uncertainty.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L10-C01 | Define the model task, population, feature rights and decision use. | Profiling expands beyond the approved security purpose. | Use-case/data review and excluded decisions. |
| L10-C02 | Preserve label provenance and prevent adversarial feedback from becoming truth. | Poisoned labels or analyst automation loops corrupt learning. | Label audit, feedback admission and poisoning/failure hypotheses. |
| L10-C03 | Test thresholds with base rates, subgroup behavior and practical alert burden. | High accuracy on an artificial set is presented as useful rare-event detection. | Confusion data, denominators, selection limits and analyst-load estimate. |
| L10-C04 | Track drift, feature availability and confidence decay. | A changed workforce or identity source invalidates the original baseline. | Re-evaluation triggers and degraded/unknown-state handling. |
| L10-C05 | Make explanations traceable to permitted source evidence. | A risk score invents causal attribution or hides unauthorized context. | Source-linked explanation, allowed evidence and alternative interpretations. |
| L10-C06 | Keep statistical risk separate from resource authorization and incident command. | A model score grants access, approves containment or declares an incident. | Independent policy/owner decision and rejected score-only action. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[nist-ai](https://www.nist.gov/itl/ai-risk-management-framework) · [nist-csf](https://www.nist.gov/cyberframework)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
