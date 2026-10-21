---
title: "AgentAssay: Token-Efficient Regression Testing for Non-Deterministic AI Agent Workflows"
authors: Varun Pratap Bhardwaj
date: 2026-03
arxiv: 2603.02601
url: https://arxiv.org/abs/2603.02601
venue: arXiv (technical report)
category: agent-evaluation-benchmarks
pdf: agent as a judge papers/stopping rules/AgentAssay - Token-Efficient Regression Testing for Non-Deterministic AI Agent Workflows (Bhardwaj 2026).pdf
folder: ["agent as a judge", "stopping rules"]
topics: ["stopping rules", "agent evaluation benchmarks"]
---
# AgentAssay: Token-Efficient Regression Testing for Non-Deterministic AI Agent Workflows

## One line
A framework for regression-testing stochastic agents: three-valued verdicts (Pass / Fail / Inconclusive) from confidence intervals and Wald's SPRT, plus a "behavioral fingerprint" of each trace tested with Hotelling's T², to decide whether a changed agent got worse while running as few paid trials as possible.

## Method
The problem: an agent can give different results on the same input, so `assert f(x) == y` means nothing. The real question is whether the new version's pass rate fell below the old one by more than δ. Answering that with a fixed sample costs a lot: about 100 trials per scenario for δ = 0.10, α = 0.05, β = 0.10.

The core idea is a three-valued verdict. The agent runs n times on a scenario, and an evaluator (rule, contract or LLM judge) scores each run 0 or 1. A Wilson interval goes around the pass rate: Pass if its lower bound is at or above the threshold θ, Fail if its upper bound is below θ, Inconclusive otherwise. "Inconclusive" means more evidence is needed. For example, 45 of 50 passes at θ = 0.85 is still Inconclusive, and only reaches Pass at n = 200. A regression verdict needs both p < α and an observed drop of at least δ.

For stopping, it uses Wald's SPRT on the per-trial log-likelihood ratio between p = θ and p = θ − δ. Testing stops when the ratio crosses log(β/(1−α)) or log((1−β)/α). In the paper's worked example (θ = 0.9, δ = 0.1) this cuts the expected trials from 109 to about 52 when the agent is fine and about 34 when it has regressed.

The claimed source of extra savings is the "fingerprint". A pass/fail bit throws away the trace, so each run is mapped to a 14-dimension vector: tool-use frequencies, trace length and depth, output length, action mix, error and recovery, and cost. Old and new versions are then compared with a multivariate test (Hotelling's T²). This catches behavior shifts even when the pass rate is unchanged. It assumes the fingerprint lies on a low-dimensional manifold, reported as 3 to 8 effective dimensions in "preliminary experiments".

Smaller layers sit on top:
- Variance-calibrated trial budgets, from 10 calibration runs.
- "Trace-first" offline checks on stored production traces: coverage, contracts, metamorphic relations.
- Cheap proxy models used as control variates.
- Warm-start SPRT seeded from earlier runs.
- Five coverage metrics, agent mutation operators, and a deploy / block / manual CI gate.

## Evaluated on
- SPRT cuts trials by 78% at the same nominal (α, β): it stops at 22 trials against 100 for the fixed sample, and savings are 77.5–78.2% in each of the three domains. However, the pass rate was 100% everywhere, so this is the stopping time when there is no regression at all.
- The fingerprint "detects what pass/fail misses": its power is 0.86 against 0.00 for the fixed sample and SPRT. The paper itself says pass/fail scored 0 because no pass-rate regression occurred. It never says what behavior change the 0.86 is measured against.
- The full system costs $0 per check, with power 0.94 in the table and 98% in the figure, because verdicts come from stored traces.
- The adaptive budget adds almost nothing: 20.3 trials both with and without it. Power goes from 0.79 to 0.80 in the text, against 0.86 for both in the table.
- The 5–20× combined saving is a product of assumed "typical ranges", not a measurement.

## Limitations admitted by the authors
- No regression was injected. Experiments with induced regressions are "in preparation". So every power and savings number comes from agents that never actually regressed.
- The tests assume trials are i.i.d. Bernoulli. Provider caching, rate limits and silent model updates during a run break that assumption. The paper offers mitigations but no robustness result.
- An LLM-judge evaluator adds its own noise. The measured pass rate then mixes agent quality with judge quality, and the paper's answer is to prefer deterministic evaluators.
- The mutation-adequacy theorem rests on the coupling effect, which has not been checked for prompt or tool mutations. Treating "no significant difference" as an equivalent mutant can inflate mutation scores.
- A wrong warm-start prior can push the Type I error up to about 7.4α (0.37 at α = 0.05) in the worst case.
- Not tested: long-horizon agents, adversarial settings, physical actuators.

## Limitations found by others

## What it leaves untried
- Inject real regressions of known size (prompt edits, model downgrades) and measure Type I error and power against that ground truth. Without this, none of the guarantees has been checked on data.
- Reconcile the 100% "full system" result with the paper's own Theorem 7.3, which says regression detection cannot be done from stored traces because the candidate version has no traces yet.
- Model judge noise inside the SPRT, for example by stopping on judge-uncertain verdicts separately, rather than folding it into one Bernoulli rate.

## Topics
[[Topic - stopping rules]] · [[Topic - agent evaluation benchmarks]]
