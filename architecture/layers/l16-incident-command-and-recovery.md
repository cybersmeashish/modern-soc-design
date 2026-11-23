# L16 — Incident command and business recovery

**Stage:** original reference design. **Proposed accountable role:** Incident commander, service owners and legal/privacy advisers.

**Inputs:** Confirmed/uncertain incident evidence, dependencies and harm.

**Outputs:** Accountable containment, communications and recovery decisions.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L16-C01 | Define activation, authority, incident ownership and business impact criteria. | Uncertain alerts trigger conflicting command or premature public conclusions. | Escalation exercise and accepted command/decision records. |
| L16-C02 | Coordinate containment with safety, continuity and evidence preservation. | An automated security action causes greater business or physical harm. | Trade-off decision and process-owner-approved containment exercise. |
| L16-C03 | Establish secure communications and local decision channels during outages. | Compromised or unavailable identity/communications prevents command. | Out-of-band contact validation and loss-of-connectivity exercise. |
| L16-C04 | Assess notification duties for the entity, jurisdiction, incident and agreement. | Generic time windows are incorrectly treated as universally applicable law. | Current applicability review by the responsible legal/privacy owners. |
| L16-C05 | Restore identity, keys, configuration, data and pending-action state with explicit loss. | A database restore is presented as restoration of the whole SOC or business. | Measured scoped restoration, missing records and remaining dependencies. |
| L16-C06 | Preserve learning, decisions and follow-through after recovery. | Lessons remain narrative and recurring causes are not treated. | Owned corrective actions, priority decision and evidence-based retest. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[nist-ir](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [nist-ot](https://csrc.nist.gov/pubs/sp/800/82/r3/final) · [nist-controls](https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
