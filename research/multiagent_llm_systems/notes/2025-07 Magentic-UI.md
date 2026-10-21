---
title: "Magentic-UI: Towards Human-in-the-loop Agentic Systems"
authors: Hussein Mozannar et al.
date: 2025-07
arxiv: 2507.22358
url: https://arxiv.org/abs/2507.22358
venue: arXiv
category: framework-production
pdf: research/multiagent_llm_systems/pdfs/2507.22358.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation", "user simulation"]
---
# Magentic-UI: Towards Human-in-the-loop Agentic Systems

## One line
An open-source web interface on an orchestrator-plus-workers agent team that treats the human as one more agent, with six mechanisms (co-planning, co-tasking, action guards, answer verification, memory, multitasking) for low-cost oversight.

## Method
Problem: web, code and file agents still fall well below human level and, because they act in the world, can take irreversible or manipulated actions. The authors argue for human involvement as a core design principle, not a fallback, provided each human touch is cheap.

Architecture: an Orchestrator (adapted from Magentic-One, built on AutoGen) directs WebSurfer, Coder, FileSurfer, optional MCP-wrapping agents and a UserProxy that stands for the human. The Orchestrator picks an agent by reading each agent's natural-language description field. Work runs in two modes.
- **Planning mode (co-planning).** The Orchestrator asks a clarifying question if the task is ambiguous, then writes a plan as a short list of steps, each with an agent name, a title and details. The user edits, regenerates or accepts it, and nothing runs until acceptance. Plain-language steps are easy for users to read but cannot express branching or parallel steps.
- **Execution mode.** Each round the Orchestrator writes a progress ledger (is the step complete, is a replan needed, which agent gets which instruction). A replan returns to the user for approval.
- **Co-tasking.** The user can pause and take over the embedded browser at any time. The Orchestrator can also hand a step to the user, but its prompt tells it to do so only after other agents fail. This threshold was tuned by unstructured use, since there is no ground-truth signal for when to interrupt.
- **Action guard.** Each action is tagged always, maybe or never irreversible. "Always" goes to the user, "never" runs, and "maybe" goes to an LLM judge that decides whether to ask the user. Docker sandboxing, a fresh browser without the user's credentials and a site allow-list sit underneath.
- **Memory.** Finished runs are distilled by an LLM into reusable plans, and the user attaches one to a new task or lets the Orchestrator retrieve it by embedding match. Preferences and personal data are not stored.

## Evaluated on
- **Autonomy is preserved despite the extra interactivity.** On the GAIA test set, 42.52 vs 38.00 for Magentic-One (which used 4o and o1). It stays below leaderboard SOTA (77 to 80) and human performance (92).
- **The web agent is competitive, not best.** o4-mini reaches 82.2 on WebVoyager (browser agent only), below Browser Use (89.1) and Operator (87.0). On WebGames it scores 45.5 vs 95.7 for humans.
- **A little human help goes a long way (simulated users, GAIA validation, GPT-4o agents).** A simulated user holding a human-written plan lifts accuracy from 30.3% to 51.9% (+71%) while being asked in only 10% of tasks, though it also supplies the final answer in 18%. A smarter-model simulated user gives 42.6%, with help asked in 4.3% of tasks.
- **Usability is acceptable but not sticky (12 users).** SUS is 74.58 and 75% found it easy to use, but only 41.7% would use it frequently. Latency was the top complaint. Users valued editing plans for subjective preferences and said multitasking is only comfortable because the guards exist.
- **Layered mitigations hold.** In 24 internal adversarial scenarios, none succeeded in the default configuration. With mitigations disabled, GPT-4o resisted social engineering but prompt injection worked: it exfiltrated SSH keys and created persistent GitHub API keys.

## Limitations admitted by the authors
- Task skill is still below human level, especially on advanced coding, video, very long action sequences and general computer use.
- No productivity result: the evaluation was simulated users plus qualitative study, and a long-term controlled trial is needed.
- The plan DSL has no branching or parallel steps, and agents sometimes do more than a step says, so the shared plan drifts from execution. Reviewing plans gets expensive as they grow.
- Users found guard prompts excessive or redundant (for example, approving add-to-cart, or approving a plan the user had just requested). When to interrupt is unsolved because no ground truth exists.
- Verification is hard. Users often had to review the agent's whole trajectory to judge correctness, which is costly when running tasks in the background.
- Tested in English only. The red-team set is small (24 scenarios) and internal, and its safety claim is called "preliminary".

## Limitations found by others

## What it leaves untried
- Learning the interruption policy, from user trust or from simulated-user feedback, instead of a hand-written description field. The paper only suggests that the simulated-user setup could serve for tuning.
- Hierarchical or branching plan representations, so that users review only the steps that need feedback.
- A real-user, long-duration comparison against doing the tasks alone. The simulated gain (30.3% to 51.9%) assumes an oracle-like user who sees the human-written plan, and the paper calls it a lower bound without evidence for real users.

## Topics
[[Topic - orchestration and delegation]] · [[Topic - user simulation]]
