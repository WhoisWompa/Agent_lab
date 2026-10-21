---
title: Improving Language Model Negotiation with Self-Play and In-Context Learning from AI Feedback
authors: Yao Fu et al.
date: 2023-05
arxiv: 2305.10142
url: https://arxiv.org/abs/2305.10142
venue: arXiv
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2305.10142.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops", "strategic play among LLM agents"]
---
# Improving Language Model Negotiation with Self-Play and In-Context Learning from AI Feedback

## One line
Two LLMs bargain as buyer and seller while a third LLM critic writes advice that is fed back as in-context demonstrations, to test whether models can improve each other without human input.

## Method
The question is whether LLMs can improve one another AlphaGo-Zero style, through playing a competitive game with minimal human supervision. The paper uses a balloon bargaining game: the seller wants a high price, the buyer a low one, and the deal price (kept in $10 to $20 by hard-coded opening offers) is the measurable objective. A gpt-3.5-turbo moderator classifies each dialog as ongoing, deal or no deal.

Only one player is improved at a time. After each round a critic LLM, always the same engine as the player it helps, reads that player's full dialog history and past feedback and writes three suggestions. The player acknowledges them and plays again, with the previous dialogs and feedback acting as few-shot demonstrations. The authors call this In-Context Learning from AI Feedback (ICL-AIF). The rival is always gpt-3.5-turbo, has no feedback, and clears its history each round. No weights change.

The authors choose in-context learning over RL because RL tuning is costly and base models are often inaccessible. They also cite work linking in-context learning to gradient descent, so the findings should plausibly carry over to fine-tuning. This claim is not tested here. The feedback is natural language rather than a scalar reward. The game also works as a capability probe, since a model needs to follow the rules, use critic advice, and keep improving over rounds.

## Evaluated on
- Capability gating: cohere-command does not understand bargaining (rejects $10 but accepts $8 as seller), and AI21 j2-jumbo-instruct ignores the critic and repeats its strategy. gpt-3.5-turbo, claude-instant and claude-v1.3 pass this check, and gpt-4 is also used later.
- AI feedback is about as useful as human feedback. Seller price rises are +0.77 vs +0.57 (gpt-3.5-turbo), +1.24 vs +1.59 (claude-instant) and +1.58 vs +1.49 (claude-v1.3). The human feedback is 3 suggestions drawn at random from a hand-written pool of 10.
- Buyers are harder to improve than sellers. For weaker models the average price moves -0.2 and -0.5 as buyer against +1.0 and +1.7 as seller. Stronger models still improve as buyer (claude-v1.3 -1.2, gpt-4 -3.0).
- One round of improvement does not mean continued improvement. Over 5 rounds gpt-3.5-turbo keeps improving, claude-instant improves at most one round, and claude-v1.3 saturates at about 3 rounds as buyer.
- A better price costs deals. Deal success falls every round, mostly below 50% by round 5 for sellers and mostly above 50% for buyers. gpt-4 gets the best price and a higher deal rate than gpt-3.5-turbo as buyer.
- Responses get longer with feedback, but length is not the driver. gpt-4 is shorter than claude-v1.3 yet gets better price and deal rate. The authors read this as "more strategic" wording; no test separates strategy from length.

## Limitations admitted by the authors
- Only strong, well-aligned models benefit (gpt-3.5-turbo, gpt-4, claude-v1.3). Weaker ones fail the rules or ignore feedback, so the method is not general across models.
- Results are a snapshot from May 2023 API models that were being updated. Failed models may pass in later versions.
- Pushing the price raises the chance of losing the deal, and success falls over rounds. The authors suggest global optimisation over rounds because the per-round objective does not capture this.
- The moderator is weakest at spotting no-deals. The authors patched it by hand (about 90+ accuracy by manual inspection), which affects the success-rate numbers.
- Human feedback is a random draw from a 10-item pool, which the authors say may understate human feedback. The comparison therefore shows parity, not superiority.
- Autonomous improvement with limited human oversight raises safety concerns that the paper names but does not study.

## Limitations found by others

## What it leaves untried
- Fine-tuning on the critic feedback, which would test the claimed link between in-context learning and gradient updates.
- Improving both players at once or varying the rival. The rival is always gpt-3.5-turbo and the single product is a balloon, so the self-play claim is really one-sided improvement against a fixed opponent.
- Optimising across rounds to trade price against deal rate, which the authors raise but do not try.

## Topics
[[Topic - self-refinement and critique loops]] · [[Topic - strategic play among LLM agents]]
