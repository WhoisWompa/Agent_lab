---
title: LiveBench: A Challenging, Contamination-Limited LLM Benchmark
authors: Colin White et al.
date: 2024-06
arxiv: 2406.19314
url: https://arxiv.org/abs/2406.19314
venue: ICLR 2025
category: self-evolving-tests
---
# LiveBench: A Challenging, Contamination-Limited LLM Benchmark

## One line
A benchmark whose questions are refreshed regularly from recent sources and scored automatically against objective ground truth, avoiding LLM judges.

## Method
Questions drawn from recent math competitions, arXiv papers, news and datasets, plus harder versions of existing tasks; released and replaced over time. Scoring by ground-truth answers, no LLM-as-judge (authors argue judges err on hard questions).

## Evaluated on
Initial release: 18 tasks in 6 categories (math, coding, reasoning, language, instruction following, data analysis); top models below 70% at launch.

## Limitations admitted by the authors
- Restricting to objectively scorable tasks leaves open-ended ability unmeasured.
- Freshness reduces but does not eliminate contamination.

## Limitations found by others


## What it leaves untried
- Target the refresh at where top systems still fail rather than at recency alone.
