---
title: Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains
authors: Vighnesh Subramaniam et al.
date: 2025-01
arxiv: 2501.05707
url: https://arxiv.org/abs/2501.05707
venue: ICLR 2025
category: debate-cooperative-reasoning
pdf: research/multiagent_llm_systems/pdfs/2501.05707.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus", "self-refinement and critique loops"]
---
# Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains

## One line
Finetunes a society of copies of one base model, each on its own debate-generated data and in a generator or critic role, so that self-improvement keeps gaining over five rounds where single-model self-finetuning stalls after one.

## Method
Problem: self-improvement (finetune a model on its own outputs) plateaus within two or three rounds because the model's answers become similar in style and method, so the next round teaches it little new. The authors call the single-model case collapse onto a narrow range of responses.

Idea: do not finetune one model. Copy the base model into N generation agents and N critic agents (N = 3 in most runs), run a multiagent debate over unlabeled questions, and train each copy only on its own debate outputs.
- The debate answer is the majority vote of the last round. No ground-truth answers are used.
- Each generation agent is finetuned on its own first-round answers that match the majority. Since each agent's correct answers differ, the N datasets differ and the agents drift apart.
- Each critic agent is finetuned on its own multi-round trajectories that end at the majority answer. Two kinds are mixed with weight w: trajectories that started wrong and were corrected, and trajectories that started right and stayed right. The first teaches fixing errors, the second teaches not abandoning a correct answer.
- At inference, generators answer in round one. Critics then read a summary of the other agents' answers, revise, and a majority vote of the last round gives the answer. Summarising strips redundancy.
- Repeat with the finetuned agents generating the next round's data.

Why it should work: each agent trains only on what it got right, so it specialises on the problems it is already good at. A toy three-topic model in the appendix shows skill on whichever topic a copy leads in grows monotonically, so copies end up specialised on different topics. This is an illustration, not evidence about LLMs.

## Evaluated on
- Beats single-round baselines on math reasoning with one finetuning round on 500 unlabeled questions: e.g. MATH, GPT-3.5 60.6 vs 55.7 for plain debate and 53.0 for STaR, which uses ground-truth labels. Phi-3 58.8 on MATH vs 53.4 for debate. Gains hold on four base models (GPT-3.5, Phi-3, Mistral, LLaMA-3).
- Keeps improving over five rounds while single-agent finetuning saturates after one round and then drops: Phi-3 MATH 58.8 to 66.0, Mistral 22.5 to 28.2. This is 12.6 and 9.31 points above the best baseline.
- Diversity is preserved: four measures (likelihood of other agents' answers, embedding dissimilarity, consensus, KL) stay flat or rise for the multiagent version and fall for single-agent finetuning. Diversity and accuracy rise together across rounds, but this is a correlation across rounds, not a test of cause.
- Each part contributes. On GPT-3.5 MATH, removing the critics gives 50.8, removing summarisation 51.7, and single-agent finetuning 56.8, against 60.6 for the full method.
- Raising the sampling temperature to get diversity does not match it; the authors say higher temperature lowers accuracy through noisier samples. Giving a single model agent ID tags is close to plain debate (50.8 vs 51.6 on LLaMA-3 MATH, against 57.4 for the full method).
- Transfers zero-shot: agents finetuned on MATH reach 53.0 on 1000 GSM problems (Mistral), above baselines trained on GSM (best 49.7). Also helps on MMLU (68.8 vs 65.8 for debate, LLaMA-3). A cooperative merge-your-answers variant gains too (GPT-3.5 MATH 53.6 to 56.4).

## Limitations admitted by the authors
- Cost. N generators plus N critics must be trained and run. Open-model runs needed four H100 or A100 GPUs and 120-240 GB of GPU memory, and inference took 12-24 hours across GPUs. The gain is therefore bought with several times the compute of single-model finetuning.

## Limitations found by others

## What it leaves untried
- Majority-vote labels are right only when most agents are. On the hardest problems the majority may be wrong, and the paper does not measure how often wrong majorities enter training or how that grows across rounds. Gains were shown on math-style tasks and one MMLU run, all with 500 training questions.
- It never tests whether diversity causes the gain. The link is a correlation across rounds, and the toy model does not show it for real LLMs.
- The authors name weight sharing across agents, distilling the debate into one model, and quantisation as fixes for cost, plus combining with RLHF or DPO. None is run, so it is unknown whether the gains survive when the multi-model cost is removed.

## Topics
[[Topic - multi-agent debate and consensus]] · [[Topic - self-refinement and critique loops]]
