---
title: The Unreliable Progress Bar: Can LLM Agents Reliably Report Task Progress Throughout Execution?
authors: Boyang Wang et al.
date: 2026-09
arxiv: 2609.08589
url: https://arxiv.org/abs/2609.08589
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2609.08589.pdf
folder: ["multiagent_llm_systems"]
topics: ["agent evaluation benchmarks", "agent system failure analysis"]
---
# The Unreliable Progress Bar: Can LLM Agents Reliably Report Task Progress Throughout Execution?

## One line
Measures whether LLMs can tell the runtime which lifecycle stage a task is in, at every stage, and finds that reports are reliable at some stages and collapse at others.

## Method
Many agent frameworks let a model-emitted signal (a "done" call, a stage tag) decide whether the loop continues or stops. The model is, in the authors' words, its own progress bar. Benchmarks score what an agent does; none scores what the model tells the runtime about whether work remains. This paper does that.

Two instruments. First, tau2-bench (telecom and retail) with one added duty: every customer-facing reply ends with a stage tag (NEEDS_INFO, READY, POST_OBS, COMPLETED). The correct tag is derived by replaying the conversation in a fresh environment and reading its state, before the model's tag is looked at. Second, StageIF, a controlled testbed of 12 scripted scenarios. The reporting duty is placed at chosen points, switched off where a report would itself be an error, and the answer key is frozen before the model answers. It scores four failure layers separately: acting instead of reporting (tool call in place of the report), omitting the report, malforming it, and naming the wrong stage. This separates a report that never arrives from one with a wrong value, and both from task success, which is read from environment state.

The authors then run bounded interventions (supply the true stage, give a constant value, add a reminder, change reasoning mode, change the continuation context) to see whether simple changes to the demand remove the gap.

## Evaluated on
- Reliability depends on stage. gpt-4.1 and gpt-5.5 are correct at 90.6-99.4% of pre-action and 87.3-88.9% of post-completion checkpoints but only 5.8-11.5% mid-task on tau2-bench.
- On StageIF the mid-task dip is large for six of seven original deployments, 29.4-89.3 points below terminal adherence. One deployment hits 97.4% terminal but 8.2% intermediate. gpt-5.5 is the exception (gap -4.2, interval includes zero).
- Failure form depends on the setting. On tau2-bench, wrong but well-formed values dominate: 82-90% of mid-task errors name a pre-action stage already left. In StageIF, omissions and tool calls in place of reports drive most of the decline; wrong values reach only 13.6 points at the post-action checkpoint and stay under 2 elsewhere.
- Newer models shift the weakness. gemini-3.8-flash, gpt-6-astra and claude-opus-5 hold 74-100% mid-task but only 48-64% at completion, always naming an earlier state.
- Simple fixes do not close the gap. Supplying the true stage covers at most one sixth of the gap; a reminder's best gain is +9.3 points against gaps of 29-89. Withdrawing a tool and assigning the step elsewhere raises false completion from 6.2% to 64.4% with task truth unchanged.
- Consequences: the marker-reporting configuration completes 13.0 points fewer tasks than a no-tool-call stop (CI +7.1 to +19.4), though the arms differ in more than the gate rule.

## Limitations admitted by the authors
- Deployment names denote a model plus its serving setup, and endpoints may silently drop sampling parameters, so results are a snapshot, not a model ranking.
- All effects are behavioral. The paper explicitly does not identify an internal mechanism, and stage, dialogue depth and available actions co-vary, so the cause of the mid-task dip is open.
- The context-change intervention is bundled (tool withdrawal plus reassignment), so it gives a total effect, not the effect of either part.
- Rollout terminal checkpoints are selected by survival, so they cannot show a stage gap in rollouts. The rollout's task-success difference is not shown to come from the mid-task wrong values.
- The tau2-bench customer-resolution cue is only a keyword proxy, so the link between caution and completion errors is an association.
- Four of eleven telecom deployments usually omit the tag and are dropped from the wrong-value analysis, and the strict parser scores gpt-6-astra at 0% (the answer sits inside a JSON wrapper), so some findings rest on an envelope-stripped diagnostic.

## Limitations found by others

## What it leaves untried
- No test of an external check. The conclusion says reports should be checked against independent task state, but no gate that does this is built or compared with model-owned termination.
- No mechanism study. Why action-bearing stages lose reports (memory, reasoning, instruction competition) is left open, so there is no fix beyond prompt tweaks that gain at most 9.3 points.
- No larger-scale scripted testbed. StageIF has 12 synthetic scenarios, which limits how far the stage pattern generalises to real long-running agents.

## Topics
[[Topic - agent evaluation benchmarks]] · [[Topic - agent system failure analysis]]
