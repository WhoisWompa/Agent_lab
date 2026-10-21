---
title: Red Teaming Language Models with Language Models
authors: Ethan Perez et al.
date: 2022-02
arxiv: 2202.03286
url: https://arxiv.org/abs/2202.03286
venue: EMNLP 2022
category: self-evolving-tests
topics: ["self-evolving tests"]
---
# Red Teaming Language Models with Language Models

## One line
A red-team LM generates test inputs against one target chatbot, a classifier judges the replies, and the red LM is improved (few-shot from past hits, supervised, then RL) to find more failures.

## Method
Red LM proposes questions; target is a 280B dialogue-prompted Gopher (DPG); an offensiveness classifier scores replies. Generation methods escalate: zero-shot, stochastic few-shot (re-using earlier successful test cases as exemplars), supervised fine-tuning on failing cases, and RL with the classifier as reward. Also probes data leakage, contact-info generation, distributional bias, and multi-turn dialogue red teaming. Judge sees only outputs and is fixed across rounds (only the attacker evolves).

## Evaluated on
Uncovers tens of thousands of offensive replies from the 280B chatbot. Reports a trade-off: RL finds the highest failure rate but with the lowest diversity of test cases; zero-shot is the most diverse but has the lowest rate.

## Limitations admitted by the authors
- Results depend entirely on the offensiveness classifier; failures it cannot detect are invisible, and it can be wrong.
- RL red LM collapses toward low-diversity, repetitive attacks (diversity vs. difficulty trade-off).
- Red teaming can only find failures, not certify their absence; coverage unknown.

## Limitations found by others
- Rainbow Teaming (2402.16822) and Curiosity-driven Red-Teaming (2402.19464) both cite the RL mode-collapse / low-diversity problem as their motivation.

## What it leaves untried
- Improve the judge (classifier) from the misjudgments surfaced by the attack loop; here only the attacker learns.

## Topics
[[Topic - self-evolving tests]]
