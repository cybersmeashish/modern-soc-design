# L06 — Schema, time and lineage

**Stage:** original reference design. **Proposed accountable role:** Data engineering and detection engineering.

**Inputs:** Raw events, schema versions and parser rules.

**Outputs:** Normalized records linked to source evidence.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L06-C01 | Select and pin canonical schema versions and producer mappings. | Field meanings change while detections continue to run. | Versioned mapping contract and schema migration cases. |
| L06-C02 | Retain raw-to-normalized lineage according to approved privacy/retention policy. | Transformation loses investigative context or retains sensitive data indefinitely. | Traceable source references and controlled redaction/deletion tests. |
| L06-C03 | Preserve event time, observed time and explicit clock uncertainty. | Collector receipt time is substituted for the original event time. | Skew, invalid-time and uncertain-ordering cases. |
| L06-C04 | Treat missing, unmapped and conflicting fields as visible quality states. | A missing identity/classification becomes a benign default. | Quality report and quarantine/uncertainty behavior. |
| L06-C05 | Bound parsing, decompression and rendering of untrusted content. | Events exhaust resources or execute through analysts or downstream tools. | Resource limits and hostile-content handling cases. |
| L06-C06 | Test detection semantics on normalized data, not just schema validity. | A valid conversion changes matching, time windows or entity meaning. | Paired raw/normalized detection cases and backend-specific results. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[ocsf](https://schema.ocsf.io/) · [otel](https://opentelemetry.io/docs/specs/otel/logs/data-model/) · [sigma](https://raw.githubusercontent.com/SigmaHQ/sigma-specification/main/README.md)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
