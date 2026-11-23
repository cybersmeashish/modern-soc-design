# L18 — Platform security, supply chain and change

**Stage:** original reference design. **Proposed accountable role:** Platform engineering and release owners.

**Inputs:** Infrastructure, detection/model packages and approved changes.

**Outputs:** Hardened platform and traceable configuration releases.

## Decisions, failure modes and acceptance evidence

| ID | Decision to make | Failure to avoid | Evidence required before acceptance |
|---|---|---|---|
| L18-C01 | Separate development, evaluation, production and privileged release contexts. | An untrusted contribution inherits production secrets or publish rights. | Environment/permission boundaries and untrusted-change cases. |
| L18-C02 | Pin and inventory components, build inputs and support dependencies. | Unknown plugins, libraries or licensing dependencies undermine recovery or offline operation. | Component/dependency register and lifecycle ownership. |
| L18-C03 | Verify package target, signer, digest, version and approval before admission. | Integrity checking accepts an unexpected signer, wrong site or replayed package. | Modified-artifact, wrong-target/signer and rollback/replay cases. |
| L18-C04 | Protect pipeline credentials, signing keys and privileged configuration. | Content authors can self-approve privileged platform changes. | Release-role separation and reviewed trust-input handling. |
| L18-C05 | Stage changes with measured rollback criteria and residual-state checks. | A reverted deployment leaves permissions, queues or model state changed. | Failed-update exercise and complete state-difference review. |
| L18-C06 | Harden the platform without equating container isolation with full trust. | A restricted container is called a secure SOC while identity and data controls remain absent. | Host/runtime/network/control-plane threat review and explicit missing evidence. |

## Review this layer

Identify the actual service, tenant, jurisdiction and implementation scope. Replace proposed owner roles with accepted responsibilities. Exercise intended, denied, degraded and recovery cases. Record what was observed and what remains unknown; a complete design record does not establish enforcement.

## Research foundations

[nist-controls](https://raw.githubusercontent.com/usnistgov/oscal-content/main/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json) · [sigma](https://raw.githubusercontent.com/SigmaHQ/sigma-specification/main/README.md)

These references inform the domain. The constraints and acceptance examples are original proposals, not quoted source requirements or a completed framework assessment.

[All layers](../../docs/layer-index.md) · [Architecture patterns](../../docs/pattern-index.md) · [Evidence stages](../../docs/evidence-and-acceptance.md).
