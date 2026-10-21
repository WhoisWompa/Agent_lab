---
title: Multi-LLM Debate: Framework, Principals, and Interventions
authors: Estornell et al.
date: 2024-12
arxiv: none
url: none
venue: NeurIPS 2024
category: debate-cooperative-reasoning
pdf: research/multiagent_llm_systems/pdfs/neurips2024-estornell-liu-multi-llm-debate.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus"]
---
# Multi-LLM Debate: Framework, Principals, and Interventions

## One line
Models debate as Bayesian updating over latent concepts, which predicts that debate collapses to the majority view (including shared errors), and three interventions (diversity pruning, quality pruning, misconception refutation) are added to counter it.

## Method
Problem: in standard debate (Du et al.), every agent reads all previous answers and re-answers. The authors argue this is unreliable because the answers act like in-context examples. Each agent infers a latent concept from the task and the other agents' answers, and the other answers reweight its generation by a "skew term" (product of their likelihoods under each concept). Debate is then an optimisation: choose the round's answers so the next round is more likely correct.

Theory, under the assumption that output depends only on the inferred concept and the model parameters:
- With n identical models, the most likely concept stops changing as n grows (Theorem 5.1): static dynamics.
- With m similar answers in the pool, the next answer is determined by their shared concept as m grows (Theorem 5.2): tyranny of the majority.
- If m agents share a misconception (an erroneous concept the model finds more plausible than the true one), final accuracy falls monotonically as m rises (Theorem 5.4). More models do not fix it when they share training data.

Interventions change what the agents see, not who debates:
- Diversity pruning: keep the k answers that are most different from each other, so no single concept dominates.
- Quality pruning: keep the k answers closest to the task.
- Misconception refutation: an LLM lists errors in each answer, then rewrites it with minimal changes.

Each comes with a theorem that it lowers the chance of converging to the wrong concept or raises the chance of the right one. Because concept distributions are intractable, similarity is proxied by sentence-embedding distance (ADA-2). Applied together in the order quality, diversity, refutation, over all past answers.

## Evaluated on
Four tasks (BoolQ, MMLU, TruthfulQA, arithmetic), four 7B-to-GPT-3.5 models, six agents, ten rounds, against Du et al.'s debate.
- Majority pressure is real: the chance a model echoes an answer rises with how many of 11 other answers give it, and diversity pruning (k=5) reduces this (Figure 1; no numbers in text).
- Debate helps less when first-round answers are similar: baseline gain falls as cosine similarity rises on BoolQ, MMLU and TruthfulQA, while the proposed method's edge is largest there.
- The combination matches or beats baseline debate in every cell. Examples: 6x GPT-3.5 on MMLU 0.79 vs 0.74 (single 0.73); 6x Llama-3 on arithmetic 0.48 vs 0.33 (single 0.25); GPT-3.5 plus Mistral on arithmetic 0.68 vs 0.56.
- Mixed-model teams gain too: GPT-3.5 plus Mistral on BoolQ 0.87 vs 0.83.
- The gap opens in later rounds (Figure 3), consistent with the claim that early rounds are not where echo chambers form.
- Parts alone are unreliable: pruning alone can fall below a single model (Mistral on MMLU, diversity pruning 0.58 vs single 0.66), so the gain comes from the combination.

## Limitations admitted by the authors
- The theory needs a latent concept space that cannot be observed, so embeddings stand in. Pruning works poorly where embeddings are uninformative: arithmetic answers all look alike, and the similarity trend does not appear on that task.
- Inference time rises, mostly from misconception refutation, which re-prompts every debater several times. The paper gives per-run times for the baseline setup (4 hours for open models, 12 for GPT-3.5 per 3,000 questions) but not the cost of the interventions.
- Individual interventions can hurt (see above); the benefit depends on using all three, in a fixed order that the paper chose empirically.

## Limitations found by others

## What it leaves untried
- The pruning step is an inexpensive way to damp majority pressure, but the paper never tests whether a stronger or differently trained model in the pool (rather than reshuffled answers) breaks a shared misconception, which the theory says more copies cannot.
- The theorems assume the latent-concept model holds for real LLMs; no experiment checks the assumption directly, only its predicted trends.
- Gains over baseline are not compared with a plain ensemble or self-consistency vote at equal compute, so the added value of exchange and the cost of refutation are not separated.

## Topics
[[Topic - multi-agent debate and consensus]]
