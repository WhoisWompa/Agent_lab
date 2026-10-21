---
title: AgentHorizon: Evaluating Agentic Judges for Long-Horizon Computer-Use Tasks
authors: Xing Han Lù et al. (ServiceNow Research, McGill, Mila; Siva Reddy)
date: 2026-10
arxiv: 2610.11050
url: https://arxiv.org/abs/2610.11050
venue: arXiv
category: agent-as-judge
topics: ["LLM and agent judges", "judge and decision-model audits"]
---
# AgentHorizon: Evaluating Agentic Judges for Long-Horizon Computer-Use Tasks

## One line
Benchmark of 1,373 human-recorded computer-use trajectories built in success/near-miss pairs to test whether agentic judges (coding-agent harnesses that inspect the trajectory with tools) can tell real success from subtle failure.

## Method
- Annotators write pairs of closely related instructions and record a trajectory for each; swapping a recording onto the other instruction yields a negative. Negatives labelled Critical Mistake, Bad Side Effect or Misunderstanding.
- Agentic judges = models running inside Codex, Claude Code, Gemini CLI, OpenCode, OpenHands harnesses, inspecting screenshots and action logs with tools; direct judges get a fixed set of screenshots in one call. Balanced accuracy.

## Evaluated on
- 1,373 items (523 pos / 850 neg), ~166 h of recordings on Windows/Linux/macOS; splits AH (528 hard), AH-S (683), AH-D (162 dev).
- 11 judge models. Best: GPT-5.5 + Codex 80.9% balanced accuracy on AH; Gemini 3.1 Pro + Gemini CLI 77.7%; Claude Opus 4.7 + Claude Code 76.0%; best open-weight agentic Qwen 3.6 27B + OpenCode 70.4%.
- Tools don't consistently help: Qwen 3.6 27B direct 77.6% > its agentic 70.4%; GPT-5.5 68.6% direct -> 80.9% agentic. Harness swap shifts GPT-5.5 by ~3.7 pts.
- Cost per trajectory ~$0.10 (Haiku 4.5) to ~$0.66 (Opus 4.7).
- Bad Side Effect hardest: best recall 24.1%, several judges <10% - judges confirm the requested output exists but miss unrequested actions. Judges also reject valid work over trivial deviations. Without the instruction, Qwen labelled 98.9% of trajectories successful.

## Limitations admitted by the authors
- Targets subtle near-miss errors, not loops/crashes/stalls.
- Difficulty splits depend on splitter models; AH-D partly exposed in pilots.
- No independent human inter-annotator agreement.
- English-only, finite apps, only screenshots + action logs; not a safety evaluation.

## Limitations found by others


## What it leaves untried
- Judges that replay or re-run actions in a live environment to check side effects (here the judge only has recordings).
- Explicit side-effect checking (diffing environment state before/after).

## Topics
[[Topic - LLM and agent judges]] · [[Topic - judge and decision-model audits]]
