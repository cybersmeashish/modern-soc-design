# L11 — Alert triage and analyst experience

**Stage:** original reference design. **Proposed accountable role:** SOC operations and case owners.

**Inputs:** Detections, context, visibility states and service impact.

**Outputs:** Prioritized review queues and attributable dispositions.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L11-C01 | Prioritize by business impact, confidence, exposure and known visibility. | Numerical severity suppresses critical but uncertain cases. | Priority rationale, missing-context cases and owner escalation. |
| L11-C02 | Deduplicate without erasing distinct actors, resources or repeated harm. | A suppression rule hides continuing compromise. | Grouping/reopen cases and access to original contributing events. |
| L11-C03 | Make routing, acknowledgement, review age and overdue escalation observable. | An alert is delivered but never accepted by an accountable analyst. | Receipt-to-disposition trace and unattended-queue exercise. |
| L11-C04 | Render attacker-controlled content safely and mark AI-generated reasoning. | Events execute through the console or misleading suggestions appear authoritative. | Hostile-content UI review and clear source/AI attribution. |
| L11-C05 | Define analyst permissions and purposeful cross-team handover. | Convenient case sharing broadens tenant or sensitive-data access. | Case/field permissions and authorized/denied handover checks. |
| L11-C06 | Represent data gaps and detection outages separately from a quiet queue. | An empty dashboard is reported as effective security. | Visibility status surfaced in queue and executive report. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[nist-ir](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [nist-controls](https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
