# P09 — Federated national and regional SOC

**Stage:** reference architecture; not a tested deployment.

## When to consider it

Accountable agencies/regions retaining local data and decisions.

## Logical arrangement

Regional SOCs retain evidence and actions; central coordination receives approved freshness-aware summaries.

```mermaid
flowchart LR
 S1[Regional sources] --> R1[Regional SOC and authority]
 S2[Other sources] --> R2[Other regional SOC]
 R1 --> E1[Approved export]
 R2 --> E2[Approved export]
 E1 --> C[Central coordination and freshness]
 E2 --> C
 C --> P[Reviewed packages] --> A[Local admission owners]
```

Arrows identify intended relationships. They are not packet observations, provider deployment evidence or proof of isolation.

## Trade-off

Distributed authority makes common policy, stale evidence and joint command explicit concerns.

## Pattern-specific design constraints

| ID | Decision to make | Failure to avoid | Acceptance evidence |
|---|---|---|---|
| P09-C01 | Separate central coordination from local authority and custody. | Central systems assume unrestricted access or command. | Federation authority matrix and denied central actions. |
| P09-C02 | Carry freshness, uncertainty and disclosure constraints in export. | Silent sites are reported as currently protected. | Aged/missing reports and prohibited disclosure cases. |
| P09-C03 | Admit shared content locally with target/version checks. | A compromised coordinator pushes stale or executable authority. | Wrong-target/signer and replay/rollback admission cases. |
| P09-C04 | Exercise multi-owner command under connectivity loss. | Ambiguity prevents accountable local response. | Regional/central exercise and independent local decisions. |

## Priority layer reviews

[L04](../layers/l04-edge-collection-and-buffering.md) · [L16](../layers/l16-incident-command-and-recovery.md) · [L20](../layers/l20-privacy-sovereignty-and-governance.md) · [L21](../layers/l21-observability-and-effectiveness.md)

All 24 layers remain in the review scope. These links highlight decisions that change most for this pattern; they do not exempt other controls.

## Environment-specific gate

Before implementation, agree the business scope, approved sources, authority boundaries, data/administrator/key/support/recovery placement, critical dependencies and response rights. Verify actual source delivery, permission boundaries, failure behavior, cost/capacity and restoration in the intended environment. Mixed patterns need an interface and responsibility review at every joining boundary.

[Pattern catalog](../../docs/pattern-index.md) · [Selection method](../../docs/architecture-selection.md) · [Acceptance record](../../templates/acceptance-record.md).
