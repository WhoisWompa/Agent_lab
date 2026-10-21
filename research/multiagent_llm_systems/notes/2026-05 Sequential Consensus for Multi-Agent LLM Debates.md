---
title: Sequential Consensus for Multi-Agent LLM Debates: A Wald-SPRT compute governor with calibration-based failure detection
authors: Andrea Morandi
date: 2026-05
arxiv: 2605.19193
url: https://arxiv.org/abs/2605.19193
venue: arXiv
category: debate-cooperative-reasoning
pdf: research/multiagent_llm_systems/pdfs/2605.19193.pdf
folder: ["multiagent_llm_systems"]
topics: ["stopping rules", "multi-agent debate and consensus"]
---
# Sequential Consensus for Multi-Agent LLM Debates

## One line
Wraps a multi-agent debate in Wald's sequential probability ratio test on a judge's per-round consensus score, so the debate stops when the score is informative enough, and the calibration of that score tells you whether stopping can be trusted at all.

## Method
Debate recipes use a fixed round count (2 in Du et al., 3 to 5 later), which overpays on easy items where agents agree in round 1. The paper adds a plug-in stopping layer that leaves the debate prompts untouched.

After each round an LLM judge reads the latest agent positions and returns a consensus score in [0,1]. Two hypotheses are tested: H1, the agents have usefully converged, against H0, they have not. Each hypothesis gets a Beta density for the score, fitted by moments on a small calibration set per task domain (the paper suggests 50 to 100 debates). The monitor sums the log-likelihood ratio of the scores round by round. It stops with "consensus" above one boundary, stops with "no-consensus" below the other, and otherwise continues. Boundaries come in closed form from the target error rates alpha and beta. A hard cap R_max (8) returns a best-effort answer flagged "capped". The answer itself is a majority vote.

Under i.i.d. scores the rule inherits Wald's error bounds and minimal expected sample size. Expected rounds scale as 1/KL between the two Beta densities, so the calibrated KL measures whether the judge's score separates useful from useless convergence. The paper's central claim is this: the calibration is a deployability diagnostic. A KL near zero means no early stop is justified, and the rule says so by running to the cap. The "no-consensus" outcome is also a signal, to escalate to a stronger model or a human.

## Evaluated on
- Simulation with Beta models, alpha=beta=0.05: about 2.4 average rounds against 5 for fixed-5 debate, with 98% classification accuracy. The Beta parameters were chosen to hit planning targets, not fitted to real scores, so this shows the machinery works but not that real judges behave this way.
- GSM8K, real LLMs (gpt-5, claude-opus-4-6, gemini-2.5-pro, with claude-opus-4-6 as judge): 98% of items stop in round 1, 4.06 calls against 15 for fixed-5, a 3.7x cut. Accuracy is 97.0% against 99.0%. The paper itself puts the 2-point gap at about 1.4 sigma, not significant.
- MMLU, real LLMs: the fitted KL is about 0 because agents converge with high judge scores whether right or wrong. The rule hits the cap on 99.5% of items and costs 2.1x fixed-5 (32 calls against 15), with accuracy unchanged (94.2% against 93.8%). The authors read this as the rule correctly reporting an uninformative signal.
- Ceiling effect: a single-round 3-agent vote already scores 94.4% (MMLU) and 99.0% (GSM8K), and fixed-5 debate does not beat it. So accuracy comparisons are not informative, and the gain is cost only.
- Simple adaptive baselines in simulation: halting when the score is at least 0.85 gets 79.5% classification accuracy at 6.79 rounds, and halting when the score stabilises gets 50.1% (chance). The SPRT gets 98.3% at 2.38 rounds.
- Correlated rounds: with lag-1 correlation 0.6, empirical errors are 0.065 and 0.072 against a nominal 0.05, within 1.5x.

## Limitations admitted by the authors
- Rounds are not i.i.d. because agents see each other's answers. The guarantees become approximate, and the error inflation was measured only in simulation.
- The judge is a single point of failure. It showed no power on multiple-choice tasks (MMLU KL about 0), so there the rule adds cost, and the authors say judge design matters more than stopping-rule design.
- Adversarial or Goodhart-style agents that fake high consensus would make the rule stop quickly on a wrong answer. This was not tested.
- The two Beta densities are fixed offline and the Beta shape is assumed. The real MMLU calibration lies well outside the simulated mis-specification range (plus or minus 25%).
- Only two tasks were run, with 200 items each, three agents, and the judge model also acting as an agent. JudgeBench and long-form tasks, other agent counts, and disjoint judge/agent backbones are untested.
- The real-LLM calibration uses gold correctness labels, so it needs labelled debates per domain. The paper has no production run.

## Limitations found by others

## What it leaves untried
- A judge that reads the whole transcript or token-level confidence to rescue MMLU-type tasks. The paper only guesses this would restore separation, with no result.
- A comparison on a harder, unsaturated benchmark or a weaker agent pool, where debate might actually beat a single vote and the 2-point accuracy cost of early stopping would be measurable.
- Using the rule's "no-consensus" output to actually route items to a stronger model or a human, and measuring the gain. It is proposed and prototyped in the paper but never evaluated.

## Topics
[[Topic - stopping rules]] · [[Topic - multi-agent debate and consensus]]
