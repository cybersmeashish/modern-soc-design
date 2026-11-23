# Cryptographic purpose and post-quantum transition

A SOC depends on more than encrypted storage. Inventory each cryptographic purpose, accountable owner, implementation/version, key custody, supplier dependency, lifetime and recovery path before choosing a migration.

| Purpose | Architectural question | Evidence required |
|---|---|---|
| Collector/service communications | Which protocol establishes secrets and authenticates each endpoint? | Actual supported protocol/implementation and interoperability observations |
| Artifact and detection/model admission | Which signature authenticates the expected signer, target, digest and version? | Separately pinned verification inputs and altered/wrong-signer/replay cases |
| Human/workload identity | Which algorithms and providers issue/verify credentials? | Issuer/audience/expiry/revocation behavior and real compatibility |
| Archived evidence and backups | Which confidentiality lifetime and keys must survive retention and recovery? | Key/owner/dependency inventory and clean authorized restore |
| Evidence custody/checkpoints | What authenticates records and anchors their history? | Signature/anchor scope, verification availability and time/completeness limitations |
| Offline imports | Which verification material, clock and trust roots work locally? | Local admission/rotation/recovery with external services unavailable |

NIST publishes distinct post-quantum standards for key encapsulation and signatures. Consult [the official project and standards](https://csrc.nist.gov/projects/post-quantum-cryptography) for current selections; do not treat a signature replacement as a key-establishment migration or label existing symmetric encryption as obsolete solely because a public-key transition is needed.

Plan through maintained implementations and supplier support. Record protocol, format and old-evidence compatibility, performance in the actual workload, validation requirements and rollback/verification dependencies. Hardware custody, software-key simulation and formally validated modules are different evidence claims.

This repository executes no PQ cryptographic implementation, TLS handshake, HSM or FIPS validation. Related [cryptographic inventory](https://github.com/cybersmeashish/crypto-implementations) and [sovereign/disconnected research](https://github.com/cybersmeashish/sovereign-disconnected-cloud-security) have their own separately scoped evidence; it is not counted as validation of this SOC architecture.

[Identity layer](../architecture/layers/l17-soc-identity-and-privileged-access.md) · [Data/retention layer](../architecture/layers/l07-data-platform-and-retention.md) · [Recovery layer](../architecture/layers/l19-resilience-and-disaster-recovery.md).
