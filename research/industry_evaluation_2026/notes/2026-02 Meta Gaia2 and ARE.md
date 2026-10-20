---
title: "Gaia2: Benchmarking LLM Agents on Dynamic and Asynchronous Environments" (and ARE)
org: Meta Superintelligence Labs / Hugging Face
date: 2026-02
url: https://arxiv.org/pdf/2602.11964
kind: benchmark
category: third-party-and-benchmarks
---
# Gaia2 and ARE (Agents Research Environments)

## One line
The successor to GAIA, presented as an ICLR 2026 oral. It runs on ARE, a simulation platform in which time keeps moving whether or not the agent acts, so it tests time-sensitive, asynchronous and ambiguous agent tasks.

## What they do
- **ARE**: an MIT-licensed simulator of a phone-like environment with apps and events that happen asynchronously.
- **Gaia2**: a CC BY 4.0 dataset of scenarios. Its splits include execution, search, adaptability, time, ambiguity, and agent-to-agent ([HF blog](https://huggingface.co/blog/gaia2); [ICLR](https://iclr.cc/virtual/2026/oral/10011092)).
- Results are run three times to account for variance ([alphaXiv](https://www.alphaxiv.org/benchmarks/meta-superintelligence-labs/gaia2)).

## Evidence
- GPT-5 (high) was the strongest overall at 42% pass@1, but it fails time-sensitive tasks.
- Kimi-K2 scored about 21%, the best open model.
- No single model led every capability.

## Limitations and criticisms
- The results are from 2025 models. No 2026 leaderboard was found.
- Third-party reimplementations, such as maseval, have not been validated against the original.

## Relevance to agent evaluation
Gaia2 adds time and asynchrony as evaluation dimensions. A judge has to consider when an agent acted, not only what it did.
