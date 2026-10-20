---
title: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments
authors: Tianbao Xie et al.
date: 2024-04
arxiv: 2404.07972
url: https://arxiv.org/abs/2404.07972
venue: NeurIPS 2024 D&B
category: agent-evaluation-benchmarks
---
# OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments

## One line
369 real desktop tasks in VMs (Ubuntu/Windows) with per-task execution-based evaluation scripts on final machine state.

## Method
Custom checker per task inspects files, app configs, and other state after the run.

## Evaluated on
Humans 72.36% vs best model 12.24% at release.

## Limitations admitted by the authors


## Limitations found by others
- Maintainers' OSWorld-Verified (Jul 2025) fixed 300+ issues: web changes, ambiguous instructions, evaluator robustness (xlang.ai/blog/osworld-verified).
- Epoch AI (Oct 2025): ~10% of tasks have serious errors (wrong answer keys, checkers too strict/lax, fatal ambiguity); ~10% depend on live internet data; ~15% need only a terminal; success often hinges on guessing intent of vague instructions.
- OSReward (2607.28609): best VLM judges disagree with the benchmarks' own verifiers on ~a quarter of desktop verdicts.

## What it leaves untried

