---
title: A Survey of AI Agent Protocols
authors: Yingxuan Yang et al.
date: 2025-04
arxiv: 2504.16736
url: https://arxiv.org/abs/2504.16736
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2504.16736.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels"]
---
# A Survey of AI Agent Protocols

## One line
Sorts the agent communication protocols of early 2025 (MCP, A2A, ANP, Agora and others) into a two-axis taxonomy, lists seven dimensions for judging them, and sketches where protocols should go next.

## Method
The problem: agents from different vendors have no shared way to reach tools, data or each other. Tool calling is proprietary per model provider, and multi-agent frameworks hard-wire the interaction into the system. That blocks interoperability and limits how far agent networks can scale. The authors argue protocols beat APIs, GUIs and XML browser-use on all four properties of Table 1: efficiency, operating range, standardization and AI-nativeness. This is a qualitative ticks table with no measurements behind it.

The taxonomy has two axes.
- Object orientation: context-oriented protocols connect an agent to data, tools and services. Inter-agent protocols connect agents to each other.
- Scope: general-purpose or domain-specific.

Placements:
- MCP is the only general context protocol. It has a host, client, server and resource, and it keeps tool execution out of the model's output. The local client builds and runs the request, so credentials need not go to a cloud LLM.
- agents.json is the domain-specific context protocol. It describes website APIs and their multi-step flows.
- A2A is task-centred. It uses Agent Cards, asynchronous tasks and opaque execution, where agents share state and artifacts, not plans.
- ANP is decentralized. It uses W3C DID identity, a meta-protocol layer and an application layer.
- Agora is a meta-protocol that addresses a stated "communication trilemma" of versatility, efficiency and portability. Frequent exchanges use structured protocols, rare ones use natural language, and plain-text Protocol Documents let agents negotiate new protocols.
- The remaining general ones (AITP, AConP, AComP, Coral) and the domain-specific human-agent, robot-agent and system-agent protocols are described in one paragraph each.

The paper proposes seven evaluation dimensions: efficiency, scalability, security, reliability, extensibility, operability and interoperability. They are borrowed from internet-protocol practice. Each gets named metrics, such as TPS-N for throughput, a Capability Negotiation Score, Message-Loss Rate and Upgrade Success Rate.

A travel-planning use case shows the structural difference:
- MCP is a star around one client. This is simple, but every call passes through the centre, which becomes a bottleneck and must know every service.
- A2A lets a flight agent ask the weather agent directly.
- ANP does the same across organization boundaries.
- Agora translates the request into per-service protocols.

The outlook has three horizons:
- Short term: protocol benchmarks, privacy-preserving exchange, a group-chat "Agent Mesh" protocol, and protocols that agents can evolve.
- Mid term: protocol knowledge trained into model weights, and layered protocol stacks.
- Long term: scaling laws for agent populations and an Agent Data Network.

## Evaluated on
Nothing is run. No protocol is measured. The evidence is descriptive.
- The metrics are defined but never applied, so no protocol is scored. The paper says it does "not engage in a direct comparison" and is "rather than proposing a specific evaluation benchmark".
- The abstract promises a "comparative performance analysis" of security, scalability and latency. Section 4 delivers metric definitions and two evolution cases, so that promise is only partly kept.
- Protocol change is shown by example. MCP gained HTTP streaming and token authentication between v1.0 and v1.2. The authors say this improved interoperability and security but may add stream latency, and they give no numbers for any of the three.
- The MCP to ANP to A2A sequence is read as a shift from tool access to peer identity to enterprise collaboration.

## Limitations admitted by the authors
- Static comparisons go stale quickly. MCP lacked HTTP and authentication when released in November 2024 and had both by early 2025. This is why the paper stops at dimensions and gives no ranking.
- No unified benchmark for protocols exists yet, so the metrics cannot be checked against each other. They list it as a short-term need.
- Most protocols are immature. Development stages in Table 3, assessed in April 2025, show only ANP and A2A as "Landing", with AITP, AConP, AComP, Coral and Agora still "Drafting" and several domain-specific ones at "Concept". The comparison covers things that may not survive.
- Training protocol knowledge into model weights would fix behavior but makes later protocol updates hard.
- A2A's opaque execution still shares task metadata, so it is only "semi-transparent" and risks exposing resources.

## Limitations found by others

## What it leaves untried
- It does not run the protocols on one workload. Without latency, token and failure numbers per protocol, the claim that A2A cuts overhead against the MCP star (the travel-planner case) is an argument, not a result.
- It does not examine the security of the protocols under attack. Security is judged only by a feature list: authentication modes, ACL granularity and desensitization. Whether those features hold up is not tested.
- The unification of tools and agents is predicted ("may gradually converge") with no evidence or design for it.

## Topics
[[Topic - communication topology and channels]]
