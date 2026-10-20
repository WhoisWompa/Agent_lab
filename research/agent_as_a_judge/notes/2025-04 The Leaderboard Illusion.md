---
title: The Leaderboard Illusion
authors: Shivalika Singh et al.
date: 2025-04
arxiv: 2504.20879
url: https://arxiv.org/abs/2504.20879
venue: arXiv (revised 2025-05)
category: alternative-paradigms
---
# The Leaderboard Illusion

## One line
Audit of Chatbot Arena showing that private testing, selective score disclosure, unequal sampling and deprecations distort rankings toward a few proprietary providers.

## Method
Analysis of Arena data (battles, model releases, deprecations), simulation of best-of-N private-variant selection, and fine-tuning experiments on Arena-like data.

## Evaluated on
Meta tested 27 private variants before Llama-4. Google and OpenAI received an estimated 19.2% and 20.4% of all Arena data; 83 open-weight models together 29.7%. Limited extra Arena data yields up to 112% relative gain on the Arena distribution (conservative estimate). Proprietary models are deprecated less often (from abstract).

## Limitations admitted by the authors
- Depends on data that Arena and providers partially disclose; some estimates are reconstructions.
- Estimates are conservative and rely on reconstructed sampling data.

## Limitations found by others
- LMArena published a public rebuttal on its blog disputing several claims (not fetched in this session).

## What it leaves untried
- Same audit for agent leaderboards (SWE-bench, WebArena) where submitters can also select runs.
