---
title: "SimulatorArena: Are User Simulators Reliable Proxies for Multi-Turn Evaluation of AI Assistants?"
authors: Yao Dou et al.
date: 2025-10
arxiv: 2510.05444
url: https://arxiv.org/abs/2510.05444
venue: arXiv
category: agent-evaluation-benchmarks
pdf: agent as a judge papers/SimulatorArena - Are User Simulators Reliable Proxies (2025).pdf
folder: ["agent as a judge"]
topics: ["user simulation", "agent evaluation benchmarks"]
---
# SimulatorArena: Are User Simulators Reliable Proxies for Multi-Turn Evaluation of AI Assistants?

## One line
A benchmark of 909 real human-LLM conversations that scores LLM user simulators on how human their messages look and whether their assistant ratings match real users', and shows that a user profile lifts that match from about 0.6 to 0.7-0.77 Spearman.

## Method
**Problem.** Multi-turn evaluation increasingly replaces the human user with an LLM, but nobody had checked whether that simulator is a valid stand-in. Prompted as a user, an LLM still acts like an assistant: 89.5 words per message from zero-shot CoT against 15.5 from real users in math tutoring.

**Idea 1: score the simulator against real users.** The simulator holds information the assistant lacks (its understanding, its preferences), which is what makes the conversation necessary. It is scored two ways:
- **Realism.** An LLM judge picks the real conversation out of a real/simulated pair; 50% means indistinguishable.
- **Proxy validity.** Assistant ratings from simulated conversations are correlated with the ratings humans gave, mainly over 27 cells of model by difficulty or document type, plus outcome agreement.

**Idea 2: condition the simulator on a user profile.** The profile has two parts, both pulled from the real conversation by GPT-4o:
- **Inherent knowledge.** For math, a level from "knows well" to "not introduced" for each concept the solution needs. For documents, a value for each preference attribute (tone, sign-off and so on).
- **Message style.** Writing and interaction attributes. Found contrastively, by asking GPT-4o what tells real users apart from simulated ones: 29 attributes for tutoring, 28 for documents.

An optional note sets a message-length range. The bet is that attribute-level behaviour generalises better than copying messages.

## Evaluated on
- **Profiles make the simulator a better proxy.** Intermediate Spearman goes from 0.607 to 0.774 in math with interaction style only, and from 0.545 to 0.704 in documents with the full profile. All four comparisons are significant (three at p<0.01).
- **What matters depends on the task.** Writing style alone barely helps (0.623 math, 0.583 docs).
- **Looking human is not the same as being a good proxy.** Length control plus writing style gets the Turing-test gap down to 5.1% in math, almost indistinguishable, yet its correlation is only 0.625. The authors state outright that higher similarity does not always mean better alignment.
- **Cheap.** About $0.09 per simulated conversation against $5.33 for a human in math, under 3% of the cost.
- **Ranking whole systems remains unreliable for documents.** The headline numbers are intermediate-level. Ranked over the 9 assistants, the best document configurations reach only 0.367 Spearman (full profile) and 0.167 (interaction style). Human document ratings were nearly tied except for Phi-3, so there was little to rank.

## Limitations admitted by the authors
- **Richer profiles are followed less faithfully.** Adding more profile information lowers how often each interaction attribute is fulfilled: current LLMs cannot meet many behavioural constraints at once.
- **Some human traits do not come through.** Avoiding LaTeX, grammar errors and sentence fragments are most often missed; the simulator stays too clean.
- **Real users vary a lot.** 78.5% of user pairs on the same document topic and model gave different interaction ratings. In math, 35.3% of pairs split on whether they reached the right answer. Any single-conversation agreement is therefore capped.
- **The scope is narrow.** One session per user, prompted simulators only (no distillation), and scoring per conversation rather than per turn.

## Limitations found by others

## What it leaves untried
- **Profiles drawn from somewhere other than the scored conversation.** Each profile is extracted from the same human conversation the simulator is then compared to, so part of the gain may come from the profile carrying that conversation's path. The test is to build profiles from pre-chat answers only, or from another conversation by the same user.
- **Agentic and adversarial users.** Both tasks are cooperative chat. Tool use, impatient users and walk-aways, where τ-bench-style simulators are deployed, are untested.
- **Separating simulator from rater.** GPT-4o is both the math simulator and the rater, and self-bias was checked only for rating assistants. Whether a rater favours conversations its own model simulated is unmeasured.

## Topics
[[Topic - user simulation]] · [[Topic - agent evaluation benchmarks]]
