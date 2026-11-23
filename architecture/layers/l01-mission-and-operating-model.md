# L01 — Mission and operating model

**Stage:** original reference design. **Proposed accountable role:** Executive sponsor and SOC service owner.

**Inputs:** Business services, risk appetite, service obligations.

**Outputs:** Mandate, scope, coverage model and decision rights.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L01-C01 | Name the services, harms and decisions the SOC exists to support. | Tool activity replaces measurable service protection. | Sponsor-approved mission and prioritized business-service register. |
| L01-C02 | Separate continuous collection, staffed monitoring, on-call response and incident command. | A 24/7 dashboard is presented as 24/7 response capability. | Coverage timetable, on-call tests and explicit response commitments. |
| L01-C03 | Assign decision rights for monitoring, investigation, containment and risk acceptance. | Analysts or suppliers make business-impacting decisions without authority. | RACI and authorized escalation/containment decision records. |
| L01-C04 | Choose internal, outsourced or shared delivery with a retained accountable owner. | MDR access and responsibilities fall between contract boundaries. | Contract/interface review and exercised joint handover. |
| L01-C05 | Set measurable objectives with denominators, unknowns and review triggers. | Activity totals imply effectiveness without known visibility. | Metric dictionary tied to service scope and evidence. |
| L01-C06 | Agree funding, change priorities and escalation for unresolved risk. | Platform purchasing displaces people, engineering and recovery investment. | Costed options, residual-risk decisions and quarterly roadmap. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[nist-csf](https://www.nist.gov/cyberframework) · [nist-ir](https://csrc.nist.gov/pubs/sp/800/61/r3/final)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
