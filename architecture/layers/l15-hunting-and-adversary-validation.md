# L15 — Threat hunting and adversary validation

**Stage:** original reference design. **Proposed accountable role:** Hunt lead, detection engineering and system owners.

**Inputs:** Threat hypotheses, visibility records and authorized test scope.

**Outputs:** Investigations, validated detections and explicit blind spots.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L15-C01 | Authorize target, techniques, safety limits and data handling before simulation. | A coverage exercise becomes an unapproved production attack. | Written scope, domain-owner acceptance and stop conditions. |
| L15-C02 | Connect ATT&CK mapping to actual sources, fields, conditions and results. | Technique counts or heatmaps are presented as tested detection coverage. | Versioned mapping plus observed detect/miss outcomes. |
| L15-C03 | Maintain benign controls and negative findings with visibility qualifications. | A hunt with absent telemetry is reported as absence of compromise. | Required-data checks, negative-result limits and missing-evidence cases. |
| L15-C04 | Exercise prevention, detection, investigation and response as separate claims. | A blocked payload is mistaken for a tested full incident workflow. | Distinct stage observations and unresolved transitions. |
| L15-C05 | Convert confirmed findings into reviewed reusable content and regression evidence. | A one-off successful exercise does not improve sustained operations. | Finding-to-rule/playbook change and reproducible retest. |
| L15-C06 | Respect OT/process constraints and use safe synthetic alternatives where necessary. | Active testing threatens physical safety or essential availability. | Safety-owner authorization and bounded passive/simulation method. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[mitre-attack](https://attack.mitre.org/resources/working-with-attack/) · [nist-ir](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
