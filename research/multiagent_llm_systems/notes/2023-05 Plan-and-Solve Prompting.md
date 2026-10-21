---
title: Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models
authors: Lei Wang et al.
date: 2023-05
arxiv: 2305.04091
url: https://arxiv.org/abs/2305.04091
venue: arXiv (cs.CL)
category: framework-production
pdf: research/multiagent_llm_systems/pdfs/2305.04091.pdf
folder: ["multiagent_llm_systems"]
topics: ["reasoning prompting"]
---
# Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models

## One line
Replaces "Let's think step by step" with a trigger sentence that asks the model to first devise a plan and then carry it out (PS), and adds detailed instructions about variables and calculation (PS+), raising zero-shot reasoning accuracy with no demonstrations.

## Method
Zero-shot chain-of-thought (CoT) fails in three ways. On 46 wrong GSM8K answers from Zero-shot-CoT with GPT-3, the authors tag 7% as calculation errors, 12% as missing-step errors and 27% as semantic misunderstanding. These percentages are shares of the 100 sampled problems, not of the wrong answers.

The paper targets the first two with prompt text alone. It is a single model call, with no second agent and no tool.

- **PS:** the trigger becomes "first understand the problem and devise a plan... then carry out the plan and solve step by step". The aim is to stop the model skipping steps in long problems.
- **PS+:** the trigger adds "extract relevant variables and their corresponding numerals" and "calculate intermediate results (pay attention to calculation and commonsense)". The stated hypothesis is that a model that drops relevant variables is more likely to miss reasoning steps. The only evidence is a correlation analysis in which variable definitions correlate negatively with missing-step errors (-0.56) and with calculation errors (-0.41). That is 100 sampled problems and not a causal test.
- A second call then extracts the final answer from the generated reasoning text, as in Zero-shot-CoT. Decoding is greedy.

The mechanism is that more specific instructions in the trigger produce a more complete, better-structured reasoning text. The paper argues this without a causal test.

## Evaluated on
All results use GPT-3 text-davinci-003 on ten datasets: six math, two commonsense, two symbolic.

- **PS+ beats Zero-shot-CoT on every dataset.** Average math accuracy is 76.7 vs 70.4. The gain is at least 5 points everywhere except GSM8K, which gains 2.9 (59.3 vs 56.4). Commonsense: CSQA 71.9 vs 65.2, StrategyQA 65.4 vs 63.8. Symbolic: Last Letter 75.2 vs 64.8, Coin Flip 99.6 vs 96.8.
- **PS+ matches zero-shot Program-of-Thought and nears few-shot CoT without demonstrations.** On math, PS+ averages 76.7 against 73.5 for PoT, 77.6 for 8-shot Manual-CoT and 75.9 for Auto-CoT. It beats PoT on five of six math sets.
- **The instruction detail is what helps.** Prompts that only extract variables score worse than plain CoT on GSM8K (50.5 vs 56.4). Plan alone gives 58.2, and the full PS+ prompt gives 59.3. So extraction without a plan hurts.
- **Error types shift as claimed.** Of 100 sampled GSM8K problems, calculation errors fall from 7% to 5% and missing-step errors from 12% to 7%. Semantic errors stay at 27%.
- **Self-consistency stacks with it.** With 10 samples PS+ reaches 73.7 on GSM8K and 84.4 on SVAMP, against 70.7 and 81.7 for Zero-shot-CoT with the same voting.
- A sample of 100 PS outputs found a plan in 90 of them, so the model does follow the instruction.

## Limitations admitted by the authors
- The prompts are sensitive to wording and hand-tuned. The appendix shows Coin Flip moving from 70.6 to 99.6 purely through trigger rewording, so the gains cost per-task prompt design.
- Semantic misunderstanding, the largest error class at 27%, is untouched: PS+ is still 27% on it. The authors leave it for future work.
- Few-shot CoT stays ahead on some tasks, such as CSQA (78.3 vs 71.9) and StrategyQA (71.2 vs 65.4).

## Limitations found by others

## What it leaves untried
- Only one model family (GPT-3 text-davinci-003) is tested. The authors do not show whether the plan instruction helps stronger or weaker models, so the gain may be specific to this model.
- The plan is never checked or refined. The paper names plan refinement as future work, and 10 of 100 PS outputs contained no plan.
- The causal claim that extracting variables prevents missing steps rests on a correlation over 100 problems, with no ablation isolating it.

## Topics
[[Topic - reasoning prompting]]
