---
title: Why we no longer evaluate SWE-bench Verified (and the July 2026 SWE-bench Pro follow-up)
org: OpenAI
date: 2026-02
url: https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
kind: benchmark
category: third-party-and-benchmarks
---
# Why we no longer evaluate SWE-bench Verified

## One line
In February 2026 OpenAI stopped reporting SWE-bench Verified, citing contamination and flawed tests, and recommended SWE-bench Pro instead. In July 2026 OpenAI then found about 30% of SWE-bench Pro broken.

## What they do
- OpenAI audited a subset of hard SWE-bench Verified tasks and checked for leakage into training data.
- It pointed instead to Scale AI's SWE-bench Pro, which has 1,865 tasks across 41 repos, drawn from copyleft and private commercial code in Python, Go, JavaScript and TypeScript ([Morph leaderboard summary](https://www.morphllm.com/swe-bench-pro)).
- The primary page returned HTTP 403 when fetched. The figures below come from Epoch's review and from secondary coverage.

## Evidence
- Epoch's summary of the OpenAI audit: it covered 27.6% of tasks, and 59.4% of those had flawed tests that rejected functionally correct submissions ([Epoch review](https://epoch.ai/benchmarks/swe-bench-verified/review)). A secondary blog describes this as 59.4% of 138 hard tasks ([Pebblous](https://blog.pebblous.ai/blog/swe-bench-verified-retired/en/)).
- Epoch: it "can be assumed that all current and future models have been trained on the codebases used in its tasks" ([Epoch review](https://epoch.ai/benchmarks/swe-bench-verified/review)).
- Saturation: the top score moved only from 74.9% to 80.9% over six months. This is a secondary source ([Pebblous](https://blog.pebblous.ai/blog/swe-bench-verified-retired/en/)).
- The SWE-bench team still maintains the Verified leaderboard, with "Bash Only" as the default view ([Morph](https://www.morphllm.com/swe-bench-pro)).
- Follow-up on 8 July 2026: OpenAI's "Separating signal from noise in coding evaluations" estimated that about 30% of SWE-bench Pro's 731 public tasks are broken ([Epoch SWE-Bench Pro review](https://epoch.ai/benchmarks/swe-bench-pro/review); [AI/TLDR](https://ai-tldr.dev/releases/openai-swe-bench-pro-audit-jul8/)).
  - Five engineers reviewed the flagged tasks.
  - Error types: misleading prompts, overly strict tests, underspecified prompts, low-coverage tests.
  - Secondary reports say OpenAI withdrew its February recommendation of Pro. This is not verified against OpenAI's page.
_Added by frontier-labs researcher (2026-10-20):_ Cross-lab reporting after the retirement: the GPT-5.5 system card (Apr 2026) has no SWE-bench Verified row ([card](https://deploymentsafety.openai.com/gpt-5-5/gpt-5-5.pdf)); Gemini 3.5 Flash (May 2026) reports SWE-Bench Pro (Public) only ([card](https://deepmind.google/models/model-cards/gemini-3-5-flash/)), whereas Gemini 3.1 Pro (Feb 2026) still reported both; Anthropic's Claude Opus 5 card (Jul 2026) still reports SWE-bench Verified 96.0% next to Pro 79.2% ([card](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf)); xAI's Grok 4.6 card (Aug 2026) reports neither, using DeepSWE, SWE-Marathon, FrontierCode and Terminal-Bench 3.0 ([card](https://media.x.ai/v1/website/card-4p6-4cd2dc57.pdf)).

## Limitations and criticisms
- The lab that retired the benchmark also chose its replacement, and that replacement was itself found about 30% broken five months later.
- The exact figures were not verified against the primary page because of the 403.
_Added by frontier-labs researcher (2026-10-20):_ A search-result summary also cites a May 2026 Datacurve audit claiming SWE-bench Pro graders mis-graded roughly a third of trials ([aiweekly](https://aiweekly.co/alerts/openai-drops-swe-bench-verified-backs-pro-after-flaw-audit)); not verified.

## Relevance to agent evaluation
Both a frontier lab and Epoch now consider the canonical coding-agent benchmark of 2024-25 contaminated and wrongly verified. Agent benchmarks built on fixed repositories and verified by unit tests have a shelf life of roughly 18 months.
