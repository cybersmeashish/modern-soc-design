# L19 — Resilience and disaster recovery

**Stage:** original reference design. **Proposed accountable role:** SRE, platform and recovery owners.

**Inputs:** Failure domains, business objectives and dependency inventory.

**Outputs:** Defined degraded modes and measured restoration.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L19-C01 | Choose failure domains, quorum and placement within sovereignty constraints. | Redundant nodes share a dependency or replicate outside approved jurisdiction. | Dependency/failure-domain map and permitted placement review. |
| L19-C02 | Specify behavior during partition, source loss, queue loss and query outage. | Response continues on stale evidence or reporting silently implies normal service. | Partition/degraded-mode exercises and freshness-aware decisions. |
| L19-C03 | Treat replicated data, backups and immutable evidence as different protections. | Replication copies deletion/corruption and is called a recoverable backup. | Independent backup, deletion/corruption and clean-target restoration checks. |
| L19-C04 | Include identities, keys, policies, licenses and pending actions in recovery scope. | Recovered data is inaccessible or stale approvals re-enable response. | Full dependency checklist, authority-state restore and replay review. |
| L19-C05 | Set RPO/RTO per service and measure actual restoration and data loss. | Design targets become reported recovery achievements. | Timestamped scoped restore trials, missing records and unsuccessful attempts. |
| L19-C06 | Reconcile regional failback, duplicates and decision ownership. | Split-brain actors repeat actions or overwrite incident evidence. | Failover/failback cases with deduplication and authority reconciliation. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[nist-controls](https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json) · [nist-ir](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
