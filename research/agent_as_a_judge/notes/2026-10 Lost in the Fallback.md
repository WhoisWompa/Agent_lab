---
title: "Lost in the Fallback: How Reliably Do Typed Decision Models Use Fallback Options?"
authors: Yuanbo Xie et al.
date: 2026-10
arxiv: 2610.19856
url: https://arxiv.org/abs/2610.19856
venue: arXiv
category: agent-evaluation-benchmarks
pdf: agent as a judge papers/decision models/open models/evaluations/Lost in the Fallback - How Reliably Do Typed Decision Models Use Fallback Options (Xie 2026).pdf
folder: ["agent as a judge", "decision models", "open models", "evaluations"]
topics: ["decision models", "judge and decision-model audits", "abstention and fallback", "presentation sensitivity"]
---
# Lost in the Fallback: How Reliably Do Typed Decision Models Use Fallback Options?

## One line
Introduces the Paired Fallback Robustness (PFR) Test and shows that open typed decision models (Jev-style choosers) often fail to pick a supplied fallback option ("Other", "Defer") even when they recognise the input's category, and flip decisions under logically equivalent wordings of the fallback rule.

## Method
Problem: typed decision models (TDMs) used for routing or as a fast System 1 controller rely on a fallback option to hand off requests that no regular option covers (general support, a slower System 2 model). Missing the fallback skips needed handling; overusing it adds cost. Prior work studied adversarial attacks; this asks about plain, non-adversarial use.

Idea: make fallback correctness testable by fixing a full category inventory U, giving some categories S their own options and covering the rest R = U \ S with one fallback. The required output is the input's category if it is in S, otherwise the fallback. Because the inventory is complete and every input has exactly one valid destination, the same input can be moved from "regular" to "fallback" just by swapping which categories get options, without changing the input or option count. PFR builds four requests per input by crossing:
- two assignments (gold category has its own option vs. gold category moved into fallback), testing *correct reassignment*: the output must change;
- two logically equivalent fallback definitions, Union (list the fallback members) and Complement (anything not covered by the other options), testing *definition consistency*: the output must not change.

The headline metric is the four-request pass rate (P4), alongside joint correctness across assignments (J) and Union/Complement disagreement (DR). Scoring per input matters because equal aggregate accuracy can hide opposite-direction flips, and trivial always/never-fallback behaviour fails the joint test. The same logic is extended to Fast/Defer policies, where the required action is fixed by a supplied quality–cost inequality.

## Evaluated on
- Fallback is the weak link: P4 ranges from 18.2% to 81.0% across twelve model–dataset settings (four 4B models; CLINC150, BANKING77, TREC50).
- Correct recognition does not transfer: on TREC inputs Intern classifies correctly in a separate task, Complement accuracy drops from 97.9% (gold-regular) to 23.1% (gold-fallback).
- Supplying the correct category is not enough: with the gold label given, JevK5 is perfect on regular cases but reaches only 71.1% (Union) and 14.8% (Complement) fallback recall on TREC.
- Equal accuracy hides different decisions: JevK5 on CLINC has J = 55.8% under both definitions and recall differing by 1.8 points, yet a third of its fallback-case choices change and only 40.9% pass all four requests. Fallback position alone swings the Complement-minus-Union gap from -41.4 to +35.2 points, averaging to +0.3.
- Defer policies fail completely: joint policy correctness is zero for all four models under both criteria; two models always choose Fast.
- Fixes trade one error for another: classify-then-map lifts Intern/TREC J from 21.0% to 65.8% but leaves 22.8% false fallback; a tuned threshold raises recall from 22.6% to 75.6% while false fallback rises from 1.4% to 20.6%. Calibrating false fallback to 5% still leaves 10.7%-44.9% disagreement and P4 as low as 3.6%.

## Limitations admitted by the authors
- Diagnosis only, no mitigation: the paper identifies the failures but develops no method to fix them, and its own interventions (membership tables, thresholds) repair some errors while introducing others.
- Controlled settings may not match real deployments: the synthetic coverage setup uses intent and question-classification datasets with a complete inventory; how often these failures occur in open-ended production routing is unshown.

## Limitations found by others

## What it leaves untried
- Training or fine-tuning on paired assignment/definition data: the analysis suggests the scores contain recoverable signal (individual thresholds would fix 359 of 500 Intern/TREC inputs vs. at most 205 with one shared threshold), so a learned fix is the obvious next step, and it is untested.
- Larger or closed models: all tested models are 4B or smaller open-weight TDMs; whether hosted Jev or larger LLMs show the same Union/Complement gap is not measured.
- Open-world fallback: inputs from genuinely unknown categories, the main real reason a fallback exists, are deliberately excluded.

## Topics
[[Topic - decision models]] · [[Topic - judge and decision-model audits]] · [[Topic - abstention and fallback]] · [[Topic - presentation sensitivity]]
