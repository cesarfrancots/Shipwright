# Improvement Log

## Scope of this review

This review focused on two things:

1. Smoke-testing the eight skills against their current prompts, references, and expected output shapes.
2. Auditing repository quality around installation, documentation, and maintainability.

The skill checks were manual functional reviews based on the current `SKILL.md` instructions and test prompts in `skills/*/tests/`.
They are useful as a first-pass product audit, but they are not a substitute for running the skills in Claude Code, Codex CLI, and GitHub Copilot end to end.

## Smoke Test Summary

| Skill | Status | Assessment |
|---|---|---|
| `pr-translator` | Functional | Clear output contract, good graceful degradation, solid categorization model. |
| `prd-builder` | Functional | Good default template and question flow, but still broad enough to benefit from sharper scoping guidance. |
| `ideation-engine` | Functional | Strong core flow and RICE framing; deep-dive path is useful and coherent. |
| `spec-diagrams` | Functional | Good for Mermaid generation, but would benefit from more concrete syntax examples and revision patterns. |
| `stakeholder-comms` | Functional | Clear audience adaptation logic and useful multi-audience behavior. |
| `metrics-definer` | Functional | Good framework selection and instrumentation structure; needs more metric specificity examples. |
| `pm-briefing` | Partially functional | Usable, but real value depends on browsing being available; offline fallback is present but generic. |
| `competitive-intel` | Partially functional | Good structure, but strong output quality will depend heavily on live research access. |

## Per-Skill Notes

### pr-translator

What works:

- The skill has a clear output structure.
- The categories are well-defined in `references/change-categories.md`.
- It handles single PRs and commit ranges explicitly.

Things to polish:

- Add one example for a commit-range summary, not only a single-PR example.
- Add clearer guidance for how to summarize very large diffs without becoming verbose.
- Add a JSON output variant for teams that want to pipe results into release automation.

### prd-builder

What works:

- Strong default template.
- Good clarifying question behavior.
- Good acceptance-criteria requirement.

Things to polish:

- Add guidance for when to stop asking questions and draft with assumptions.
- Add one compact example output snippet so the desired tone is easier to infer.
- Add explicit distinction between MVP requirements and future-phase requirements.

### ideation-engine

What works:

- The mode system is coherent.
- The deep-dive follow-up is useful and well scoped.
- RICE is baked into the core flow instead of treated as optional.

Things to polish:

- Add one worked scoring example to make the intended level of estimate precision clearer.
- Add a tie-break rule when ideas have similar RICE scores.
- Add a recommendation on how to collapse duplicate ideas during divergent brainstorming.

### spec-diagrams

What works:

- Clear focus on Mermaid output.
- Good default behavior for ambiguity handling.

Things to polish:

- Add at least one example for each of the most common diagram types.
- Add explicit syntax constraints to reduce invalid Mermaid output.
- Add guidance for how to revise an existing diagram while preserving node names.

### stakeholder-comms

What works:

- Strong audience framing.
- Multi-audience use case is already covered by tests.

Things to polish:

- Add output variants for email, Slack update, and release note format.
- Add guidance for preserving dates, numbers, and risk wording exactly.
- Add one customer-facing example to keep tone consistent.

### metrics-definer

What works:

- Good framework references.
- Useful instrumentation plan structure.

Things to polish:

- Add one worked example with realistic baselines and targets.
- Add guidance on how to avoid vanity metrics.
- Add stronger event naming conventions for analytics consistency.

### pm-briefing

What works:

- Correctly degrades when browsing is unavailable.
- Good scope framing.

Things to polish:

- Add a stronger offline mode with competitor and trend synthesis heuristics.
- Add source quality labels beyond `live research | contextual only`.
- Add a section for "Implications for our roadmap" to make the output more PM-native.

### competitive-intel

What works:

- Good quick vs deep split.
- SWOT framing is useful for PM workflows.

Things to polish:

- Add a standard comparison matrix schema so outputs are more consistent.
- Add guidance to separate fact, inference, and recommendation.
- Add a lightweight offline mode for when no browsing is available.

## Cross-Cutting Findings

### High Priority

1. Add real execution-based validation.
   Current tests are prompt specs, not runnable validation.
   The repo needs a simple smoke-test harness or documented workflow that actually runs the skills through at least one supported assistant.

2. Fix repository branding drift.
   The GitHub repository is `Shipwright`, while the product and directory naming are still `PM Pilot` and `pm-pilot`.
   That mismatch is manageable internally but weakens discoverability and creates documentation confusion.

3. Improve installation robustness for GitHub Copilot.
   `install.sh` detects Copilot via a `copilot` binary, which is not a reliable universal signal.
   Copilot is often editor-scoped, not CLI-scoped.

### Medium Priority

1. Add `.gitattributes`.
   Without line-ending normalization, shell scripts and markdown files may drift to CRLF on Windows clones.

2. Align all docs to the current repo URL.
   This review found outdated placeholder install URLs in `docs/quickstart.md`.

3. Expand examples.
   The repo has workflow examples, but not full example outputs.
   Adding realistic output snapshots would make quality expectations much clearer.

4. Add CI for structural validation.
   At minimum:
   frontmatter validation, required file checks, placeholder URL detection, and basic shell-script linting.

### Lower Priority

1. Add machine-readable output modes for selected skills.
   `pr-translator`, `metrics-definer`, and `competitive-intel` would benefit most.

2. Add a formal versioning and release process.
   The skills include metadata versions, but the repo has no release notes or compatibility matrix per release.

3. Add community skill scaffolding.
   The contribution guide mentions structure, but there is no reusable template generator yet.

## Immediate Next Steps

1. Build a validation workflow that runs one smoke prompt per skill on at least Claude Code and Codex CLI.
2. Decide whether the product name is `PM Pilot` or `Shipwright`, then align README, docs, installer URLs, and folder naming.
3. Strengthen `install.sh` for Copilot and document workspace-targeted installation more explicitly.
4. Add CI checks for frontmatter, repo structure, placeholder strings, and line endings.
5. Add one real example output per Phase 1 skill.

## Changes made during this review

- Corrected install URLs in `docs/quickstart.md`.
- Added `.gitattributes` to reduce line-ending issues across platforms.
