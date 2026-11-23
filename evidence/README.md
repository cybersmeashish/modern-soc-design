# Execution evidence and its limits

[Actual verification](verification.json) · [Model and design-record outputs](model-results.json) · [Source correspondence](source-manifest.json) · [Regression log](tests.log).

The tools execute planning arithmetic and documentation-consistency cases. The isolated OrbStack run records non-root execution, read-only source/image filesystems, loopback-only interfaces, no default IPv4 route and a blocked external-connect probe.

Those execution properties apply to the **tool-check container**, not to a deployed SOC or physical air-gap environment. The design diagrams and 224 constraint records are reference proposals. There is no operational telemetry pipeline, SIEM benchmark, learned-model test, live response action or provider deployment in this release.

The unique regression count is recorded from actual unittest execution; repeated environments are not added. Source hashes establish correspondence, not complete software trust or independent assurance. Documentation counts and selected control mappings do not prove implementation or compliance.

Reproduce inside the named OrbStack workspace with [the development guide](../docs/development.md). Changes to code/catalog/input files invalidate the recorded correspondence and require fresh evidence.
