---
title: Gaming the Judge: Unfaithful Chain of Thought Can Undermine Agent Evaluation
authors: Muhammad Khalifa et al. (U. Michigan, LG AI Research, UIUC)
date: 2026-01
arxiv: 2601.14691
url: https://arxiv.org/abs/2601.14691
venue: arXiv
category: agent-as-judge
---
# Gaming the Judge: Unfaithful Chain of Thought Can Undermine Agent Evaluation

## One line
Shows that rewriting only a web agent's chain-of-thought (actions and screenshots unchanged) makes trajectory-reading VLM judges call failures successes, raising false positive rates by up to 90%.

## Method
- Attacker LLM rewrites CoT segments with five strategies (full text says Claude-Sonnet-4-Thinking; abstract-level summaries say Claude-3.5-Sonnet); content-based (e.g. Progress Fabrication, Environment Blaming) vs style-based (e.g. Competence Boosting).
- Judges see task, action history with CoTs, and screenshots; nine VLM judges (GPT-4o, GPT-5-mini, o4-mini, Claude-Sonnet-4, Qwen-2.5-72B, GLM-4.1V-9B-Thinking, Qwen-3-VL-8B, Pixtral-12B, Gemini-2.5-Flash). Judges are non-agentic (read fixed trajectories).

## Evaluated on
- 800 trajectories, 659 web tasks (300 from AgentRewardBench; 500 new, silver-labelled by GPT-5-high).
- Progress Fabrication: +20-30 FPR points on GPT-4o and GLM-4.1V (70-100% relative); Qwen-2.5-72B and GLM-4.1V >50% absolute FPR. Style-only: +5-10 points. Claude-Sonnet-4 +7.8 under Environment Blaming; o4-mini +7.5 (+117%).
- Mitigations: manipulation-aware prompt (o4-mini, Claude 7.5% -> 3% delta FPR; GPT-4o 27% -> 18%; Pixtral 36% -> 32%); WebJudge rubric inconsistent; majority voting and extended thinking reduce but do not remove (Claude 36% -> 22%). Lower FPR costs recall; removing CoTs drops recall up to 13 pts.

## Limitations admitted by the authors
- Only web environments; only prompt-based mitigations; five strategies not exhaustive; single rewrite model.

## Limitations found by others


## What it leaves untried
- Judges that verify narrated claims against environment state with tools (suggested, untested) - an Agent-as-a-Judge that ignores CoT and checks the world.
- Trained (not prompted) robustness to manipulated reasoning.
