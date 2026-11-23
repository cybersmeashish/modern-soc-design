# Contribute a decision and its evidence

Useful additions include a missing architecture constraint, a scoped pattern variation, a reproducible model correction, an environment failure observation or a documented integration trade-off.

1. State the service/scope and relevant layer/pattern ID.
2. Read the applicable primary source and record version/date and attribution.
3. Explain the decision, failure mode and acceptance evidence.
4. Separate proposal, declaration, local observation, environment observation and independent review.
5. Use synthetic or explicitly authorized material. Exclude credentials, real customer records and confidential incident/contract details.
6. Run the documented checks in the repository-specific OrbStack workspace.
7. Record limitations and the decision another practitioner can reproduce.

Catalog files are the maintained inputs. Rebuild chapters with `tools/build_docs.py` inside OrbStack. Preserve existing stable IDs and use a new ID for a materially distinct record. Counts describe records, not implemented controls or operational coverage.

For confidential security issues, use [the security reporting guidance](SECURITY.md).
