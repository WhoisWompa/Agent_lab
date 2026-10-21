---
title: LLM Critics Help Catch LLM Bugs (CriticGPT)
authors: Nat McAleese et al.
date: 2024-06
arxiv: 2407.00215
url: https://arxiv.org/abs/2407.00215
venue: arXiv (OpenAI)
category: trained-judges-reward-models
topics: ["trained judges and reward models", "preference learning", "LLM and agent judges"]
---
# LLM Critics Help Catch LLM Bugs (CriticGPT)

## One line
RLHF-trained GPT-4 critic that writes code-review critiques of ChatGPT code; catches more bugs than paid contractors but also hallucinates bugs.

## Method
- Data: contractors inserted subtle bugs into ChatGPT answers ('tampering') with a reference explanation, collected adversarially so the critic missed each bug in at least one of three samples; plus naturally occurring bugs. Critique comparisons were rated by humans and used to train a reward model, then RL.
- Inference: Force Sampling Beam Search (FSBS) samples 28 critiques and picks the one maximising RM score + length modifier x number of highlighted code spans; the modifier trades comprehensiveness against hallucinations/nitpicks.
- Sees only the question and the code answer; no execution, no repo access.

## Evaluated on
- Model critiques preferred over human critiques in 63% of cases on naturally occurring bugs, and over 80% on inserted bugs ([arXiv HTML](https://arxiv.org/html/2407.00215)).
- CriticGPT misses inserted bugs much less than ChatGPT; matching via pre-training alone would need about 30x compute.
- Found hundreds of errors in ChatGPT training data rated 'flawless' (mostly non-code, out of distribution).
- Human+CriticGPT teams write more comprehensive critiques than humans alone and hallucinate less than the model alone.

## Limitations admitted by the authors
- Short code snippets only; no multi-file / repo navigation.
- Absolute rates of nitpicks and hallucinated bugs remain high; longer critiques find more bugs and hallucinate more.
- Bugs spread across many lines not studied.
- Single critique step; debate or multi-step methods untested.
- Dual-use risk.

## Limitations found by others
- Wen et al. 2024 'Language Models Learn to Mislead Humans via RLHF' (arXiv:2409.12822): RLHF-trained models become better at convincing human evaluators of wrong answers, which is the failure mode a critic has to counter.

## What it leaves untried
- Critic with code execution or repository access.
- Training on naturally occurring rather than inserted bugs at scale.

## Topics
[[Topic - trained judges and reward models]] · [[Topic - preference learning]] · [[Topic - LLM and agent judges]]
