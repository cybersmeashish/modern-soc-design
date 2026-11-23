# L23 — Interoperability, integration and migration

**Stage:** original reference design. **Proposed accountable role:** Integration owners and security architecture.

**Inputs:** Source/query/case/tool contracts and vendor dependencies.

**Outputs:** Controlled compatible interfaces and tested exit paths.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L23-C01 | Version data, query, case and response contracts independently. | A working event connector is mistaken for operational interoperability. | Contract tests across fields, time semantics, identity and actions. |
| L23-C02 | Verify schema translation and detection behavior on each destination backend. | Equivalent-looking rules produce different matches or missed events. | Representative events and backend-specific query observations. |
| L23-C03 | Bound API limits, credentials, retries, callback trust and provider dependencies. | Integration fails on throttling or broad credentials expand response authority. | Rate/failure/permission cases and controlled retry behavior. |
| L23-C04 | Plan dual-run migration with deduplication and explicit authority cutover. | Two platforms generate duplicate cases or conflicting containment. | Parallel comparison, ownership switch and rollback decision. |
| L23-C05 | Test export/import of raw evidence, context, cases and content. | Vendor exit preserves files but loses useful meaning or custody. | Alternative-path reproduction with versioned manifests. |
| L23-C06 | Separate documented provider capability from your own deployment observation. | A reference diagram or product page is presented as tested platform behavior. | Source/version register and environment-specific evidence requirements. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[ocsf](https://schema.ocsf.io/) · [otel](https://opentelemetry.io/docs/specs/otel/logs/data-model/) · [sigma](https://raw.githubusercontent.com/SigmaHQ/sigma-specification/main/README.md) · [aws-lake](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html) · [sentinel](https://learn.microsoft.com/en-us/azure/sentinel/best-practices-workspace-architecture)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
