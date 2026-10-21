---
title: "Rewarding Doubt: A Reinforcement Learning Approach to Calibrated Confidence Expression of Large Language Models"
authors: David Bani-Harouni et al.
date: 2025-03
arxiv: 2503.02623
url: https://arxiv.org/abs/2503.02623
venue: ICLR 2026
category: trained-judges-reward-models
pdf: agent as a judge papers/decision models/open models/papers/Rewarding Doubt - RL Approach to Confidence Calibration of LLMs (Stangel 2025).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["calibration", "open decision models", "judges as reward signals"]
---
# Rewarding Doubt: A Reinforcement Learning Approach to Calibrated Confidence Expression of Large Language Models

## One line
Fine-tunes an LLM with PPO on a log-scoring-rule reward so that the 0-10 confidence it verbalizes next to each answer matches its actual probability of being right.

## Method
Problem: LLMs asked to state a confidence are overconfident. The zero-shot base model puts almost every answer at 8 or above. The existing fixes either read confidence off something outside the generated text (token probabilities, consistency across samples, a probe on hidden states), or fine-tune on confidence labels built in advance. The authors argue the second kind can only be as good as those labels, and that supervised imitation of the labels loses whatever calibration guarantee the labeller had.

Idea: treat stating a confidence as a bet and reward it with the logarithmic scoring rule. The reward is log(p) if the answer is correct and log(1-p) if it is wrong. This rule is strictly proper: for a true chance of being right p*, the expected reward p*·log(p) + (1-p*)·log(1-p) is concave and peaks only at p = p*. So the reward-maximising policy is exactly calibrated, and no confidence labels are needed. The only signal is whether the answer was right. Confident wrong answers cost more than hedged ones gain, penalising both over- and underconfidence.

Design choices that carry the claim:
- The answer is generated first and then frozen. Only the confidence tokens get the reward. This keeps calibration training from changing what the model answers.
- p is clipped to [0.001, 0.999] so the log stays finite. Inside the clipped bands the model cannot tell confidences apart. The authors call this effect minor.
- Correctness comes from a rule-based judge (exact match, or word-overlap F1 above 0.5).
- The confidence is verbalized by the model itself, so at inference it costs a few tokens.

## Evaluated on
- Near-perfect calibration on the training domain: on TriviaQA, ECE drops from 0.3459 (zero-shot verbalized) to 0.0226 and AUROC rises from 0.5858 to 0.8592. The hidden-state probe has a slightly lower ECE (0.0189) but a lower AUROC (0.8173).
- Accuracy is unchanged: 0.6310 before and 0.6309 after on TriviaQA, and the same holds across all models.
- It works in the multi-answer setting, where each listed fact gets its own confidence: on QAMPARI, ECE is 0.0816 vs 0.5319 for the base model and 0.1117 for the probe.
- It partly transfers out of domain. Trained on TriviaQA, on MedQA it reaches ECE 0.1145 vs 0.4480 (base) and 0.2099 (probe). On CommonsenseQA the ECE does not improve (0.2930 vs 0.2820), though AUROC rises from 0.5425 to 0.6385.
- The gains vary by model. Qwen-2.5-3B ends at ECE 0.1483 and Gemma-2-9B at 0.0922. On both, the probe calibrates better (0.0186 and 0.0301).

## Limitations admitted by the authors
- Only tested on 3B to 9B models, because of compute. Whether the reward still helps larger models is untested.
- Correctness must come from an exact rule-based check that gives a binary signal. Free-form or judged answers are named as future work. This matters because the calibration guarantee only holds if the correctness label is right.
- ECE alone can mislead. A model that always gives moderate confidence looks calibrated under ECE while telling cases apart poorly. They lean on AUROC for CommonsenseQA, where ECE did not improve.
- Clipping removes the guarantee at the extremes. Confidences within 0.001 of 0 or 1 get the same reward.
- Good average calibration can still be wrong on important individual cases, and a numeric confidence may make users over-trust the model.

## Limitations found by others

## What it leaves untried
- Rewarding against an LLM judge's verdict instead of exact match. This is the setting where the confidence would be used in agent-as-a-judge pipelines, and there judge noise directly corrupts the proper-scoring guarantee.
- Using the trained model as a judge, i.e. calibrating confidence in verdicts on other models' outputs rather than in its own factual answers. The paper only calibrates self-assessment of answers it generated itself.
- Training answer and confidence together. Freezing the answer protects accuracy, but it leaves open whether a jointly trained model would learn to abstain or pick safer answers.

## Topics
[[Topic - calibration]] · [[Topic - open decision models]] · [[Topic - judges as reward signals]]
