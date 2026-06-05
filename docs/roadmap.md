# Research Agent Toolkit Roadmap

This roadmap tracks planned maintenance and extension work for Research Agent Toolkit.

## v1.0.0 release readiness

Goal: prepare a clean v1.0.0 research-preview release.

Tasks:

- Confirm package version and README release boundary are aligned.
- Confirm tests pass in GitHub Actions.
- Confirm the CLI quick-start commands work from a fresh clone.
- Review architecture and demo documentation for public readability.
- Add release notes summarizing CLI, workflow automation, literature monitoring, generated artifacts, safety defaults, and known limitations.
- Tag v1.0.0 after the checklist is complete.

## Stricter source verification mode

Goal: add an optional strict verification mode for users who need higher auditability.

Planned work:

- Add a configuration option for strict direct-page verification.
- Record observed page titles when direct verification is available.
- Improve reporting for items whose titles, dates, or source metadata cannot be verified.
- Add tests for accepted metadata, rejected metadata, and fallback behavior.

## MCP adapter

Goal: add a Model Context Protocol (MCP) adapter so the toolkit can interoperate with external research tools.

Planned work:

- Define a small MCP-facing interface for literature-monitor runs.
- Expose read-only report artifacts through the adapter.
- Keep the adapter optional so the default workflow remains lightweight.
- Document example usage for local research assistants.

## Additional research-topic presets

Goal: support more research communities beyond the initial biomedical imaging preset.

Candidate presets:

- general biomedical AI;
- radiology foundation models;
- computational pathology;
- clinical natural language processing;
- scientific machine learning;
- open-source developer tooling.

Each preset should include topic keywords, source priorities, ranking hints, and example report sections.

## Web dashboard prototype

Goal: provide a lightweight interface for reviewing generated reports and configuration.

Planned work:

- Show included and excluded candidates from the latest run.
- Display source, score, verification status, and inclusion reason.
- Provide links to generated Markdown and JSON artifacts.
- Keep the first version read-only.

## Draft review mode improvements

Goal: make report review safer before external sharing.

Planned work:

- Improve draft-review documentation.
- Add clearer configuration examples.
- Add tests for mode selection.
- Keep dry-run behavior as the default.
