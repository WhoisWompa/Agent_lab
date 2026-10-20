---
title: Many SWE-bench-Passing PRs Would Not Be Merged into Main
authors: METR
date: 2026-03
arxiv: none
url: https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/
venue: METR note
category: agent-evaluation-benchmarks
---
# Many SWE-bench-Passing PRs Would Not Be Merged into Main

## One line
Maintainers of SWE-bench Verified repos review test-passing agent PRs; about half would not be merged.

## Method
4 active maintainers of scikit-learn, Sphinx and pytest reviewed 296 AI PRs that pass the grader, plus 47 real merged human PRs as a noise control, blind to authorship.

## Evaluated on
Merge rate about 24 pp (24.2) below SWE-bench score on average, statistically significant, after noise adjustment.

## Limitations admitted by the authors
- Agents got no chance to iterate on review feedback, so this is not claimed as a capability ceiling.
- Three repos, four reviewers.

## Limitations found by others


## What it leaves untried
- Using maintainer-style review as an automated (LLM-agent) judge and validating it against these labels.
