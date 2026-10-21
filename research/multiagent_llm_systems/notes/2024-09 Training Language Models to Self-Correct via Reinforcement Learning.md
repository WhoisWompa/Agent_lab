---
title: Training Language Models to Self-Correct via Reinforcement Learning
authors: Aviral Kumar et al.
date: 2024-09
arxiv: 2409.12917
url: https://arxiv.org/abs/2409.12917
venue: arXiv
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2409.12917.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops", "judges as reward signals"]
---
# Training Language Models to Self-Correct via Reinforcement Learning

## One line
SCoRe trains a single LLM with two-stage multi-turn RL on its own samples so that its second attempt reliably improves on its first, with no external feedback at test time.

## Method
The problem is intrinsic self-correction: the model must decide by itself whether its first answer is wrong and rewrite it, with no oracle, teacher model or second corrector model. Prompting for this often makes things worse. The paper first shows why the obvious training recipes fail, using SFT on self-generated correction traces (STaR, and Pair-SFT, which pairs wrong with right answers).

- Distribution shift: an offline model learns to fix the mistakes of the data-collecting model, but its correction rate on its own first attempts degrades during training.
- Behavior collapse: the model learns to give the best first answer and then barely edit it. Edit-distance histograms show the fine-tuned models often make no edit at all. The reason given is that "answer well first, never change it" fits the training set as well as true correction does, and only the second generalises. Plain on-policy multi-turn RL collapses the same way, so on-policy data fixes the first failure but not the second.

SCoRe's fix has two parts.
- Stage I trains the second attempt to maximise reward while a strong KL penalty pins the first attempt to the base model. This decouples the two attempts and gives an initialisation that does not collapse.
- Stage II runs RL on both attempts, with a shaped bonus on the second attempt of alpha times (reward of attempt 2 minus reward of attempt 1). The bonus rewards flipping wrong to right and penalises flipping right to wrong, so "do not edit" no longer looks as good as true correction.

The reward is a ground-truth answer checker (MATH answer match, code tests), used in training only.

## Evaluated on
- First clearly positive intrinsic self-correction on MATH (Gemini 1.5 Flash): accuracy goes from the first to the second attempt by +4.4 points (60.0 to 64.4). The base model loses 11.2 (52.6 to 41.4), Self-Refine loses 1.0, and the best prior fine-tuning baseline, Pair-SFT, gains 1.8.
- It fixes more and breaks less: 5.8% of problems go wrong-to-right (base 4.6%), and 1.4% go right-to-wrong (base 15.8%).
- Code (Gemini 1.0 Pro, trained on MBPP, tested on HumanEval): self-correction gain of +12.2 points (base +3.0), while Pair-SFT is negative (-1.8). Offline repair on MBPP-R rises from 47.3% to 60.6%.
- Ablations on MATH show every piece matters. Without Stage I the gain is 2.2 (vs 4.4). Without reward shaping it is 2.6. Single-turn RL gives a gain of -2.4. Replacing REINFORCE with STaR in Stage II reaches only 58.4 second-attempt accuracy.
- Compute use: with a 32-sample budget, spending half on one self-correction round per sample beats pure parallel voting, +10.5 against +7.4 points of accuracy.

## Limitations admitted by the authors
- Only one round of self-correction (two attempts) was trained, for infrastructure reasons. Later rounds may be less effective, and this is untested.
- Training needs two stages, so two runs. The authors suggest unifying them but do not.
- Training needs a ground-truth reward, so it works only where answers can be checked automatically. This is stated as an assumption, and no setting without it is tried.
- The authors suggest that learning meta-strategies like this may need more than standard fine-tuning, such as the progress-style regularisation. This is a conjecture, not tested elsewhere.

## Limitations found by others

## What it leaves untried
- More than two attempts with RL. Multi-round correction is where SFT baselines claim gains, so the claim that RL is better there is not shown.
- Tasks beyond math and code, and models beyond the Gemini family, since all results are on two task types and two Gemini models. Whether the collapse analysis and the progress bonus carry over is unsupported.
- Whether a learned self-correction can be combined with an external critic or a judge at inference time. The paper stays in the setting with no outside feedback.

## Topics
[[Topic - self-refinement and critique loops]] · [[Topic - judges as reward signals]]
