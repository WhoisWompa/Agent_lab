---
title: Debating with More Persuasive LLMs Leads to More Truthful Answers
authors: Akbir Khan et al.
date: 2024-02
arxiv: 2402.06782
url: https://arxiv.org/abs/2402.06782
venue: ICML 2024 (best paper)
category: alternative-paradigms
---
# Debating with More Persuasive LLMs Leads to More Truthful Answers

## One line
Shows that on information-asymmetric reading comprehension, non-expert judges (LLMs and humans) pick the correct answer more often when two expert LLMs debate, and that more persuasive debaters raise judge accuracy.

## Method
QuALITY long-story QA; debaters see the story, judge does not. Two debaters argue for two candidate answers over several rounds; quotes are checked against the text (verified quotes). Compared to consultancy (one model argues an assigned side) and a naive judge baseline. Debater persuasiveness is raised by inference-time optimisation (best-of-N, critique-and-refine) and measured by Elo. Judge sees only the transcript.

## Evaluated on
Judge accuracy: LLM judges 76% with debate vs 48% naive baseline; human judges 88% with debate vs 60% baseline (from abstract). Higher debater persuasiveness (Elo) correlated with higher judge accuracy in debate but not in consultancy.

## Limitations admitted by the authors
- Only one task family (reading comprehension) where the weak/strong gap is information, not reasoning ability.
- Verified quotes give the judge a ground-truth channel unavailable in many real oversight settings.
- Persuasiveness optimised only at inference time, not by training.
- Information-asymmetry reading task; debaters assigned sides.

## Limitations found by others
- Kenton et al. 2024 (arXiv 2407.04622): with no information asymmetry (math, logic, code), debate vs direct QA is mixed.
- Recchia et al. 2025 (arXiv 2507.19486): reanalysis suggests earlier positive results partly came from evaluators' outside knowledge, an advantage that shrinks as models get stronger.
- A 2025 benchmark paper (arXiv 2504.03731) argues plain judge accuracy is the wrong metric and that earlier debate-vs-consultancy baselines were flawed.

## What it leaves untried
- Debaters with tool access and a judge that can verify claims by execution.
- Applying the protocol to judging long agent trajectories, where the 'hidden text' is the trajectory.
