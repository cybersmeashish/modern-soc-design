"""Build original architecture chapters from the maintained catalogs. Run inside OrbStack."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
layers=json.loads((ROOT/'catalog/layers.json').read_text())['layers']
patterns=json.loads((ROOT/'catalog/patterns.json').read_text())['patterns']
sources={s['id']:s for s in json.loads((ROOT/'catalog/source-register.json').read_text())}

def write(path,text):
 p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.rstrip()+'\n')
def layerpath(l):return f"architecture/layers/{l['id'].lower()}-{l['slug']}.md"
def patternpath(p):return f"architecture/patterns/{p['id'].lower()}-{p['slug']}.md"
def cells(value):return value.replace('|','\\|').replace('\n',' ')
for l in layers:
 rows='\n'.join(f"| {c['id']} | {cells(c['decision'])} | {cells(c['failure_mode'])} | {cells(c['acceptance_evidence'])} |" for c in l['constraints'])
 refs=' · '.join(f"[{sid}]({sources[sid]['url']})" for sid in l['source_ids'])
 write(layerpath(l),f"""# {l['id']} — {l['title']}

**Stage:** original reference design. **Proposed accountable role:** {l['proposed_owner']}.

**Inputs:** {l['inputs']}.

**Outputs:** {l['outputs']}.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
{rows}

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

{refs}

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
""")
for p in patterns:
 rows='\n'.join(f"| {c['id']} | {cells(c['decision'])} | {cells(c['failure_mode'])} | {cells(c['acceptance_evidence'])} |" for c in p['constraints'])
 priority=' · '.join(f"[{lid}](../layers/{next(l['id'].lower()+'-'+l['slug']+'.md' for l in layers if l['id']==lid)})" for lid in p['priority_layers'])
 write(patternpath(p),f"""# {p['id']} — {p['title']}

**Stage:** {p['stage']}.

## When to consider it

{p['fit']}

## Logical arrangement

{p['topology']}

```mermaid
{p['mermaid']}
```

Arrows identify intended relationships. They are not packet observations, provider deployment evidence or proof of isolation.

## Trade-off

{p['tradeoff']}

## Pattern-specific design constraints

| ID | Decision to make | Failure to avoid | Acceptance evidence |
|---|---|---|---|
{rows}

## Priority layer reviews

{priority}

All 24 layers remain in the review scope. These links highlight decisions that change most for this pattern; they do not exempt other controls.

## Environment-specific gate

Before implementation, agree the business scope, approved sources, authority boundaries, data/administrator/key/support/recovery placement, critical dependencies and response rights. Verify actual source delivery, permission boundaries, failure behavior, cost/capacity and restoration in the intended environment. Mixed patterns need an interface and responsibility review at every joining boundary.

[Pattern catalog](../../docs/pattern-index.md) · [Selection method](../../docs/architecture-selection.md) · [Acceptance record](../../templates/acceptance-record.md).
""")
layer_rows='\n'.join(f"| {l['id']} | [{l['title']}](../{layerpath(l)}) | {l['proposed_owner']} |" for l in layers)
write('docs/layer-index.md',f"""# The 24-layer architecture review

The layers separate decisions and ownership; they are not necessarily 24 products or physical services. Combine implementations while retaining explicit trust and evidence boundaries.

| Layer | Review chapter | Proposed accountable role |
|---|---|---|
{layer_rows}

There are {sum(len(l['constraints']) for l in layers)} layer constraint records. Proposed roles and acceptance cases require actual owner agreement and environment-specific evidence.

[Pattern choices](pattern-index.md) · [Machine-readable layer catalog](../catalog/layers.json).
""")
pattern_rows='\n'.join(f"| {p['id']} | [{p['title']}](../{patternpath(p)}) | {cells(p['tradeoff'])} |" for p in patterns)
write('docs/pattern-index.md',f"""# Twenty architecture patterns

Choose and combine patterns according to authority, connectivity, visibility, scale, skills and recovery. This is an archetype catalog, not every vendor or deployment combination.

| Pattern | Architecture | Central trade-off |
|---|---|---|
{pattern_rows}

The patterns add {sum(len(p['constraints']) for p in patterns)} pattern-specific constraint records to the layer catalog. They are reference topologies, not deployed SOCs.

[Selection method](architecture-selection.md) · [Machine-readable patterns](../catalog/patterns.json).
""")
constraint_rows=[]
for group,records in [('layer',layers),('pattern',patterns)]:
 for record in records:
  for c in record['constraints']:constraint_rows.append({'id':c['id'],'scope':group,'parent':record['id'],**{k:c[k] for k in ('decision','failure_mode','acceptance_evidence')}})
write('catalog/constraint-register.json',json.dumps({'reviewed_on':'2026-11-23','stage':'reference design decisions and proposed acceptance evidence','records':constraint_rows},indent=2))
source_rows='\n'.join(f"| {s['id']} | [{cells(s.get('title',s['id']))}]({s['url']}) | {s['retrieved_at']} |" for s in sources.values() if s['status']==200)
write('docs/sources.md',f"""# Primary-source register

Reviewed 23 November 2026. Source content was retrieved in the OrbStack workspace; raw third-party pages are not redistributed. Links, retrieval metadata and byte digests are in [the source register](../catalog/source-register.json).

| ID | Primary source | Retrieved UTC |
|---|---|---|
{source_rows}

Selected NIST SP 800-53 catalog records were read from the official OSCAL source, version **5.2.0**. [Selected records](../catalog/selected-controls.json) record the actual IDs and titles used for the assessment aid.

The MITRE SOC-book page returned 403 and the Australian logging page timed out in this retrieval. They remain explicitly unavailable entries in the register and are not used to support specific statements. The accessible MITRE ATT&CK, NIST audit controls and other retrieved sources provide the stated research foundations.

## Original contribution and source boundary

The layer decomposition, pattern diagrams, constraint register, proposed ownership, acceptance examples, decision method, templates and planning code are original reference work by Ashish Srivastava. Source frameworks do not prescribe this exact architecture. Provider documents are documentation findings; no cloud service was deployed or benchmarked here.

A standards citation, technique map, record checker or numerical model is not a certification, legal determination or independent assessment.
""")
write('README.md',f"""# Modern SOC Design

**Architecture decisions for security operations that must remain observable, accountable and recoverable.**

By [Ashish Srivastava](https://github.com/cybersmeashish) · vCISO advisory, security transformation and AI assurance.

A maintained reference connecting business mission, telemetry, security data, detection, investigation, AI, human decisions, response, sovereignty and recovery. It covers **24 layers**, **20 architecture patterns** and **224 structured constraint records**: 144 layer decisions and 80 pattern-specific decisions.

**Stage:** architecture reference with locally checked planning/record-consistency tools. The diagrams are intended topologies; they do not assert a deployed SOC, tested provider capacity, compliance certification or client adoption.

## Start with the decision you need

| Reader or question | Start here |
|---|---|
| CEO/CISO: what should we fund and who owns the outcome? | [Executive decision brief](docs/executive-brief.md) |
| Architect: how do all layers connect? | [System planes](architecture/system-planes.md) and [24-layer catalog](docs/layer-index.md) |
| Which deployment fits our authority/connectivity constraints? | [20 patterns](docs/pattern-index.md) and [selection method](docs/architecture-selection.md) |
| Engineer: what might fail and how should we test it? | [Constraint register](catalog/constraint-register.json), [failure catalog](docs/failure-catalog.md), [acceptance record](templates/acceptance-record.md) |
| Is AI allowed to act? | [AI layer](architecture/layers/l14-ai-copilots-and-agents.md) and [action authority](architecture/layers/l13-response-orchestration.md) |
| How much storage, queue headroom and staffing might we need? | [Planning method](docs/planning-models.md) and [synthetic inputs](examples/planning/capacity.json) |
| What is actually tested? | [Execution evidence](evidence/README.md) and [evidence stages](docs/evidence-and-acceptance.md) |

## Logical flow

```mermaid
flowchart LR
 S[Scoped telemetry sources] --> C[Collection and buffering] --> I[Durable ingest and quarantine]
 I --> D[Governed evidence and normalized data] --> A[Detections and analytics]
 A --> K[Analyst investigation and cases] --> P[Action proposal]
 P --> G[Independent identity policy and approval] --> T[Registered targets]
 H[Coverage and freshness] -.-> K
 X[Verified subject service and grants] -.-> G
```

Detection and AI output may propose an action. Independent authority must determine the subject, service, object, tenant, purpose, approval and limits before execution. Privacy, identity, platform security, governance, capacity and recovery apply across the flow.

## Deployment breadth

On-premises · cloud-native · hybrid/multi-cloud · lakehouse · composable · XDR-led · MDR · MSSP · federated national/regional · sovereign connected · strictly disconnected · intermittent edge · OT/industrial · AI-assisted · bounded automation · follow-the-sun · regulated assurance · multi-region recovery · serverless · small-team.

These archetypes can be combined. The repository does not claim to enumerate every vendor combination or every organization-specific constraint.

## Reuse the design method

1. Define the service, business harm, coverage commitment and accountable decision owners.
2. Select/combine patterns and review all layers, including excluded visibility and critical dependencies.
3. Record trusted/untrusted inputs, data/authority/evidence exits and permitted response actions.
4. Set acceptance evidence for legitimate, denied, degraded and recovery cases.
5. Measure the intended environment, retain failures/unknowns and obtain responsible-owner acceptance.

[Design brief](templates/design-brief.md) · [Decision record](templates/architecture-decision.md) · [Source contract](templates/telemetry-contract.md) · [Control/evidence crosswalk](docs/control-to-evidence.md) · [Industry adaptation](docs/industry-adaptations.md).

## Local tools and evidence

The standard-library tools estimate capacity/staffing and identify contradictions in synthetic design records. They do not implement telemetry collection, SIEM search, detection engines, production authorization or response tools.

Run development and validation in the repository-specific OrbStack workspace described in [AGENTS.md](AGENTS.md) and [the development guide](docs/development.md). The checked source snapshot and actual results are linked from [evidence](evidence/README.md).

## Connected portfolio

[AI in security](https://github.com/cybersmeashish/ai-in-security) · [Enterprise AI Gateway](https://github.com/cybersmeashish/enterprise-ai-security-architectures) · [Sovereign and disconnected cloud](https://github.com/cybersmeashish/sovereign-disconnected-cloud-security) · [Sovereign AI](https://github.com/cybersmeashish/sovereign-AI) · [Government](https://github.com/cybersmeashish/government-security) · [BFSI](https://github.com/cybersmeashish/bfsi-security) · [Oil & Gas](https://github.com/cybersmeashish/oil-gas-security) · [Connected research](https://github.com/cybersmeashish/Ashish-research).

[Crypto transition](docs/crypto-transition.md) · [Glossary](docs/glossary.md) · [Primary sources](docs/sources.md) · [Contribution method](CONTRIBUTING.md) · [Research roadmap](ROADMAP.md) · [Security reporting](SECURITY.md).
""")
print(json.dumps({'layers':len(layers),'patterns':len(patterns),'constraint_records':len(constraint_rows),'generated_chapters':len(layers)+len(patterns)},indent=2))
