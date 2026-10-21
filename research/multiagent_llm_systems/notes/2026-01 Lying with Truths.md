---
title: "Lying with Truths: Open-Channel Multi-Agent Collusion for Belief Manipulation via Generative Montage"
authors: Jinwei Hu et al.
date: 2026-01
arxiv: 2601.01685
url: https://arxiv.org/abs/2601.01685
venue: arXiv
category: role-based-team
pdf: research/multiagent_llm_systems/pdfs/2601.01685.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams", "strategic play among LLM agents", "communication topology and channels"]
---
# Lying with Truths: Open-Channel Multi-Agent Collusion for Belief Manipulation via Generative Montage

## One line
A Writer-Editor-Director team of attacker agents picks and orders only true evidence fragments so that victim LLM agents infer a false conclusion on their own, and downstream judges then ratify it.

## Method
Earlier collusion work assumes a hidden channel or a backdoor that smuggles a payload. This paper attacks a different surface: the victim's drive to make a coherent story out of scattered facts (the "overthinking" or causal-illusion tendency). No fragment is false. The lie lives in the selection and the order.

The attack is formalised as finding an ordered stream of fragments that each satisfy a Local Truth constraint (consistent with ground truth) while the victim's posterior belief in a fabricated hypothesis exceeds its belief in the real one (the Global Lie condition). Belief updating is treated as approximate Bayesian inference, so the attacker is reshaping the perceived likelihood, not the prior.

Generative Montage splits the work into three attacker roles.
- The Writer drafts a narrative from true fragments only, using vague wording and generalisation to bridge toward the target lie.
- The Editor cuts the narrative into posts and searches for the ordering that maximises implied causal links between them (the film "montage" idea).
- The Director stands in for the victim. It scores how strongly an output induces the lie and runs a three-way gate: accept above a threshold if every fragment is true, reject if any is not, otherwise send back a critique. Writer-Director and Editor-Director are two separate debate loops.

Approved posts are spread over many Sybil bot accounts on a public feed, in the designed time order. Victims are ordinary analyst agents; they are benign but reach the false conclusion and publish it with confident reasons. Downstream decision layers (a five-victim majority vote, or an LLM judge that sees raw evidence plus victim reports) then treat these endorsements as independent confirmation. The paper calls the victims "implicit colluders".

## Evaluated on
- Victims adopt the lie across 14 model families, with attack success 74.4% for proprietary and 70.6% for open-weights models on six real rumor events. Victims are usually confident: mean confidence is about 0.75 to 0.9 for most models.
- The most capable reasoners are not safer in the open-weights group. Distilled-reasoning models score higher than base models, and chain-of-thought prompting raises success by 3.1 points (Qwen2.5-7B) and 4.7 points (DS-R1-Distill-Qwen-7B). The proprietary models show the opposite trend, which the authors attribute to deployment goals and safety training (asserted, not tested).
- The lie cascades. Both majority vote and the LLM judge give deception rates well above 50% across families and events; the judge is only modestly better than the vote. The authors read this as: once the victims are misled, a judge who reads their reports inherits the error.
- The team matters. On the Charlie Hebdo event, removing the debate cuts attack success from 77.0% to 63.5%, removing the Editor to 69.7%, and collapsing to one LLM to 26.8%.
- The number of posts has an inverted-U effect. Posts 1 to 5 are too thin, 16 to 20 add contradictions, and 11 to 15 work best (one model, one event).

## Limitations admitted by the authors
- Everything is simulated, text-only and built from one rumor dataset (PHEME). Real platforms have algorithmic curation, varied users and organic counter-narratives, so real-world success is unknown.
- No defence is proposed. The Discussion only lists untested ideas (belief-trajectory monitoring, entropy analysis, cross-model divergence, provenance auditing, adversarial fine-tuning).
- Multimodal and other domains (finance, science misinformation) are not covered.

## Limitations found by others

## What it leaves untried
- No defence is run against the attack. A detector that tracks the victim's belief trajectory fragment by fragment would show whether the abrupt shift they describe is actually detectable.
- The judge that sees raw evidence is a single small model (DeepSeek-R1-Distill-Qwen-14B), so how a stronger or tool-using judge fares is open. That is the question that decides how serious the cascade is.
- The "reasoning amplifies vulnerability" claim rests on two models and a 3 to 5 point chain-of-thought gap, and the proprietary models show the reverse. A controlled comparison of the same model with and without reasoning would settle it.

## Topics
[[Topic - role-based agent teams]] · [[Topic - strategic play among LLM agents]] · [[Topic - communication topology and channels]]
