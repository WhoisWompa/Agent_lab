---
title: Verify, Repair, Repeat, or Stop? Robust Stopping for Noisy Verify-Repair Loops in LLM Agents
authors: Yitao Wu et al.
date: 2026-07
arxiv: 2607.17641
url: https://arxiv.org/abs/2607.17641
venue: arXiv
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2607.17641.pdf
folder: ["multiagent_llm_systems"]
topics: ["stopping rules", "self-refinement and critique loops"]
---
# Verify, Repair, Repeat, or Stop? Robust Stopping for Noisy Verify-Repair Loops in LLM Agents

## One line
VRR-Stop decides when to stop a noisy verifier/repairer loop by estimating the probability the current plan is valid and stopping once one more repair is expected to do more damage than good, with a conservative keep-best fallback when the verifier cannot tell valid from invalid plans.

## Method
Problem: in a verify-repair loop the repairer can break a plan that was already correct, and the verifier can accept the broken one. Acceptance then keeps rising while true validity falls, so pass rate cannot be the stopping signal. The authors measure repair damage reaching 0.94 in some trajectories.

Idea, in three parts:
- **Four-parameter noise model.** Verifier false-accept rate and false-reject rate (together Youden's J = 1 - false-accept - false-reject, the verifier's discrimination), plus repairer fix rate alpha (invalid to valid) and damage rate beta (valid to invalid). This separates verifier noise from repairer noise, which pass-rate curves entangle.
- **Belief filtering and a sign rule.** Eight repeated verifier votes per round update a Bayesian posterior b that the plan is truly valid. One more repair has expected gain (1-b)·alpha - b·beta, which is zero at b* = alpha/(alpha+beta). Below b* keep repairing, above it commit. The boundary depends only on the repairer, not on verifier noise, which only affects how reliably b is located. Parameters come from an unlabeled binomial-mixture EM on vote counts plus at most 300 labeled before/after pairs. Only the sign of the gain must be identifiable, not every parameter. A proposition bounds the chance that the estimated action differs from the true one.
- **VRR-Guard fallback.** When J is near zero the mixture is unidentifiable (the EM likelihood flattens), so the loop keeps an incumbent best plan and replaces it only if the new plan gets at least delta more votes (delta = 5 of 8). A Hoeffding bound makes wrong replacement decay exponentially in delta and M·J. Mode choice is made offline from a held-out labeled separation test, not online.

Assumptions: votes are conditionally independent given true state, noise parameters are stable within a decision window, validity is binary, and the stopping target is one-step myopic.

## Evaluated on
- Repair is often harmful: in a stress run validity rises 0.45 to 0.87 at two rounds, then falls to 0.12 by round 6, while independent resampling stays at 0.47-0.85. Across eight settings six decline monotonically (damage 0.615-0.938). A process-reward verifier with J = 0.805 still drops from 0.727 to 0.097 under five rounds.
- VRR-Stop beats fixed five-round repair by 60.6 points on GSM8K with Qwen2.5-3B (0.722 vs 0.116) using 0.72 repair rounds on average; no-repair scores 0.700, so the gain over doing nothing (+2.2 points) is within noise.
- It edges the oracle-parameter reference (0.722 vs 0.694), and beats majority-vote stopping by 3.2 points.
- Flip risk of the stopping sign is 0.183 when J <= 0.15 and decision margin <= 0.10, versus 0.014 when J >= 0.4 or margin >= 0.30 (about 13x).
- At J = 0.03 (Llama) calibrated stopping collapses from 0.803 to 0.223; VRR-Guard recovers 0.793. Guard stays near no-repair in all seven shifted settings.

## Limitations admitted by the authors
- Local-stationarity and binary-validity assumptions: the model cannot express repair dynamics that change by round. The authors list round-varying dynamics as future work.
- Near-zero J breaks calibration. More data worsened the estimate (rho1 hat 0.077 at N=300 vs true 0.609), so the method needs a separate test to know when to abandon it.
- Guard does not dominate: in the favorable setting it scores 0.810 vs 0.875 for fixed repair, and it costs about 2.0 points against no-repair on Mistral.
- The sample-complexity bound holds only for an idealized single-query loop; deployed reliability is shown by simulation only.
- Conditional independence of repeated votes ignores instance difficulty; the authors say a beta-binomial diagnostic exists but treat it as an approximation.

## Limitations found by others

## What it leaves untried
- Online switching between Stop and Guard: mode is fixed offline per scenario, so a deployed system cannot detect a drifting verifier by itself.
- Multi-step look-ahead instead of one-step gain, which may matter where a harmful repair is followed by a recovery.
- Non-binary validity, such as partially correct plans or tool-use plans scored by steps.

## Topics
[[Topic - stopping rules]] · [[Topic - self-refinement and critique loops]]
