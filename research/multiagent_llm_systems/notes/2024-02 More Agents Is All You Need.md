---
title: More Agents Is All You Need
authors: Junyou Li et al.
date: 2024-02
arxiv: 2402.05120
url: https://arxiv.org/abs/2402.05120
venue: TMLR (10/2024)
category: debate-cooperative-reasoning
pdf: research/multiagent_llm_systems/pdfs/2402.05120.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus", "reasoning prompting"]
---
# More Agents Is All You Need

## One line
Sampling the same LLM many times and taking a majority vote (Agent Forest) raises accuracy steadily with the number of samples, often matching or beating more elaborate prompting and multi-agent frameworks.

## Method
The problem: multi-agent frameworks (debate, reflection) and prompt tricks (chain of thought) are credited with gains, but nobody had isolated how much comes from simply having more agents. The paper strips the idea to two steps. Sample: run the query N times through one LLM, or through any existing method (CoT, debate, reflection) as a plug-in. Vote: pick the answer most similar to all the others. For multiple-choice and math this is the most frequent answer; for code it is the sample with the highest summed BLEU similarity to the rest. No training, no extra prompts, no communication between the agents.

The second half explains where the gain is largest, using a synthetic task (sum of S products of integers in [-I, I], answer a bucket out of K) that varies three difficulty dimensions separately. Gains first rise then fall as inherent difficulty (I) grows, because past some point the model cannot solve the task at all. Gains rise with the number of steps S, because errors accumulate across steps and voting repairs each one. Accuracy rises with the prior probability of the right answer (1/K). Two add-ons follow from this. Step-wise Agent Forest decomposes the task and votes at each step. Hierarchical Agent Forest first solves a coarse version (K=8) then a fine one (K=32), possibly with a cheaper model first and a stronger one second.

## Evaluated on
- Accuracy grows with ensemble size (up to 40) on every model and task: GSM8K gains of 12 to 24 points, MATH 6 to 10, MMLU 5 to 11, HumanEval 4 to 9, Chess only 1 to 4.
- Small models overtake larger ones: Llama2-13B reaches 59% on GSM8K against 54% for a single Llama2-70B query; 70B and GPT-3.5 also reach their larger counterparts at ensemble sizes 15 and 20 (Figure 1).
- It stacks with other methods: adding voting to CoT, zero-shot CoT, SPP, debate and reflection gives gains up to 27 points (SPP on GSM8K, 70B). Standalone voting has the best average rank (2.5 overall) against 2.7 to 4.4 for the others, so the prompting and collaboration machinery adds little over voting alone.
- Gains are larger for harder problems and weaker models: relative gain on MATH vs GSM8K is 34 to 200% vs 16 to 69%; GPT-3.5 gains 8 to 16% in a given task against 28 to 200% for Llama2-13B.
- The extensions help: hierarchical voting lifts a K=32 task from 21% to 31% with GPT-3.5, and from 35% (GPT-4 alone) to 47% when GPT-3.5 gives the coarse answer and GPT-4 the fine one. Step-wise voting gives 15 to 42% gains, rising with difficulty.

## Limitations admitted by the authors
- Cost grows linearly with ensemble size (token usage scales proportionally, and more when combined with other methods); the authors only note that identical inputs could allow cheaper sampling and leave it as future work.
- Voting plus debate failed on code for Llama2-13B and 70B (HumanEval 0 both with and without voting), which they attribute to other agents' answers corrupting code logic. Combining is therefore not always safe.
- Returns shrink at extreme difficulty: gains fall at I=400 because the task exceeds the model's ability. Voting cannot fix a model that is mostly wrong.
- Debate runs were capped at ensemble size 10 versus 40 for the others, because of communication overhead.

## Limitations found by others

## What it leaves untried
- No cost-matched comparison: the headline that voting beats other methods is at 40 samples versus a single run of each, so it is unclear how voting compares at equal token budget (the paper gives per-call token counts, not budget-matched accuracy).
- No analysis of when voting fails by design: it needs the correct answer to be the plurality. The paper does not test tasks where errors are correlated across samples (Chess shows only 1 to 4 point gains, unexplained).
- The scaling is shown only on Llama2 and GPT-3.5/4, and the difficulty study uses a single synthetic arithmetic task on GPT-3.5, so whether the three properties hold elsewhere is unsupported.

## Topics
[[Topic - multi-agent debate and consensus]] · [[Topic - reasoning prompting]]
