---
title: Let Models Speak Ciphers: Multiagent Debate through Embeddings
authors: Chau Pham et al.
date: 2023-10
arxiv: 2310.06272
url: https://arxiv.org/abs/2310.06272
venue: ICLR 2024
category: debate-cooperative-reasoning
pdf: research/multiagent_llm_systems/pdfs/2310.06272.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus", "communication topology and channels"]
---
# Let Models Speak Ciphers: Multiagent Debate through Embeddings

## One line
CIPHER lets debating LLMs pass each other the probability-weighted average of vocabulary embeddings instead of a sampled token, so no belief is thrown away, and it beats natural-language debate by 0.5-5.0% with no weight changes.

## Method
Problem: in debate, each agent writes text, and writing text means sampling one token per position. That collapses the model's whole next-token distribution into a single choice. When the most likely token is wrong, the correct one is discarded. The paper's example is LLaMA-2-70B writing "9" where "6" was right. Earlier debate and self-refinement work also works mainly with GPT-4-class models, and the paper reports weaker open models gain little from it.

Idea: drop the sampling step. At each position the agent computes the softmax distribution over the vocabulary and emits the expectation of the token embeddings under it. That vector is fed straight back into the model as the next input, and sent to the other debaters as their input. Generation stops when the nearest vocabulary embedding to the new vector is the end-of-sequence token. Each debater sees the question plus every debater's embedding-form answer from the previous round. At the end the vectors are mapped back to words by nearest-neighbour search, so humans can still read the result. It needs no training. It requires debaters that share a tokenizer. If their embedding tables differ (LLaMA-65B and LLaMA-2-70B), the average is taken with the receiver's table.

Why it should work: the authors compare it to Expected SARSA, which replaces a sampled action value with its expectation over actions and has lower variance than SARSA. Averaging keeps information exactly where the model is unsure. They support this with an ablation: using CIPHER only at high-uncertainty positions (by entropy or max-probability) tracks full CIPHER, while using it only at confident positions drops accuracy "hugely" (no figure given in the text).

Final answer: take the debater with the lowest temperature. Majority vote is unsuited to two-agent or open-ended debates, and this choice is cheaper because only one model runs the last round. Best results pair a low-temperature debater with a high-temperature one. The high-temperature debater's flatter distribution carries the low-confidence alternatives the other one drops.

## Evaluated on
- Beats natural-language debate (NLD) on five reasoning sets with two LLaMA-family models, by 1.0-5.0%. For LLaMA-2-70B: GSM8K 66.0 vs 64.8, Formal Logic 52.4 vs 49.2, Arithmetic 85.0 vs 81.1. It also beats five-sample majority vote on every set but one (Arithmetic 85.0 vs 79.7).
- Helps weaker open models: on GSM8K the gain over NLD is 0.5-3.5% across Falcon-40B-Instruct, MPT-30B, WizardMath-70B and others.
- Mixed-model debate works: on Arithmetic, LLaMA-65B rises from 35.0% in round 1 to 62.5% in round 3 when debating LLaMA-2-70B. NLD reaches 60.5%.
- Output is deterministic (standard deviation 0.0), while the baselines vary by 0.5-3.0% across datasets from token sampling.
- More rounds and more debaters help both CIPHER and NLD, with small gains at higher cost.

## Limitations admitted by the authors
- Only works across models that share a tokenizer. Different tokenizers split words differently and aligning their embedding-vocabulary mappings is unsolved. The authors expect open LLaMA-family models to keep this usable.
- Debate can hurt a weak model. With LLaMA-2-7B on GSM8K, a CIPHER debate scores 17.5% against 15.0% alone, while a nonsense debate partner drops it to 0.0% (misaligned partner 11.3%). The 70B model is robust to bad partners.
- Results are sensitive to temperature pairs, which were tuned by Bayesian optimization for each method on a 200-question validation set. A mismatched pair loses accuracy, so the gain depends on tuning. When debaters have different temperatures, swapping the order of their answers in the prompt changes accuracy by up to roughly 15 points (read off a figure).
- The intermediate "ciphers" are not natural language. Humans see them only through nearest-neighbour decoding, and the sample decoding in the appendix is partly garbled text. The claim that they are interpretable is shown on one example only.

## Limitations found by others

## What it leaves untried
- Closed or different-tokenizer models. The paper never tests GPT-class models, which prior debate work depended on.
- Any explanation of why the model can read an averaged vector it was never trained on. The paper offers the Expected SARSA analogy and one attention heatmap with a few bright spots, which is weak evidence.
- Comparison with other ways of keeping uncertainty in text debate, such as sharing top-k tokens or verbalised confidence. NLD is the only debate baseline.

## Topics
[[Topic - multi-agent debate and consensus]] · [[Topic - communication topology and channels]]
