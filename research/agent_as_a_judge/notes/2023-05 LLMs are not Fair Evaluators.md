---
title: Large Language Models are not Fair Evaluators
authors: Peiyi Wang et al.
date: 2023-05
arxiv: 2305.17926
url: https://arxiv.org/abs/2305.17926
venue: ACL 2024
category: llm-judge-foundations
---
# Large Language Models are not Fair Evaluators

## One line
Shows that simply swapping answer order can flip GPT-4/ChatGPT verdicts and proposes multiple-evidence, balanced-position and human-in-the-loop calibration.

## Method
Pairwise scoring by GPT-4/ChatGPT on the Vicuna benchmark. Fixes: Multiple Evidence Calibration (explain before scoring, sample several), Balanced Position Calibration (average over both orders), Human-in-the-Loop Calibration (balanced position diversity entropy picks hard items for humans).

## Evaluated on
Vicuna Benchmark 80 questions with human win/tie/lose labels. With ChatGPT as evaluator, Vicuna-13B 'beats' ChatGPT on 66/80 queries just by order manipulation. Calibration brings judge closer to human labels.

## Limitations admitted by the authors
- Small benchmark (80 questions) and two candidate models.
- Human-in-the-loop step reintroduces annotation cost.

## Limitations found by others
- Shi et al. 2024 (2406.07791): position bias is not random, varies by judge and task, and grows when the quality gap between answers is small, so averaging over orders turns hard items into ties rather than correct verdicts.

## What it leaves untried
- Testing calibration on tasks with objective ground truth rather than human preference.
