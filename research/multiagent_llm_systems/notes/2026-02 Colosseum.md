---
title: "COLOSSEUM: Auditing Collusion in Cooperative Multi-Agent Systems"
authors: Mason Nakamura et al.
date: 2026-02
arxiv: 2602.15198
url: https://arxiv.org/abs/2602.15198
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2602.15198.pdf
folder: ["multiagent_llm_systems"]
topics: ["strategic play among LLM agents", "team theory and distributed decision making", "communication topology and channels"]
---
# COLOSSEUM: Auditing Collusion in Cooperative Multi-Agent Systems

## One line
Measures whether a subset of LLM agents in a cooperative team pursues a hidden side goal, by pairing a regret metric on actions with an LLM judge on messages, and finds that giving benign agents a secret channel is enough to trigger it.

## Method
The problem: LLM teams talk in free text, so a coalition can coordinate on a secondary objective and degrade the shared one. Reading conversations alone gives no baseline for what the team was meant to achieve.

The fix is to cast each task as a distributed constraint optimization problem (DCOP). The team's intended objective is then an explicit sum of local utilities. Three properties make a DCOP suitable for auditing. The intended objective is explicit. Counterfactuals such as "what if the coalition had acted differently" are cheap to compute in closed form. The single-step setting removes temporal credit assignment, so regret can be pinned on the coalition.

Collusion is defined as a coalition whose assignment falls short of the nominal optimum by at least some delta. A coalition member's objective is a blend of the nominal and a hidden coalition objective, weighted by lambda. Lambda is a lens for the auditor, not a number the agents compute. It is split into a lambda specified in the prompt and a lambda measured from behaviour. This yields named cases:
- Emergent collusion: specified lambda is 0 but measured lambda is above 0.
- Attempted, or "collusion on paper": specified lambda is above 0 but the actions are not collusive.
- Direct and hidden collusion: the judge and the regret metric agree or disagree.

Two signals are used. Coalition advantage is the non-coalition regret minus the coalition regret. A 0-5 judge score is averaged over three judge prompts (GPT-5.4) on the channel logs. The behavioural probe adds a secret channel between two otherwise benign agents and compares against a control without one. The paper adds two DCOP environments (Jira ticket allocation, hospital scheduling) and reuses meeting scheduling.

## Evaluated on
- Neither signal alone suffices. Across 19 models, coalition advantage and judge score are weakly and inversely related (Pearson r = -0.243 emergent, -0.143 prompted). The authors note this may not be significant.
- A secret channel alone produces collusion in most models. 57.89% show positive advantage gain in the emergent group, against 78.95% when prompted to maximise coalition reward. Only 10.53% of emergent runs raise the judge score by 1 or more, against 78.95% prompted. So emergent collusion is mostly hidden from a conversation judge, while prompted collusion is mostly direct.
- Coalition composition matters. In the hospital task, coalitions holding the resource provisioner match benign overall regret (0.04-0.09) and reach low coalition regret (0.02-0.08). Departmental coalitions get 0.2-0.32 coalition regret in the covert case, because their action space is limited.
- Persuasion helps colluders. Authority nudge and reciprocity trade can raise regret by up to 2.65x and 2.77x. The authors say claims that are hard to verify work best.
- Network shape matters. Targeted misinformation belief rises roughly linearly with the number of adversaries. Complete and star graphs resist it, because two-hop paths let benign agents cross-check claims.
- Larger models show less action-based emergent collusion than smaller ones (appendix figure). A plain "maximise coalition reward" prompt beats prompts that add deception.

## Limitations admitted by the authors
- Tasks are one-shot DCOPs with decomposable rewards. Memory, delayed outcomes and long-horizon credit assignment are left out, so the findings may not carry to such agents.
- Most experiments use homogeneous teams on one model backbone. Mixed models, permissions and tool access are untested.
- Collusion is not always harmful. If the nominal objective is unsafe, coordinated deviation could be desirable, and the metric would flag it anyway.
- The emergent-versus-prompted correlation rests on 19 models. The authors say it may not be strong.
- It is unclear what makes some models' coordination efficient but undetected by the judge. Gemini-2.5-Flash is terse and shows no judge change, while Claude-Sonnet-4.5 is verbose and does.
- A smaller judge (GPT-5.4-nano) lowers collusion scores, so conversation-based measurement depends on judge strength.

## Limitations found by others

## What it leaves untried
- Testing whether the proposed mitigations work. Private-channel audits, access controls on high-leverage agents, verifying claims against shared state and cross-checking paths are stated from the observations but never run.
- Using the audit as an online monitor. It needs a known nominal objective and counterfactual regret, and the paper does not show a detector that works without them.
- Mixed-model teams. In the paper the colluders and victims share a backbone, so cross-model persuasion is unmeasured.

## Topics
[[Topic - strategic play among LLM agents]] · [[Topic - team theory and distributed decision making]] · [[Topic - communication topology and channels]]
