---
title: Eval-driven development: Build better AI faster
org: Vercel (Malte Ubl, Alice Alexandra Moore, Ido Pesok)
date: 2024-10
url: https://vercel.com/blog/eval-driven-development-build-better-ai-faster
kind: production-practice
category: production-practice
---
# Eval-driven development: Build better AI faster

## One line
Vercel's Oct 2024 description of v0's eval-driven development (pre-window, still cited): code checks, human feedback and LLM grading, with eval results on every PR.

## What they do
Code checks (valid code blocks, imports, multi-file usage, comment-to-code ratio against "laziness"); end-user and dogfood feedback into the eval set; LLM grading for complex judgments; prompts iterated almost daily; scripted full-suite runs reporting pass/fail and regressions; Braintrust for logging/manual review; "Every GitHub pull request that impacts the output pipeline includes eval results."

## Evidence
Refusal and safety evals held at 100%; other evals intentionally not all passing; failing prompts added as new cases. Claims LLM grading costs 1.5-2x code grading.

## Limitations and criticisms
Admits maintaining the suite as the system changes is an ongoing challenge; scaling without dropping human review unsolved.

## Relevance to agent evaluation
Early public example of evals as a PR gate; 2025-26 Vercel guidance (https://vercel.com/i/ai-agent-evaluation-frameworks-production) adds "cheapest check first" and measured judge position bias (pb from 0.002 Gemini 2.5 Pro to 0.192 Qwen 3 8B across 21 judges; from search snippet, not fetched).
