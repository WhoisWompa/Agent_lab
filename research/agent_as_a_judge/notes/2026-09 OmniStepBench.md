---
title: "OmniStepBench: Deployment-Aware Agent Evaluation across Modalities and Task Complexity"
authors: Yu Liu et al.
date: 2026-09
arxiv: 2609.06059
url: https://arxiv.org/abs/2609.06059
venue: arXiv
category: agent-evaluation-benchmarks
pdf: agent as a judge papers/DAREBench - Deployment-Aware and Reliable Evaluation of Models as Agents (2026).pdf
folder: ["agent as a judge"]
topics: ["agent evaluation benchmarks", "alternative evaluation paradigms"]
---
# OmniStepBench: Deployment-Aware Agent Evaluation across Modalities and Task Complexity

(The PDF file is named DAREBench; the v2 text in it is titled OmniStepBench.)

## One line
A 233-task agent benchmark that runs every model in one shared runtime, reports accuracy per workload type (text or multimodal, crossed with single-step, multi-step or tool-using), and adds an audit step: a second judge checks whether the first judge's positive scores are backed by what the agent actually did.

## Method
The problem: agent leaderboards give one aggregate score, run each model in a different harness, and grade with LLM judges that can give credit for work that never happened. That makes them a poor basis for choosing a model to deploy. The paper's answer has three parts.
- **Workload matrix instead of one score.** Tasks taken from 22 existing benchmarks are sorted into a 2×3 grid: input modality (text or multimodal) crossed with execution form (single-step, multi-step, multi-step plus tools). Accuracy is reported per cell, on the assumption that deployment needs map onto a cell, not onto an average.
- **One runtime and a contract for each task.** Every model runs in the same OpenClaw agent loop with the same tools. Each task states which artifacts it must produce, with a validity check for each one. The idea is that differences in score then reflect the model and not how well it fits a particular harness.
- **Evidence-based audit of judge credit.** Tasks are scored by rules, by an LLM judge (Qwen3.5-VL-Plus, rubric plus a summarised trajectory), or a weighted mix of both. Every positive score the judge gives passes through cheap deterministic flags: assistant output length, whether the agent wrote a file, whether it called a tool, total tokens. Flagged cases go to a meta-judge from another model family (Claude-Opus-4.6). It sees the full trajectory, the artifacts, the rubric and the first judge's reasoning, and rules the score "hallucination" or "legitimate". A hallucinated score is set to zero, and a legitimate one is kept as it is. The design rests on the assumption that the judge's errors are false positives with weak execution evidence, so cheap high-recall rules followed by one expensive check can catch them.

## Evaluated on
- **No single model wins every cell, so a single ranking misleads.** GPT-6.1-Sol leads text on average (81.2) but GPT-6-Astra leads multimodal (78.0). Claude-Opus-4.8 is best on MM-SS (85.0) but only sixth on the multimodal average (71.1).
- **Accuracy falls as tasks get longer and use tools.** The top text model goes from 96.1 single-step to 71.3 with tools. MM-MT is the hardest cell: the best score is 67.6 and Gemini-3.1-Pro gets 32.7.
- **Cost and accuracy are only loosely linked.** GPT-6.1-Sol reaches 81.2 text at $0.100 per task, while GPT-6-Astra gets 80.3 at $0.654. MiMo-V2.6-Pro gets 77.4 at $0.009.
- **Local models lag behind, and the gap is widest on long tasks.** The best local model, Qwen3.6-27B, reaches 61.8 text and 55.1 multimodal, against 81.2 and 78.0 for the best API models. On Text-MT it scores 37.2 against 71.3.
- **The audit catches real judge errors, but they are rare.** Of 4,096 judge or hybrid scores, the rules flagged 182 and the meta-judge confirmed 143, about 3.5%. 124 of the 143 were in local runs. Deadlock loops (86) and pseudo-tool-call credulity (20) occurred only in local runs.
- **After the audit, scores are closer to experts.** On 100 stratified trajectories graded by human experts, the mean absolute error was 0.049 after the audit against 0.098 for the primary judge alone.

## Limitations admitted by the authors
- **One runtime only (OpenClaw).** Rankings may not hold in harnesses with different tool semantics or orchestration. This weakens the claim that the comparisons can be attributed to the models, since harness fit is fixed rather than removed.
- **API and local models are not compared on equal terms.** Local models ran with a 32K context on one GPU, while API models had their native limits. Deadlock loops are defined as running out of the 32K window, so most of the audit's findings, and part of the local-model gap, may come from the setup rather than the models.
- **233 tasks cannot cover real-world agent work.** Results depend on the task mix and should not be read as a universal ranking.
- **The judge-error patterns belong to this deployment profile.** The authors warn against applying the pattern counts to other runtimes or context limits.

## Limitations found by others

## What it leaves untried
- **Auditing scores the judge set too low, and checking whether the rules miss cases.** Only positive scores that trip the rules ever reach the meta-judge. Unflagged hallucinations and wrongly low scores are never reviewed, and the paper does not measure the rules' recall. The 3.5% figure is therefore a floor, not an error rate.
- **Partial correction instead of all-or-nothing.** An unsupported score is reset to zero as a whole. A run that did half the work but was over-credited cannot be graded down to what it actually earned.
- **Testing the judges against their own families.** The meta-judge (Claude-Opus-4.6) and the primary judge (a Qwen model) belong to families that are among the models being ranked. The paper does not test for self-preference, and it reports results from a single seed with no variance, even though some cells hold only 20 tasks.

## Topics
[[Topic - agent evaluation benchmarks]] · [[Topic - alternative evaluation paradigms]]
