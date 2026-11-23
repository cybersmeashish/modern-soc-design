# L07 — Security data platform and retention

**Stage:** original reference design. **Proposed accountable role:** Data platform, privacy and evidence owners.

**Inputs:** Raw/normalized events, cases, classification and retention decisions.

**Outputs:** Queryable authorized evidence and managed lifecycle.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L07-C01 | Separate raw, normalized, indexed, aggregate and case-evidence retention. | One retention setting hides duplicated storage or deletes necessary evidence. | Tier-specific inventory and lifecycle policy with business owners. |
| L07-C02 | Enforce tenant, purpose, field and region authorization through every query/export path. | An analyst UI filter is bypassed by a lower-level query engine. | Storage/API/export negative cases and authorized controls. |
| L07-C03 | Model index, replication, compression, cardinality and query concurrency separately. | Raw ingest arithmetic is mistaken for SIEM capacity. | Declared assumptions followed by real workload-specific measurements. |
| L07-C04 | Control legal holds, deletion, backups and derived copies explicitly. | A deletion or hold applies only to the primary index. | Lifecycle dependency map and approved hold/deletion exercises. |
| L07-C05 | Design key ownership, rotation and restoration for each evidence tier. | Key loss makes archived evidence unusable or admins can decrypt all tenants. | Custody map, separation-of-duty checks and authorized restore evidence. |
| L07-C06 | Preserve portability and the meaning of exported evidence. | Vendor exit produces unqueryable data or loses identities and timestamps. | Schema/version manifest and import/re-query validation on an alternative path. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[nist-controls](https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json) · [aws-lake](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
