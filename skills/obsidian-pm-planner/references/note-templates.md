# Shipwright Note Templates

Use these as the canonical Shipwright templates when the MCP server is unavailable or when templates need to be reviewed by a human.

## Common Frontmatter

Every note should include:

```yaml
type: ""
status: ""
owner: ""
created: YYYY-MM-DD
updated: YYYY-MM-DD
initiative: ""
prd: ""
sprint: ""
tags: []
```

## Template Keys

- `initiative`
- `prd`
- `adr`
- `research-note`
- `sprint-plan`
- `release-note`
- `metrics-plan`
- `stakeholder-update`
- `daily-log`

## Additional Metadata by Template

- `initiative`: `success_metric`, `target_date`
- `prd`: `stage`, `mvp_scope`, `future_phases`
- `adr`: `decision_date`, `supersedes`
- `research-note`: `source_type`, `confidence`
- `sprint-plan`: `sprint_id`, `start`, `end`
- `release-note`: `release_date`, `version`
- `metrics-plan`: `north_star`, `guardrails`
- `stakeholder-update`: `audience`, `period`
- `daily-log`: `date`

## Core Sections

### Initiative

- Outcome
- Success Metrics
- Linked PRD
- Linked Decisions
- Metrics Plan
- Current Risks
- Sprint Notes
- Release Notes

### PRD

- Problem
- Goals
- Non-Goals
- MVP Scope
- Future Phases
- Acceptance Criteria
- Related Initiative
- Linked Decisions
- Metrics Plan
- Release Notes

### ADR

- Context
- Decision
- Consequences
- Related Initiative
- Related PRD

### Sprint Plan

- Goals
- Planned Scope
- Linked Initiatives
- Current Risks
- Mid-Sprint Update
- End-of-Sprint Outcome

### Release Note

- Summary
- Customer Impact
- Shipped PRDs
- Stakeholder Update
- Follow-up Monitoring
