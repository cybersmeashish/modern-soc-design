# Evidence stages and acceptance

| Stage | What it supports | What it does not establish |
|---|---|---|
| Planned | A proposed decision or test | Implemented behavior |
| Documented | Inspectable ownership/flow/control design | Enforced boundaries or accepted real ownership |
| Tested local | Observed scoped model/code behavior | A production SOC, provider capacity or learned-model quality |
| Tested environment | Observations in a named actual environment with inputs/method | Unmeasured failure modes, whole-estate coverage or legal compliance |
| Independently reviewed | A separate review with explicit scope and attribution | Unlimited certification or continued correctness after change |

## Claim record

Each claim should name scope, owner, method, inputs/versions/hashes, timestamp, actual observation, expected behavior, limitations, unresolved gaps, review triggers and acceptance decision. Failed and indeterminate cases remain visible. Repeating a test in two environments does not double the unique test count.

## This release

The layer/pattern catalogs and diagrams are documented reference designs. Planning and record-consistency tests were executed in OrbStack. The record checker accepts internally consistent synthetic declarations; it cannot authenticate owner acceptance, identity, approval tokens, time, physical placement or evidence references.

It does not collect events, deploy queues/SIEMs, execute response actions, authenticate production users, prove physical air gaps, evaluate learned models or measure operational throughput. No source-to-case production trial or independent client acceptance is asserted.

## Deployment acceptance gates

1. Actual scope, applicable requirements, owners and response rights accepted.
2. Source delivery, data/identity/tenant/field/purpose boundaries observed.
3. Relevant allowed, denied, stale, missing, malformed and overload cases measured.
4. Key/identity/config/data/authority restoration and remaining dependencies observed.
5. Representative workload, cost, staffing and response distributions reviewed.
6. Residual gaps accepted or blocked by accountable owners; evidence expiry/change triggers set.

Use the [acceptance record](../templates/acceptance-record.md). A record completeness check is not a substitute for these environment gates.
