# L13 — Response orchestration and action governance

**Stage:** original reference design. **Proposed accountable role:** Response service owners and business process owners.

**Inputs:** Action proposals, independent identity, policy and approvals.

**Outputs:** Bounded attributable actions and observed side effects.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L13-C01 | Authorize subject, service, action, object, tenant and purpose independently of alert/model text. | A tool proposal or influential alert becomes execution authority. | Explicit action matrix and forged-context/foreign-resource denials. |
| L13-C02 | Bind high-impact approval to exact action, resource, scope and expiry. | An approval is reused for another account or a later incident. | Different-action/resource, expired and replayed approval cases. |
| L13-C03 | Specify idempotency, partial effects, retry limits and compensation boundaries. | Retries duplicate containment or imply rollback of irreversible actions. | Interrupted/repeated/partial-success observations and escalation paths. |
| L13-C04 | Apply per-tenant action budgets, rate limits and maximum blast radius. | One bad rule or compromised agent performs fleet-wide disruption. | Batch/rate/resource-limit cases and independent stop control. |
| L13-C05 | Authenticate callbacks and verify the resulting system state. | A forged success callback is counted as containment. | Authenticated receipt plus independently observed permitted state change. |
| L13-C06 | Define emergency and degraded authority without fail-open elevation. | Identity/provider outage grants unrestricted local response privileges. | Scoped emergency grants, expiry, accountability and denied escalation. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[nist-zero-trust](https://csrc.nist.gov/pubs/sp/800/207/final) · [nist-ir](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [nist-controls](https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
