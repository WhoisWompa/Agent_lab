---
title: Agreement Without Alignment: Label-Free Rubric Clarification Increases LLM-Judge Consensus but Not Agreement with Humans
authors: Sangdo Han, Moonsoo Kim
date: 2026-10
arxiv: 2610.13303
url: https://arxiv.org/abs/2610.13303
venue: arXiv
category: self-evolving-tests
topics: ["LLM and agent judges", "self-evolving tests"]
---
# Agreement Without Alignment: Label-Free Rubric Clarification Increases LLM-Judge Consensus but Not Agreement with Humans

## One line
Preregistered test of label-free rubric repair: rewriting the rubric clauses LLM judges disagree on most raises judge-judge consensus but not agreement with humans.

## Method
Rubrics split into sub-criteria; the most contested (highest inter-judge disagreement on a dev split) are rewritten by an editor model; compared with editing random clauses. A stage moving text-checkable criteria to deterministic checkers was also tried. Five-judge panel from three providers; humans used only for assessment.

## Evaluated on
SummEval: judge-judge Krippendorff alpha +0.069 (95% CI 0.046-0.092) over the original rubric, +0.074 over random-edit control; human agreement change Kendall tau -0.007 (CI -0.037 to 0.021). HealthBench meta-eval and USR Topical-Chat: preregistered criteria not met. Human agreement lower after contested-clause edits than control on all three datasets (CIs include zero). 129,770 judge requests.

## Limitations admitted by the authors
- Deterministic-checker stage produced no transfer.
- Three datasets: summarisation, dialogue, health.

## Limitations found by others


## What it leaves untried
- Combine disagreement-driven selection with a small human-labelled anchor set to separate consensus gains from alignment gains.

## Topics
[[Topic - LLM and agent judges]] · [[Topic - self-evolving tests]]
