# Test: explicit JSON output

## Input

Use the `pr-translator` skill.

Summarize this pull request as JSON for a release note:

- Added a new onboarding checklist shown after workspace creation.
- Fixed a bug where invited users sometimes landed on a blank page after accepting the invite.

## Expected Behavior

- [ ] Output is valid JSON only.
- [ ] Output preserves the same information as the markdown format.
- [ ] Output still reflects the default markdown behavior unless JSON is explicitly requested.
