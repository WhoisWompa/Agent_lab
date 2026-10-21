---
title: "Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning"
authors: Ahsan Bilal et al.
date: 2026-08
arxiv: 2608.05643
url: https://arxiv.org/abs/2608.05643
venue: arXiv
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2608.05643.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops", "reasoning prompting"]
---
# Refining Over Resampling: Test-Time Self-Correction for LLM Reasoning

## One line
Spends test-time compute on N independent reasoning rollouts, each repaired by D rounds of self-critique and self-correction, then majority-votes the refined answers, with no verifier and no training.

## Method
The paper attacks two weaknesses of width-only test-time scaling (sample many, vote or rerank).
- Diversity saturation: more samples keep landing in the same few semantic clusters. On AIME-24 the number of distinct reasoning clusters only grows from about 1.2 at N=2 to about 2.5 at N=32.
- A per-trace accuracy floor: if a model's intended answer is right with probability λ and a random perturbation (rate h) corrupts it, expected single-trace accuracy is below λ. Every i.i.d. rollout shares this perturbation, so adding rollouts does not remove it. The argument rests on a simple model of hallucination borrowed from earlier work, and the paper does not test it directly.

The remedy uses one base model in three prompted roles: generator, critic, corrector. Each of N rollouts goes through D cycles. The generator continues the trace, the critic names logical or arithmetic errors (or confirms the trace), and the corrector rewrites it. The N terminal answers are plurality-voted. Breadth is meant to keep distinct starting directions. Depth is meant to repair local errors before the vote. Voting absorbs noisy corrections, so no reward model is needed. The authors present this as an alternative to verifier-based selection, whose quality depends on reward-model calibration, and to trained correctors (SCoRe, ReVISE), which need extra training.

## Evaluated on
Five math benchmarks (AIME24, AIME25, AMC, OlympiadBench, MATH500), four open-weight models (1.5B to 8B), N=8, D=4.
- Beats the strongest equal-sample baseline (RM@8, a 32B reward model) in most cells. Qwen2.5-1.5B on MATH500 goes from 29.6% to 58.0%, and on AMC from 25.0% to 32.5%. Ministral-8B on AMC goes from 30.0% to 42.5%.
- Gains shrink for the strongest model. Qwen2.5-Math-7B beats RM@8 by 2.36 average points, which the authors read as the baselines already recovering part of the headroom. On AIME24 the method only ties or trails RM@8 for that model (10.0 vs 13.33).
- The critic stage matters: removing it drops Qwen2.5-1.5B from 32.5% to 27.5% on AMC and from 58.0% to 55.6% on MATH500. This shows the gain is not only extra tokens, though the test is on two models.
- Refinement keeps rollouts distinct. Terminal diversity is 0.97, 0.95, 0.97 and 0.80 across the four models, so it does not collapse the vote.
- Individual corrections are noisy. Per-rollout net benefit is negative at some depths, and voting suppresses the isolated regressions. The authors argue this is why the vote is needed.
- Compute-normalized gain is positive everywhere, largest for Qwen2.5-1.5B (average 13.21% to 25.67% over Maj@8).
- Breadth and depth do not trade off monotonically on AMC23. Several moderate settings tie at 32.5% for Qwen2.5-1.5B, and Ministral-8B ranges from 35.0% to 45.0% across settings.

## Limitations admitted by the authors
- Higher inference cost: every rollout runs generate, critique and correct each round, so there are more forward passes than greedy, majority vote or best-of-N. The main comparison fixes sample count, not TFLOPs. It is not an equal-compute comparison against a majority vote scaled to the same budget.
- It depends on the base model critiquing itself: a wrong critique or over-correction of a valid solution causes rollout-level regressions, and voting only reduces their effect.
- Only math with well-defined, easily extracted answers was tested. Open-ended or ambiguous tasks, where the critique signal is weaker, are untested.

## Limitations found by others

## What it leaves untried
- A true equal-FLOP comparison against majority voting or best-of-N with a larger N. Without it, the headline claim that refining beats resampling is not separated from "more compute helps".
- Stopping refinement early per rollout or per question. The paper fixes D=4, yet its own data show accuracy is non-monotonic in D and corrections can be harmful.
- Any domain without a checkable final answer, such as code or open-ended text. The voting step has no equivalent there.

## Topics
[[Topic - self-refinement and critique loops]] · [[Topic - reasoning prompting]]
