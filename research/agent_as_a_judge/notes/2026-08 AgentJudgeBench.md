---
title: AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling
authors: Abhigya Verma et al.
date: 2026-08
arxiv: 2608.26623
url: https://arxiv.org/abs/2608.26623
venue: EMNLP 2026
category: agent-as-judge
topics: ["judge and decision-model audits", "agent evaluation benchmarks"]
---
# AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling

## One line
Benchmark of 3,808 tool-calling workflow instances across DAG topologies and difficulty tiers, showing judge alignment hits a 77-82% ceiling on hard queries regardless of judge size.

## Method
- Six workflow DAG topologies x three difficulty tiers; five generators (3B-70B open + GPT-5.4); six judges (~20B to frontier, incl. QwQ-32B, GPT-OSS-120B, Gemini-2.5-Pro); with and without ground truth. Non-agentic judges.

## Evaluated on
- Alignment degrades 1.5x faster without ground truth; on hard no-GT queries all judges fall in 77-82%. Ground truth can lower alignment (GPT-5.4 -1.5, Gemini-2.5-Pro -3.9 pts) via over-anchoring. Rubrics up to +6.5 pts, not uniform across pairs. CoT and temperature negligible.

## Limitations admitted by the authors
- No explicit limitations at abstract level; rubric gains and the ceiling are prompt/generator dependent.

## Limitations found by others


## What it leaves untried
- Testing whether tool-using judges that execute the workflow break the hard-query ceiling.

## Topics
[[Topic - judge and decision-model audits]] · [[Topic - agent evaluation benchmarks]]
