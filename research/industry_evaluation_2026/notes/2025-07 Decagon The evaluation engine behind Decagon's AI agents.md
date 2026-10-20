---
title: The evaluation engine behind Decagon's AI agents
org: Decagon (Max Lu)
date: 2025-07
url: https://decagon.ai/blog/evaluation-engine-ai-agents
kind: production-practice
category: production-practice
---
# The evaluation engine behind Decagon's AI agents

## One line
Decagon's 6 Jul 2025 post: every model or component variant passes offline LLM-judge and ground-truth evaluation, audited by human labellers, before gradual online A/B testing on CSAT and resolution rate.

## What they do
- Offline: LLM-as-judge scores (query, context, response) triplets from real interactions on relevance, correctness, naturalness, empathy; samples stratified by issue type and customer segment.
- Ground-truth set of curated queries with expert-written ideal responses for factuality and intent coverage.
- Human labellers audit a subset of triplets "to further validate the LLM-as-judge scoring."
- "Every variant must demonstrate consistent performance offline before it is eligible for online testing."
- Online: gradual traffic ramp; tracks CSAT and resolution rate; watches for "noise, novelty effects, and performance drift"; customers can opt out of experimentation.
- Related: Decagon Simulations (Sep 2025) built around Agent Operating Procedures (AOPs): AI-generated mock-user conversations across channels against user-defined success criteria; historical transcripts where agents struggled can be uploaded as tests; voice conditions (accents, speed, background noise, interruptions, emotional tone); unit tests for accuracy/policy, integration checks for correct tool/action calls.

## Evidence
No thresholds, sample sizes, agreement rates or results given. Vendor-authored.

## Limitations and criticisms
Marketing-adjacent; does not say how disagreement between judge and human audits is handled or how often audits run. A third-party review (sitegpt.ai) claims sims run on schedule or in CI with PagerDuty alerts; unverified.

## Relevance to agent evaluation
Canonical two-stage pattern (offline judge gate -> online A/B on business metrics) for customer-facing agents, plus AOP-driven simulation where the procedure text is both the agent's spec and the test oracle.
