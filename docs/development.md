# Reproduce and maintain inside OrbStack

The authoritative development source is the persistent named workspace described in [AGENTS.md](../AGENTS.md). The host review mirror is not the development environment.

The recorded environment uses Python 3.12.16 in the official image pinned to digest `sha256:5e2bdb1b0d542d5039cffb8181c65930093949194a65c365dfb1b0fe13a4fa5b`. There are no third-party Python project dependencies.

## Run checks

```bash
docker --context orbstack exec -w /workspaces/modern-soc-design/repo modern-soc-design-dev python tools/build_docs.py
docker --context orbstack exec -w /workspaces/modern-soc-design/repo modern-soc-design-dev python -m unittest discover -s tests -v
docker --context orbstack exec -w /workspaces/modern-soc-design/repo modern-soc-design-dev python tools/verify_reference.py --out /tmp/modern-soc-check
```

## Workspace custody

Inspect/start the existing project container and named volume. Do not reset it to recreate a checkout. If setting up another machine, create a dedicated volume, establish a non-root owner and transfer only the reviewed public source into `/workspaces/modern-soc-design/repo`.

Development runs non-root with dropped capabilities, a read-only image filesystem and the named workspace as its writable project source. Source retrieval uses the development network. The recorded validation also runs in a separate network-disabled OrbStack container with the workspace mounted read-only.

Host commands are limited to orchestration, review transfers, UI actions and the existing guarded publication controls. Publication tooling verifies the authorized account, compares existing Git state, preserves unrelated content and checks remote blob bytes. No credential or Docker-socket mount is required inside the container.

Re-running source research or changing code/catalog inputs invalidates the old source manifest and requires new scoped execution evidence. Documentation counts alone are not a security test.
