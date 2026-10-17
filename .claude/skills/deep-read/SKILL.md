---
name: deep-read
description: Read one paper in full and what it rests on. Use when the user says "go deeper on <paper>", "deep read <paper>", or "/deep-read <paper>". Launches the deep-read workflow and relays only its report, so the main session stays clean.
---

# Deep read

The deep-read team is the `deep-read-run` workflow in `.claude/workflows/deep-read.js`, led by the deep reader. This skill is the main session's only contact with it: hand over the paper, read back the report.

## Steps

1. Find the paper note. Glob `notes/Paper - *<words from the user>*.md`. If none matches, the paper has not been read at abstract depth yet; say so and stop. A research run brings papers in; a deep read only deepens one that is there. If several match, ask which.
2. Call `Workflow` with `scriptPath` set to the absolute path of `.claude/workflows/deep-read.js` in this repo, and `args: {paper, date}`, `paper` being the note path and `date` today as `YYYY-MM-DD`. The user asked for this run, so it is opted in.
3. The run is in the background. Wait for its notification. Do not read the vault or the run's journal while it runs.
4. On the result: give the user the report as it is, the research note title, and the reference counts: found in the vault, read now, not found on arXiv. That is the deliverable.

## What stays out of the main session

The full text, the reference list, the abstracts, the notes. The run writes all of it into the vault. If the user wants more than the report, point them to the paper note, now at depth full, and the research note.

## Rules

- One paper per run. Going a level deeper is a second run on one of the references.
- The paper note must exist before the run starts.
