---
title: Position: LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks
authors: Kambhampati et al.
date: 2024-02
arxiv: 2402.01817
url: https://arxiv.org/abs/2402.01817
venue: ICML 2024
category: generator-critic-loop
pdf: research/multiagent_llm_systems/pdfs/2402.01817.pdf
folder: ["multiagent_llm_systems"]
topics: ["self-refinement and critique loops"]
---
# Position: LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks

## One line
Argues that LLMs can neither plan nor verify plans on their own, and proposes a generate-test-critique loop in which the LLM only guesses candidates and external sound verifiers decide what is accepted.

## Method
The problem: claims that LLMs plan and can improve by self-critique are widespread, while the opposite error (using the LLM only as a text-to-solver translator) wastes what it can do. The paper's position has two halves.

First, the negative half. An LLM is a "giant pseudo System 1" doing approximate retrieval, so it cannot plan or verify. Verification is not easier than generation for it, because if the model is retrieving, task difficulty should be irrelevant, and nothing in training teaches it "corrections data". Apparent successes are explained as (a) confusing general planning knowledge with executable plans, (b) tasks where sub-goals do not interact or the world is forgiving, (c) humans in the loop quietly repairing plans, or (d) external verifiers (simulators, arithmetic checks) doing the real work, as in Tree of Thoughts on the 24 puzzle.

Second, the LLM-Modulo framework. The LLM gets the problem and proposes a candidate plan. A bank of critics checks it. Hard critics check correctness (causal, timeline, resource constraints, unit tests; for PDDL, the VAL validator) and are model-based, so they are sound. Soft critics check style and preferences and may be LLM-based. A plan is returned only when every hard critic signs off, so soundness comes from the critics, not the LLM. A meta (backprompt) controller pools the critiques into the next prompt, ranging from "try again" to a full list of faults, and may diversify prompts to widen candidate coverage. LLMs also act as reformulators (translating a plan into each critic's formal representation) and help experts draft the domain models behind critics. Humans take part only once per domain and once per problem, never in the inner loop, which the authors say is too costly and invites Clever Hans effects. Completeness depends on the LLM being able to generate the relevant candidates.

## Evaluated on
This is a position paper; evidence is mostly the authors' earlier work plus two preliminary case studies.
- LLMs fail at autonomous planning: about 12% of GPT-4 plans were executable and goal-reaching on average. Zero-shot Blocksworld reached 59.3% for the best model in the paper's table (Claude-3-Opus), but obfuscated "Mystery BW" gave 0% to 0.16% zero-shot for nearly all models. This supports retrieval over planning.
- Self-critique does not help: on graph coloring, GPT-4 was no better at verifying than at solving, and self-critique loops did worse than the baseline because the model passed over correct colorings it had produced.
- Chain-of-thought and ReAct prompting are reported as largely ineffective for planning (cited, no figures given here).
- With VAL as external critic and back-prompting, Blocksworld rose to 82% within 15 rounds and Logistics to 70%. Mystery BW reached only about 10%, because the LLM cannot produce plausible candidates there.
- On a travel-planning benchmark where the best baseline strategy scored 0.7% with GPT-3.5-Turbo, adding automated critics with up to 10 back-prompting cycles gave roughly 6x the baseline, even with weaker models. LLMs could also write the critic functions and enumerate needed critics (with light human supervision).

## Limitations admitted by the authors
- Completeness is bounded by the LLM's candidate generation: in Mystery BW the loop stalled near 10% because no good candidates appeared, though anything returned was still correct.
- Sound critics need models of the domain, and someone must write them; "you can substitute a simulator, but someone has to write that simulator too". Soft critics based on LLMs carry no guarantees.
- Where a combinatorial solver already applies, it can be orders of magnitude more resource-efficient than this loop.
- The travel-planning results are described as preliminary and the framework is a vision rather than a fully tested system.

## Limitations found by others

## What it leaves untried
- No comparison of LLM-Modulo against a solver or against a plain LLM-translates-to-solver pipeline on the same tasks, so the claimed advantage in expressiveness is argued, not measured.
- No cost accounting (calls per solved instance, critic-authoring effort); the 15- and 10-round budgets are the only numbers given.
- No test of the claim that verified plans make better fine-tuning data, which is asserted but not run.

## Topics
[[Topic - self-refinement and critique loops]]
