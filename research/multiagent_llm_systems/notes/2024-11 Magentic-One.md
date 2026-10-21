---
title: Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks
authors: Fourney et al.
date: 2024-11
arxiv: 2411.04468
url: https://arxiv.org/abs/2411.04468
venue: arXiv
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2411.04468.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation", "agent evaluation benchmarks"]
---
# Magentic-One: A Generalist Multi-Agent System for Solving Complex Tasks

## One line
An Orchestrator agent plans with two ledgers and directs four tool-specialist agents (web, files, code, terminal) to solve open-ended web and file tasks, reaching results statistically comparable to the best systems on three benchmarks without per-benchmark tuning of the team.

## Method
The problem is a generalist agent that plans, acts, observes and recovers from errors across tasks that need a browser, files and code. The paper's answer is one lead agent plus workers split by tool, not by human-style role (no "researcher" or "critic"). The authors argue tool-based agents separate concerns more cleanly: a researcher and an analyst would both need a browser and code. This is asserted, not tested.

The Orchestrator runs two nested loops.
- Outer loop: it fills a task ledger (given facts, facts to look up, facts to derive, educated guesses) and then writes a natural-language plan. The plan is a hint in the manner of chain of thought; nobody must follow it exactly. Guesses let memorised knowledge be used cautiously, as a fallback when the team is stuck or out of time.
- Inner loop: each step it fills a progress ledger by answering five questions: is the task done, is the team looping, is progress being made, who speaks next, and what instruction to give. A stall counter goes up on a loop or no progress. Above 2, it leaves the inner loop, reflects on what went wrong, rewrites the ledger and plan, and every agent clears its context.
- Termination is configurable (attempt or time limits); at the end the Orchestrator reports an answer or its best guess.

Workers hide low-level actions behind one broad capability each, so the Orchestrator picks an agent, not one of dozens of actions. WebSurfer drives a browser using set-of-marks screenshots. FileSurfer reads files as Markdown. Coder writes a fresh standalone program per request. ComputerTerminal runs code deterministically, with no LLM call. The harness enforces the stall counter, context resets and termination. The LLM judges progress and completion, so those judgments are unchecked.

The paper also contributes AutoGenBench, which runs each task in fresh Docker containers so earlier runs (an installed library, deleted files) cannot help or harm later ones.

## Evaluated on
- Competitive with state of the art, without a changed team: GAIA 38.0% test (best listed: 40.53%), AssistantBench accuracy 27.7%, WebArena 32.8% with GPT-4o only. Differences from most baselines are not significant at alpha 0.05. WebPilot and Jace.AI (57.1%) are significantly higher on WebArena.
- Stronger on hard tasks than easy ones: on AssistantBench hard, 16.9% (GPT-4o) against 13.3% for the best baseline, but behind it on easy (69.9% vs 81). The authors guess a fixed overhead that helps long tasks and adds error chances on short ones.
- The Orchestrator's ledgers matter: replacing it with a plain speaker-selector cut GAIA validation performance by 31%.
- Every worker matters: removing one cut performance by 21% (Coder plus Terminal) to 39% (FileSurfer). Remaining agents sometimes compensated, for example by reading code to predict its output.
- Adding o1-preview for the Coder and Orchestrator outer loop gave the largest gain on GAIA (32.33 to 38.00). The reason given, reasoning-heavy tasks, is a hypothesis. o1 refused 26% of WebArena Gitlab tasks, so that variant was dropped there.
- Top failure codes from an LLM-coded postmortem: persistent inefficient actions, insufficient verification before declaring completion, and inefficient navigation. The coding is done by GPT-4o and is not validated against humans.

## Limitations admitted by the authors
- Accuracy-only scoring ignores cost and latency; a correct answer that is too slow or expensive may be worth nothing.
- Cost is high: dozens of LLM calls per task, "perhaps several US dollars" and tens of minutes per task, not measured formally.
- WebArena has no hidden test set. On the authors' own split, validation scored 35.1% against 30.5% on test, so some over-fitting from debugging on validation.
- Team is fixed at five agents. Unneeded ones distract the Orchestrator; missing expertise cannot be added at run time.
- Nothing is learned between tasks, so WebArena sub-tasks are rediscovered each time.
- Modalities and actions are narrow: no video, no hover or drag, no figure or layout reading from files, no code needing API keys.
- The Coder rewrites whole programs and cannot work in multi-file code bases, which rules out benchmarks like SWE-bench.
- Observed risks: agents locked an account through repeated login attempts, then tried a password reset. Some tried to recruit humans, such as by emailing authors or drafting a freedom-of-information request. Containers, network blocks and log monitoring stopped them.

## Limitations found by others

## What it leaves untried
- No comparison against a single-agent system with the same tools and model, so the claim that the multi-agent design is the main driver of performance is unsupported.
- No test of function-based against role-based agent teams, or of peer-to-peer control against the central Orchestrator, though both are named as open.
- No cheaper models for WebSurfer or FileSurfer, nor long-term memory, which the paper expects to cut cost and repeated work.

## Topics
[[Topic - orchestration and delegation]] · [[Topic - agent evaluation benchmarks]]
