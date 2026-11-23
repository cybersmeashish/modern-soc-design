# L17 — SOC identity and privileged access

**Stage:** original reference design. **Proposed accountable role:** IAM, platform and evidence owners.

**Inputs:** Human/workload identities, resource policy and emergency authority.

**Outputs:** Scoped sessions, service grants and attributable administration.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L17-C01 | Enforce resource/tenant/purpose permissions beneath consoles and workflow tools. | An authorized dashboard hides broad storage or API permissions. | Direct API/storage/export denial cases and legitimate-user controls. |
| L17-C02 | Separate platform admin, evidence reader, key custodian and action approver. | One operator can grant actions, decrypt records and erase the evidence. | Role/duty matrix and privileged-operation review. |
| L17-C03 | Use verified request-bound human and workload context with explicit delegation. | Agent or service credentials inherit broader authority than the user. | Issuer/audience/expiry/delegation checks and denied privilege expansion. |
| L17-C04 | Manage secret distribution, rotation, revocation and unavailable identity services. | Revoked credentials or stale local state remain usable without accountability. | Rotation/revocation/offline cases with bounded local authority. |
| L17-C05 | Make emergency access scoped, time-bounded and independently reviewable. | Emergency accounts become persistent unreviewed bypasses. | Grant, usage, expiry and review records. |
| L17-C06 | Inventory cryptographic purpose and migration dependencies separately. | A generic quantum-safe claim ignores authentication, signatures or archived evidence. | Purpose-specific crypto inventory and implementation-specific compatibility plan. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[nist-zero-trust](https://csrc.nist.gov/pubs/sp/800/207/final) · [nist-controls](https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json) · [nist-pqc](https://csrc.nist.gov/projects/post-quantum-cryptography)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
