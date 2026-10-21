---
title: Echoing: Identity Failures when LLM Agents Talk to Each Other
authors: Sarath Shekkizhar et al.
date: 2025-11
arxiv: 2511.09710
url: https://arxiv.org/abs/2511.09710
venue: ICLR 2026 Workshop on Agents in the Wild
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2511.09710.pdf
folder: ["multiagent_llm_systems"]
topics: ["strategic play among LLM agents", "role-based agent teams", "agent system failure analysis"]
---
# Echoing: Identity Failures when LLM Agents Talk to Each Other

## One line
Names and measures "echoing", where an LLM agent in a two-agent negotiation drops its assigned role and starts speaking as its counterpart, and shows prompts, reasoning and a structured-output protocol only reduce it.

## Method
The problem: agent-agent (AxA) conversations have no human to ground or correct them, so behaviour can drift in ways single-agent tests never show. The authors model AxA as a partially observable game between two agents. Each has its own identity, objective, private tools and private utility. Only natural-language messages cross between them. The failure they define is echoing: an agent's later messages use the language, perspective or decisions of the partner's identity, such as a customer saying "We look forward to welcoming you".

Echoing is detected by a GPT-4o judge that reads the whole conversation and returns a binary flag, the guilty agent and the first offending message. Counting is restricted to conversations that completed a transaction, so the study isolates behaviour from task success. This is the paper's point that completion hides the failure: the transaction closes but on worse terms for one side.

Three mitigations are tried. Stronger identity prompts (minimal, behavioural, and an "identity boundary" prompt that forbids adopting the partner's goals). More reasoning effort. A protocol-level structured response in which every message must declare the sender's role in a separate field.

## Evaluated on
- Echoing is common and model-dependent: 5% to 70% across 22 customer-side models in three transactional domains (hotel, car sales, supply chain). Gemini-2.5-Flash stays at 64-73%. GPT-5 is 2-10% in the domain that varies most. Llama-3.1 8B and 70B score 11.5% and 9.1%, below many larger proprietary models, so scale does not explain it.
- Reasoning does not fix it: 32.7%, 32.8% and 32.9% at low, medium and high effort, against 37.7% without reasoning. Effort level makes almost no difference. Reasoning traces show the models rarely check their own role.
- Prompting is not enough: even the explicit anti-echoing prompt leaves susceptible models high, for example Gemini-2.5-Flash.
- Success metrics miss it: 93% of conversations completed despite drift, and echoing conversations run slightly longer (9.6 vs 8.7 turns).
- Onset is late: average first echo at turn 7.6 (median 8.0), and the likelihood rises with turn index. The authors read this as attention or context decay, but they do not test it.
- Structured role declaration cuts echoing to under 10% for GPT and Sonnet models (9% in the abstract). It does not reach zero.
- Domain matters: GPT-4o goes 58% in car sales, 25% in hotels, 17% in supply chain. A doctor-patient advisory domain is much lower (GPT-5 2%, Gemini-2.5 15-18%, Llama-3.1-8B 30%). The authors guess this is because of a clear authority gradient, without testing it.

## Limitations admitted by the authors
- Only customer-seller and one doctor-patient setting. Multi-party, collaborative planning and long-horizon tasks may show other failures.
- Customer models vary much more (22) than seller configurations (3, chosen as low-echoing models). Customer agents echo more, so the asymmetry is observed but not explained, and symmetric pairings are untested.
- The metric is an LLM judge. Agreement with humans is 91.1% on 150 conversations (precision 86.7%, recall 95.1%). Other judges disagree on rates: GPT-4o flags 28.0%, GPT-4.1 flags 46.2%. Rates may therefore be underestimated, and no non-LLM detector was tried.
- Complete mitigation was not the goal. An "identity refresh" injected every few turns made conversations disordered and leaked the reminder text into the output, so it was dropped.
- Gemini-2.5 models were not tested with structured output because they could not combine tools with it. No activation analysis on open-weight models, so the cause is unknown.

## Limitations found by others

## What it leaves untried
- Training-side fixes: the paper blames alignment on human-facing data (stronger echoing in the consumer role, an unsupported explanation) but trains nothing on AxA data to test it.
- Turn-level interventions such as periodic summaries, left for future work after the refresh attempt failed. Because onset is around turn 7-8, they matter.
- Measuring outcome damage: the paper says echoing worsens deal terms, but reports no utility loss or counterpart exploitation figure.

## Topics
[[Topic - strategic play among LLM agents]] · [[Topic - role-based agent teams]] · [[Topic - agent system failure analysis]]
