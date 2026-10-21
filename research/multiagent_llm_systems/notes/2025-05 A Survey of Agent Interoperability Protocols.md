---
title: A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)
authors: Abul Ehtesham et al.
date: 2025-05
arxiv: 2505.02279
url: https://arxiv.org/abs/2505.02279
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2505.02279.pdf
folder: ["multiagent_llm_systems"]
topics: ["communication topology and channels"]
---
# A Survey of Agent Interoperability Protocols: MCP, ACP, A2A, ANP

## One line
A descriptive survey of four agent communication protocols (MCP, ACP, A2A, ANP) that compares their architecture, discovery, messaging and security, and proposes a four-stage adoption order.

## Method
The problem: LLM agents built on different frameworks connect through ad hoc integrations that are hard to scale, secure or reuse. The paper's answer is not a new protocol. It reads four existing ones as layers of one stack, each solving a different interoperability gap.

- **MCP** (Anthropic, Nov 2024) connects a model to tools and data. It is a JSON-RPC 2.0 client-server design exposing four primitives: Tools (model-controlled), Resources (application-controlled), Prompts (user-controlled) and Sampling (server-controlled). Transport is stdio or HTTP with SSE.
- **ACP** (IBM, Mar 2025) is a REST interface between independent agents. Messages are ordered lists of MIME-typed parts. It supports sync, async and streaming execution, and session state. A registry or well-known manifest handles discovery, including offline.
- **A2A** (Google, Apr 2025) delegates tasks between opaque agents. A client agent reads a remote agent's Agent Card (skills, auth needs), sends a Task, and gets Artifacts back. Updates arrive over SSE or push notification.
- **ANP** targets the open internet. Identity is a W3C DID (did:wba), agents describe themselves in JSON-LD, and a meta-protocol negotiator lets agents agree on an interaction protocol in natural language.

For each protocol the paper walks a lifecycle (creation, operation, update, termination) and tabulates threats with mitigations. Examples are tool poisoning and rug-pull redefinition for MCP, Agent Card spoofing for A2A, session hijacking for ACP, and DID spoofing for ANP. A comparison table sets them side by side. Its reasoning is that "no single protocol suffices across all contexts", so the paper recommends adopting them in order: MCP for tool access, then ACP for structured messaging, then A2A for enterprise collaboration, then ANP for open agent markets. The stated basis is protocol maturity, integration complexity and use-case fit. The paper gives no measurement behind the ordering.

It also places the four in a history: KQML (1993) and FIPA-ACL (2000) had formal speech-act semantics but heavy XML encodings and little uptake outside academia and defense. SOA and ESBs decoupled services but were brittle. Function calling and ReAct (2023) put tool use inside the model but left discovery, authentication and cross-framework reuse unsolved.

## Evaluated on
There are no experiments, benchmarks or deployments. The claims rest on protocol documentation and prior security write-ups.

- The comparison table is the main result. Per protocol it records the architecture model, discovery method, auth, message format, session support and scope. MCP is client-server with manual or static discovery. ACP is brokered by a registry. A2A is peer-like with Agent Card retrieval. ANP is fully peer-to-peer with search-engine discovery.
- The security tables claim every protocol needs lifecycle-wide controls (signed manifests, scoped short-lived tokens, TLS or mTLS, drift detection). This is a synthesis of sources. Several cited sources are a blog post and a Medium guide, and no attack was reproduced.
- The adoption roadmap is argued from the comparison. No pilot, cost figure or interoperability test supports it.

## Limitations admitted by the authors
- Each protocol has a stated weakness in the comparison. MCP assumes a centralized server and is open to prompt injection. ACP needs a registry and strong control over servers. A2A is enterprise-centric and assumes an agent catalog. ANP has high negotiation overhead and an immature ecosystem. These matter because they fix where each protocol stops being usable.
- The conclusion says that bridges between protocols, trust frameworks for agent collaboration and standardized evaluation benchmarks are still missing. So the paper cannot say how well any of the protocols works in practice.
- The opening notes that universally adopted standards "remain nascent". The ranking of protocols may therefore change quickly.

## Limitations found by others

## What it leaves untried
- No empirical test of the roadmap. Measuring latency, token or context cost, and failure rates of MCP, ACP and A2A on one workload would show whether the staged order beats using one protocol.
- No reproduction of the listed attacks (tool poisoning, Agent Card spoofing) against real implementations. Without it, the mitigations are unvalidated.
- No treatment of how agent quality, as opposed to message format, is affected by the protocol. The paper does not connect protocol choice to task success in multi-agent LLM systems.

## Topics
[[Topic - communication topology and channels]]
