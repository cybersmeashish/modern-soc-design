"""Deterministic planning arithmetic, not measured SIEM throughput or staffing guarantees."""
import argparse
import json
import math
from pathlib import Path

def number(data, key, minimum=0, strict=False):
    value = data.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{key}: finite numeric input required")
    if value < minimum or (strict and value == minimum):
        raise ValueError(f"{key}: outside allowed range")
    return float(value)

def capacity(data):
    avg=number(data,"average_eps");peak=number(data,"peak_eps");size=number(data,"event_bytes",0,True)
    if peak < avg: raise ValueError("peak_eps must be at least average_eps")
    hot=number(data,"hot_days");cold=number(data,"additional_cold_days")
    compression=number(data,"stored_to_raw_ratio",0,True)
    if compression>1: raise ValueError("stored_to_raw_ratio must be in (0,1]")
    replicas=number(data,"hot_copies",0,True)
    if not replicas.is_integer(): raise ValueError("hot_copies must be an integer")
    coldcopies=number(data,"cold_copies",0,True)
    if not coldcopies.is_integer(): raise ValueError("cold_copies must be an integer")
    overhead=number(data,"hot_index_overhead_ratio")
    outage=number(data,"outage_hours");service=number(data,"processing_eps")
    daily=avg*size*86400/1e9;backlog_events=peak*outage*3600
    margin=service-avg
    catchup=0.0 if backlog_events==0 else (backlog_events/margin/3600 if margin>0 else None)
    outputs={"raw_gb_per_day":daily,"hot_gb":daily*hot*compression*replicas*(1+overhead),
        "additional_cold_gb":daily*cold*compression*coldcopies,"backlog_events":backlog_events,
        "raw_queue_gb":backlog_events*size/1e9,"catchup_hours":catchup,
        "recovery_headroom_eps":margin,"recovery_headroom_available":margin>0,
        "finite_catchup_possible":backlog_events==0 or margin>0,
        "scope":"decimal GB; independent non-overlapping hot/additional-cold windows; assumed rates/ratios"}
    if any(isinstance(v,float) and not math.isfinite(v) for v in outputs.values()):
        raise ValueError("derived quantities exceed finite numeric range")
    return outputs

def staffing(data):
    alerts=number(data,"alerts_per_day");minutes=number(data,"mean_review_minutes")
    seats=number(data,"continuous_staffed_seats");paid=number(data,"paid_hours_per_week",0,True)
    availability=number(data,"availability_ratio",0,True);productive=number(data,"productive_ratio",0,True)
    utilization=number(data,"target_utilization",0,True)
    if any(x>1 for x in (availability,productive)) or utilization>=1:
        raise ValueError("ratios must be in (0,1], and target_utilization in (0,1)")
    coverage=seats*168/(paid*availability)
    demand=alerts*minutes/60*7
    workload=demand/(paid*availability*productive*utilization)
    lower=max(coverage,workload)
    if not math.isfinite(lower):raise ValueError("derived staffing exceeds finite range")
    return {"coverage_fte":coverage,"workload_fte":workload,"planning_fte_lower_bound":lower,
        "rounded_planning_fte":math.ceil(lower),"weekly_review_hours":demand,
        "scope":"max of coverage and workload, not their sum; mean-load lower bound, not p95 latency or full staffing"}

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("kind",choices=["capacity","staffing"]);parser.add_argument("input",type=Path)
    args=parser.parse_args();print(json.dumps((capacity if args.kind=="capacity" else staffing)(json.loads(args.input.read_text())),indent=2,allow_nan=False))
