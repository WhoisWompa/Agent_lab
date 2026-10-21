---
title: "Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty"
authors: Mehul Damani et al.
date: 2025-07
arxiv: 2507.16806
url: https://arxiv.org/abs/2507.16806
venue: ICLR 2026
category: trained-judges-reward-models
pdf: agent as a judge papers/decision models/Beyond Binary Rewards - Training LMs to Reason About Their Uncertainty, RLCR (Damani 2025).pdf
folder: ["agent as a judge", "decision models"]
topics: ["calibration", "judges as reward signals"]
---
# Beyond Binary Rewards: Training LMs to Reason About Their Uncertainty

## One line
RLCR adds a Brier-score term to the binary correctness reward in RL reasoning training, so the model learns to state a calibrated confidence alongside its answer at no cost in accuracy.

## Method
The problem: RLVR's 0/1 reward pays a lucky guess the same as a confident right answer, and treats abstaining the same as being wrong, so it trains overconfident guessing. After RLVR, stated confidence piles into 0.9-1.0 whatever the input. Out of domain, answers stated at 0.8-0.9 are right only about 30% of the time.

The fix: the model writes an answer, then an uncertainty analysis, then a number q, and is rewarded with R = 1[correct] - (q - 1[correct])^2. Theorem 1 is an argument about proper scoring rules. For any answer, expected reward peaks when q equals the true success probability. Among calibrated answers, it peaks for the answer most likely to be right. The second half is the new part, and it holds only for a **bounded** rule, one where S(p,1) - S(p,0) stays below the correctness bonus. The Brier gap is at most 1, so a +1 bonus is enough. The log score's gap is unbounded as p goes to 0. So a log-score reward can pay more for a deliberately wrong answer at confidence 0 than for an honest weak guess. Calibration-only RL fails the same way: an empty answer at confidence 0 scores perfectly.

What it assumes: correctness is a Bernoulli(p_y) draw, read as the model's subjective uncertainty. A verifier supplies ground truth during training. Each sample gives one answer and one confidence. Why it generalises out of domain is left as untested hypotheses.

## Evaluated on
- **Calibration improves and accuracy holds, in domain.** HotpotQA: ECE 0.37 to 0.03 (RLVR to RLCR), accuracy 63.0% vs 62.1%. Math: ECE 0.26 to 0.10, accuracy 72.9% vs 72.7%.
- **RLVR makes out-of-domain calibration worse; RLCR improves it.** Averaged over 6 OOD sets: base ECE 0.40, RLVR 0.46, RLCR 0.21. A separate 7B confidence classifier on RLVR gets 0.24.
- **The reward does the work, not the prompt.** Prompting RLVR to analyse its uncertainty moves ECE only from 0.37 to 0.34. RLCR with no analysis reaches 0.09 at a similar token cost (113 vs 92 tokens).
- **Boundedness matters.** On a 5-arm toy task, the log-score variant drops to 0% accuracy (it answers -1 at confidence 0). The Brier variant keeps 34.4% accuracy at ECE 0.02.
- **Confidence works as a free reward model.** Weighting votes by confidence beats plain voting, picking the most confident answer, and likelihood-based selection as N grows. Results carry over to OLMo-2-7B (ECE 0.38 to 0.09) and Qwen3-8B (0.36 to 0.23).

## Limitations admitted by the authors
- **Out-of-domain calibration is still poor.** ECE is 0.21 out of domain vs 0.03 in domain.
- **Contradictory answers can both get high confidence.** Out of domain, confidences over mutually exclusive answers to one question still sum above 1 for RLCR. RLVR overshoots more.
- **The SFT warm-up hurts generalisation.** SFT+RLCR gets the best math calibration, but its OOD accuracy is 43.8% (RLVR: 52.5%). A prompt fix brings it back to 49.8%; the authors blame mostly math-style answer formatting.
- **The log-score failure did not appear on real QA.** RLCR-Log on HotpotQA keeps 59.5% accuracy. The authors say whether hacking appears depends on the data and model size, which the paper does not map out.
- **The analysis text may not be what sets the number.** A 7B classifier calibrates just as well without RLCR's analysis text; only the 0.5B and 1.5B classifiers gain from it.

## Limitations found by others

## What it leaves untried
- **Training a judge with RLCR.** Train a judge with this reward so each verdict carries a calibrated confidence that can decide when to escalate. The paper only calibrates a solver on tasks with verifiable answers.
- **Training without ground truth.** The reward needs correctness labels. Open-ended tasks scored by a noisy judge, where calibration matters most, are untried.
- **Robustness to input changes.** The paper does not test whether stated confidence holds up under adversarial or cosmetic changes to the input.

## Topics
[[Topic - calibration]] · [[Topic - judges as reward signals]]
