# L12 — Investigation, forensics and case evidence

**Stage:** original reference design. **Proposed accountable role:** Incident investigators and evidence custodians.

**Inputs:** Scoped events, evidence references and investigation authority.

**Outputs:** Reproducible case record and controlled evidence access.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L12-C01 | Define case state, evidence scope, investigator authority and provenance. | The case combines unsupported assertions or unauthorized records. | Attributable evidence-to-claim index and subject/tenant access checks. |
| L12-C02 | Preserve original evidence separately from analysis and derived copies. | Normalization or analyst edits overwrite the source record. | Raw/derived distinction, protected original and reproducible transformations. |
| L12-C03 | Record custody, hashes and independent anchors with honest tamper limits. | A hash chain is claimed to prove completeness or trustworthy event time. | Alteration/gap checks and explicit anchor/time limitations. |
| L12-C04 | Handle uncertain time and partial ordering instead of fabricating chronology. | Clock skew creates a false sequence or attribution. | Event/observation times, uncertainty bounds and competing timelines. |
| L12-C05 | Control export recipients, fields, purpose and retention/hold decisions. | A valid investigator session permits unrestricted external disclosure. | Purpose-bound export and invalid-recipient/classification cases. |
| L12-C06 | Keep investigation continuity available when central systems fail. | Loss of case tooling destroys local decisions or evidence custody. | Offline procedure, locally accepted owners and reconciled handover. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[nist-ir](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [nist-controls](https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
