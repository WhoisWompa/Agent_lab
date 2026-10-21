---
title: Why we no longer evaluate SWE-bench Verified
authors: OpenAI (Frontier Evals)
date: 2026-02
arxiv: none
url: https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
venue: OpenAI blog
category: agent-evaluation-benchmarks
topics: ["agent evaluation benchmarks"]
---
# Why we no longer evaluate SWE-bench Verified

## One line
OpenAI retires SWE-bench Verified as a frontier metric because of flawed tests and training-data contamination.

## Method
Audit of 138 hard / commonly failed tasks by reviewers; contamination probe by asking frontier models to reproduce gold fixes.

## Evaluated on
59.4% of 138 audited tasks had material issues in test design or problem description (a secondary write-up says 'more than 60% unsolvable as written'). GPT-5.2, Claude Opus 4.5 and Gemini 3 Flash Preview reproduced some original fixes from memory. Recommended SWE-bench Pro instead.

## Limitations admitted by the authors
- Audit targeted the hardest tasks, so the 59.4% is not a rate for all 500 tasks.

## Limitations found by others
- Per a secondary source (codex.danielvaughan.com, 2026-07-31), OpenAI's 2026-07-08 post 'Separating signal from noise in coding evaluations' audited 731 public SWE-bench Pro tasks, flagged ~27-34% as broken and withdrew the Pro recommendation. Not verified against the primary post.
- A Datacurve audit (May 2026, secondary report) claimed Pro graders mis-graded about a third of trials. Unverified.

## What it leaves untried
- No replacement verifier design is proposed; the problem is relocated to the next benchmark.

## Topics
[[Topic - agent evaluation benchmarks]]
