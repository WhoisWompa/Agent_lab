---
title: "TraceFix: Repairing Agent Coordination Protocols with TLA+ Counterexamples"
authors: Shuren Xia et al.
date: 2026-05
arxiv: 2605.07935
url: https://arxiv.org/abs/2605.07935
venue: CAIS '26
category: framework-production
pdf: research/multiagent_llm_systems/pdfs/2605.07935.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "communication topology and channels"]
---
# TraceFix: Repairing Agent Coordination Protocols with TLA+ Counterexamples

## One line
An LLM designs a multi-agent coordination protocol, a TLA+ model checker attacks it, and the checker's counterexample traces drive repair until no deadlock or lock violation remains; the verified protocol then runs under a monitor.

## Method
Problem: independent LLM agents run concurrently, message asynchronously and share locks, so races, deadlocks, missed handshakes and early termination appear only under rare interleavings. A one-shot protocol, from a human or an LLM, looks plausible but is never exhaustively checked. Adding locks only trades races for deadlocks.

Idea: generating a correct concurrent protocol is hard, but checking one is mechanical. TraceFix treats the first protocol as a hypothesis to attack.

- An orchestration agent first writes a protocol topology from a task description. This is a declarative record of agents, shared resources (locks, counters) and directed FIFO channels with fixed label sets. It is schema-checked before anything else runs.
- The same agent then writes one PlusCal process per agent (send, receive, acquire, release, and `either/or` branches for choices the LLM might make). TLC explores every interleaving and every branch within bounds (channel queue depth 3 by default).
- TLC checks four safety properties: mutual exclusion, deadlock freedom, no orphan locks at termination, and drained channels. When one fails, the minimal counterexample trace goes to a repair agent, which edits the PlusCal (not the topology). Typical repairs are a lock order, a missing handshake, or a loop that breaks a cyclic wait.
- Verified process bodies are pasted into each agent's system prompt. At runtime a monitor rejects any send, receive or lock operation that the topology does not admit. Agents keep free use of their domain tools. The monitor does not enforce step order, so the verified state machine is carried by the prompt only.

Scope is coordination safety only. Task quality and liveness (guaranteed termination) are not checked.

## Evaluated on
- The loop converges. All 48 tasks (16 scenario families at three difficulty tiers) pass TLC. 30 pass first try (62.5%) and the rest need 1 to 4 repairs. First-try pass is 87.5% on Easy and 25% on Hard.
- Failures are channel problems, not lock problems. Deadlocks are 20 of 29 repairs (69%). One cause is an `either/or` that commits to a branch before checking the channel (7 cases). Another is a hub agent exiting before a retrying satellite finishes (6 cases). All 9 lock-only tasks pass first try, since alphabetical lock order is a pattern LLMs reproduce.
- Checking stays cheap. State spaces run from 30 to 7.7 M distinct states, yet every task verifies in under 60 s (median under 1 s).
- Topology monitoring gives the best runtime. With gpt-5-mini it reaches 89.4% average and 81.5% full completion, against prompt-only at 86.2% and 69.7%, and chat-only at 75.0% and 29.3%. Deadlock or livelock is 8.8% against 21.1% for prompt-only and 32.6% for chat-only. Chat-only has 61.2% of tool calls hitting resource conflicts.
- Rigid enforcement costs completion. The mediator-enforced runtime has the fewest deadlocks (4.5%) but only 44.7% full completion. It cannot adapt when a domain tool fails.
- The verified protocol buffers a weaker model. Moving from gpt-5-mini to gpt-5-nano costs verified-protocol runtimes about 15 points of average completion, against about 33 points for prompt-only and chat-only.
- Verification itself matters. In a paired ablation on 15 tasks under the same runtime, verified protocols cut deadlock/livelock from 31.1% to 14.1% and raised completion from 72.6% to 82.1%. The gap is largest under injected faults.

## Limitations admitted by the authors
- The guarantee holds only within bounds (finite agents, counters, queue depth); outside them it is incomplete.
- Liveness is not checked. The authors argue that valid protocols can loop forever, for example a reviewer who keeps rejecting.
- The monitor enforces topology, not step order. Step-order deviations still cause the 8.8% deadlocks in the monitored runtime, and the authors suggest a per-agent program-counter extension.
- When TLC times out on the hardest tasks (5 of 29 repairs), repairs simplify retries and branching. This can weaken fidelity to the intended coordination. The ablation shows mixed results on timeout-labeled tasks, while deadlock-labeled tasks show clear gains.
- Only one protocol-design model (Claude Opus 4.6) and two OpenAI runtime models were used, so generalization is open.
- Task semantics and output quality are not verified.

## Limitations found by others

## What it leaves untried
- No ablation separates the monitor from step-order enforcement. The conclusion lists this as future work, so it is not known which part of the runtime gain comes from the monitor.
- The benchmark is the authors' own and was built so that TLC is the ground truth. The paper invites tests on independently designed tasks but does not run any, so the 48-task result may not transfer to protocols someone else writes.
- Whether the checked state machine is followed at runtime is never measured directly. The paper gives only end-state outcomes (deadlock rate, completion), not a count of how often agents depart from the verified step order.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - communication topology and channels]]
