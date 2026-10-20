---
title: Frontier safety frameworks in 2026 - Anthropic RSP, OpenAI Preparedness Framework, Google DeepMind FSF
org: Anthropic; OpenAI; Google DeepMind (comparison via CASRAI and others)
date: 2026-07
url: https://casrai.org/compare/rsp-vs-preparedness-framework-vs-frontier-safety-framework
kind: standard-or-regulation
category: third-party-and-benchmarks
---
# Frontier safety frameworks: what evaluations they commit to (2026)

## One line
All three major frameworks commit to evaluating dangerous capabilities before deployment, against named thresholds. They differ in early-warning layers, safety-case requirements and how much they publish per model. Versions in 2026 are inconsistently reported.

## What they do
Version numbers, as reported (conflicting):
- **Anthropic RSP**: v3.4 effective 8 Jul 2026 per CASRAI; v3.0 effective 24 Feb 2026 per another tracker ([CASRAI](https://casrai.org/compare/rsp-vs-preparedness-framework-vs-frontier-safety-framework); [futureagi](https://futureagi.com/blog/frontier-model-safety-analysis-2026/)).
- **Google DeepMind FSF**: v3.x (17 Apr 2026). It adds Tracked Capability Levels as an early-warning layer and a harmful-manipulation Critical Capability Level ([comparativeai](https://comparativeai.org/companies/google-deepmind/safety-framework/)).
- **OpenAI Preparedness Framework**: v2 (15 Apr 2025) is cited as still governing in September 2026. One tracker lists an update on 28 May 2026 ([vorplabs](https://vorplabs.com/ai-regulatory-updates/frontier-ai-frameworks)).
  - METR's GPT-5.6 Sol evaluation explicitly tests against Preparedness v2's "Critical AI Self-Improvement" threshold ([METR](https://metr.org/blog/2026-06-26-gpt-5-6-sol/)).

Shared commitments:
- capability evaluation before deployment;
- safety cases, or affirmative cases, once thresholds are crossed (Anthropic and DeepMind);
- system cards or risk reports.

## Evidence
- One source reports that OpenAI publicly classified a model as Critical for cybersecurity in September 2026. This is unverified.
- DeepMind reportedly does not commit to publishing per-model results for its Critical Capability Levels.
- Third-party roles in practice: the labs grant pre-deployment access to METR, Apollo and the US and UK AISIs, and those results appear in system cards (see the respective notes).

## Limitations and criticisms
- Commentators describe RSP v3 as a weakening and Preparedness v2 as a simplification. This is opinion ([futureagi](https://futureagi.com/blog/frontier-model-safety-analysis-2026/)).
- Version facts came from secondary trackers; the lab documents were not fetched.

## Relevance to agent evaluation
The thresholds that gate deployment are increasingly agentic: autonomous AI R&D, self-improvement, and cyber operations. So frontier safety frameworks are now among the main consumers of long-horizon agent evaluations.
