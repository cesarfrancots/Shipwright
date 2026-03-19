# Workflow Example: Sprint Review

## Goal

Turn merged engineering work into a PM-ready review plus tailored updates.

## Flow

1. Run `pr-translator` on merged PRs or a sprint commit range.
2. Review the categorized summary and risks.
3. Feed the result into `stakeholder-comms` for leadership and support variants.

## Sample Prompt

```text
Use pr-translator to summarize these sprint commits for a PM, then create one leadership update and one support update from the output.
```

## Output Artifacts

- sprint summary
- release risk list
- leadership update
- support-ready talking points
