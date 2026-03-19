# Test: basic PR summary

## Input

Use the `pr-translator` skill.

Summarize this pull request for a PM:

- Added a new onboarding checklist shown after workspace creation.
- Fixed a bug where invited users sometimes landed on a blank page after accepting the invite.
- Moved analytics dispatch into a background worker and updated the worker deployment manifest.

## Expected Behavior

- [ ] Output starts with a TL;DR line.
- [ ] Output includes `What Changed`, `User Impact`, `Risks`, and `Follow-Up Actions`.
- [ ] Changes are classified into categories from the reference file.
- [ ] The summary uses product language rather than code jargon.
