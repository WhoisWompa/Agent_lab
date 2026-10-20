---
title: GDPval - evaluating AI on real-world economically valuable tasks
org: OpenAI
date: 2025-09
url: https://www.transformernews.ai/p/openai-gdpval-ai-jobs-work
kind: benchmark
category: third-party-and-benchmarks
---
# GDPval (OpenAI)

## One line
OpenAI's benchmark of expert-made deliverables across 44 occupations. Expert graders compare a model's output with a human professional's, blind. By 2026 frontier models were judged as good as or better than experts in over 80% of comparisons.

## What they do
- Tasks come from industry professionals, with reference deliverables in occupations that contribute most to GDP.
- Experts grade blind and pairwise, model against human. The "wins or ties" rate is the headline.
- OpenAI also built an automated grader.
- Artificial Analysis runs its own variant, GDPval-AA, as 10% of its index ([AA](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index)).

## Evidence
- **2025 gold subset**: Claude Opus 4.1 was rated equal or better in 47.6% of comparisons; GPT-5 high in 38.8% ([Transformer](https://www.transformernews.ai/p/openai-gdpval-ai-jobs-work); [Empiricrafting](https://empiricrafting.substack.com/p/evaluating-gdpval-openais-eval-for)).
- **Automated grader**: about 66% agreement with human experts ([Medium critique](https://medium.com/@pranil.dasika/openais-gdpval-why-the-66-automated-grading-problem-matters-more-than-the-48-win-rate-a5e542508196)).
- **2026, from an aggregator** quoting launch posts dated 23 Apr 2026 ([benchmarklist](https://benchmarklist.com/benchmarks/openai_gdpval/)), unverified against OpenAI:
  - GPT-5.5: 84.9%
  - GPT-5.4: 83.0%
  - Claude Opus 4.7: 80.3%
- No official OpenAI post updating GDPval in 2026 was found.
_Added by frontier-labs researcher (2026-10-20):_ 2026 lab cards mostly report Artificial Analysis's GDPval-AA (pairwise judge, Elo) rather than expert-graded GDPval: Claude Opus 5 GDPval-AA v2 1861 ([card](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf)), Grok 4.6 1753 ([card](https://media.x.ai/v1/website/card-4p6-4cd2dc57.pdf)), Gemini 3.5 Flash 1656 vs GPT-5.5 1769 ([card](https://deepmind.google/models/model-cards/gemini-3-5-flash/)). OpenAI's own GPT-5.5 launch post states 84.9% on GDPval across 44 occupations ([OpenAI](https://openai.com/index/introducing-gpt-5-5/), via search extract).

## Limitations and criticisms
- Tasks are one-shot and well specified, with no iteration or workplace context.
- Expert grading is expensive. The automated grader agrees with humans only about 66% of the time.
- OpenAI built the benchmark and reports its own results.
- Epoch lists "economic value benchmarks" among its review topics ([Epoch job post](https://www.builtinaustin.com/job/researcher-benchmark-reviews/10053209)).

## Relevance to agent evaluation
GDPval is the template for evaluation grounded in economic value. Pairwise judging against human experts is the expensive gold standard, and 66% agreement shows how far LLM judges are from replacing expert graders of complex deliverables.
