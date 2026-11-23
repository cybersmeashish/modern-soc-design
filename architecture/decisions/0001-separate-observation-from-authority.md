# ADR 0001 — separate observation from authority

**Status:** reference decision. **Scope:** every pattern that can propose or dispatch actions.

Events, detections, analyst recommendations and model outputs can be inaccurate or attacker-controlled. Their content must not create a subject, tenant, permission, approval or response budget.

The selected design uses an independent action-authority boundary. It derives trusted subject/service context, resolves resources, checks tenant/action/purpose, verifies exact approval where needed, bounds execution and independently observes effects.

A fully manual process, provider-native gate and custom gateway are alternative implementations. Each needs environment-specific evidence of the same boundary. A separate component in a diagram does not establish that a bypass is blocked.

Consequences include explicit ownership, integration cost, failure/degraded modes and approval latency. An unavailable authority service must not become unrestricted response. Low-impact local work may continue only under separately approved bounded local authority.

[Action layer](../layers/l13-response-orchestration.md) · [AI layer](../layers/l14-ai-copilots-and-agents.md).
