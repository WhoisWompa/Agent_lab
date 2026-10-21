---
title: "Co-Saving: Resource Aware Multi-Agent Collaboration for Software Development"
authors: Rennai Qiu et al.
date: 2025-05
arxiv: 2505.21898
url: https://arxiv.org/abs/2505.21898
venue: arXiv (preprint, under review)
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2505.21898.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams", "communication topology and channels"]
---
# Co-Saving: Resource Aware Multi-Agent Collaboration for Software Development

## One line
Adds "shortcuts" mined from past successful runs to a ChatDev-style software team so it skips redundant instructor-assistant rounds, cutting tokens by 50.85% while raising code quality.

## Method
The problem: role-based teams such as ChatDev run long chat chains (instructor comments, assistant rewrites the code) and never look at how many tokens or how much time they have used. Cost grows with every round, and nothing tells the team when to stop.

The paper models one run as a directed graph. Nodes are successive code solutions and edges are the instructions that turn one into the next. A shortcut is an extra edge from node i to a later node j, which skips the steps in between. Its text is a single instruction saying how to go from the earlier code to the later code. It is not a concatenation of the intermediate edges (the case study shows it is more detailed). Shortcuts are extracted from every run in a training set and stored as memory.

At run time the system retrieves a similar past task, the "reference chain", and scores that task's shortcuts:
- **Feasibility filter.** A shortcut is dropped if the time or tokens needed to produce it exceed what is left in the budget.
- **Value.** Each solution node is scored by its embedding similarity to the task, times its similarity to the final solution, times 1 if the code compiles and 0 if not. The shortcut's value is the score gain from its start node to its end node.
- **Cost.** Time and tokens are each turned into percentile ranks among all shortcuts, then combined by harmonic mean.
- **Emergency factor.** The harmonic mean of the fraction of the time budget and the fraction of the token budget already spent. It moves the weight from value (early, resources plentiful) to cost (late, resources scarce). The paper gives the factor's definition and rationale but not the exact formula that combines it with value and cost.

The chosen shortcut is handed to the reviewing agent, which writes a fuller instruction from it. A hard rule ends the run once the live graph has as many edges as the reference graph. The harness enforces that stop rule and the budget filter. Prompts only supply the shortcut text.

## Evaluated on
SRDD software tasks (five categories, 40 subcategories), with GPT-3.5-Turbo as the base model.
- Higher overall quality than every baseline: 0.2515 against ChatDev 0.1510, MetaGPT 0.0593, ReAct 0.1965 and GPT-4 0.2109. The abstract's "10.06% improvement over ChatDev" matches the absolute gap (0.1005) in this product-of-four-scores metric, not a relative gain. Relative to ChatDev it is about 67%.
- Far more runs finish inside the budget: budgeted completion rate 0.7280 against ChatDev 0.0160 and MetaGPT 0.2720. Single-agent baselines score 1.0 on this rate but write less complete code (GPT-Engineer completeness 0.5200).
- The three parts each matter in the ablation. Removing the feasibility filter drops completion rate from 0.80 to 0.60. Removing cost leaves it at 0.75 and lowers completeness from 0.925 to 0.825. Removing the emergency factor lowers quality from 0.5453 to 0.4811.
- Runs get shorter: Figure 3 shows lower path length, time and tokens with Co-Saving. The text gives no numbers beyond the 50.85% token figure.

## Limitations admitted by the authors
- Completeness is lower than ChatDev (0.8160 against 0.9040). The authors say that when the budget runs out the system stops early and trades completeness for efficiency.
- The consistency metric (embedding similarity of code to requirement) barely separates systems, with all values near 0.77 to 0.81. The authors say current embeddings cannot see fine code-text mismatches, so this dimension says little.
- Single-agent baselines inflate executability (ReAct 1.0, Co-Saving 0.6880), because stubbed code still compiles. Executability alone is therefore a weak comparison.

## Limitations found by others

## What it leaves untried
- Only GPT-3.5-Turbo and one dataset (SRDD, software) are tested. Whether shortcuts transfer to other base models or non-code tasks is not examined.
- The forced stop copies the length of the retrieved reference chain. If the new task is harder than its reference, the run is cut short. The paper does not test retrieving a poor reference or measure how often the early stop costs correctness.
- The value, cost and emergency terms are combined heuristically with no tuning or sensitivity study. The reported ablations also use a different quality scale from the main table (full model 0.5453 against 0.2515), which the paper does not explain.

## Topics
[[Topic - role-based agent teams]] · [[Topic - communication topology and channels]]
