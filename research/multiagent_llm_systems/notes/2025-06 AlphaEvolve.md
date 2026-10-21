---
title: AlphaEvolve: A coding agent for scientific and algorithmic discovery
authors: Alexander Novikov et al.
date: 2025-06
arxiv: 2506.13131
url: https://arxiv.org/abs/2506.13131
venue: arXiv (Google DeepMind white paper)
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2506.13131.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops"]
---
# AlphaEvolve: A coding agent for scientific and algorithmic discovery

## One line
An evolutionary loop in which an ensemble of Gemini models rewrites code and automatic evaluators score every rewrite, used to find new algorithms, new mathematical constructions and faster pieces of Google's compute stack.

## Method
The problem: getting LLM pipelines to make real discoveries, not just score well on benchmarks. The idea is to let the LLM propose and let code execution judge. The human supplies the "what": a starting program with the parts to change marked, and an `evaluate` function that maps a program to one or more scalar scores. The system supplies the "how".

Each round, a controller samples a parent program and some high-scoring "inspiration" programs from a database. A prompt sampler builds a long prompt from them: their code, their scores and outputs, problem context, and prompts that the LLM itself evolved (meta-prompts). The LLMs return edits as search/replace diffs, which are applied to the parent. Evaluators run the child and its scores go back into the database. The database mixes MAP-elites and island-population ideas so it keeps improving the best programs while staying diverse.

What is new compared with its predecessor FunSearch:
- It evolves a whole file of hundreds of lines in any language, not one function of 10-20 lines.
- It uses a fast Gemini Flash model for volume and a stronger Pro model for occasional better ideas.
- It optimizes several metrics at once. The authors find this helps even when only one metric matters, probably because programs good under different metrics put varied examples in the prompt.
- It evaluates with a cascade of increasingly hard tests, runs evaluations in parallel (up to roughly 100 compute-hours per candidate), and can add LLM-graded feedback such as program simplicity.

Correctness comes from the harness, not the LLM. Wrong suggestions are filtered because every candidate is executed and scored. In the deployed cases the evolved part is only a heuristic (scheduler priority, tile sizes), so the surrounding system stays correct by construction.

## Evaluated on
- Beats the best known result on matrix-multiplication tensor ranks for 14 targets. For 4x4 complex matrices it gets 48 scalar multiplications, against Strassen's 49 that stood for 56 years. The 4x4 result needed only a simple starting program.
- On over 50 open math problems: matches the best known construction in about 75% and finds a better one in about 20%. Examples are the Erdős minimum overlap problem and kissing numbers in 11 dimensions.
- A scheduling heuristic for Google's Borg, chosen over deep RL for interpretability, recovers on average 0.7% of fleet compute that would otherwise be stranded. Post-deployment measurements confirmed the simulator results.
- A tiling heuristic for a Gemini training kernel gives an average 23% kernel speedup and 1% shorter Gemini training time. It took days instead of months of engineering.
- Ablations on tensor decomposition and kissing numbers: removing evolution, prompt context, meta-prompt evolution, full-file evolution, or the large model each lowers the curve. The text reports this as "significant" for each. Results are averaged over three seeds, and no per-component numbers appear in the text.

## Limitations admitted by the authors
- It only works where an automatic evaluator exists. Problems that need manual experiments are out of scope, which is why it targets maths, computer science and systems.
- LLM-graded evaluation of ideas is supported but "not a setting we have optimized for".
- Gains on its own infrastructure are moderate, and the feedback loop for improving the next version takes months.
- Some wins are not purely the system's. Certain matrix results improved when the authors seeded their own ideas. The circuit-design bit-trimming was also found independently by downstream synthesis tools.
- The way the problem is framed biases the result. Evolving a constructor function may favor symmetric objects, so different problems need different abstractions. The authors give this as a hypothesis without testing it.

## Limitations found by others

## What it leaves untried
- Distilling the evolution-improved outputs back into the base LLM. The authors name it as the natural next step but do not run it.
- Feeding LLM feedback on high-level ideas before the implementation stage, which would reach domains with no executable evaluator.
- Comparison with a plain repeated-sampling budget on the engineering tasks. The ablations cover only two math tasks, and no cost figures are given for the deployed results.

## Topics
[[Topic - self-refinement and critique loops]]
