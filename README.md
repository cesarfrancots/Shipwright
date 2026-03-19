# Shipwright

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
![Platforms: Claude Code, Codex CLI, GitHub Copilot](https://img.shields.io/badge/platforms-Claude%20Code%20%7C%20Codex%20CLI%20%7C%20GitHub%20Copilot-1f6feb)

Shipwright is an open-source collection of Agent Skills for product managers.
It turns AI coding assistants into practical PM copilots for PR translation, PRD generation, ideation, metrics planning, stakeholder communication, diagramming, briefings, and competitive analysis.
The project follows the [Agent Skills open standard](https://agentskills.io), so the same skill pack can run across compatible assistants.

## Why Shipwright

- Reduce PM time spent decoding technical artifacts.
- Standardize recurring outputs like PRDs, release summaries, and stakeholder updates.
- Reuse proven frameworks (RICE, HEART, AARRR, SWOT) inside the assistant workflow.
- Keep skills portable across platforms instead of tied to one vendor.

## Install

Install all skills:

```bash
curl -sSL https://raw.githubusercontent.com/cesarfrancots/Shipwright/main/install.sh | bash
```

Install only selected skills:

```bash
curl -sSL https://raw.githubusercontent.com/cesarfrancots/Shipwright/main/install.sh | bash -s -- --skills pr-translator,prd-builder,ideation-engine
```

## Skill Catalog

| Skill | Description | Slash Command |
|---|---|---|
| `pr-translator` | Turn pull requests, diffs, and commit ranges into PM-friendly summaries. | `/pr-translate` |
| `prd-builder` | Draft full PRDs with goals, stories, requirements, and metrics. | `/prd` |
| `ideation-engine` | Brainstorm and prioritize 10 ideas with RICE scoring. | `/ideate` |
| `spec-diagrams` | Convert product flows and specs into Mermaid diagrams. | `/diagram` |
| `stakeholder-comms` | Rewrite project updates for leadership, sales, support, or customers. | `/comms` |
| `metrics-definer` | Define north star metrics, guardrails, and instrumentation plans. | `/metrics` |
| `pm-briefing` | Create a PM news and market briefing from topic context. | `/pm-briefing` |
| `competitive-intel` | Compare competitors, surface market gaps, and recommend positioning. | `/competitive` |
| `obsidian-pm-planner` | Set up an Obsidian vault for PM planning, notes, and traceable documentation. | `/obsidian-plan` |
| `pdf-ops` | Generate, review, and refine PDFs with layout and quality checks. | `/pdf-ops` |

## Quick Start Workflow

```text
/pr-translate Summarize these sprint commits for product:
- feat: add shared dashboard views
- fix: stop duplicate share emails
- chore: add rollout flag and alerts
```

Then run:

```text
/comms Create one update for leadership and one for support based on that summary.
```

Expected output includes a TL;DR, categorized changes, user impact, risks, and follow-up actions tailored to each audience.

## Repository Structure

```text
skills/                  # 10 production skills
docs/                    # PRD, quickstart, platform setup
examples/                # End-to-end PM workflows
shipwright_obsidian_mcp/ # Optional local MCP server for Obsidian
install.sh               # Cross-platform symlink installer
RULES.md                 # Canonical project rules
```

## Documentation

- [Quickstart](docs/quickstart.md)
- [Platform setup](docs/platform-setup/claude-code.md)
- [Obsidian MCP](docs/integrations/obsidian-mcp.md)
- [Project rules](RULES.md)
- [Contributing](CONTRIBUTING.md)
- [License](LICENSE)

## Compatibility

- Claude Code
- OpenAI Codex CLI
- GitHub Copilot
- Cursor (open-standard compatible)
- Gemini CLI (open-standard compatible)

## Contributing

New skills are welcome.
Follow [CONTRIBUTING.md](CONTRIBUTING.md), keep `SKILL.md` frontmatter valid, and include at least one reference file plus two tests per skill.

## Built With

Built with the [Agent Skills open standard](https://agentskills.io), so PM workflows stay portable across AI assistants instead of getting trapped in a single platform.
