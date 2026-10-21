---
title: "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"
authors: Qingyun Wu et al.
date: 2023-08
arxiv: 2308.08155
url: https://arxiv.org/abs/2308.08155
venue: arXiv
category: framework-production
pdf: research/multiagent_llm_systems/pdfs/2308.08155.pdf
folder: ["multiagent_llm_systems"]
topics: ["role-based agent teams", "orchestration and delegation"]
---
# AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

## One line
An open-source framework that expresses LLM applications as conversations between configurable agents backed by LLMs, tools, or humans, with control flow programmed in both natural language and Python.

## Method
The problem: multi-agent LLM applications need different agent sets and conversation patterns (single or multi-turn, static or dynamic, with or without humans), and each is usually built from scratch. The paper claims one generic abstraction can cover them.

Two ideas carry it.
- **Conversable agents.** Every agent can send, receive and generate a reply, and can be backed by an LLM, a human, a tool (code or function execution), or a mix. Two built-ins cover common cases: an AssistantAgent (LLM, writes code) and a UserProxyAgent (runs code, or asks a human). Developers extend these rather than write agents anew, so roles are reusable.
- **Conversation programming.** Computation is what an agent does when it gets a message; control flow is who messages whom next. By default an agent that receives a message automatically calls its reply function and answers the sender until a termination condition holds. No separate control module exists; the flow emerges from the registered reply functions. Control is mixed: natural language (the assistant's system message tells it to fix errors and answer "TERMINATE" when done) and Python (max auto-replies, human-input mode, custom reply functions). Dynamic flows come from function calls that message other agents, or from a built-in GroupChatManager that picks the next speaker with a role-play prompt and broadcasts its reply to all.

Why it should work: chat-tuned LLMs take feedback well, so execution errors, critiques and human input can all be returned as messages. Splitting work into agents also gives modularity: a safety check or grounding role can be added or removed without touching the rest.

## Evaluated on
Six applications. Four have numbers; the others (dynamic group chat, conversational chess) are mostly demonstrations.
- Math (MATH, GPT-4): the default two-agent pair beats vanilla GPT-4 and commercial tools on 120 level-5 problems, 52.5% against 48.33% (ChatGPT + Code Interpreter), 45.0% (ChatGPT + Plugin), 30.0% (GPT-4), 26.67% (multi-agent debate), 23.33% (LangChain ReAct). On the whole test set it scores 69.48% against 55.18% for the one other system run there (which system is not stated in the text).
- Retrieval-augmented QA (Natural Questions, GPT-3.5): letting the assistant reply "UPDATE CONTEXT" to trigger more retrieval gives F1 25.88 and recall 66.65. Replacing that with "I don't know" drops them to 15.12 and 58.56, below DPR (22.79 / 62.59).
- ALFWorld (134 tasks, GPT-3.5): adding a grounding agent that injects commonsense rules when errors repeat lifts average success to 69% from 54% for the two-agent version and ReAct (the text says a 15% gain), and best-of-3 to 77% from 63% and 66%.
- OptiGuide coding with a Commander, Writer and Safeguard: a separate safeguard raises F1 for spotting unsafe code by 8% with GPT-4 (96% against 88%) and 35% with GPT-3.5 (83% against 48%) over one agent doing both, on 100 tasks. Core workflow code shrinks from over 430 lines to 100; user time falls about 3x against ChatGPT + Code Interpreter (Appendix D).
- Chess: without the board agent, illegal moves disrupted games, though a prompt asking for legal moves was the only substitute tried; no numbers are given.
- Role-play speaker selection beat a task-only prompt on 12 hand-made tasks with higher success and fewer LLM calls; the numbers are only in the appendix.

## Limitations admitted by the authors
- The work is "in its early experimental stages". Which tasks gain from multiple agents, and the best number and roles of agents for a task, are left as open questions; no general rule is given.
- More agents and more autonomy bring safety risks: cascading failures, reward hacking, and risky code execution such as package installs. Human oversight is available through the proxy agent but its right level is left to the developer.
- Complex workflows become hard to log and debug, and can degrade into unintelligible chatter between agents.
- Simple role-play alone is insufficient. The authors saw CAMEL fail on most problems mainly because it cannot execute code, so capable tool-using agents matter more than conversation itself (an observation, not a measured comparison).

## Limitations found by others

## What it leaves untried
- No cost accounting. Multi-agent chat uses more LLM calls than a single model, yet token or call counts appear only for the speaker-selection pilot. Whether gains survive equal compute is unknown.
- Baselines are uneven: ReAct ran on text-davinci-003 while AutoGen used GPT-3.5, and some baselines were skipped on the full MATH set. How much comes from the framework versus the backend model is not separated.
- Automatic design of agent topology and conversation patterns is named as future work but not attempted.

## Topics
[[Topic - role-based agent teams]] · [[Topic - orchestration and delegation]]
