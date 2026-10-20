---
title: Inspect AI and Inspect Evals
org: UK AI Security Institute / Meridian Labs
date: 2025-08
url: https://www.aisi.gov.uk/blog/the-inspect-sandboxing-toolkit-scalable-and-secure-ai-agent-evaluations
kind: tooling-product
category: eval-tooling
---
# Inspect AI and Inspect Evals

## One line
Inspect is the MIT-licensed eval framework from UK AISI (with Meridian Labs) for agentic and safety evals, with sandboxed tool execution and a community benchmark library (inspect_evals).

## What they do
Tasks = dataset + solver (agent) + scorer; model-graded and code scorers; sandbox toolkit (Aug 2025) to run model-requested actions in isolation; sandboxes for Docker, Kubernetes, EC2, Proxmox, Modal (Meridian) and Vagrant; Inspect Scout (transcript analysis) and Inspect Viz (https://inspect.aisi.org.uk/extensions/extensions_content.html).

## Evidence
GitHub: inspect_ai 3,045 stars, inspect_evals 706 stars, both MIT, pushed 2026-10-19 (GitHub API).

## Limitations and criticisms
Claims about how widely frontier labs use it came only from low-quality sites; unverified. Teams must set own network/credential/tool-approval rules (https://aicoolies.com/reviews/inspect-ai-review).

## Relevance to agent evaluation
Inspect Scout is a transcript-analysis tool — i.e., LLM scanning of agent transcripts, closely related to agent-as-judge. The research-grade harness for agent evals.

