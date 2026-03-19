# PDF Workflow Reference

## Modes

- `create`: build a new PDF from structured input.
- `review`: inspect an existing PDF for quality and correctness.
- `extract`: pull text or sections for reuse.
- `revise`: apply a targeted change set and re-check output.

## Review Checklist

1. Verify title, date, owner, and document purpose are present.
2. Check body hierarchy:
   headings, section order, and paragraph spacing.
3. Validate tables and charts:
   labels, alignment, and readability at normal zoom.
4. Confirm no clipping, overlap, or orphan lines on page breaks.
5. Check footer/page numbers consistency.
6. Confirm final filename and versioning format.

## Severity Rubric

- `critical`: wrong data, unreadable content, or broken layout.
- `major`: noticeable formatting issues that reduce confidence.
- `minor`: cosmetic improvements with no factual risk.

## Suggested Revision Log Format

```text
- [critical] Page 2: table headers overlap row 1. Fix column widths.
- [major] Page 4: section title wraps awkwardly. Increase top margin by 4px.
- [minor] Page 1: subtitle could use stronger contrast.
```
