---
title: LinkedIn Hiring Assistant and GenAI assistant evaluation (ZenML summaries)
org: LinkedIn (via ZenML LLMOps database)
date: 2025
url: https://zenml.io/llmops-database/building-an-enterprise-grade-ai-agent-for-recruiting-at-scale
kind: production-practice
category: production-practice
---
# LinkedIn Hiring Assistant and GenAI assistant evaluation (ZenML summaries)

## One line
Secondary summaries of LinkedIn's recruiting agent and earlier GenAI assistant evaluation; primary posts not fetched.

## What they do
Hiring Assistant: plan-and-execute agent with sub-agents (intake, sourcing, evaluation, outreach, screening, learning); ~90% of LLM calls come from the candidate-evaluation agent. Earlier assistant used a three-tier eval workflow: engineers' fast coarse checks, annotators with ~1-day turnaround, member feedback at scale (https://www.zenml.io/llmops-database/building-and-scaling-a-production-generative-ai-assistant-for-professional-networking).

## Evidence
EON-8B domain-adapted model +4 pts absolute vs GPT-4o mini on candidate-job matching (secondary). Pre-automation, metrics lagged 1+ day and relied on eyeballing.

## Limitations and criticisms
Secondary source only.

## Relevance to agent evaluation
Three-tier human/annotator/user evaluation latency ladder is a common large-company pattern.
