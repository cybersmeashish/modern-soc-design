# Twenty architecture patterns

Choose and combine patterns according to authority, connectivity, visibility, scale, skills and recovery. This is an archetype catalog, not every vendor or deployment combination.

| Pattern | Architecture | Central trade-off |
|---|---|---|
| P01 | [Centralized on-premises SOC](../architecture/patterns/p01-centralized-on-premises.md) | Local control brings platform, storage, skills, update and recovery obligations. |
| P02 | [Cloud-native SOC](../architecture/patterns/p02-cloud-native-soc.md) | Managed operations add region, API, identity, billing and supplier dependencies. |
| P03 | [Hybrid and multi-cloud SOC](../architecture/patterns/p03-hybrid-multi-cloud.md) | Coordination simplifies while identity, egress, queries and time semantics remain heterogeneous. |
| P04 | [Security data lakehouse](../architecture/patterns/p04-security-data-lakehouse.md) | Flexible analytics adds catalog, authorization, cost and lifecycle complexity. |
| P05 | [Composable SOC platform](../architecture/patterns/p05-composable-platform.md) | Flexibility requires integration, patch, support and recovery ownership. |
| P06 | [XDR-led SOC](../architecture/patterns/p06-xdr-led-soc.md) | Quick integration can coexist with proprietary logic and raw-evidence limits. |
| P07 | [MDR and shared-responsibility SOC](../architecture/patterns/p07-mdr-and-shared-responsibility.md) | Coverage and skills add access, contract, handover and supplier concentration obligations. |
| P08 | [MSSP multi-tenant SOC](../architecture/patterns/p08-mssp-multi-tenant.md) | Shared efficiency increases isolation, admin and noisy-neighbor risks. |
| P09 | [Federated national and regional SOC](../architecture/patterns/p09-federated-national-and-regional.md) | Distributed authority makes common policy, stale evidence and joint command explicit concerns. |
| P10 | [Sovereign connected SOC](../architecture/patterns/p10-sovereign-connected-soc.md) | Connectivity must not obscure external authority and disclosure obligations. |
| P11 | [Strictly disconnected SOC](../architecture/patterns/p11-strictly-disconnected-soc.md) | Local autonomy brings local lifecycle, intelligence age, admission, staffing and recovery burdens. |
| P12 | [Intermittent edge and remote-site SOC](../architecture/patterns/p12-intermittent-edge-and-remote-sites.md) | Continuity depends on outage assumptions, local authority and safe reconciliation. |
| P13 | [OT and industrial SOC](../architecture/patterns/p13-ot-and-industrial-soc.md) | Better visibility must respect safety, availability, protocol limits and engineering authority. |
| P14 | [AI-assisted human-led SOC](../architecture/patterns/p14-ai-assisted-human-led-soc.md) | Assistance adds instruction, retrieval, provider, model-update and confidence risks. |
| P15 | [Bounded closed-loop automation](../architecture/patterns/p15-bounded-closed-loop-automation.md) | Speed increases the cost of policy mistakes, stale inputs, duplicated execution and partial failures. |
| P16 | [Follow-the-sun global SOC](../architecture/patterns/p16-follow-the-sun-global.md) | Coverage depends on lawful access, staffing, fatigue, context continuity and actual acknowledgement. |
| P17 | [Regulated and high-assurance SOC](../architecture/patterns/p17-regulated-high-assurance.md) | Higher assurance increases evidence, operational separation and change-management effort. |
| P18 | [Multi-region recovery SOC](../architecture/patterns/p18-multi-region-recovery.md) | Availability can conflict with placement, authority, replication cost and consistent action state. |
| P19 | [Serverless and elastic SOC](../architecture/patterns/p19-serverless-elastic.md) | Elasticity remains constrained by quotas, cold starts, API rates, state and cost. |
| P20 | [Small-team and resource-constrained SOC](../architecture/patterns/p20-small-team-resource-constrained.md) | Focus and outsourcing can help but do not create unstaffed coverage or universal detection. |

The patterns add 80 pattern-specific constraint records to the layer catalog. They are reference topologies, not deployed SOCs.

[Selection method](architecture-selection.md) · [Machine-readable patterns](../catalog/patterns.json).
