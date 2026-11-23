# L14 — AI copilots and bounded agents

**Stage:** original reference design. **Proposed accountable role:** AI platform, SOC and action-authority owners.

**Inputs:** Untrusted events, scoped retrieval, models and tool proposals.

**Outputs:** Evidence-linked assistance subject to independent decisions.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L14-C01 | Treat logs, retrieved documents, prompts and tool descriptions as untrusted instructions. | Attacker-authored evidence redirects the assistant or adds authority. | Direct/indirect instruction cases and independently enforced tool policy. |
| L14-C02 | Apply subject/tenant/field authorization before retrieval enters model context. | Post-generation redaction is used to compensate for unauthorized retrieval. | Mixed-tenant/document cases and permitted-context controls. |
| L14-C03 | Register model/provider placement, retention, data use and offline dependencies. | Sensitive evidence exits to an unapproved model service. | Provider/data-boundary review and allowed/denied egress tests. |
| L14-C04 | Require evidence-linked outputs and preserve uncertainty and human decision ownership. | Confident generated text invents facts, chronology or approval. | Unsupported-claim cases, citations and clear proposed/accepted decision states. |
| L14-C05 | Bound loops, delegation, costs, concurrency and fallback behavior. | Agent failures cause uncontrolled spending, latency or cascading actions. | Budget/step/timeout tests and explicitly safe fallback. |
| L14-C06 | Admit model, retrieval and policy updates through controlled evaluation and rollback. | An approved assistant changes behavior after an unreviewed update. | Versioned admission, adversarial/benign cases and change-triggered re-evaluation. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[nist-ai](https://www.nist.gov/itl/ai-risk-management-framework) · [nist-zero-trust](https://csrc.nist.gov/pubs/sp/800/207/final)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
