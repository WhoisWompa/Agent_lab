---
title: "Knowing When to Stop: Bayesian Optimal Stopping for LLM Evaluations"
authors: Toby D. Pilditch
date: 2026-08
arxiv: 2608.14425
url: https://arxiv.org/abs/2608.14425
venue: arXiv
category: agent-evaluation-benchmarks
pdf: agent as a judge papers/stopping rules/Knowing When to Stop - Bayesian Optimal Stopping for LLM Evaluations (Pilditch 2026).pdf
folder: ["agent as a judge", "stopping rules"]
topics: ["stopping rules"]
---
# Knowing When to Stop: Bayesian Optimal Stopping for LLM Evaluations

## One line
optstop (UK AISI) stops an LLM evaluation item by item and group by group once a hierarchical Bayesian credible interval on the score is narrower than a set width, cutting 57% to 97% of planned trials with the same overall score.

## Method
Problem: evaluations run every item a fixed number of times (epochs), even after the estimate is already precise. IRT/adaptive-testing methods cut items but need a pre-calibrated item bank, which new or safety benchmarks lack.

Idea: treat evaluation as sequential measurement with a precision-based stopping rule. After each batch, fit a posterior and stop when the (default 97%) credible interval width W falls below δ (δ = 0.05 means ±2.5 points). This happens at two levels. At the item level, a Beta posterior over that prompt's success rate decides when more epochs are useless. At the grouping level (user-defined, e.g. model × task), a hierarchical logit-normal model partially pools items, so the group estimate stays stable even when items have different numbers of epochs, and the whole group stops once its interval is narrow, skipping the items not yet run. Every item stays eligible; nothing is pre-selected.

The justification is the Stopping Rule Principle: a Bayesian posterior depends only on prior and likelihood, so stopping on the data does not invalidate it. The author admits this holds strictly only for the fixed-prior group model, not the data-dependent item-level prior.

Extras:
- **Three score types.** Binary (logit-normal), ordinal rubrics (ordered logistic; stops when a narrow modal interval is backed by low entropy, or when the entropy itself has converged for spread-out distributions), and bounded continuous (modelled on item means, about 20× cheaper).
- **Stabilisation fallback.** Stop when the slope of recent CI widths is near zero.
- **Asymmetric conservatism.** If estimated performance is below 1%, the CI width is multiplied by c = 5 before the comparison, so near-zero models get sampled longer and rare successes (pass@k) have a chance to show up.

Assumes exchangeable observations within a grouping and randomised item order.

## Evaluated on
- **Large savings with the same score.** In nine cells (3 score types × low/mid/high performance; 200 items × 10 epochs), 57.2% to 97.3% of trials were removed, 81.1% on average. The mean absolute score deviation from the full run was 0.006 on [0,1], and the worst was 0.022, inside δ.
- **No systematic truncation bias overall.** A pooled meta-analysis gives an effect of +0.0003, 97% HDI [−0.002, +0.003], inside a ±0.02 equivalence region. Before pooling, only 6 of 9 cells accepted equivalence.
- **Richer scores save more.** Continuous saved 95.1% on average, ordinal 75.0%, binary 73.3%. Extreme performance (near floor or ceiling) also saves more than mid-range, because mid-range scores have the most variance.
- **Rankings survive truncation.** The max_tokens 5,000 > 500 > 50 order was preserved, with non-overlapping HDIs in both full and truncated runs.
- **Conservatism prevents early false negatives.** On synthetic data with 1% true success, c = 1 stopped at 120 trials with a fourfold overestimate (0.027 vs 0.0065). c = 5 stopped at 910 trials with 0.008.

## Limitations admitted by the authors
- **Interval coverage is below nominal.** In simulation, nominal 94% intervals covered about 80% of the time under moderate heterogeneity, and 0% at exact 0/1 boundaries. The guarantee is on interval width, not on the true value being inside it.
- **The ordinal pathway stops on the mode, not the mean.** The high-ordinal cell was off by −0.059 (HDI [−0.114, −0.001]). Ordinal interval coverage of the full-run mean was 0/15, 12/15 and 1/15. Anyone reporting means from a mode-stopped run inherits this gap.
- **Ordinal savings depend on item order.** With shuffled order they were 95.7% to 97.3%, against 57% to 92% with fixed order. In mid-ordinal, the number of items used ranged from 30 to 90 across shuffles.
- **Epochs are treated as independent.** Correlated repeats of the same item inflate the effective sample size and speed up stopping.
- **The stabilisation fallback is untested at default settings.** It was validated only with thresholds relaxed 100×. Under defaults, no matrix cell would have triggered it. At high c, it gives non-monotonic, MCMC-dependent stopping (CV up to 13%).
- **Conservatism was not exercised in the main experiment.** The lowest cell (p ≈ 0.05) sat above the 1% trigger, so the safety mechanism rests only on synthetic data.
- **One configuration, single author.** Everything was run at 200 items × 10 epochs. Leaner designs leave less room to stop early, and broader replication is called for.

## Limitations found by others

## What it leaves untried
- **Judge noise.** No test where the score comes from an LLM or agent judge whose own noise and bias change from run to run. Stopping on a narrow interval around a biased judge only locks in the bias faster.
- **Comparison stopping.** No rule that stops when the decision is settled (model A vs B, or pass vs fail against a threshold) rather than when an interval is narrow. The paper names inference-based rules but does not test them, and they could stop far earlier for clear comparisons.
- **Agentic tasks.** No agentic or multi-step benchmarks, even though the paper motivates the method with their cost (hundreds of dollars per task). Correlated epochs and drifting environments there would stress the exchangeability assumption most.

## Topics
[[Topic - stopping rules]]
