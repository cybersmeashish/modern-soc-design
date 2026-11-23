# The 24-layer architecture review

The layers separate decisions and ownership; they are not necessarily 24 products or physical services. Combine implementations while retaining explicit trust and evidence boundaries.

| Layer | Review chapter | Proposed accountable role |
|---|---|---|
| L01 | [Mission and operating model](../architecture/layers/l01-mission-and-operating-model.md) | Executive sponsor and SOC service owner |
| L02 | [Asset, identity and business context](../architecture/layers/l02-asset-and-risk-context.md) | Asset owners and security architecture |
| L03 | [Telemetry producers and visibility](../architecture/layers/l03-telemetry-producers.md) | Source-system owners and telemetry engineering |
| L04 | [Edge collection and buffering](../architecture/layers/l04-edge-collection-and-buffering.md) | Telemetry engineering and site operator |
| L05 | [Ingestion and streaming](../architecture/layers/l05-ingestion-and-streaming.md) | Platform and telemetry engineering |
| L06 | [Schema, time and lineage](../architecture/layers/l06-schema-time-and-lineage.md) | Data engineering and detection engineering |
| L07 | [Security data platform and retention](../architecture/layers/l07-data-platform-and-retention.md) | Data platform, privacy and evidence owners |
| L08 | [Context and threat intelligence](../architecture/layers/l08-context-and-threat-intelligence.md) | Threat intelligence and context owners |
| L09 | [Detection engineering and content lifecycle](../architecture/layers/l09-detection-engineering.md) | Detection engineering and domain owners |
| L10 | [Analytics, UEBA and model assurance](../architecture/layers/l10-analytics-and-ueba.md) | Analytics owners and privacy reviewers |
| L11 | [Alert triage and analyst experience](../architecture/layers/l11-alert-triage-and-analyst-experience.md) | SOC operations and case owners |
| L12 | [Investigation, forensics and case evidence](../architecture/layers/l12-investigation-forensics-and-cases.md) | Incident investigators and evidence custodians |
| L13 | [Response orchestration and action governance](../architecture/layers/l13-response-orchestration.md) | Response service owners and business process owners |
| L14 | [AI copilots and bounded agents](../architecture/layers/l14-ai-copilots-and-agents.md) | AI platform, SOC and action-authority owners |
| L15 | [Threat hunting and adversary validation](../architecture/layers/l15-hunting-and-adversary-validation.md) | Hunt lead, detection engineering and system owners |
| L16 | [Incident command and business recovery](../architecture/layers/l16-incident-command-and-recovery.md) | Incident commander, service owners and legal/privacy advisers |
| L17 | [SOC identity and privileged access](../architecture/layers/l17-soc-identity-and-privileged-access.md) | IAM, platform and evidence owners |
| L18 | [Platform security, supply chain and change](../architecture/layers/l18-platform-security-and-change.md) | Platform engineering and release owners |
| L19 | [Resilience and disaster recovery](../architecture/layers/l19-resilience-and-disaster-recovery.md) | SRE, platform and recovery owners |
| L20 | [Privacy, sovereignty and governance](../architecture/layers/l20-privacy-sovereignty-and-governance.md) | Risk, privacy, jurisdiction and key owners |
| L21 | [Observability and effectiveness measures](../architecture/layers/l21-observability-and-effectiveness.md) | SRE, detection and SOC service owners |
| L22 | [Capacity, cost and staffing](../architecture/layers/l22-capacity-cost-and-staffing.md) | Platform economics and SOC workforce owners |
| L23 | [Interoperability, integration and migration](../architecture/layers/l23-interoperability-and-migration.md) | Integration owners and security architecture |
| L24 | [Assurance and acceptance evidence](../architecture/layers/l24-assurance-and-acceptance.md) | Control owners and independent reviewers |

There are 144 layer constraint records. Proposed roles and acceptance cases require actual owner agreement and environment-specific evidence.

[Pattern choices](pattern-index.md) · [Machine-readable layer catalog](../catalog/layers.json).
