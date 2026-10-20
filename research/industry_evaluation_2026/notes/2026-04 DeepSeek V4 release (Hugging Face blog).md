---
title: DeepSeek-V4: a million-token context that agents can actually use
org: DeepSeek (via Hugging Face blog)
date: 2026-04
url: https://huggingface.co/blog/deepseekv4
kind: lab-practice
category: frontier-labs
---
# DeepSeek-V4: a million-token context that agents can actually use

## One line
Hugging Face's 24 Apr 2026 write-up of the DeepSeek V4 release (V4-Pro 1.6T/49B active, V4-Flash 284B/13B), summarising DeepSeek's reported agentic benchmarks, an internal R&D coding eval, a developer survey and the DSec sandbox platform used for agent RL.

## What they do
- Reported: Terminal Bench 2.0 67.9 (V4-Pro-Max), SWE Verified 80.6, MCPAtlas Public 73.6, Toolathlon 51.8, MRCR 8-needle >0.82 to 256K and 0.59 at 1M.
- Internal R&D coding eval: 30 tasks (PyTorch, CUDA, Rust, C++); V4-Pro-Max 67% vs Sonnet 4.5 47% and Opus 4.5 70%.
- Human signal: survey of 85 DeepSeek engineers using V4-Pro daily; 52% would replace their primary coding model.
- RL infrastructure: DSec (Rust) with four substrates (function calls, containers, Firecracker microVMs, QEMU VMs) behind one SDK, hundreds of thousands of concurrent sandboxes, preemption-safe trajectory replay. Agent behaviour trained with RL against real tool environments.

## Evidence
- Knowledge/reasoning "competitive but not leading". Later checkpoints (V4-Pro-0813) report Terminal-Bench 2.1 87.9 and DeepSWE 62.7 on vendor pages (https://deepinfra.com/deepseek-ai/DeepSeek-V4-Pro-0813) - not independently reproduced.

## Limitations and criticisms
- Harness details for public benchmarks not given; no description of reward models/verifiers in the post. CAISI found V4 weaker on its held-out evals than on DeepSeek's self-reports.
- I did not read DeepSeek's own technical report; sources disagree on its arXiv ID.

## Relevance to agent evaluation
Chinese labs describe agent evaluation mostly through public agentic benchmarks plus internal task sets and developer surveys; the same sandbox fleet used for RL is the eval substrate.
