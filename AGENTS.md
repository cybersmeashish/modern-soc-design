# Development and publication rules

All project development, edits, research analysis, dependency installation, builds, tests and artifact generation must run in the repository-specific OrbStack container. Use `docker --context orbstack` explicitly.

- Container: `modern-soc-design-dev`.
- Canonical workspace: `/workspaces/modern-soc-design/repo`.
- Persistent named volume: `modern-soc-design-workspace`, mounted at `/workspaces`.
- The host copy is for review, transfers and guarded publishing, not project-runtime execution.
- Never mount host credentials, home directories or the Docker socket into development containers.
- Do not delete persistent workspace volumes as ordinary cleanup.
- Restore unavailable OrbStack access or report the blocker; do not fall back to macOS runtimes.
- Preserve mandatory publication checks: authorized account/repository, reviewed paths, non-forced branch updates, remote byte checks and existing-content preservation.

Update catalog inputs first, regenerate documentation, run relevant planning/record tests and validate local links. Evidence must distinguish design from observation. Do not promote a complete record, local calculation or reference diagram to a deployed-control, compliance, client or operational-capacity claim.
