# Select an architecture by its constraints

Treat jurisdiction, action authority, safety and offline dependency requirements as hard constraints. Ranking an attractive product does not resolve a hard conflict.

| Question | Architectural consequence | Starting patterns |
|---|---|---|
| Must operations continue without central connectivity? | Local identity/time/keys, durable buffering, update admission and owned local action | P11, P12 |
| Must raw evidence and decisions remain locally accountable? | Separate local custody/authority from permitted central summaries | P09, P10, P17 |
| Does one operator serve unrelated tenants? | Enforce separation below query, cache, case and response interfaces | P08, P07 |
| Is cloud administration or region access a critical dependency? | Explicit provider/identity/region failure modes and regional boundaries | P02, P03, P19 |
| Is data reused across several analytics consumers? | Common lineage/authorization/lifecycle with distinct query semantics | P04, P05 |
| Does automation affect safety or essential service availability? | Domain-owner decisions, bounded actions and process-safe alternatives | P13, P15, P17 |
| Is staffing geographically distributed or limited? | Accepted handover and realistic coverage/workload capacity | P16, P20 |
| Must recovery survive a region failure? | Permitted failure domains, authority reconciliation and full restore scope | P18, P03 |
| Does AI access investigation data or tools? | Permission-first retrieval, untrusted instructions and independent action authority | P14, P15 |

## Decision record

Use the [design brief](../templates/design-brief.md) and [architecture decision](../templates/architecture-decision.md). Record constraints, feasible alternatives, selected pattern composition, reasons, costs, evidence, unresolved risks and responsible acceptance.

Review every layer. Identify joins between selected patterns: schema, identity, custody, freshness, operator authority, export and recovery. The design checker identifies selected record contradictions only; it does not select an optimal architecture or authenticate its declarations.

## Candidate products and documentation findings

| Documented example | Role it informs | What still requires your own evidence |
|---|---|---|
| Amazon Security Lake user guide | Cloud security data organization and source integration | Your permissions, region/support boundaries, actual source delivery, cost and downstream semantics |
| Microsoft workspace architecture documentation | Workspace and data/access boundary decisions | Your tenant/workspace grants, routing, obligations and actual query behavior |
| OCSF | A possible event-schema foundation | Selected version, producers, mappings, field/time semantics and detections |
| OpenTelemetry log data model | Event and observation context | Your collection rights, exported fields, loss, identity and downstream interpretation |
| Sigma specification | Portable detection representation | Your target backend translation, data availability, match behavior and maintenance |

These are research examples, not product endorsements, capability rankings, price recommendations or tested deployments. Links and actual retrieval metadata are in [sources](sources.md).
