---
title: Galileo: Luna-2 small evaluation models; acquired by Cisco/Splunk
org: Galileo / Cisco
date: 2026-02
url: https://docs.galileo.ai/concepts/luna/luna
kind: tooling-product
category: eval-tooling
---
# Galileo: Luna-2 small evaluation models; acquired by Cisco/Splunk

## One line
Galileo differentiates with Luna-2, fine-tuned small language models (LoRA heads on a shared SLM) that run judge metrics cheaply at low latency, and was acquired by Cisco in May 2026 to fold into Splunk Observability.

## What they do
- Docs table: Luna-2 $0.02 per M tokens, 0.95 F1, 152 ms avg latency vs GPT-4o $2.50, 0.94 F1, 3,200 ms. Enterprise tier only. A third-party review notes the product page lists $0.12/M (conflict).
- arXiv paper Feb 2026 (https://www.arxiv.org/pdf/2602.18583): each metric is a LoRA/PEFT head on shared SLM backbone; aims for "accuracy at par or higher than LLMAJ using frontier LLMs while drastically reducing" cost/latency.
- Cisco intent-to-acquire blog: https://blogs.cisco.com/news/cisco-announces-the-intent-to-acquire-galileo ; reported completed 22 May 2026; galileo.ai/pricing redirects to Splunk agent observability pricing (https://www.developersdigest.tech/blog/llm-observability-acquisitions-2026).

## Evidence
- Cost/latency/F1 numbers are vendor-reported; no independent benchmark found.

## Limitations and criticisms
- Distilled judges inherit training-label biases; locked to enterprise tier; product future tied to Splunk.

## Relevance to agent evaluation
- The cost-aware alternative to frontier-LLM judges: small distilled evaluators enable scoring 100% of production traffic and use as guardrails. Relevant for cheap first-pass judging in a cascade.

