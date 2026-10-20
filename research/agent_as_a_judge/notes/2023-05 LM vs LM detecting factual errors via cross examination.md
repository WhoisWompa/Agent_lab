---
title: LM vs LM: Detecting Factual Errors via Cross Examination
authors: Roi Cohen et al.
date: 2023-05
arxiv: 2305.13281
url: https://arxiv.org/abs/2305.13281
venue: EMNLP 2023
category: alternative-paradigms
---
# LM vs LM: Detecting Factual Errors via Cross Examination

## One line
An examiner LM cross-examines an examinee LM about a claim through multi-turn questions and flags the claim as false when it finds inconsistencies.

## Method
Examiner generates follow-up questions, examinee answers, examiner decides correct/incorrect from inconsistencies. No reference documents, no tools; only the two models' text.

## Evaluated on
Factual closed-book QA claims (e.g. LAMA, TriviaQA, Natural Questions, PopQA); reported to outperform baselines such as self-confidence and 'is it true?' prompting (exact F1 not re-verified this session).

## Limitations admitted by the authors
- Cannot catch errors the examinee states consistently; requires the examiner to ask good questions; multiple LLM calls.

## Limitations found by others
- Huang et al. 2023 (arXiv 2310.01798): without external feedback LLMs often fail to self-correct, which bounds what consistency-only checks can find.

## What it leaves untried
- Cross-examining an agent about its trajectory (why it took an action) as an evaluation signal.
