---
title: Intelligent AI Delegation
authors: Tomasev et al.
date: 2026-02
arxiv: 2602.11865
url: https://arxiv.org/abs/2602.11865
venue: arXiv
category: orchestrator-worker
pdf: research/multiagent_llm_systems/pdfs/2602.11865.pdf
folder: ["multiagent_llm_systems"]
topics: ["orchestration and delegation", "contract theory", "mechanism design"]
---
# Intelligent AI Delegation

## One line
A conceptual framework (no system, no experiments) that treats delegation between humans and AI agents as more than task splitting: it adds authority transfer, accountability, trust and verification, and maps these onto nine protocol components for a future "agentic web".

## Method
The problem: current multi-agent systems decompose and hand off work with hard-coded heuristics. They cannot adapt when a sub-agent degrades or fails, and nothing says who is accountable when a chain A to B to C goes wrong. The authors borrow from human organisations (principal-agent problem, span of control, authority gradient, zone of indifference, transaction-cost economics, contingency theory) and define delegation as a sequence of decisions covering allocation, authority, responsibility, role boundaries, intent and trust.

They describe a task by about eleven axes (complexity, criticality, uncertainty, verifiability, reversibility, contextuality, subjectivity and others) plus granularity, autonomy, monitoring and reciprocity. Delegator and delegatee can each be human or AI.

Five requirements (dynamic assessment, adaptive execution, structural transparency, scalable market coordination, systemic resilience) map onto nine protocol parts:
- **Decomposition**: "contract-first". A sub-task may be delegated only if its result can be checked, so anything too subjective or costly to verify is split again until it matches the delegatee's verification ability (unit tests, formal proofs).
- **Assignment**: decentralised market hubs with bids and certificates, ending in a smart contract. The contract is bidirectional (cancellation compensation, renegotiation) and fixes monitoring and autonomy level.
- **Multi-objective optimisation**: Pareto trade-off of cost, latency, quality, privacy and uncertainty, re-run continuously. Below a "complexity floor", direct execution beats delegation because overhead exceeds task value.
- **Adaptive coordination**: external and internal triggers (outage, budget overrun, failed check, unresponsive agent) start re-delegation. Reversible failures re-delegate automatically; irreversible high-criticality ones go to termination or a human. Cooldowns and damping prevent oscillation.
- **Monitoring**: outcome vs process, direct vs indirect, black vs white box, zero-knowledge proofs for privacy, and signed attestations passed up chains.
- **Trust and reputation**: ledger, web of credentials, behavioural scores. Trust is the delegator's private threshold; reputation is public history.
- **Permissions**: privilege attenuation down the chain, just-in-time access, automated revocation.
- **Verifiable completion**: direct check, third-party audit, cryptographic proof, or a consensus game; escrow bonds and dispute panels. Liability flows up the chain.
- **Security**: a threat taxonomy (malicious delegatee or delegator, Sybil attacks, collusion, cognitive monoculture) and defence in depth.

A separate section covers ethics: meaningful human control, accountability vacuums, de-skilling, and "cognitive friction" balanced against alarm fatigue. A protocol section finds MCP, A2A, AP2 and UCP lack the pieces needed. For example, A2A has no slot for a ZK proof or signature chain, and MCP gives binary access with no attenuation. It sketches extensions: a verification policy field, a monitoring stream with four detail levels, request-for-quote bids and attenuated capability tokens.

## Evaluated on
Nothing is tested. The paper reports no experiments, numbers or prototype.
- Support is argument by analogy to human organisations and a review of prior work (mixture of experts, hierarchical RL, Contract Net, MARL).
- The protocol gap analysis is qualitative: each protocol is checked against the framework's requirements by reading its design, not by running it.

## Limitations admitted by the authors
- The protocol extensions are "illustrative", "neither comprehensive, nor meant as a definitive proposal", and other protocols may fit better. The framework is therefore a direction, not a specification.
- Verification cost: ZK proofs and consensus games add latency and compute (a "reliability premium"). This could make safety a luxury good, and competing agents may skip checks to win on price.
- Verification is fallible: subjective tasks cause disagreement even with rubrics, and errors may surface after settlement, hence the need for disputes and retroactive reputation updates.
- Ledger reputation can be gamed by accepting only easy tasks. Detecting malicious intent in isolated sub-tasks is hard when an adversary fragments a goal into benign pieces.
- Human oversight does not scale: verifying long reasoning traces overloads people, and too many verification requests cause rubber-stamp approval.
- State-snapshot resumption needs partial-compensation clauses and may not apply to all tasks.

## Limitations found by others

## What it leaves untried
- No implementation or simulation of the market, bidding and re-delegation cycle. Whether oscillation damping and the complexity floor work as claimed is untested.
- No comparison with existing heuristic orchestrators. The claim that they fail on adaptation and accountability rests on the literature review, not on measured failures.
- No account of how an LLM delegator would estimate a delegatee's success rate, cost and duration, which the decomposition step depends on, given that the paper itself notes models are overconfident.

## Topics
[[Topic - orchestration and delegation]] · [[Topic - contract theory]] · [[Topic - mechanism design]]
