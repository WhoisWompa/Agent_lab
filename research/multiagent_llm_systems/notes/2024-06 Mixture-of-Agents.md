---
title: Mixture-of-Agents Enhances Large Language Model Capabilities
authors: Junlin Wang et al.
date: 2024-06
arxiv: 2406.04692
url: https://arxiv.org/abs/2406.04692
venue: arXiv (preprint, under review)
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2406.04692.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus", "role-based agent teams", "communication topology and channels"]
---
# Mixture-of-Agents Enhances Large Language Model Capabilities

## One line
Stacks several layers of different LLMs, each layer reading all answers from the layer before and synthesizing a better one, so a team of open-source models beats GPT-4o on AlpacaEval 2.0 with no fine-tuning.

## Method
The problem: scaling a single model is expensive, yet different LLMs have different strengths. The paper's observation, which it calls "collaborativeness", is that an LLM answers better when shown other models' answers, even when those answers are worse than what it would write alone (shown for six popular LLMs on AlpacaEval 2.0, Figure 1; no per-model numbers in the text).

Mixture-of-Agents (MoA) turns that into a layered structure. Layer 1 agents answer the prompt independently. Every agent in layer 2 receives the prompt plus all layer-1 answers, wrapped in one "aggregate and synthesize" prompt that tells it to criticise the answers, since some may be biased or wrong, and not copy them. This repeats for l layers, and one model in the last layer writes the final output. Models can be reused within and across layers. It runs purely through prompting, with no training and no gating network. The authors frame it as a model-level analogue of Mixture-of-Experts, where the LLM itself plays both gate and expert.

Models take two roles. Proposers supply diverse reference answers, even if their own score is mediocre. Aggregators merge inputs and should stay good when inputs are weaker than their own output. Layer membership is chosen by two criteria: past win rate and diversity of outputs. The default uses six open models over 3 layers with Qwen1.5-110B as final aggregator. Variants are MoA w/ GPT-4o (GPT-4o as final aggregator) and MoA-Lite (2 layers, Qwen1.5-72B as final aggregator).

## Evaluated on
- Beats the strongest closed model on AlpacaEval 2.0 with open models only: length-controlled win rate 65.1% for MoA vs 57.5% for GPT-4o. With GPT-4o as final aggregator it reaches 65.7%. MoA-Lite gets 59.3%.
- Gains are small on MT-Bench, where single models already score above 9 out of 10: 9.25 for MoA vs 9.19 for GPT-4o, and 9.40 for the GPT-4o-aggregator variant. The authors still call it first place.
- On FLASK, MoA beats its own aggregator (Qwen1.5-110B) on robustness, correctness, factuality, completeness and others, and beats GPT-4o on correctness, factuality, insightfulness, completeness and metacognition. It is slightly more verbose.
- The aggregator is synthesizing, not picking. Using the same aggregator as a ranker that selects one proposal scores clearly lower (shown in a figure, no number in the text). The aggregator's text also resembles the proposals the evaluator preferred, with positive Spearman correlation for BLEU, TF-IDF and Levenshtein similarity.
- Diversity and width both help. With 6 proposers, different models give 61.3% against 56.7% for one model sampled six times. One proposer gives 47.8%, and more proposers generally help. Roles are real: WizardLM 8x22B is the best proposer (63.8%) but a weak aggregator (52.9%), while Qwen1.5-110B is strong at both (61.3% as aggregator, 56.7% as proposer).
- Cost: MoA-Lite matches GPT-4o's cost with higher quality, and beats GPT-4 Turbo by about 4% while costing more than twice less. MoA and MoA-Lite lie on the cost and compute Pareto front. Latency is proxied by TFLOPs, with GPT-4's size taken from a rumored 8x220B architecture, so that comparison is unverified.
- Appendix: on MATH, accuracy rises with each added layer (for example Qwen1.5-72B from 0.428 to 0.552 over three layers), and the authors say it is complementary to chain of thought and self-consistency (stated, not tested here).

## Limitations admitted by the authors
- Time to first token is high: nothing can be streamed until the last layer finishes, which hurts user experience. They suggest fewer layers, noting the first aggregation gives the largest boost, and chunk-wise aggregation, which they do not test.
- The design choices (layer count, model per layer, aggregator) are hand-picked; "systematic optimization of MoA architecture" is left as future work.
- MT-Bench improvements are marginal, which the authors attribute to a ceiling effect.

## Limitations found by others

## What it leaves untried
- Judging quality is almost entirely by GPT-4-based evaluators (AlpacaEval, MT-Bench, FLASK) that also score the GPT-4 baselines. Human checks and verifiable-answer tasks beyond one MATH table are missing, so the gain may partly reflect evaluator preference.
- No comparison with debate-style multi-round exchange or a stronger single-agent prompt under equal compute, even though the related work cites a study finding the latter comparable to multi-agent approaches.
- No test of whether the aggregator can recover when most proposals are wrong, beyond two hand-picked case studies.

## Topics
[[Topic - multi-agent debate and consensus]] · [[Topic - role-based agent teams]] · [[Topic - communication topology and channels]]
