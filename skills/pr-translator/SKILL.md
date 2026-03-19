---
name: pr-translator
description: >
  Translate pull requests, diffs, and commit ranges into a structured product-facing summary.
  Use when someone says summarize this PR, explain this diff, what shipped, release notes, commit range, or changelog.
  Produce a TL;DR, categorized changes, user impact, risks, and follow-up actions for product and stakeholder review.
license: Apache-2.0
metadata:
  author: pm-pilot
  version: "1.0.0"
  tags: [product-management, release-notes, pull-requests, changelog, stakeholder-updates]
---

# PR Translator

## When to Use This Skill

Use this skill when the user provides a pull request diff, patch, commit range, or a list of commits and wants a business-readable summary.

If no diff, patch, PR description, or commit list is provided, ask the user: "Please paste the PR diff, patch, commit range, or the merged commit list you want summarized."

Read `references/change-categories.md` before classifying changes.

## Instructions

1. Identify the source material.
   Accept one PR, multiple PRs, a commit range, or an ad hoc diff.
2. Extract the functional units of change.
   Group related file edits into a single product change when they support the same outcome.
3. Classify each unit into one primary category:
   `user-facing features`, `bug fixes`, `performance`, `refactors`, or `infrastructure`.
4. Prefer user impact over implementation detail.
   Translate code activity into behavior, workflow, reliability, cost, or delivery impact.
5. Call out uncertainty explicitly.
   If a change may be risky but the diff is incomplete, label it as an inference.
6. Note operational signals.
   Highlight migrations, config changes, auth changes, billing changes, integrations, analytics changes, or rollout flags.
7. Support both narrow and aggregate summaries.
   For a single PR, keep categories compact.
   For a commit range, summarize by major theme first, then by category.
8. Avoid hallucinating intent.
   If the purpose of a change is unclear, write what the diff shows and what should be verified.
9. For large diffs, compress repeated implementation details.
   Summarize by theme first, cap each category at the highest-signal changes, and prioritize behavior, user impact, and operational changes over mechanical file churn.

## Output Format

Use markdown and follow this structure exactly unless the user requests another format:

If the user requests JSON, return valid JSON only with the same information organized under keys for `tldr`, `scope`, `what_changed`, `user_impact`, `risks`, and `follow_up_actions`.
Keep markdown as the default output format.

### TL;DR

Write one sentence that captures the most important outcome.

### Scope

- Source: single PR | multiple PRs | commit range
- Confidence: high | medium | low
- Primary themes: comma-separated list

### What Changed

For each category that applies:

#### <Category Name>

- Change: plain-language statement of what changed
- Evidence: key files, modules, or commit themes
- Why it matters: product or operational impact

### User Impact

- Who is affected
- What changes in behavior, reliability, speed, or workflow
- Whether the change is visible immediately, behind a flag, or internal only

### Risks

- Risk: concise statement
- Severity: low | medium | high
- Reason: why the risk exists
- Validation needed: monitoring, QA, migration check, rollout guard, or stakeholder confirmation

### Follow-Up Actions

- Recommended PM or release action
- Recommended engineering or QA action
- Recommended communication action

## Examples

### Example Input

`Summarize this PR for product: adds invoice reminders, fixes duplicate sends, and updates the background worker deployment.`

### Example Output

#### TL;DR

Invoice reminders are now more reliable for customers, with a deployment update that supports the rollout.

#### Scope

- Source: single PR
- Confidence: medium
- Primary themes: billing reminders, notification reliability, worker deployment

#### What Changed

##### User-Facing Features

- Change: Added scheduled invoice reminder emails for overdue invoices.
- Evidence: reminder scheduler and billing notification templates.
- Why it matters: gives finance teams an automated way to reduce missed collections.

##### Bug Fixes

- Change: Prevented duplicate reminder sends when retry jobs overlap.
- Evidence: retry guard and send de-duplication logic.
- Why it matters: reduces customer confusion and support load.

##### Infrastructure

- Change: Updated worker deployment settings for the reminder job.
- Evidence: background job configuration and deployment manifests.
- Why it matters: supports stable processing in production.

#### User Impact

- Finance and operations users receive a new reminder workflow.
- Customers should see fewer duplicate reminder emails.
- The deployment change is internal but affects reliability.

#### Risks

- Risk: Reminder timing may differ from the intended billing policy.
- Severity: medium
- Reason: schedule logic changed and policy details are not visible in the diff.
- Validation needed: confirm timing rules with billing stakeholders and monitor send volumes after rollout.

#### Follow-Up Actions

- Add the feature to release notes.
- Verify reminder timing in staging with realistic invoice states.
- Notify support in case customers ask about reminder frequency.

### Example Input

`Summarize this commit range for a release note: feat: add workspace audit exports; fix: prevent duplicate exports on retry; chore: add queue metrics and alerts.`

### Example Output

#### TL;DR

Audit exports are now available, retries are safer, and the rollout gained the monitoring needed to support the change.

#### Scope

- Source: commit range
- Confidence: medium
- Primary themes: audit exports, retry safety, queue observability

#### What Changed

##### User-Facing Features

- Change: Added workspace audit exports for admins.
- Evidence: export workflow and related UI or API changes.
- Why it matters: gives admins a new way to retrieve audit data.

##### Bug Fixes

- Change: Prevented duplicate exports when retry logic runs more than once.
- Evidence: retry guard and deduplication checks.
- Why it matters: reduces duplicate work and confusing output.

##### Infrastructure

- Change: Added queue metrics and alerts to support the export rollout.
- Evidence: monitoring and alerting configuration.
- Why it matters: makes the release easier to operate and validate.

#### User Impact

- Admin users can export audit data.
- Retry behavior is more reliable.
- The monitoring changes are internal but improve rollout confidence.

#### Risks

- Risk: Export volume may be higher than expected after launch.
- Severity: medium
- Reason: the change introduces a new admin workflow that could be used heavily.
- Validation needed: monitor queue depth, failure rates, and export latency after rollout.

#### Follow-Up Actions

- Add the export capability to release notes.
- Confirm alert thresholds after the first production rollout.
- Share rollout guidance with support and operations.
