---
name: vault-notes
description: The note conventions for the Obsidian vault at notes/. Read before writing or editing any note there. Seven note types (session, decision, agent, paper, repo, research, topic), arXiv categories as the only tags, index lines with a summary, explicit links, flat folder, wikilinks.
---

# Vault notes

The vault is `notes/` at the root of the Agents directory. Obsidian reads it; agents write plain markdown into it. Nothing else is needed.

## Shape

Flat. No subfolders. The filename is the note title. Title Case. Seven kinds, told apart by the filename prefix and the `type` field:

| Kind | Filename | One per |
|---|---|---|
| session | `Session YYYY-MM-DD.md` | day. A second session the same day appends to the same note |
| decision | `Decision - <short title>.md` | decision |
| agent | `Agent - <folder-name>.md` | agent folder in this directory |
| paper | `Paper - <title>.md` | paper |
| repo | `Repo - <owner> <name>.md` | GitHub repository |
| research | `Research - <short title>.md` | research run or deep read |
| topic | `Topic - <Name>.md` | tag |

Every kind has an index note (`Sessions Index`, `Decisions Index`, `Agents Index`, `Papers Index`, `Repos Index`, `Research Index`, `Topics Index`), newest first. `Index.md` links them all.

## Index lines

An entry in `Papers Index`, `Repos Index` and under `Papers` or `Repos` in a topic note is one line: the link, the tags, a dash, the note's `summary`.

```markdown
- [[Paper - Reflexion]] cs/AI cs/CL cs/LG — After a failed attempt the agent writes a verbal reflection and reads it on the next try.
```

The sentence is what the research lead reads to decide whether to open the note, so it says what the work does, not that it is interesting. Other indexes stay plain links.

## Templates

Frontmatter fields are fixed. Headings are fixed. Leave a heading empty rather than drop it.

### Session

```markdown
---
type: session
date: 2026-10-11
agents: [email-triage]
---
# Session 2026-10-11

## What was worked on
Prose. What was tried, what was dropped and why. This is where the thinking lives.

## Decisions
- [[Decision - Tool results go first]]

## Open
What was left unresolved.

## Related
[[Agent - email-triage]]
```

### Decision

```markdown
---
type: decision
date: 2026-10-11
status: accepted
supersedes:
tags: [cs/AI, cs/CL]
---
# Decision - Tool results go first

## Decision
One or two sentences. What was decided.

## Why
The reasoning. Name the sources inside the sentence: [[Paper - Lost in the Middle]] shows recall drops mid-prompt.

## Rejected
What else was considered and why not.

## Related
[[Session 2026-10-11]]
[[Agent - email-triage]]
```

`status` is `accepted` or `superseded`. Decisions are never edited after the day they are written. To change one, write a new decision with `supersedes: [[Decision - Old title]]`, then set the old note's `status` to `superseded` and add `superseded by [[Decision - New title]]` under its Decision heading. Nothing else in the old note changes.

### Agent

```markdown
---
type: agent
folder: email-triage
status: building
---
# Agent - email-triage

## What it does
Same text as its row in list_of_agents.md.

## Decisions
- [[Decision - Tool results go first]]

## Related
[[Session 2026-10-11]]
```

`status` is `building`, `running` or `retired`.

### Paper

```markdown
---
type: paper
title: Reflexion
authors: Shinn et al.
year: 2023
url: https://arxiv.org/abs/2303.11366
read: 2026-10-14
depth: abstract
tags: [cs/AI, cs/CL, cs/LG]
summary: After a failed attempt the agent writes a verbal reflection and reads it on the next try.
---
# Paper - Reflexion

## What it claims
The findings, in our words.

## Why it matters to us
What it changes about how we build agents. Empty if nothing yet.

## Open questions
What the paper leaves unanswered or did not consider. One line each.

## Method
## Results
## Limitations

## Cites
- [[Paper - ReAct]]
- Plain text for a reference that has no note.

## Cited by
- [[Paper - Self-Refine]]

## Used by
- [[Decision - Tool results go first]]

## Related
[[Paper - Generative Agents]]
```

`depth` is `abstract` when only the abstract was read, `full` once a deep read has happened. `Method`, `Results` and `Limitations` are empty at abstract depth and filled by the deep read, which upgrades the note in place. `Cites` is written by the deep read only. `Cited by` is appended by whoever writes a note for a paper that a deep read cited. `Used by` is appended to by whoever writes a decision that cites the paper. `tags` are the paper's arXiv categories in slash form.

### Repo

```markdown
---
type: repo
name: owner/name
url: https://github.com/owner/name
read: 2026-10-14
tags: [cs/AI, cs/MA]
paper: [[Paper - Reflexion]]
summary: Reference implementation of Reflexion with a pluggable memory store.
---
# Repo - owner name

## What it does
From the README, in our words.

## Why it matters to us
What it changes about how we build agents. Empty if nothing yet.

## Open questions
What the README leaves unanswered. One line each.

## Used by

## Related
[[Paper - Reflexion]]
```

`paper` is the paper note the README points at, or empty. Tags come from that paper; without one, the nearest one or two categories by judgment.

### Research

One per research run or deep read. Holds everything a later session needs before deciding to search again.

```markdown
---
type: research
date: 2026-10-14
status: open
kind: run
tags: [cs/AI, cs/MA]
---
# Research - Memory across runs

## Problem
What is stuck, in our words, and what a solution has to do. For a deep read: the paper, as a link.

## Questions
The lead's question list as it now stands. One line each, marked answered, kept, dropped or new, with the reason.

## Waves
### Wave 1 - 2026-10-14
What was asked. What came back, as links: [[Paper - Lost in the Middle]].
Verdict: continue, stop or ask, and the reason.

## Repos
- [[Repo - owner name]]

## Outcome
The synthesis or the report. Empty while open.

## Related
[[Session 2026-10-14]]
```

`status` is `open` or `closed`. `kind` is `run` or `deep`. Appended to, one `### Wave` heading per wave, until closed. Papers and repos go in their own notes and are linked from the wave that found them.

### Topic

Two levels. Archive notes exist from the start and list their categories. Category notes are created on first use.

```markdown
---
type: topic
tag: cs/MA
archive: cs
---
# cs.MA - Multiagent Systems

## Papers
- [[Paper - Generative Agents]] cs/AI cs/MA — Agents store each event and retrieve by recency, importance and relevance before acting.

## Repos

## Decisions
- [[Decision - Tool results go first]]

## Research
- [[Research - Memory across runs]]

## Related
[[Topic - Computer Science]]
[[Topics Index]]
```

## Tags

A tag is an arXiv category from `arXiv Categories`, written with the first dot as a slash: `cs.MA` becomes `cs/MA`, `stat.ML` becomes `stat/ML`, `hep-th` stays `hep-th`. Nothing else is a tag. Obsidian nests slash tags under their archive on its own.

To use a category whose `Topic - <category>.md` does not exist yet: create it from the template, with the name from `arXiv Categories`, add it under `Categories` in its archive note, and add it to `Topics Index` under its archive. Only the librarian and the record fork do this.

## Links

- A link goes inside the sentence where the thing is used, so the backlink pane shows how, not just that.
- `Related` at the bottom holds the rest.
- Every note links to at least one other note.
- Link by exact title: `[[Decision - Tool results go first]]`.
- `Cites`, `Cited by` and `Used by` are written out in the text even though Obsidian would infer them, because the librarian follows them with grep.

## Filing a note

When a note is created:

1. Add it to its kind's index, at the top. Paper and repo entries use the index line form.
2. For each tag, add it to that topic note under Papers, Repos, Decisions or Research, creating the topic note first if needed. Paper and repo entries use the index line form.
3. If a decision cites a paper, add the decision under the paper's `Used by`.
4. If a decision or session touches an agent, add it to that agent note.
5. If a research wave finds a paper or repo, link its note from that wave.
6. If a paper note is written for a reference of a deep read, add the deep-read paper under its `Cited by`.

Reads in Obsidian and in a plain text editor equally. No callouts, no embeds, no plugins.
