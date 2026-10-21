---
title: "MapCoder: Multi-Agent Code Generation for Competitive Problem Solving"
authors: Md. Ashraful Islam et al.
date: 2024-05
arxiv: 2405.11403
url: https://arxiv.org/abs/2405.11403
venue: arXiv
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2405.11403.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams", "self-refinement and critique loops"]
---
# MapCoder: Multi-Agent Code Generation for Competitive Problem Solving

## One line
Four prompted LLM agents (retrieval, planning, coding, debugging) imitate a programmer's cycle, and a confidence-ordered traversal over plans lets the system fix code using only the problem's sample input/output.

## Method
The problem: single-pass or chain-of-thought prompting fails on competition-level code, and the reflection methods that fix this (Reflexion, AlphaCodium) depend on LLM-written extra test cases. Those tests can be wrong. The authors report that 8% of Reflexion failures on HumanEval and 15% on MBPP come from incorrect generated tests, and that Reflexion with ChatGPT drops 26.3% on HumanEval.

MapCoder is a fixed pipeline of four roles, all the same underlying LLM:
- **Retrieval agent**: no external retriever. The LLM writes k similar but distinct problems with code and a plan, then names the relevant algorithm and a short tutorial. The authors say this instruction order is crucial, but show no ablation of it.
- **Planning agent**: writes one plan per recalled example (not one merged plan, so irrelevant examples do not contaminate the others) and then scores each plan with a 0-100 self-rated confidence.
- **Coding agent**: turns the top-scored plan into code and runs it on the sample I/O.
- **Debugging agent**: on failure, receives the code, the test log and the plan, and repairs up to t times. Using the plan as the reference for the fix is claimed as the key difference from plain reflection.

Dynamic traversal: try plans in descending confidence. If the code passes the sample I/O it is returned. Otherwise debug up to t times, then fall to the next plan, up to k plans. Cost is O(kt). The only test signal is the sample I/O in the problem statement, so the harness (not the LLM) decides pass or fail, and the confidence score only orders plans and is never checked for calibration.

## Evaluated on
- New best pass@1 across benchmarks with GPT-4: HumanEval 93.9% (Reflexion 91.0%, Direct 80.1%), CodeContest 28.5% (Direct 12.1%), APPS 22.0% (Direct 12.7%).
- Gains are largest on hard problems with ChatGPT: CodeContest 12.7% vs 5.5% direct (+132.8%), against +67.3% on HumanEval.
- Matches a rival at lower sampling: CodeContest pass@1 28.5% equals AlphaCodium's pass@5 of 29%. At pass@5 with GPT-4, MapCoder reaches 35.2%.
- Every agent matters (ChatGPT, HumanEval, full system 80.0%): removing debugging alone costs 17.5 points, removing planning alone 12.5, and removing retrieval alone 5.0.
- Transfers across models: Gemini Pro 69.5% vs 64.6% direct on HumanEval, and Mistral-7B 57.6% vs 27.3%. Gains are smaller on Gemini's CodeContest (4.8% vs 3.6%).
- More plans or debug attempts buy accuracy at the cost of time: HumanEval rises from 62.8% to 80.5% as t goes from 0 to 5 at k=3, and k=5 adds nothing at t=5 (80.5% both).

## Limitations admitted by the authors
- Cost: an average of 16.7 API calls and 21.25k tokens per problem, against 1 call and 0.64k tokens for direct prompting. Token use was not optimised.
- Dependence on sample I/O: there are only 2.82 per HumanEval problem, so passing them does not mean the code is right. Adding 5 more samples gave a 1.5% gain, which suggests the limited signal costs accuracy.
- Hard problems stay hard: gains are limited above difficulty 1000 on xCodeEval. Combinatorics, constructive, number theory, divide-and-conquer and DP are mostly unsolved. In five DP problems inspected by hand, the agents misread the problem, fell back to greedy or brute force, or built the DP table wrongly.
- Running generated code needs a sandbox; the paper does not provide one.
- Only closed models were tested in depth; open-source code models (CodeLlama, Llama 3, Mixtral) are listed as future work.

## Limitations found by others

## What it leaves untried
- No ablation of the confidence ordering against random plan order, and no check that the self-rated score predicts correctness. The "dynamic traversal" claim is untested on its own.
- No equal-budget comparison: MapCoder uses roughly 16 times the calls of direct prompting, and the baselines get one call each. Part of the gain may simply be more samples.
- Retrieval, planning and debugging are the same LLM with different prompts, so errors are likely to be shared. A different model per role is not tried.

## Topics
[[Topic - role-based agent teams]] · [[Topic - self-refinement and critique loops]]
