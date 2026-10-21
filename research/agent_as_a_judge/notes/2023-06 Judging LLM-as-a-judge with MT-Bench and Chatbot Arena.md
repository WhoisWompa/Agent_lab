---
title: Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena
authors: Lianmin Zheng et al.
date: 2023-06
arxiv: 2306.05685
url: https://arxiv.org/abs/2306.05685
venue: NeurIPS 2023 Datasets and Benchmarks
category: alternative-paradigms
topics: ["LLM and agent judges", "judge and decision-model audits", "alternative evaluation paradigms", "presentation sensitivity"]
---
# Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena

## One line
Introduces MT-Bench and early Chatbot Arena; GPT-4 judge agrees with humans over 80%, on par with human-human agreement, while naming position, verbosity and self-enhancement biases.

## Method


## Evaluated on
- (llm-judge-foundations) MT-Bench (80 multi-turn questions, 3K expert votes) and 30K Chatbot Arena conversations. GPT-4 pairwise vs humans on MT-Bench (non-tie votes): 85% vs human-human 81%. Chatbot Arena: 87% (non-tie), 64% with ties. Position consistency on swap (default prompt): GPT-4 65.0%, GPT-3.5 46.2%, Claude-v1 23.8%; few-shot raises to 77.5% / 55.0% / 63.7%. 'Repetitive list' verbosity attack fools Claude-v1 and GPT-3.5 91.3% of the time, GPT-4 8.7%. Self-enhancement: GPT-4 ~10% and Claude-v1 ~25% higher win rate for themselves than humans give. Math grading failure on 10 questions: default 70%, CoT 30%, reference-guided 15%.

## Limitations admitted by the authors
- Limited math/reasoning grading ability; position, verbosity and self-enhancement bias.
- Position bias toward the first slot in most judges.
- Verbosity bias (repetitive, longer answers favoured).
- Self-enhancement bias suggested but not conclusively established (limited data, small differences).
- Weak at grading math and reasoning; judges are misled by the answers they read.
- Only helpfulness is judged; safety and honesty are neglected; several quality dimensions are merged into one score.
- Multi-turn prompt designs can make the judge mis-identify which response is meant.

## Limitations found by others
- The '80%+ human agreement' headline counts non-tie votes and uses exact-match agreement; Norman et al. 2026 (2606.19544) show exact-match overstates discrimination, with a 33-41 pp gap to Cohen's kappa on MT-Bench.
- Zheng et al. 2024 null-model attack (2410.07137): a constant, input-independent response scores 9.55 on MT-Bench.
- Thakur et al. 2024 (2406.12624): even in a clean setting with high inter-human agreement only the largest judges approach humans, and scores can differ by up to 5 points while percent agreement looks high.
- Wang et al. 2023 (2305.17926): position bias alone can let Vicuna-13B beat ChatGPT on 66/80 queries.

## What it leaves untried
- Swap-and-tie is a conservative patch; the paper does not test whether ties hide real preferences or measure the cost in discriminative power.
- No adversarial robustness study of the judge (later done by Raina 2024, JudgeDeceiver, null models).

## Topics
[[Topic - LLM and agent judges]] · [[Topic - judge and decision-model audits]] · [[Topic - alternative evaluation paradigms]] · [[Topic - presentation sensitivity]]
