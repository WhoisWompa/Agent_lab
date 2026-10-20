---
title: AutoDetect: Towards a Unified Framework for Automated Weakness Detection in Large Language Models
authors: Jiale Cheng et al.
date: 2024-06
arxiv: 2406.16714
url: https://arxiv.org/abs/2406.16714
venue: Findings of EMNLP 2024
category: self-evolving-tests
---
# AutoDetect: Towards a Unified Framework for Automated Weakness Detection in Large Language Models

## One line
Three LLM agents (Examiner, Questioner, Assessor) iteratively search for the weaknesses of one target LLM and turn them into targeted test questions.

## Method
Examiner builds a taxonomy of the task area; Questioner writes questions per node; the target answers; Assessor grades, analyses failures and proposes new weak points, and the Questioner generates harder or related questions. The loop runs per target model, so tests are tailored. Output-only, no execution.

## Evaluated on
Identification success rate above 30% on prominent models (ChatGPT, Claude). Fine-tuning on discovered weaknesses improved models, framed as a self-improvement loop. Code: github.com/thu-coai/AutoDetect.

## Limitations admitted by the authors
- Assessor is an LLM with no ground truth for open questions; misgrading inflates 'weakness' rates.
- Covers instruction following, math and coding; agentic settings not tested.

## Limitations found by others


## What it leaves untried
- Check the Assessor's own errors and refine grading criteria across rounds; only the question side evolves.
