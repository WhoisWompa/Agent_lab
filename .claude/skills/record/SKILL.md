---
name: record
description: Record this session into the vault at notes/. Run at the end of a session, or when the user says "record", "note this down", or "save the decisions". Spawns a fork that writes the session note, one decision note per decision made, and updates agent, topic and index notes.
---

# Record

The documentation agent. It is a fork of the current session so it has seen the actual reasoning, not a summary of it.

## Steps

1. Launch `Agent` with `subagent_type: "fork"` and the brief below, verbatim, with today's date filled in.
2. Relay its report to the user: which notes were written or changed.

## The brief

```
Record this session into the vault at notes/.

Rules:
1. You write only inside notes/. Nothing else in the repo changes.
2. You never open any .env.
3. Every note follows .claude/skills/vault-notes/SKILL.md. Read it first.

Do:
- Read Decisions Index and Sessions Index so you do not record a decision twice.
- Write or append Session <today>.md: what was worked on, in prose, including what was tried and dropped, and the ideas raised that were not settled, with the reasoning as it stood. Nothing has to be settled to be recorded. The reasoning is the point; keep it.
- Write one Decision note per decision settled in this conversation that is not already in the vault. A decision is a choice between alternatives that will shape later work. Not a task done, not a bug fixed. If a decision replaces one already in the vault, supersede it per the rules.
- Write or update Agent notes for each agent folder touched.
- Write or append a Research note for each research run started or continued in this conversation, one Wave heading per wave, and a Paper note for each paper the run touched.
- File every note: indexes, topic notes, Used by sections, as the rules say.
- Tags are arXiv categories in slash form, from notes/arXiv Categories.md, nothing else. If a category's topic note does not exist yet, create it per the vault rules. A decision about the project's own tooling that fits no category carries no tags; say so in your report.

Report: a list of notes written and notes changed, one line each. Nothing else.
```
