---
title: Scaling Agents for Computer Use
authors: Gonzalo Gonzalez-Pumariega et al.
date: 2025-10
arxiv: 2510.02250
url: https://arxiv.org/abs/2510.02250
venue: arXiv
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2510.02250.pdf
folder: ["multiagent_llm_systems"]
topics: ["LLM and agent judges"]
---
# Scaling Agents for Computer Use

## One line
Runs many independent computer-use agent rollouts and picks the best with Behavior Judge (BJudge), a VLM judge that compares short "behavior narratives" instead of raw screenshot trajectories, reaching 72.6% on OSWorld.

## Method
Problem: a computer-use agent that runs once is brittle. Small errors compound over dozens of steps, so the same agent succeeds on one attempt and fails on the next. Different agents solve complementary task subsets (the paper's Figure 2), so sampling many rollouts and selecting one ("wide scaling") should help. The bottleneck is selection. Trajectories are long, multimodal and mostly irrelevant detail, many tasks have several valid solutions, and OSWorld's scripted checkers cannot be used at run time.

Idea: split the judge's job in two.
- A narrative generator (a VLM) looks at each transition (screenshot before, action, screenshot after) and writes the facts that the action changed. For pointer actions it marks the click point on the before image and adds a zoomed crop of the after image, because click hallucination ("Save was clicked" when it was not) can decide success. The after screenshot is taken 3 seconds later to catch delayed effects. The narrative is the facts plus the first and last screenshots.
- A comparative evaluator, one VLM call, sees all candidate narratives and picks the best as a single multiple-choice question. The prompt asks it to cite and contrast facts.

Why it should work: the judge no longer has to read the long history within each rollout, so it can spend its effort on discriminating between candidates. Choosing among candidates jointly is also cheaper than a pairwise tournament.

Rollouts come from Agent S3, a rebuilt baseline. It drops the manager-worker hierarchy for one flat policy and lets that policy call a coding agent (Python/Bash in a sandbox) as one of its actions. Candidates can be pooled across different models for diversity.

## Evaluated on
- Reaches 72.6% on OSWorld at 100 steps, using 10 rollouts from GPT-5 and Opus 4.5. That beats the prior best scaling method, GTA1 at 63.4%, and the human level of 72.36%. GPT-5 rollouts alone give 69.9%, against 62.6% for a single Agent S3 run.
- The new baseline helps by itself. Agent S3 improves on Agent S2 by 13.8 points (48.8 to 62.6), with 52.3% fewer LLM calls and 62.4% less time per task.
- Comparison beats independent scoring. An adapted WebJudge, which scores each trajectory separately, plateaus and drops near 10 rollouts, and gets 50.4% against BJudge's 60.2% with GPT-5 Mini rollouts.
- The narrative representation matters. With GPT-5 Mini rollouts it gets 60.2%, against 56.0 (screenshots only), 55.0 (3-6 sentence summary) and 56.8 (per-screenshot captions).
- Diversity raises the ceiling. GPT-5 plus Opus gives the best success at 71.6%. Mixing all four models gives the highest coverage, with a correct answer somewhere for 80.5% of tasks.
- Selection accuracy is 78.4% on the 159 tasks where candidates disagree, scored by OSWorld scripts. It rises to 92.8% after human inspection, because the scripts accept only one predefined solution.
- Transfers with N=3 rollouts: WindowsAgentArena 50.2 to 56.6 at 100 steps, AndroidWorld 68.1 to 71.6.
- Judging is cheap next to rollouts: about $0.14 against $0.72 per task for GPT-5 (narratives $0.11, judging $0.03).

## Limitations admitted by the authors
- It needs several independent rollouts from the same starting state. This holds in snapshot-able VMs, but concurrent runs on a live desktop can interfere, and shared external state (email, cloud storage, shopping carts) leaks between runs.
- Narrative hallucinations cause errors. Of 12 failures examined, 8 came from the VLM misreading fine detail, e.g. dropping the minus sign on -17.0 even with zoom.
- The other 4 failures come from code-to-GUI handoff. The GUI agent fails to recognise the coding agent's edit and overwrites it. The judge then prefers that rollout because its GUI narrative is rich, over a correct one-step code solution with a thin narrative. This points to a bias toward verbose narratives.
- Small compute budgets do not benefit. A single agent wins when splitting the budget leaves each worker too few steps to finish.

## Limitations found by others

## What it leaves untried
- Judge fixes for narrative-length bias and hallucination. The paper names both failure causes but offers no fix or measurement beyond 12 cases.
- Narrative generation inside the rollout instead of afterwards, to cut latency. The authors say it could be done and only run it post hoc (the full run took 17h33m).
- A trained judge. Everything here is prompted. The open-model test shows the judge model matters: Qwen3 narrator and evaluator gave 40.9% against 51.5% for GPT-5 on the same rollouts.

## Topics
[[Topic - LLM and agent judges]]
