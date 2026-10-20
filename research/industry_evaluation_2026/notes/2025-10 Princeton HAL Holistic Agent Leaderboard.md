---
title: "Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation" (and HAL Reliability)
org: Princeton (Kapoor, Narayanan et al.)
date: 2025-10
url: https://hal.cs.princeton.edu/
kind: third-party-evaluator
category: third-party-and-benchmarks
---
# HAL: Holistic Agent Leaderboard (Princeton)

## One line
An academic third-party agent leaderboard and harness (paper at ICLR 2026). It runs many agents on many benchmarks at once, inspects logs with LLMs to find shortcuts, and in 2026 shifted from leaderboard updates to measuring reliability.

_Added by eval-tooling researcher (2026-10-20):_ HAL (ICLR 2026) is a standardised, cost-aware agent evaluation harness and leaderboard that ran 21,730 rollouts (9 models × 9 benchmarks, ~$40k) and used LLM-assisted log inspection to find shortcuts and unsafe actions.

## What they do
- **Harness**: a standardised harness that runs evaluations in parallel across many VMs. It reports accuracy together with cost.
- **Log inspection**: LLM-aided inspection of agent logs to find shortcuts and misbehaviour.
- **Validation run**: 21,730 rollouts across 9 models and 9 benchmarks ([arXiv 2510.11977](https://arxiv.org/pdf/2510.11977); [ICLR 2026](https://iclr.cc/virtual/2026/poster/10006806)).
- **Reliability follow-up**: "Towards a Science of AI Agent Reliability" ([arXiv 2602.16666](https://arxiv.org/pdf/2602.16666v2)) proposes a profile of 12 metrics covering:
  - consistency;
  - robustness;
  - predictability;
  - error severity.
- **Reliability Dashboard**: published at hal.cs.princeton.edu/reliability.

_Added by eval-tooling researcher (2026-10-20):_ Parallel harness across VMs (weeks → hours); reports cost alongside accuracy; scaffolds strongly affect accuracy and cost; LLM-assisted log review found agents searching HuggingFace for answer keys and misusing credit cards in flight booking; released 2.5B tokens of logs (https://proceedings.iclr.cc/paper_files/paper/2026/hash/a0928f924a344aaebbb7f6cd8d56e34c-Abstract-Conference.html).

## Evidence
- Higher reasoning effort reduced accuracy in the majority of runs.
- Agents were found searching HuggingFace for a benchmark's answer key instead of solving the task.
- The HAL site says the team has paused updating the leaderboard with new models to focus on reliability.
- Secondary summary of the reliability paper ([TinyFish](https://current.tinyfish.ai/issue/29/foundations/article/16274/what-a-benchmark-score-actually-contains)), not verified against the paper:
  - Across 14 models over 18 months, accuracy rose while reliability barely moved on open-ended tasks such as GAIA.
  - A GPT-4o agent scored over 60% on a single tau-bench run, but its pass rate fell below 25% when the same task was run 8 times.

_Added by eval-tooling researcher (2026-10-20):_ Finding: higher reasoning effort reduced accuracy in most runs. GitHub princeton-pli/hal-harness 308 stars, archived (last push 2026-07-01) per GitHub API.

## Limitations and criticisms
- The leaderboard is no longer updated, so it does not cover 2026 frontier models.
- Princeton's comment on NIST AI 800-2 argues that reliability should be a primary evaluation objective ([Princeton](https://sage.cs.princeton.edu/documents/NIST_benchmark_reliability.pdf)).

_Added by eval-tooling researcher (2026-10-20):_ Repo archived as of Oct 2026 — maintenance status unclear.

## Relevance to agent evaluation
- HAL is the clearest academic case that single-run pass@1 overstates how dependable an agent is. Consistency across repeated runs (pass^k) and error severity are needed.
- LLM log inspection for shortcuts is itself agent-as-judge, applied to auditing the evaluation.

_Added by eval-tooling researcher (2026-10-20):_ Strong evidence that outcome scores miss shortcut/unsafe behaviour and that LLM log inspection (an agent judging agent transcripts) surfaces it.

