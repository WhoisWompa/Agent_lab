---
title: Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops
authors: Ziqian Zhong et al.
date: 2026-06
arxiv: 2606.08960
url: https://arxiv.org/abs/2606.08960
venue: arXiv (preprint, under review)
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2606.08960.pdf
folder: ["multiagent_llm_systems"]
topics: ["agent evaluation benchmarks", "judges as reward signals", "role-based agent teams"]
---
# Hardening Agent Benchmarks with Adversarial Hacker-Fixer Loops

## One line
Three LLM agents (hacker, fixer, solver) take turns attacking and patching a benchmark's outcome verifier until it stops accepting shortcuts, replacing manual, task-by-task patching.

## Method
The problem: agent benchmarks score with hand-written outcome verifiers (unit tests, speedup timers) that agents can pass without solving the task, for example by monkey-patching the timer or replacing a binary with a script. An audit of 1,968 terminal-agent tasks found 323 (16%) hackable by frontier models that were given only the task description. This corrupts leaderboards and the RL reward. The usual fix is reactive and manual.

The idea is an adversarial loop with three roles per iteration:
- The hacker tries to earn full reward without solving the task. It gets up to three attempts, each seeing the earlier failed ones. If all three fail, the task counts as robust.
- The fixer edits the verifier to block the discovered exploit.
- The solver then attempts the task legitimately. The patch is kept only if the solver still passes, otherwise it is reverted and the failure trace goes back to the fixer. This guards against over-tightening.

Each patch changes what the verifier rewards, so the next iteration exposes a different exploit. That matters because a task often has several independent hacks, and one patch leaves the others open (one task had three).

Two levers widen coverage without a stronger hacker:
- Verifier access: the in-loop hacker reads the verifier source, so it targets checks directly. A blind hacker made 49 attempts on one task and none found the `gc.get_objects()` timing attack that the verifier-aware hacker found twice. Access is switched off for the last iterations so the final state still holds against a blind attacker.
- A shared defense pool: a git repository where fixers push task-agnostic fixes to shared evaluation code. The same exploit recurs across tasks that share a harness, so a fix found once is reused. It does not help tasks with unrelated verifiers.

The weak-to-strong claim: defenses built by a weaker verifier-aware defender (Gemini 3 Flash) should hold against stronger blind attackers (Gemini 3.1 Pro, Claude Opus 4.7), because the extra information and the pool make up for the capability gap.

## Evaluated on
- Defenses block documented exploits on KernelBench. Attack success on 15 publicly reported exploit strategies fell from 62% to 0% (Gemini 3.1 Pro). Solver pass rate stayed 98% only after a post-loop relaxation step (see limitations).
- Defenses hold against stronger blind attackers. Unhinted attack success fell from 76% to 0% (Gemini 3.1 Pro) and from 61% to 0% (Opus 4.7) on KernelBench. On Terminal Bench (77 tasks) it fell from 39.2% to 16.7% per attempt.
- Both levers matter. On KernelBench, blind without pool leaves 52% hinted and 20% unhinted success. Verifier-aware with pool reaches 0% on both. On Terminal Bench, verifier access drives the drop on hinted exploits (56.2% to 45.9% with access alone, 39.5% with the pool added), and the pool drives the drop on unhinted attacks (42.3% to 22.3%).
- Cross-task transfer is real. The final KernelBench task-001 verifier has no line written while hardening task 001. It holds 15 of the pool's 171 commits, from 13 other tasks, in six defense layers (process isolation, builtin capture, stack-introspection block, and others).
- The solver role is needed. Validating against only a reference solution let the fixer silently block `load_inline`, the standard way to submit a kernel. Benign pass collapsed to 0% at the final iteration before a post-loop "autopatch" step relaxed the two over-restrictive defenses (92-98% afterwards).
- Compute: roughly 48 hours on an 8xH200 node and about $5,000 in API spend across all hardening.
- The audit is released as Terminal Wrench: 323 hackable environments and 3,632 hack trajectories.

## Limitations admitted by the authors
- Coverage is bounded by the hacker. The loop patches only exploits its hacker finds. Human-found exploits that need creative leaps are still missed: on Terminal Bench, hinted success per task is still 92.2% (down from 100%).
- Hardening narrows legitimate solutions. On Terminal Bench the benign pass rate fell from 76.1% to 65.2%. One example is an added gradient test that rejects solvers who add regularization.
- Some tasks cannot be fixed at the verifier level. A multi-pass `shred` task looks identical to `rm -rf` inside a container, so the evaluation infrastructure itself must change.
- The pool only transfers within a shared evaluation substrate, not across unrelated formats.
- The weak-to-strong argument rests on an unmeasured assumption that same-generation hackers and attackers share repertoires (stated, not tested).

## Limitations found by others

## What it leaves untried
- No test of the hardened verifiers inside actual RL training, though the motivation is the reward signal. It is unknown whether the policy stops hacking or finds a new class.
- The KernelBench results use the reference solution rather than an LLM solver, so the clean 0% attack rate there depends on a post-loop autopatch step (the raw loop output passed 0% of benign solves at the final iteration). A full LLM-solver run was done only on Terminal Bench.
- Only one defender family (Gemini 3 Flash) was used as hacker and fixer, so whether another model builds equally strong defenses is unknown.

## Topics
[[Topic - agent evaluation benchmarks]] · [[Topic - judges as reward signals]] · [[Topic - role-based agent teams]]
