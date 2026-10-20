---
title: Decision-Time Guidance for Long-Trajectory Agentic Coding Systems (ZenML summary)
org: Replit (via ZenML)
date: 2026-01
url: https://www.zenml.io/llmops-database/decision-time-guidance-for-long-trajectory-agentic-coding-systems
kind: production-practice
category: production-practice
---
# Decision-Time Guidance for Long-Trajectory Agentic Coding Systems (ZenML summary)

## One line
Secondary summary of Replit's classifier-triggered micro-instructions for long agent trajectories.

## What they do
Lightweight multi-label classifier decides when to inject short situational instructions from a reusable bank; ephemeral, prompt-cached. Earlier LangChain case study: reliability is highest in early steps of long trajectories and drops later, motivating easy revert (https://www.langchain.com/breakoutagents/replit).

## Evidence
Secondary; no eval numbers.

## Limitations and criticisms
Not a Replit primary source; eval methodology not described.

## Relevance to agent evaluation
Reliability decay over trajectory length is a recurring practitioner finding; step-indexed failure analysis matters for long agents.
