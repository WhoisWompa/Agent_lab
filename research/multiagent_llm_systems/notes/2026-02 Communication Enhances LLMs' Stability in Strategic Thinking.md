---
title: Communication Enhances LLMs' Stability in Strategic Thinking
authors: Nunzio Lore et al.
date: 2026-02
arxiv: 2602.06081
url: https://arxiv.org/abs/2602.06081
venue: arXiv
category: topology-communication
pdf: research/multiagent_llm_systems/pdfs/2602.06081.pdf
folder: ["multiagent_llm_systems"]
topics: ["strategic play among LLM agents", "communication topology and channels"]
---
# Communication Enhances LLMs' Stability in Strategic Thinking

## One line
Letting small LLM agents exchange one free sentence of costless, non-binding "cheap talk" before each move in a repeated Prisoner's Dilemma makes their cooperation trajectories smoother and more predictable, though not necessarily more cooperative.

## Method
The problem: small LLMs swing widely with context framing and sampling, so the same game produces erratic cooperation paths. The authors treat stability as a prerequisite for steering agents toward good outcomes. Without it, any intervention cannot be told apart from random drift. A system that settles on a consistent trajectory, even a poor one, can be corrected. One that oscillates cannot.

The intervention is pre-play messaging. Before each of ten rounds, two agents each send a one-sentence message and are told it is non-binding and should be read with caution. The control sees only play history. Stability is the RMSE between the round-by-round average cooperation rate and a LOWESS smooth of it. Low RMSE means the population follows a smooth path. High RMSE means erratic jumps around the trend. The paper reports "stability" in this sense only. Payoff is deliberately not the target.

The game is described by its payoff matrix only, never named, so the model cannot lean on memorised Prisoner's Dilemma lore. Six framings are used (neutral, team, social, business, environment, international relations). Four 7B-9B open models are tested: Qwen 2.5 7B, Falcon 3 7B, Granite 3.3 8B and Gemma 2 9B. A later extension puts 50 agents on random, power-law and core-periphery networks, and tests a one-word message limit.

## Evaluated on
- **Messaging lowers instability in most cases.** 17 of 24 model-context pairs show a significant RMSE drop and 20 of 24 differences are positive (p < 0.001 for both). Every significant effect is a reduction.
- **Volatile models gain most.** Qwen's business framing falls from 0.4082 to 0.0045 and Granite's environment framing from 0.3701 to 0.0457. Already-stable Falcon and Gemma gain a few hundredths at most, because there is little noise to remove.
- **Stability does not follow size.** The 7B models split into very volatile (Qwen) and very stable (Falcon), and the 9B Gemma is stable. The authors conclude training and architecture matter more than parameter count.
- **The effect survives prompt rewording.** With a lightly edited prompt 22 of 24 differences are positive. With a heavily reworded prompt 19 of 24 are positive. Fewer pairs reach significance in both, and the authors attribute this to lower baseline instability.
- **At temperature 0, noise is not the whole story.** Qwen and Granite drop to RMSE 0 with messaging in 5 of 6 contexts. But Falcon and Gemma, fully stable without messaging, become unstable in the "social" framing only (Falcon RMSE 0.4283), and the paper attributes this to a clash between the pro-social cue and the defection-dominant payoffs. This explanation is offered, not tested.
- **Narrow channels can hurt in networks.** Full messaging helps or is neutral. In 50-agent networks, one-word messages push Qwen and Gemma below the no-message baseline on random graphs (RMSE differences -0.0236 and -0.0106, both significant). The authors suggest silence can beat a low-bandwidth signal, but they only hypothesise the reason.

## Limitations admitted by the authors
- Only 7B-9B models were tested. Larger models may have different stability or use messages for deceptive coordination, and this is untested.
- Only the iterated Prisoner's Dilemma with unstructured cheap talk is used, so results may not carry to settings with strictly dominant deception or enforceable commitments.
- Results depend on the specific prompts and decoding settings, so the authors call them directional evidence, not benchmarks. Falcon's significant contexts shrink to one under the robust prompt, and Gemma's instability rises there.
- The one-word channel is not significantly better than silence in the dyadic case (16 of 24 positive, p = 0.076), so its benefit is not established.
- Network runs are small (10 networks per model), and Qwen shows no significant effect there under full messaging, so the network result is thin.

## Limitations found by others

## What it leaves untried
- It never measures payoff or cooperation level, so it cannot say whether the stabilised path is better. A stable defection trap would count as a success.
- It does not test costly signalling or structured negotiation, where commitments could change the dynamics. The paper names these only as future work.
- The mechanism is not probed. No interpretability work or message-content analysis shows why messages damp noise. The "semantic conflict" account of the social-framing failures is conjecture.

## Topics
[[Topic - strategic play among LLM agents]] · [[Topic - communication topology and channels]]
