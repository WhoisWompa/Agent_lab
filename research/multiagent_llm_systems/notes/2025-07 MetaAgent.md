---
title: "MetaAgent: Automatically Constructing Multi-Agent Systems Based on Finite State Machines"
authors: Yaolun Zhang et al.
date: 2025-07
arxiv: 2507.22606
url: https://arxiv.org/abs/2507.22606
venue: ICML 2025
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2507.22606.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "communication topology and channels", "role-based agent teams"]
---
# MetaAgent: Automatically Constructing Multi-Agent Systems Based on Finite State Machines

## One line
Given only a task-type description, an LLM designs a multi-agent system as a finite state machine (agents, states, natural-language transition conditions), merges redundant states, and deploys it with per-state verifiers that can retry or trace back.

## Method
**Problem.** Hand-designed multi-agent systems cover only a few scenarios. Earlier automatic designers each fall short in one way: SPP, AutoAgents and EvoAgent design one system per case, not per task type. SPP and AutoAgents cannot use tools. ADAS and Symbolic Learning need many iterations plus external data. Nearly all of them use a linear, debate or orchestrator structure, which cannot go back and repair an earlier step.

**Idea.** One designer LLM reads the task-type description and produces three things.
- A minimal set of agents, each with a name, system prompt and tools (code interpreter, search engine).
- A set of states. Each state has an instruction, an assigned agent, and "listeners", the agents whose memory receives the state's output. This controls who sees what, and every agent also sees the original user input.
- Natural-language transition conditions between states.

Each state also gets a condition verifier, an LLM that shares the solver's prompt plus the exit conditions. It checks the solver's output (text plus tool results) against those conditions. There are three outcomes.
- A condition holds, so the machine advances.
- A condition points to an earlier state, so it traces back. Example: a tester finds a bug and returns control to the programmer state.
- No condition holds, so it takes a null-transition: feedback goes to the same agent, which retries, up to a maximum number of interactions.

**Optimization without data.** The first design tended to have too many states and long information chains. An "adaptor" LLM compares every pair of states and asks whether their agents' roles are distinct enough to justify separate agents, since role diversity is the point of a multi-agent system. If not, it merges the states and their prompts, and repeats until nothing merges. No training data or iterative search is used.

**Generality argument.** Linear pipelines are FSMs with one fixed transition per state and no traceback or null-transition. Debate is an FSM that can only trace back from the last state to the first. An orchestrator system is an FSM in which all states share one verifier. This is a formal-style argument, not an experiment.

## Evaluated on
All main results use GPT-4o at temperature 0.
- **Beats other prompt-based and auto-design methods on text tasks.** Trivial Creative Writing 0.86 vs 0.79 for SPP and 0.76 for Direct. GPQA Diamond 0.60 vs 0.55 for Self-Refine and 0.46 for Direct.
- **Close to a hand-built specialist on ML tasks.** Average normalized score 0.83 vs 0.86 for Data Interpreter. The other auto-designed systems score 0.16 (SPP) and 0.00 (AutoAgents), which the authors attribute to missing tool feedback and hallucinated data handling.
- **Far above MetaGPT on software tasks.** The score is the share of four checkpoints passed (e.g. opens, operates, scores correctly), averaged over five programs. MetaAgent gets 0.85 vs 0.35 for MetaGPT, 0.20 for AutoAgents and 0.15 for SPP.
- **Each feature carries weight.** Removing optimization costs 26.5% on ML, 35.3% on software, 24.4% on writing and 6.67% on GPQA. Removing traceback costs 58.8% on software and 13.3% on ML. Removing tools costs 13.33% on GPQA and 8.1% on writing.
- **Cheaper in total tokens.** Software tasks cost 47,752 tokens (5,378 for design) vs 60,237 for MetaGPT and 52,180 for AutoAgents. ML tasks cost 46,289 vs 65,355 for MetaGPT and 62,585 for AutoAgents.
- **Model quality matters on both sides.** On ML, GPT-4o for both roles scores 0.83. GPT-3.5-Turbo for both scores 0.12. Downgrading only the designer gives 0.39 and downgrading only the executor gives 0.26, so the executor matters more. The text prints the 0.26 and 0.35 values against the opposite roles from the table.

## Limitations admitted by the authors
- The paper has no limitations section. The conclusion claims only strengths.
- The first FSM design often failed because of too many redundant states. The merge step is a patch for a designer weakness, not a fix to the designer. Without it, scores drop 6.67% to 35.3%.
- Quality depends heavily on the base model. Both roles on GPT-3.5-Turbo give 0.12 vs 0.83 on ML, so the "no external data" advantage holds only with a strong model.

## Limitations found by others

## What it leaves untried
- No comparison with ADAS or Symbolic Learning, the two methods whose data and iteration costs motivate the paper. The comparison table credits them with failing on external-data dependence, but no runs back it up.
- No comparison with hand-written state-machine frameworks (StateFlow and the like, cited in related work). The claim that learned transitions beat hard-coded string matching is not tested.
- Only one foundation-model family (GPT-4o, plus GPT-3.5 in one ablation), small task sets (five ML, five software tasks, hand-made four-point checklists), and no variance reported. The benefit of designing per task type vs per case is shown by token cost only, not by quality.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - communication topology and channels]] · [[Topic - role-based agent teams]]
