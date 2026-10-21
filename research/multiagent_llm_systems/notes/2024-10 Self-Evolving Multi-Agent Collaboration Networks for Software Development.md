---
title: Self-Evolving Multi-Agent Collaboration Networks for Software Development
authors: Yue Hu et al.
date: 2024-10
arxiv: 2410.16946
url: https://arxiv.org/abs/2410.16946
venue: arXiv
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2410.16946.pdf
folder: ["multiagent_llm_systems"]
topics: ["automated pipeline and topology search", "self-refinement and critique loops", "role-based agent teams"]
---
# Self-Evolving Multi-Agent Collaboration Networks for Software Development

## One line
EvoMAC rewrites a coding team's agents, prompts and workflow at test time, per task, using compiler feedback from LLM-written unit tests as a "textual gradient"; the paper also adds rSDE-Bench, a requirement-level coding benchmark.

## Method
Hand-designed multi-agent coding systems (ChatDev, MetaGPT) are fixed: their performance is capped by the human workflow and they do not adapt to a new task. EvoMAC treats the team as a small neural network. Agents are neurons, their prompts are weights, and the dependency graph (a DAG) is the layers.

One round has four steps:
- **Forward pass.** A coding organizer agent splits the requirements into subtasks and builds a team of coding agents with a workflow. The number of agents varies with the task.
- **Target proxy.** A separate testing team, built the same way, writes unit tests from the task text. The paper assumes writing tests is much easier than writing the code, and that a compiler can run the code against them objectively.
- **Loss.** The execution log is the "loss": which requirements pass, which functions fail, which tests are unmet.
- **Textual backpropagation.** A gradient agent reads the log and, per coding agent, says whether its subtask is done, whether it introduced errors, and which subtasks are missing. It can also flag the test code itself as wrong. An updating agent then deletes finished agents, appends fix hints to faulty agents' prompts, and adds agents for missing subtasks, redrawing the workflow.

The design choice that matters is the grounded feedback. A plain self-critique agent can be biased or hallucinate, so after several rounds the team "entrenches" its own preferences. Execution against tests is objective. The harness runs the code. The prompts only ask LLMs to write tests, read logs and rewrite the team.

rSDE-Bench: 53 tasks (45 websites, 8 games), 616 requirements, each paired with a black-box test. Accuracy is the share of tests passed. Earlier software benchmarks scored by text similarity or executability, which cannot tell whether requirements are met.

## Evaluated on
- Test-based scoring tracks human judgment where earlier metrics do not: correlation with expert human scores is 0.9922, against 0.2583 (consistency) and 0.3041 (quality). The paper's example scores 2/13 requirements met but 0.89 on consistency.
- With GPT-4o-Mini, EvoMAC beats the best baselines. Website Basic: 89.38 vs 62.90 single-agent and 62.67 for ChatDev. Game Basic: 77.54 vs 42.76 single-agent and 53.63 for ChatDev. HumanEval: 94.51 vs 90.85 for the best baseline.
- Accuracy rises with evolving rounds on all five settings, with GPT-4o-Mini and with Claude-3.5-Sonnet, and the stronger driver stays ahead. Game logic errors persist while page-display errors fall fast, so curves jump early and then plateau.
- Removing the compiler and using an LLM critique instead (ablation f vs g) costs 12.67 and 14.97 points on Website Basic and Advanced, and 21.74 and 18.28 on Game Basic and Advanced. Grounded feedback is the main factor.
- Shrinking the coding team to one agent costs 7.19 and 5.26 points on Website Basic and Advanced; shrinking the testing team to one agent costs 6.85 and 6.48. Multiple agents give more flexible edits.
- EvoMAC leads across task lengths. It degrades less on websites, which split into modules, than on games, which need coordinated state.

## Limitations admitted by the authors
- The method needs a cheap target proxy and an objective executor. The paper says this holds for code (tests are easier than programs, a compiler checks them), but the claim for other domains is not tested.
- Hard logic errors in games persist across rounds and performance plateaus, so the loop mostly fixes isolated, easy faults.
- Game tasks degrade more with longer requirements, because they need coordinated management.
- The benchmark covers only two software types, websites and games; the authors plan more types and a reward model to learn from feedback.

## Limitations found by others

## What it leaves untried
- Cost and latency. Each round runs a testing team, a gradient agent and an updating agent, but the paper reports no token or time cost, so gains per unit compute are unknown.
- Test quality. Everything is aligned to LLM-written tests; the paper gives no measure of how often those tests are wrong or how often the "wrong test code" check fires, so errors in the proxy could steer the team wrong.
- Other domains with a verifier, and comparing textual backpropagation with simply re-running a fixed team on the same test feedback.

## Topics
[[Topic - automated pipeline and topology search]] · [[Topic - self-refinement and critique loops]] · [[Topic - role-based agent teams]]
