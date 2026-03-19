# Test: complex commit range

## Input

Use the `pr-translator` skill.

Summarize the following commit range for a sprint review:

- `feat: launch usage alerts for enterprise admins`
- `fix: stop duplicate Slack alerts on retry`
- `perf: batch usage event aggregation to reduce dashboard latency`
- `refactor: split billing alert service into notifier and scheduler modules`
- `chore: add Terraform outputs for alerting queue and new CloudWatch alarms`

## Expected Behavior

- [ ] Output treats the input as a commit range rather than a single PR.
- [ ] Output groups related work into product themes.
- [ ] Output classifies changes into all applicable categories.
- [ ] Risks mention rollout, monitoring, or unclear areas when appropriate.
