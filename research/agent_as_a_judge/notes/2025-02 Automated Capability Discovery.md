---
title: Automated Capability Discovery via Foundation Model Self-Exploration
authors: Cong Lu, Shengran Hu, Jeff Clune
date: 2025-02
arxiv: 2502.07577
url: https://arxiv.org/abs/2502.07577
venue: arXiv
category: self-evolving-tests
---
# Automated Capability Discovery via Foundation Model Self-Exploration

## One line
A 'scientist' foundation model open-endedly proposes new tasks to probe a subject model, keeping an archive of interestingly-new tasks, to discover capabilities and failures.

## Method
Open-endedness loop (OMNI-EPIC lineage): the scientist proposes a task family with instructions and a scoring method (code check or LLM judge), checks novelty against the archive, the subject attempts it, results are stored. Tasks are clustered afterward into capability and failure areas. Subject may be the same model as the scientist.

## Evaluated on
Thousands of tasks per run, clustered into dozens of capability/failure areas, on GPT, Claude and Llama families. Human surveys showed high agreement with model-generated scores.

## Limitations admitted by the authors
- Auto-scored tasks can be wrong; humans checked only a sample.
- Interestingness is judged by the same kind of model, which shapes what is explored.

## Limitations found by others


## What it leaves untried
- Close the loop: use human-disagreement cases to recalibrate the scorer.
- Point it at an agent with tools rather than a chat model.
