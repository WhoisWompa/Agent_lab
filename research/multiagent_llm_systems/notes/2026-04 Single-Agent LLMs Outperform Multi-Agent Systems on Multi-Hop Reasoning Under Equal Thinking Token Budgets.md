---
title: Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets
authors: Dat Tran et al.
date: 2026-04
arxiv: 2604.02460
url: https://arxiv.org/abs/2604.02460
venue: arXiv (preprint, under review)
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2604.02460.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels", "multi-agent debate and consensus"]
---
# Single-Agent LLMs Outperform Multi-Agent Systems on Multi-Hop Reasoning Under Equal Thinking Token Budgets

## One line
Once the thinking-token budget is held equal, a single agent matches or beats five multi-agent designs on multi-hop questions, and an information-theoretic argument says why and when that flips.

## Method
The problem: reported gains of multi-agent systems (MAS) are confounded by extra test-time compute, since MAS spend more tokens across calls. The paper fixes the total thinking-token budget B (reasoning tokens only, not prompts or answers) and compares one agent that gets all of B in one call (SAS) against MAS that split B across planner, workers and aggregator.

The theory is the Data Processing Inequality. Messages M passed between agents are a function of the full context C, so I(Y;C) >= I(Y;M). The best achievable error with C is therefore never worse than with M, because a single agent can simulate the message channel internally. Under a fixed budget and perfect context use, SAS cannot lose to MAS in information terms.

The argument also gives a prediction. If the single agent's effective context is degraded (deleted, masked, substituted or distracting content), its information drops, and a MAS that filters or factorises may recover more. MAS still cannot exceed the information in the clean context. The theory is a bound on information, not a proof about trained LLMs. Whether real models behave this way is left to the experiments.

The main comparison is SAS against Sequential MAS (planner, k steps each with B/k, aggregator). It is the cleanest analogue because it differs only in making intermediate reasoning explicit messages instead of latent. Subtask-parallel, parallel-roles, debate and ensemble variants are also run, plus SAS-L, a single agent prompted to analyse ambiguities before answering.

## Evaluated on
- SAS is the best or statistically tied system at every budget from 500 to 10,000 tokens, across Qwen3-30B-A3B, DeepSeek-R1-Distill-Llama-70B and Gemini 2.5 Flash and Pro, on FRAMES and 4-hop MuSiQue. At 100 tokens nobody reasons usefully. Averaged over all model and dataset cells, SAS is 0.427 against Sequential 0.386 at 5k tokens, and 0.426 against 0.387 at 10k.
- SAS also uses fewer thinking tokens. For Qwen3 on FRAMES at the 10k cap, SAS averages 1,307 tokens, Sequential 1,808, Debate 4,061.
- Debate is the strongest MAS variant. Ensemble can top single-agent scores only on Gemini-2.5-Pro FRAMES at 5k and 10k (0.710 and 0.719 against 0.700 and 0.692), and there it spends several times the tokens.
- Context degradation, on Qwen3 with MuSiQue at 1,000 tokens, shows a crossover. Under masking at 70%, Sequential beats SAS (0.231 against 0.220). Under substitution at 70% it is 0.225 against 0.200. At 30% corruption SAS leads, 0.243 against 0.217 for substitution. Distractor sentences never produce a crossover, so SAS stays ahead.
- Across Gemini versions with no token cap, SAS is equal or slightly ahead of Sequential (Gemini-2.5-Pro 0.399 against 0.396, Gemini-3-Pro-Preview 0.491 against 0.489). The two sets of 95% intervals overlap in several rows, so these are ties more than wins.
- Error analysis: SAS wins by staying close to the question constraints. Sequential wins when its breadth reaches the gold answer, but it often drifts or drops a correct span at the end (23 such cases for Gemini-Flash). The gold answer appears in SAS thoughts in 42.7% of SAS-right cases against 18.6% for MAS.

## Limitations admitted by the authors
- Text-only multi-hop reasoning. Tool use, vision and safety settings, where MAS may help, are out of scope, so the claim does not cover them.
- Gemini's thinking accounting is unreliable. For Flash at a 10k request the API reported 1,687 thinking tokens against about 359 visible tokens (4.7x), and visible thought plateaus near 350 tokens for SAS. So the budgets are matched on the requested cap, not on tokens actually spent, and this can tilt Gemini comparisons.
- Only an upper cap on thinking is enforced, with no lower bound, so models may leave budget unused. Equal budget is not equal compute used.
- The benchmarks have an artifact. Deep LLM paraphrase of questions raised Gemini-Flash SAS from 0.331 to 0.358 while regex paraphrase lowered it, which hints at memorisation. This could inflate any system's score.

## Limitations found by others

## What it leaves untried
- The degradation crossover is shown on one open model, one dataset and one budget (Qwen3, MuSiQue, 1,000 tokens). Whether real long or noisy contexts cause the same degradation, and at what level, is not measured.
- It does not test an adaptive system that chooses SAS or MAS by estimated context quality. Its own result implies such a switch would capture both regimes.
- Tool-using or heterogeneous-model MAS, where information is genuinely not available to one agent, are not run. There the single-agent bound does not apply.

## Topics
[[Topic - communication topology and channels]] · [[Topic - multi-agent debate and consensus]]
