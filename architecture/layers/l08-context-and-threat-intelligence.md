# L08 — Context and threat intelligence

**Stage:** original reference design. **Proposed accountable role:** Threat intelligence and context owners.

**Inputs:** Indicators, business context, identities and supplier intelligence.

**Outputs:** Bounded contextual joins with confidence and provenance.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L08-C01 | Record intelligence provenance, confidence, expiry and allowed use. | A stale or untrusted indicator becomes an automatic blocking rule. | Source/expiry review and low-confidence or expired-indicator cases. |
| L08-C02 | Respect sharing markings, licensing, recipients and disclosure purpose. | Intelligence or customer evidence is redistributed outside permitted scope. | Recipient/purpose controls and denied-disclosure cases. |
| L08-C03 | Resolve entities with tenant/time boundaries and conflict handling. | Shared infrastructure or reused identifiers create false attribution. | Ambiguous joins preserved as unknown, with reviewer evidence. |
| L08-C04 | Distinguish observations, analytic inference and actor attribution. | A technique or indicator match is presented as proof of who attacked. | Claim-by-claim source trail and alternative explanations. |
| L08-C05 | Protect enrichment services from arbitrary URLs and resource exhaustion. | Attacker-supplied indicators trigger SSRF, egress or lookup storms. | Allowed destinations, bounded lookups and failure behavior. |
| L08-C06 | Retain historical context needed to reproduce a decision. | Later context updates rewrite the reason for an earlier alert. | Versioned enrichment snapshot and reproducible case reasoning. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[mitre-attack](https://attack.mitre.org/resources/working-with-attack/) · [first-tlp](https://www.first.org/tlp/) · [nist-csf](https://www.nist.gov/cyberframework)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
