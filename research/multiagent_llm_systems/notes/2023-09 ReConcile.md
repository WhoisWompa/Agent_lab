---
title: "ReConcile: Round-Table Conference Improves Reasoning via Consensus among Diverse LLMs"
authors: Justin Chih-Yao Chen et al.
date: 2023-09
arxiv: 2309.13007
url: https://arxiv.org/abs/2309.13007
venue: arXiv (v3, Jun 2024)
category: debate-cooperative-reasoning
pdf: research/multiagent_llm_systems/pdfs/2309.13007.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus", "social choice"]
---
# ReConcile: Round-Table Conference Improves Reasoning via Consensus among Diverse LLMs

## One line
Several different LLMs (ChatGPT, Bard, Claude2) discuss a reasoning question over up to three rounds, seeing each other's answers, explanations and stated confidence, and the team answer is a confidence-weighted vote.

## Method
Problem: self-refinement stalls when a model is overconfident (the paper cites "Degeneration-of-Thought"), and multi-agent debate usually runs several copies of one model. Copies share pre-training data and architecture, so they share biases and give little outside feedback. The paper's case study describes debate "echo chambers".

Idea: use agents from different model families, so their errors differ, and give the discussion three ingredients.
- **Round 0.** Each agent gives a step-by-step answer, an explanation and a verbalised confidence (a prompted number from 0 to 1).
- **Discussion prompt.** In each later round every agent sees all agents' answers grouped by answer value, with the explanations under each group, plus each agent's confidence. It then revises its own answer, explanation and confidence.
- **Convincing samples.** For each agent, 4 questions are picked where its first answer was wrong but a human explanation fixed it. These are shown to the other agents as in-context examples, so they learn to write explanations that persuade that agent. An agent's own samples are left out of its prompt; adding them gave similar accuracy.
- **Stop and vote.** The loop ends at consensus or after the round limit. The team answer is the argmax over answers of the summed recalibrated confidences (a fixed function f applied to each stated confidence). Plain majority and uncalibrated weighting also work; the calibrated vote is "slightly better" and one f works across all seven tasks.

Assumes agents can follow long prompts and report usable confidence. Datasets with no human explanations simply drop the convincing samples.

## Evaluated on
- Beats single-agent and single-model multi-agent baselines on 5 benchmarks. On date understanding it scores 86.7 against 75.3 for the best debate baseline (+11.4); on StrategyQA 79.0 against 71.3. Math gains are smaller (GSM8K 85.3, AQuA 66.0) because ChatGPT is already strong there.
- Beats zero-shot GPT-4 on commonsense without using GPT-4: StrategyQA 79.0 vs 75.6, CSQA 74.7 vs 73.3. GPT-4 stays ahead on GSM8K (90.7 vs 85.3) and Date (89.0 vs 86.7).
- Works with other agent mixes. With GPT-4 as an agent, StrategyQA reaches 87.7 against 75.6 for zero-shot GPT-4. With GPT-4, Claude2 and DeepSeekMath, MATH reaches 58.3 against 48.7 for the best debate and 44.0 for GPT-4. ANLI reaches 57.7 vs 48.3 for debate.
- Model diversity is the largest single ablation factor. On StrategyQA, replacing the three models with three ChatGPTs drops accuracy from 79.0 to 72.2. Removing convincing samples gives 74.5, grouping 76.7, confidence 77.7. Response similarity (BERTScore) is lowest for the mixed team (0.8739) against 0.9102 for three ChatGPTs.
- Every agent improves, not only the team. ChatGPT goes from 71.0 to 77.0 over three rounds (StrategyQA), with team accuracy 74.3 to 79.0.
- Consensus is reached for all samples by round 3. The debate baseline still has 13% unresolved after round 4. Accuracy saturates after about two rounds.

## Limitations admitted by the authors
- The models are closed APIs, so their training data, scale and behaviour are unknown and uncontrollable. The GPT-4 comparison is affected: the paper notes GSM8K training samples may be in GPT-4's pre-training data.
- Confidence is a prompted verbal number, "post-hoc in nature". It is a self-report, and the vote depends on it.
- The method needs models that follow long instructions. The authors expect open models to fix this later; no evidence is given.

## Limitations found by others

## What it leaves untried
- Cost against accuracy. The team makes 3, 6 or 9 calls per question, but the only matched-compute comparison is self-consistency. Cost is not weighed against the stronger single model, and the 8-point MATH gain depends on GPT-4 being one of the agents.
- Whether stated confidence is calibrated. The ablation shows a 1.3-point gain from confidence (77.7 to 79.0), but no calibration measurement of the verbal scores is given.
- Larger or stricter testing. Main results use 100 samples per dataset, and a full-test-set check covers only two datasets. Tasks beyond short-answer reasoning are not tried.

## Topics
[[Topic - multi-agent debate and consensus]] · [[Topic - social choice]]
