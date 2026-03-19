# Test: Review Release Pack PDF

## Input

`Review docs/release-pack.pdf and tell me if it is safe to send to executives.`

## Expected Behavior

- Classifies the task as `review`.
- Returns a prioritized issue list using critical/major/minor severity.
- Includes a pass/fail recommendation for sharing.
- Provides a short set of concrete revisions.
- Mentions when visual validation is partial due to missing rendering tools.
