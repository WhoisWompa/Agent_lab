---
title: Introducing BigLaw Bench
org: Harvey
date: 2024-08
url: https://www.harvey.ai/blog/introducing-biglaw-bench
kind: benchmark
category: production-practice
---
# Introducing BigLaw Bench

## One line
Harvey's in-house, lawyer-built benchmark of real legal tasks with per-task rubrics, used to compare models and its own system (Aug 2024; GPT-5 result reported Aug 2025).

## What they do
Tasks and per-question rubrics written by in-house attorneys from BigLaw backgrounds; scores answer quality (positive points for meeting requirements, negative for errors/hallucinations) and source reliability. Snorkel AI partnered on a "BigLaw Bench: Research" agentic variant.

## Evidence
Harvey self-reported 74% answer score vs GPT-4o 61% (2024); GPT-5 topped at 89.22% (https://www.artificiallawyer.com/2025/08/08/gpt-5-tops-harveys-biglaw-bench-eval/). Self-reported.

## Limitations and criticisms
Vendor-run; an analyst called for an industry-wide non-partisan benchmark (https://legaltechnology.com/the-gen-ai-llm-benchmarking-war-starts-here-harvey-releases-new-evaluation-framework/). Engineering details of Harvey's internal expert-review process not found in this pass.

## Relevance to agent evaluation
Example of expert-authored rubric evals as the core of a high-stakes vertical product; expertise is the bottleneck.
