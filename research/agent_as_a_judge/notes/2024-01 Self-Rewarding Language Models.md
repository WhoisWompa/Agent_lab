---
title: Self-Rewarding Language Models
authors: Weizhe Yuan et al.
date: 2024-01
arxiv: 2401.10020
url: https://arxiv.org/abs/2401.10020
venue: ICML 2024
category: trained-judges-reward-models
---
# Self-Rewarding Language Models

## One line
One model acts as both policy and LLM-as-a-judge of its own outputs, and iterative DPO on self-judged pairs improves both roles.

## Method
- Seed: small human-written instruction-following data (Open Assistant) and evaluation-format data.
- Each iteration: model generates candidates, scores them with a 5-point additive judging prompt, builds preference pairs, DPO. Self-generated labels.
- Pointwise judge with chain-of-thought justification.

## Evaluated on
- Llama 2 70B after 3 iterations: AlpacaEval 2.0 win rate 20.44%, above Claude 2, Gemini Pro and GPT-4 0613 at the time (paper abstract).
- Judge agreement with human rankings improves across iterations.

## Limitations admitted by the authors
- Only 3 iterations; saturation and reward hacking unstudied.
- Output length grows across iterations, which inflates AlpacaEval.
- Safety evaluation absent.

## Limitations found by others
- Meta-Rewarding (arXiv:2407.19594): the judge improves little after the first iterations and saturates; scores cluster.

## What it leaves untried
- A way to improve the judge independently of the policy (taken up by Meta-Rewarding).
