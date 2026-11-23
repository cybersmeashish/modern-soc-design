"""Check documentation contradictions. This does not test deployed controls or certify a SOC."""
import argparse
import json
import math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def review(record):
    scope="record consistency only; declared owners, permissions, timestamps and references are not authenticated"
    if not isinstance(record,dict):
        return {"status":"needs_review","issues":[{"code":"invalid_record_shape","message":"JSON object required"}],"scope":scope}
    if any(not isinstance(record.get(k,{}),dict) for k in ("response","visibility","data_policy","proposed_layer_owners")) or not isinstance(record.get("critical_dependencies",[]),list) or any(not isinstance(d,dict) for d in record.get("critical_dependencies",[])):
        return {"status":"needs_review","issues":[{"code":"invalid_record_shape","message":"Nested record types invalid"}],"scope":scope}
    if not isinstance(record.get("pattern_id"),str):
        return {"status":"needs_review","issues":[{"code":"unknown_pattern","message":"Pattern ID must be a string"}],"scope":scope}
    errors=[]
    def issue(code,message):errors.append({"code":code,"message":message})
    patterns={p["id"] for p in json.loads((ROOT/"catalog/patterns.json").read_text())["patterns"]}
    layers=json.loads((ROOT/"catalog/layers.json").read_text())["layers"]
    if record.get("pattern_id") not in patterns:issue("unknown_pattern","Choose a registered reference pattern")
    owners=record.get("proposed_layer_owners",{})
    for layer in layers:
        if not isinstance(owners,dict) or not isinstance(owners.get(layer["id"]),str) or not owners[layer["id"]].strip():issue("missing_owner",layer["id"])
    if record.get("connectivity") not in {"connected","intermittent","strict_airgap"}:issue("unknown_connectivity","Connectivity scope required")
    if record.get("connectivity")=="strict_airgap":
        for dep in record.get("critical_dependencies",[]):
            if dep.get("location")=="external" and dep.get("required_offline") and not dep.get("local_alternative"):
                issue("external_offline_dependency",str(dep.get("name")))
    tenants=record.get("tenant_count")
    if isinstance(tenants,bool) or not isinstance(tenants,int) or tenants<1:issue("invalid_tenant_count","Positive tenant count required")
    elif tenants>1 and not record.get("data_policy",{}).get("tenant_isolation_declared"):issue("missing_tenant_boundary","Multi-tenant separation must be documented")
    response=record.get("response",{})
    if not response.get("independent_authorization"):issue("proposal_as_authority","Declare independent action authorization")
    if response.get("failure_behavior")!="deny":issue("fail_open_response","Unknown authority must not become an allow")
    high=response.get("high_impact_actions",[])
    if high and not response.get("exact_expiring_approval"):issue("unbounded_approval","High-impact actions need exact scoped expiring approval")
    if high and (not isinstance(response.get("max_actions_per_job"),int) or isinstance(response.get("max_actions_per_job"),bool) or response["max_actions_per_job"]<1):issue("missing_action_budget","Bound action count")
    evidence=record.get("visibility",{})
    age=evidence.get("reported_age_seconds");ttl=evidence.get("current_max_age_seconds")
    valid_time=all(not isinstance(v,bool) and isinstance(v,(int,float)) and math.isfinite(v) and v>=0 for v in (age,ttl))
    if not valid_time:issue("invalid_freshness","Finite nonnegative reported age and threshold required")
    elif evidence.get("status")=="current" and age>ttl:issue("stale_as_current","Reported evidence exceeds the declared current threshold")
    if evidence.get("status")=="current" and not evidence.get("origin_verified"):issue("unverified_as_current","Declared unverified evidence cannot also be current")
    if evidence.get("status") not in {"current","delayed","missing","unverified"}:issue("unknown_visibility","Declare visibility state")
    if record.get("sovereignty_claim")=="proven" and record.get("placement_evidence_kind")!="tested_environment":issue("declaration_as_assurance","Placement strings are not environment observation")
    claim=record.get("evidence_claim")
    if claim not in {"design_only","tested_local","tested_environment","independent_review"}:issue("unknown_evidence_kind","Declare evidence kind")
    if claim in {"tested_environment","independent_review"} and not record.get("environment_evidence_references"):issue("unsupported_environment_claim","Provide scoped evidence references for the claimed stage")
    return {"status":"documentation_valid" if not errors else "needs_review","issues":errors,
        "scope":"record consistency only; declared owners, permissions, timestamps and references are not authenticated"}

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("input",type=Path);args=parser.parse_args()
    result=review(json.loads(args.input.read_text()));print(json.dumps(result,indent=2));raise SystemExit(0 if not result["issues"] else 1)
