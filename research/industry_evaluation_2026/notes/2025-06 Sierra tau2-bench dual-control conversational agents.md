---
title: tau2-bench: Evaluating Conversational Agents in a Dual-Control Environment
org: Sierra Research (Barres, Dong, Ray, Si, Narasimhan)
date: 2025-06
url: https://sierra.ai/resources/research/tau-squared-bench
kind: benchmark
category: production-practice
---
# tau2-bench: Evaluating Conversational Agents in a Dual-Control Environment

## One line
Sierra's June 2025 benchmark (arXiv 2506.07982) extending tau-bench so both agent and simulated user act on a shared environment (telecom domain), measured with pass^k; listed here for its link to Sierra's production simulation practice.

## What they do
Dual-control environment: the simulated user must take actions (e.g. toggle device settings) under the agent's guidance; outcome graded on final database/environment state; pass^k reports consistency across repeated trials. Repo: https://github.com/sierra-research/tau2-bench. Later extensions: tau3-bench voice (Mar 2026) and tau-voice (278 grounded customer-service tasks, May 2026) per Sierra's research pages (not fetched in this pass).

## Evidence
Not fetched in depth here; other researchers likely cover it under benchmarks. No public statement found of which production customers use tau2-bench directly as a release gate.

## Limitations and criticisms
Benchmark, not a production report; Anthropic notes Opus 4.5 "failed" one task by finding a policy loophole better for the user, showing state-match grading can penalise good behaviour.

## Relevance to agent evaluation
The public template for simulated-user plus final-state evaluation that Sierra, Intercom and Decagon productise.
