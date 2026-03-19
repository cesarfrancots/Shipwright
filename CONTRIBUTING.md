# Contributing to PM Pilot

Thanks for contributing.
PM Pilot is a plain-files repository, so good contributions are mostly about disciplined structure and strong skill authoring.

## Development Workflow

1. Create or update a skill under `skills/`.
2. Follow the SKILL.md contract in `RULES.md`.
3. Add at least one reference file and two test files.
4. Run a manual smoke test with the target assistant.
5. Open a pull request with a Conventional Commit title.

## Adding a New Skill

Create this structure:

```text
skills/<skill-name>/
├── SKILL.md
├── references/
│   └── <reference-file>.md
└── tests/
    ├── test-basic.md
    └── test-edge-case.md
```

## SKILL.md Requirements

- `name` matches the directory name exactly.
- `description` starts with an action verb and includes three or more trigger keywords.
- `license` is `Apache-2.0`.
- `metadata` includes `author`, `version`, and `tags`.
- Body instructions stay under the context budget and use imperative voice.

## Testing Guidance

Every skill should include:

- one straightforward scenario
- one ambiguous or edge-case scenario

Test files should describe expected behavior rather than an exact output string.

## Writing Guidance

- Prefer references for long frameworks and templates.
- Avoid platform-specific assumptions in instructions.
- Ask before guessing when critical context is missing.
- Default to markdown output unless another format is explicitly useful.

## Pull Request Checklist

- [ ] Skill structure matches repository rules
- [ ] Frontmatter is valid YAML
- [ ] Description quality checklist passes
- [ ] At least one real test was run manually
- [ ] Commit title follows Conventional Commits
