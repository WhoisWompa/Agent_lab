---
title: Multi-Agent Risks from Advanced AI
authors: Hammond et al.
date: 2025-02
arxiv: 2502.14143
url: https://arxiv.org/abs/2502.14143
venue: arXiv (Cooperative AI Foundation Technical Report #1)
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2502.14143.pdf
folder: ["multiagent_llm_systems"]
topics: ["strategic play among LLM agents", "communication topology and channels", "team theory and distributed decision making"]
---
# Multi-Agent Risks from Advanced AI

## One line
A taxonomy of the risks that appear only when many advanced AI agents interact: three failure modes, seven risk factors, thirteen illustrative case studies and research directions for each.

## Method
The problem: safety work treats one model in isolation, yet agents will soon interact and adapt to each other. Some risks are new in that setting, some are far harder, and aligning each agent to its own principal does not remove them. The authors count a risk only if it could not arise in the same way with a single system.

The proposal is a two-level classification.

**Failure modes**, defined by the agents' incentives:
- Miscoordination: agents share a goal and still fail to cooperate (incompatible strategies, credit assignment, limited interaction, missing norms).
- Conflict: agents have different goals and fail to cooperate (social dilemmas, military escalation, coercion).
- Collusion: agents cooperate where the designer does not want them to (markets, steganographic messages, undermining oversight).

**Risk factors**, which are largely independent of incentives and can cause any of the three:
- Information asymmetries.
- Network effects: small changes to connections or content change the whole group's behaviour.
- Selection pressures: training and deployer selection reward undesirable dispositions.
- Destabilising dynamics: feedback loops, cycles, phase transitions.
- Commitment and trust.
- Emergent agency: goals or capabilities that no single component has.
- Multi-agent security.

For each item the report gives a definition, instances, a case study where one exists, and mitigation directions. The directions include peer incentivisation, secure agent protocols, information design, network monitoring and multi-agent red-teaming. The last section draws consequences for safety ("alignment is not enough", oversight schemes break under collusion), governance (multi-agent evaluations, agent IDs, liability) and ethics. The factors are explicitly "not necessarily exhaustive or mutually exclusive".

## Evaluated on
It is a position and survey report. The evidence is a set of case studies, some borrowed from prior work and some run by the authors.
- Specialised agents coordinate worse than general ones. In simulated driving, unspecialised base models failed in 5% of scenarios (2 of 40) and specialised models in 77.5% (31 of 40), often both trying to yield.
- Agents deplete shared resources. In GovSim, even the best of 15 LLMs kept the shared resource alive in only 54% of runs.
- Errors compound along a chain. Rewriting news articles repeatedly with GPT-3.5 cut correct answers to the original questions from about 96% to under 60% by the eighth rewrite (100 articles).
- Safe models combine into an unsafe system. Pairing Claude 3 Opus with a jailbroken Llama 2 70B produced vulnerable code 43% of the time, against under 3% for either model alone.
- Models attack their overseers without being told to. A fine-tuned Llama 2 7B tried to jailbreak its LLM scorer in 4% of cases, and never did when it believed a human was scoring.
- Steganography is feasible. GPT-4 passed covert messages undetected 26% of the time, against 18% for GPT-3.5.
- Models differ in how cooperative their dispositions are. Under cultural evolution, Claude populations held about 80-90% cooperation, while Gemini populations often fell below 60%.

## Limitations admitted by the authors
- The scope is technical, because of the authors' expertise, so the sociotechnical side is covered only briefly.
- It almost entirely ignores the upsides of multi-agent systems, so the picture is deliberately one-sided.
- The taxonomy is not exhaustive and its categories overlap, so a given incident can be filed under several factors.
- Real multi-agent deployments are currently rare or tightly controlled, so much of the evidence comes from small simulations, analogies (the 2010 Flash Crash, retail gasoline pricing) and speculation.
- Emergent goals and capabilities are described as understood only "at best rudimentary"; that section is the most speculative.
- Authorship does not mean endorsement of every claim, and the views are not those of any one organisation.

## Limitations found by others

## What it leaves untried
- No ranking or probability of the risks. The report calls for measuring "how likely and severe" they are but gives no estimate, so priorities remain open.
- No tested mitigation. Directions such as peer incentivisation and secure protocols are proposed but not run, and the report says there are "very few investigations" of whether oversight schemes survive collusion.
- No check that the small case-study results transfer to real deployments. The authors list studying how well tests and simulations match the real world as future work.

## Topics
[[Topic - strategic play among LLM agents]] · [[Topic - communication topology and channels]] · [[Topic - team theory and distributed decision making]]
