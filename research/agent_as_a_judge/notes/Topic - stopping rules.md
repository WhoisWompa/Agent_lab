---
type: topic
group: Judging and evaluation
---
# Topic - stopping rules

When to stop sampling, testing or evaluating: sequential tests (SPRT, group sequential), adaptive testing, Bayesian optimal stopping, sample-size reduction with valid error control. A confidence gate that routes cases to a bigger model is not a stopping rule unless framed as sequential testing.

Group: Judging and evaluation. See [[Topics]]. Same group: [[Topic - LLM and agent judges]], [[Topic - judge and decision-model audits]], [[Topic - trained judges and reward models]], [[Topic - agent evaluation benchmarks]], [[Topic - user simulation]], [[Topic - alternative evaluation paradigms]], [[Topic - self-evolving tests]], [[Topic - judges as reward signals]].

## Papers (8)
- [[2024-03 AutoEval done right]] — Prediction-powered inference for evaluation: unbiased metric estimates from many judge labels plus a small human-labelled set. (also: [[Topic - LLM and agent judges]])
- [[2024-08 Can unconfident LLM annotations be used for confident conclusions]] — Confidence-driven inference: combine LLM annotations with a few strategically chosen human labels (where the LLM is unconfident) to get valid statistical estimates. (also: [[Topic - LLM and agent judges]], [[Topic - confidence-gated escalation]])
- [[2024-10 Limits to scalable evaluation at the frontier]] — Proves that when the judge is no more accurate than the evaluated model, no debiasing method can cut required ground-truth labels by more than half. (also: [[Topic - LLM and agent judges]])
- [[2025-03 ConSol]] — Replaces fixed 40-sample self-consistency voting with Wald's sequential probability ratio test, which stops sampling once one answer is significantly ahead of the runner-up, cutting tokens by 64-89% at roughly the same accuracy. (also: [[Topic - alternative evaluation paradigms]])
- [[2026-01 Confident Rankings with Fewer Items]] — Extends IRT-based computerized adaptive testing from right/wrong items to continuous scores (ROUGE, BLEU, LLM-as-judge) and adds a multi-model ranker that stops as soon as every adjacent pair of models is confidently ordered or declared a tie.
- [[2026-03 AgentAssay]] — A framework for regression-testing stochastic agents: three-valued verdicts (Pass / Fail / Inconclusive) from confidence intervals and Wald's SPRT, plus a "behavioral fingerprint" of each trace tested with Hotelling's T², to decide whether a changed agent got worse while running as few paid trials as possible. (also: [[Topic - agent evaluation benchmarks]])
- [[2026-07 Stop Guessing When to Stop Testing]] — Replaces fixed-size benchmark runs with group sequential testing, so an evaluation feeds examples in batches and stops as soon as a user-chosen statistical goal (a CI width, a significant gap, a threshold crossed) is met, with error rates still valid despite the repeated looks.
- [[2026-08 Knowing When to Stop]] — optstop (UK AISI) stops an LLM evaluation item by item and group by group once a hierarchical Bayesian credible interval on the score is narrower than a set width, cutting 57% to 97% of planned trials with the same overall score.
