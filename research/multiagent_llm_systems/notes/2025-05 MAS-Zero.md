---
title: "MAS-Zero: Designing Multi-Agent Systems with Zero Supervision"
authors: Zixuan Ke et al.
date: 2025-05
arxiv: 2505.14996
url: https://arxiv.org/abs/2505.14996
venue: arXiv (NeurIPS 2025 SEA Workshop)
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2505.14996.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "orchestration and delegation"]
---
# MAS-Zero: Designing Multi-Agent Systems with Zero Supervision

## One line
A meta-agent designs, critiques and rewrites a multi-agent system for each single question at inference time, with no validation set, and picks the final answer from the designs' outputs plus the plain single-agent outputs.

## Method
Problem: hand-built multi-agent systems (MAS) fit the underlying LLM poorly. Automatic designers (MaAS, ADAS, AFlow) need a labelled validation set, so they output one fixed MAS for the whole task set. They also cannot decompose a question or fall back to a simpler system. On hard tasks this shows: many of them barely beat plain chain-of-thought (CoT) on AIME24, and ADAS scores 0% on AIME24 with GPT-4o.

Three steps, all prompting with black-box LLM access:
- **MAS-Init**: run four fixed building blocks (CoT, CoT-SC, Debate, Self-Refine) on the question. Their outputs ground the design and stay in the candidate pool.
- **MAS-Evolve**: the meta-agent writes the MAS as executable code. It splits the question into sub-tasks and assigns each a sub-MAS by rewiring or re-parameterising the building blocks. It may not invent new agents or prune without grounding. It then runs the code and critiques it using sub-task and agent outputs, not only the final answer. The critique tests solvability (can each sub-task be solved alone by its sub-MAS) and completeness (do the sub-tasks together cover the question). Agents can emit a [TOO HARD] token. Each design, its outputs and its feedback go into an experience library that is fed to the next round (5 rounds).
- **MAS-Verify**: the meta-agent selects among all 9 candidates (4 blocks plus 5 evolved designs). It ranks by answer frequency, drops invalid answers, then picks the best one. Selection is easier than scoring each candidate alone. This is what lets the system revert to a simple block when that block is best.

The paper's reasoning: the intermediate signals are richer than sparse outcome correctness, and per-instance design avoids the mismatch of one tuned MAS.

## Evaluated on
- Beats every manual and automatic baseline on average for reasoning (AIME24, GPQA) with all three backbones. With GPT-4o: 41.97 average vs 33.91 for the best baseline (AFlow). AIME24 reaches 33.33 vs 20.83 for AFlow. The one loss to AFlow is on AIME24 with Qwen, by one question out of 24.
- Coding (SWE-Bench-Lite-Oracle): 25.83 vs 16.25 for AFlow with GPT-4o (58% relative gain). 16.74 vs 6.67 with Llama, a 149% gain.
- Agentic search: only a small average gain over the blocks (37.31 vs 37.19 for Debate). It loses to Debate and Self-Refine on Frames.
- Sits on the accuracy-cost Pareto front on all three GPT-4o benchmarks. It is much cheaper than AFlow, MaAS and ADAS, except ADAS on GPQA, which costs more for a 12% accuracy gain.
- Ablations on GPT-4o, average accuracy 41.97: removing MAS-Verify costs 21.70 points, MAS-Init 11.50, decomposition 8.96, meta-feedback 8.38. Accuracy at iterations 0 and 1 is clearly lower than later ones.
- Simple CoT and CoT-SC beat the automatic baselines MAS-GPT, ADAS and MaAS on several benchmarks. This is the argument for keeping the fallback.

## Limitations admitted by the authors
- Test-time token use is higher than for manual MAS. Cost is justified only against other automatic methods, which pay validation costs.
- The self-evolving signal is noisy and depends on the LLM. Sampling three feedbacks and choosing one lowered accuracy (31.77 vs 41.97), so a principled way to make feedback reliable is missing.
- Verification is the bottleneck. Using the last iteration instead of selection costs 21.70 points. An oracle verifier lifts GPQA to about 95%, so the self-verifier leaves most of the headroom unused. On Frames, errors grounded in retrieved text are hard to detect, so MAS-Zero loses there.
- The meta-agent role needs a strong LLM. GPT-OSS-20B, Qwen2.5-7B, Qwen2.5-Coder-3B and GPT-4.1-nano could not follow instructions or write valid Python.
- Performance is capped by the individual agents. A stronger meta-agent over GPT-4o agents gave 48.38 vs 83.38 with o3-mini in both roles.
- Five evolve iterations is the context-length maximum, so deeper evolution is not tested. Qwen2.5-32B was excluded from SWE because of its 32K context.

## Limitations found by others

## What it leaves untried
- A better verifier or external checker in MAS-Verify. The oracle result shows the headroom but no practical verifier is built.
- Training the meta-agent, or handing it to a small model, instead of prompting a frontier LLM.
- A new building block from the meta-agent. It is forbidden from inventing agents, so the design space stays limited to the four hand-made blocks.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - orchestration and delegation]]
