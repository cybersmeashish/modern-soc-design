# Capacity and workforce planning models

The tools use standard-library arithmetic and synthetic inputs. Their outputs are **estimates from declared assumptions**, not measurements of ingest, search, recovery, analyst productivity or p95 response latency.

## Storage and backlog

Input sizes use decimal bytes/GB: one GB is 1,000,000,000 bytes. `event_bytes` represents the assumed event payload; network framing, service overhead and billing units require separate measurement.

- Raw GB/day = average EPS × event bytes × 86,400 / 1e9.
- Hot GB = raw GB/day × hot days × stored/raw ratio × hot copies × (1 + hot index overhead).
- Additional cold GB = raw GB/day × additional cold days × stored/raw ratio × cold copies.
- Outage backlog events = assumed peak EPS × outage hours × 3,600.
- Raw queue GB = backlog events × event bytes / 1e9.
- Catch-up hours = backlog events / (processing EPS − average EPS) / 3,600, only when the net drain is positive.

Hot and additional-cold windows are non-overlapping. If the estate keeps raw archives alongside indexed copies, explicitly model those additional retained copies. The single stored/raw ratio is a simplification; use measured separate ratios before investment decisions.

The example assumes 1,000 average EPS, 5,000 peak EPS, 1,000-byte events and a four-hour peak-rate outage. Its arithmetic yields 86.4 raw GB/day, 72 GB of raw backlog and ten catch-up hours at 3,000 processing EPS. These numbers are synthetic assumptions. If processing equals or falls below continuing average input, nonzero backlog has no finite catch-up result; the model returns `null`, not a successful zero-time restore.

## Workforce

- Coverage FTE = continuous staffed seats × 168 weekly hours / (paid hours/FTE/week × availability).
- Weekly mean review demand = daily alerts × mean review minutes / 60 × 7.
- Workload FTE = weekly demand / (paid hours × availability × productive ratio × target utilization).
- Planning lower bound = max(coverage FTE, workload FTE), rounded up for the integer display.

Coverage and workload are not added because staffed analysts can handle work during coverage hours. Availability represents time at work; productive ratio represents the portion assigned to this task; utilization reserves handling headroom. Agree these meanings and avoid double-discounting the same time.

The example produces a coverage lower bound of 10.5 FTE, displayed as 11. It excludes specialist roles, incident surges, handover, case complexity, correlated arrivals and scheduling constraints. It cannot promise service-level or tail latency. Model those with representative observed distributions and a validated scheduling/queue method.

## Execute in OrbStack

```bash
docker --context orbstack exec -w /workspaces/modern-soc-design/repo modern-soc-design-dev python tools/planning.py capacity examples/planning/capacity.json
docker --context orbstack exec -w /workspaces/modern-soc-design/repo modern-soc-design-dev python tools/planning.py staffing examples/planning/staffing.json
```

[Inputs](../examples/planning/capacity.json) · [No-headroom case](../examples/planning/no-recovery-headroom.json) · [Actual model execution](../evidence/model-results.json).
