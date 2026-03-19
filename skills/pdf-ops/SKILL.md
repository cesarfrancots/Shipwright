---
name: pdf-ops
description: >
  Generate, inspect, and refine PDF deliverables for product work.
  Use when someone says PDF report, export doc, render check, layout review, extraction, or printable brief.
  Produce validated PDF artifacts plus a concise quality checklist and revision notes.
license: Apache-2.0
metadata:
  author: shipwright
  version: "1.0.0"
  tags: [pdf, documentation, reporting, quality-assurance, product-management]
---

# PDF Ops

## When to Use This Skill

Use this skill when a PM needs to create, inspect, or improve a PDF.
Run it for product briefs, release reports, stakeholder packs, or any PDF export that must be readable and visually clean.

Read `references/pdf-workflow.md` before generating output.

## Capabilities

- Create structured PDFs from markdown or provided content.
- Extract text from existing PDFs for summarization or comparison.
- Validate rendering quality page-by-page before sharing.
- Return a revision log with concrete fixes when issues are found.

## Instructions

1. Confirm the task type:
   create, review, extract, or revise.
2. Confirm required output:
   destination filename, audience, page style, and language.
3. If creating a PDF, build the content outline first, then generate.
4. If reviewing, inspect both text content and rendered layout.
5. Report issues with severity:
   critical (must fix), major (should fix), minor (nice to fix).
6. Always include a quality checklist:
   headers, spacing, page breaks, tables, and legibility.
7. If local dependencies are missing, degrade gracefully:
   state what is missing and provide install commands.
8. Keep all file paths explicit and avoid assumptions about platform-specific tools.

## Dependency Guidance

Preferred Python packages:

```bash
python -m pip install reportlab pdfplumber pypdf
```

Optional renderer for visual checks:

```bash
pdftoppm -png INPUT.pdf page
```

If `pdftoppm` is unavailable, continue with text and metadata checks and call out that visual validation is partial.

## Output Format

### Task Summary

- Mode: create | review | extract | revise
- Input files:
- Output files:

### Result

- What was produced or analyzed
- Key findings

### Quality Checklist

- Typography and spacing
- Page flow and breaks
- Tables/charts readability
- File integrity

### Next Actions

- Required fixes
- Optional improvements

## Example Input

`Review this release summary PDF and list layout defects before I send it to leadership.`

## Example Output

A prioritized PDF review with detected defects, suggested fixes, and a clear share/no-share recommendation.
