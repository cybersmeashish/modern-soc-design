# Proposed failure and acceptance experiments

These are **environment experiments to perform**, not executed outcomes in this repository. The executed planning/record checks are in [evidence](../evidence/README.md).

| Injection or condition | Observation required | Unsafe failure to identify |
|---|---|---|
| Source permission removed | Missing-source state and accepted ownership | Quiet queue reported as healthy |
| Sensor alive, required events absent | Independent completeness/coverage warning | Heartbeat mistaken for event delivery |
| Oversized/malformed record | Bounded parser and quarantined reason | Process execution, resource exhaustion or silent disappearance |
| Queue/disk exhausted | Documented backpressure, priority and loss | Unaccounted critical evidence loss |
| Collector restart | Durable data and explicit duplicates/gaps | Unreported buffer loss |
| Site connectivity removed | Local operation, bounded action and central freshness | Unrestricted emergency authority or stale green status |
| Identity/DNS/time/licensing unavailable | Stated degraded mode with dependency ownership | Hidden cloud dependency prevents local operation |
| Clock skew and invalid time | Uncertainty and qualified ordering | Fabricated incident chronology |
| Cross-tenant query/cache/export | Denial below the UI and valid tenant access preserved | Label-only isolation |
| Stale context or revoked action grant | Independent current authorization or safe denial | Old approval reused for a new resource |
| Forged approval/success callback | Rejection and independently observed outcome | Log/model text or receipt treated as authority |
| Interrupted/repeated response | Idempotency, partial effects and owned escalation | Duplicate or falsely reported containment |
| Prompt/indirect instruction injection | Scoped retrieval and independent tool decisions | Untrusted evidence grants a privileged action |
| Wrong-signer/target/update replay | Quarantine with independent trusted inputs | Signed-but-unapproved content promoted |
| Lost key/clean restore | Measured config/data/identity/key/authority scope and loss | Database-only restore called full recovery |
| Region partition/failback | Permitted local ownership and reconciliation | Split-brain repeated actions or overwritten evidence |
| Supplier unavailable or exit | Accessible retained evidence and alternative roles | Both visibility and investigation disappear |
| Workload/query/model burst | Bounded cost, queue age and effective degradation | Infinite retry or financially unbounded execution |

Define permitted targets and safety limits before testing. OT/clinical/essential-service changes require the responsible process owners. Preserve actual failures and unknowns; do not fill missing measurements with expected successes.
