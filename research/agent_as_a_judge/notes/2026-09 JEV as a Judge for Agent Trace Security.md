---
title: "JEV as a Judge for Agent Trace Security: An Empirical Comparison with Generative LLM Judges"
authors: Zhiqiang Wang et al.
date: 2026-09
arxiv: 2609.34862
url: https://arxiv.org/abs/2609.34862
venue: arXiv
category: alternative-paradigms
pdf: agent as a judge papers/decision models/open models/evaluations/JEV as a Judge for Agent Trace Security - Comparison with Generative LLM Judges (Wang 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits"]
---
# JEV as a Judge for Agent Trace Security: An Empirical Comparison with Generative LLM Judges

## One line
Compares JEV, a typed decision model, with four generative LLM judges on labelling completed tool-using agent traces safe or unsafe. JEV ends up slightly more accurate on average and 30x faster and cheaper, while GLM-5.2 stays more precise.

## Method
The problem: whether a trace is unsafe depends on context (was a transmitted value authorised; was an injected instruction seen or followed). Generative judges handle this but pay for rationales, JSON validation and repair calls. Does a deployment needing only a bounded verdict have to pay for that?

The alternative is JEV's typed interface. The judge gets a state (the rendered trace) and four typed questions in one request:
- an overall 1-5 risk score
- authorization (four choices)
- intrinsic safety (three choices)
- severity (0-5)

It returns each answer with a probability distribution and no free text. Generative judges get the same trace rendering and the same five risk anchors, plus a rationale and evidence. Both verdicts use one rule: unsafe if score >= 3. The rubric separates authorization from intrinsic safety: consent does not make harm safe, and meeting an attack is not following it.

The paper proposes no new method; the bet is that typed questions keep most of the accuracy at a fraction of the latency and cost.

## Evaluated on
- **Highest mean F1, but a narrow margin.** JEV scores 77.8 mean positive-class F1 against 74.1 for GLM-5.2. The other judges score 49.4-61.0. On the traces both judges answered, the gap is 2.7 points, with an exploratory bootstrap interval of [0.5, 4.8].
- **The ranking flips by dataset.** JEV leads on ATBench500 (93.8 vs 85.9) and MCPHunt (61.1 vs 44.9). GLM leads on R-Judge (93.4 vs 88.5) and TraceSafe (72.4 vs 67.8).
- **JEV balances precision and recall; the generative judges lean toward precision.** JEV's mean precision and recall differ by 2.1 points, against 24.0-54.8 for the generative judges. GLM, for example, has 91.9 precision but only 64.1 recall.
- **Much faster and cheaper.** JEV's median latency is 0.99 s; the generative judges average 9.61-37.39 s. JEV costs an estimated $0.000195 per valid verdict, 6.8-76.3x less than the others.
- **Holds up better on long traces.** Above 16 steps JEV scores 57.5 F1 against GLM's 50.6. On inputs of 8k tokens or more it scores 62.8 against 48.7.

## Limitations admitted by the authors
- **The prompts were not the same.** The LLM prompt adds detailed rules for counterevidence and action stages, and asks for Chinese explanations. JEV gets shorter instructions. Part of the gap may come from instructions, not interface.
- **The authors relabelled two datasets.** TraceSafe and MCPHunt use the study's revised labels (resisted injections and signal-only cases count as safe), unreviewed by anyone independent. MCPHunt supplies most of JEV's mean advantage: +14.2 F1 on paired traces.
- **Missing outputs bias the comparison.** Each judge is scored only on its valid answers; DS-V4-Pro's 98.7% ATBench500 accuracy covers 151 of 500 traces. The paired comparison does not remove this bias.
- **Cost and latency depend on setup.** Latency excludes failed calls, repairs and retries. Cost uses configured prices with JEV charged nothing for output tokens, which explains part of the 76x gap.
- **The length trend depends on dataset mix.** Without MCPHunt, GLM beats JEV in most bins (83.0 vs 75.5 at 4 steps or fewer, 73.1 vs 70.0 above 16), so "better on long traces" mostly reflects MCPHunt.

## Limitations found by others

## What it leaves untried
- **No threshold sweep or precision-recall curve.** Every judge uses the same cutoff of 3. GLM's high precision and low recall suggest it is mis-thresholded, not weaker, so a per-judge sweep could close or reverse the 3.7-point gap.
- **JEV's probabilities are never used.** JEV returns a distribution for every answer, but the paper scores only the top answer and never tests calibration. The screening-then-escalation pipeline the paper recommends depends on routing uncertain traces to a closer review, and it is never built or measured.
- **Precision as a screen is not examined.** On MCPHunt JEV raises 439 false positives against 531 true positives. How many false alarms a screen can afford is not discussed.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]]
