---
title: "General Decision Models: Benchmarking and Insights Beyond Jev"
authors: Feiyu Duan et al.
date: 2026-10
arxiv: 2610.03935
url: https://arxiv.org/abs/2610.03935
venue: arXiv
category: trained-judges-reward-models
pdf: agent as a judge papers/decision models/open models/papers/General Decision Models - Benchmarking and Insights Beyond Jev (Duan 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "papers"]
topics: ["decision models", "open decision models", "judge and decision-model audits"]
---
# General Decision Models: Benchmarking and Insights Beyond Jev

## One line
Maps where single-pass decision models like Jev can replace LLMs, alone and composed into agents and simulations, and builds an open one by distilling an LLM's own reasoning into its first answer token.

## Method
The problem: "general decision models" like Jev map a context, an instruction and a finite option set to a probability over the options in one forward pass, with no generated text. Nobody knew which decisions they handle reliably, or what happens when many are chained in an agent or added up across a population. Jev is also closed.

Two contributions:
- **JEVal**, a bilingual benchmark that recasts 10 domains into one decision format (choice, true/false, or ordered score), plus probes beyond it: exact-number and probability tasks, long contexts, Jev picking actions in a tau-bench agent, and social simulation.
- **SII-Decision**, an open decision model built in two steps. (1) *First-Token Decision Readout*: end the prompt with "The correct answer is (" and take the next-token softmax over the option label tokens only. The pretrained output rows become a decision head with no new parameters. (2) *Reasoning-to-Readout Self-Distillation*: the same model reasons (two chains), and its readout distribution at the end of each chain is averaged into a target. The no-reasoning version is trained to match that target at its first token, with a small KL anchor to the frozen original readout against forgetting. No gold labels, no stronger teacher. Why it should work: thinking repairs readout errors almost one-way (on JevBench it fixes all but one Qwen3.8-27B readout error and breaks none), so the knowledge is already there.

## Evaluated on
- Single-pass decision models match thinking LLMs on overall accuracy: Jev 78.38% and SII-Decision-27B 79.24% sit within three points of GPT-6-Luna (80.93%) and thinking GLM-5.3-Flash (80.37%), and are better calibrated (ECE 0.053 and 0.015, against 0.078 for the best-calibrated LLM).
- They are strongest when the evidence is in the input and weaker on specialist knowledge: SII-Decision-27B and Kev-27B lead long-context document tasks, while the best decision model trails the best LLM by 3 to 6 points in medicine, finance and law.
- They pick the right option but overstate its probability: Jev chooses the mode on 100/100 prior-probability items but gives it 89.35% of the mass when the truth is 35.60%. On near-rounding arithmetic it gets 44% exact but 97% within one.
- Faster steps make a worse agent: with Jev choosing actions on tau-bench, median episode time falls from 267s to 161s, but success drops from 77.6% to 66.1% and P95 time rises from 696s to 816s.
- Individual survey prediction nearly matches LLMs at far lower cost (39.87% vs 40.41%, 8.4s vs 211.6s per item). Election aggregates call 47/51 states but with roughly twice the vote-share error (MAE 6.52 vs 3.06 points) and a pro-Democrat bias (+3.73).

## Limitations admitted by the authors
- Distillation passes on how options are weighed, not intermediate computation: on GPQA and MMLU-Pro it recovers a quarter or less of the accuracy that thinking adds, so multi-step reasoning is not compressed into one pass.
- The student is only as good as its teacher's reasoning. On TruthfulQA thinking Qwen3.8-27B stays below Jev, so distillation lowers accuracy. SII-Decision-4B is less calibrated than Intern-Decision-4B.
- Scaling stalls at about 39K questions. Questions the model writes itself are too easy to carry signal, and it cannot check whether harder ones are correct. The dev set also picks checkpoints, so scores are optimistic.
- The agent study covers two tau-bench environments, one run per task, and the audit found both action and argument errors without isolating a dominant cause.
- Jev is the only decision model probed in depth, so the patterns may not generalise.

## Limitations found by others

## What it leaves untried
- Recalibrating the decision distribution before downstream use. The paper shows the argmax is right and the mass is wrong, the gap behind the election vote-share error, but never tries to fix it.
- Escalating to a generative LLM when the decision model is unsure of the next action. The tau-bench failures come from compounding single-step errors, and confidence-gated routing is the obvious test of the mixed systems it proposes as future work.

## Topics
[[Topic - decision models]] · [[Topic - open decision models]] · [[Topic - judge and decision-model audits]]
