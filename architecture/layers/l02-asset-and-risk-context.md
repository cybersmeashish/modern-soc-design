# L02 — Asset, identity and business context

**Stage:** original reference design. **Proposed accountable role:** Asset owners and security architecture.

**Inputs:** Asset inventory, service dependencies, identity directories.

**Outputs:** Versioned criticality and authority context.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L02-C01 | Define the inventory boundary, exclusions and discovery sources. | Unknown assets disappear from the coverage denominator. | Inventory reconciliation with explicit unidentified and excluded records. |
| L02-C02 | Use tenant/provider-qualified immutable identifiers and historical validity. | Reused IP addresses or names merge unrelated systems. | Collision, reassignment and historical-lookup cases. |
| L02-C03 | Record criticality, data class, action owner and recovery dependencies. | Response choices ignore service impact or regulated information. | Business-owner review of critical paths and proposed actions. |
| L02-C04 | Preserve provenance, confidence and expiry for context joins. | Stale CMDB or graph context is treated as current truth. | Freshness thresholds, conflicting-source cases and unresolved joins. |
| L02-C05 | Connect human, workload and delegated identities without expanding authority. | A powerful service identity masks an unauthorized originating subject. | Subject/service/action/resource decision matrix and denied cases. |
| L02-C06 | Review changes to tools, assets, suppliers and destinations. | An integration silently creates a new data exit or response target. | Change event linked to ownership and boundary acceptance. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[nist-csf](https://www.nist.gov/cyberframework) · [nist-zero-trust](https://csrc.nist.gov/pubs/sp/800/207/final)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
