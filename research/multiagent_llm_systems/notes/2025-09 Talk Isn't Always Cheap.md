---
title: Talk Isn't Always Cheap: Understanding Failure Modes in Multi-Agent Debate
authors: Wynn et al.
date: 2025-09
arxiv: 2509.05396
url: https://arxiv.org/abs/2509.05396
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2509.05396.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus", "agent system failure analysis"]
---
# Talk Isn't Always Cheap: Understanding Failure Modes in Multi-Agent Debate

## One line
Shows empirically that multi-agent debate among mixed-capability LLMs often lowers accuracy below plain majority voting, because agents flip from correct to incorrect answers under peer pressure.

## Method
The problem: debate is widely assumed to help, since agents can challenge flawed reasoning. Prior work mostly tested groups of one model, and a theoretical result (Estornell and Liu) predicts that diversity of ability should help. This paper tests that in heterogeneous groups.

The setup is the standard debate of Du et al. Three agents answer a question, then for two rounds each agent sees the others' answers and reasoning and revises its own. The final answer is a majority vote. The comparison point is a majority vote over the same agents' first answers, with no exchange. Groups mix a strong model (GPT-4o-mini), a middle one (Llama-3.1-8B) and a weak one (Mistral-7B) in different counts.

The paper then looks for the cause by tracking each agent's answer transitions (correct to correct, correct to incorrect, and so on) across rounds. It checks how the chance of a correct-to-incorrect flip depends on how many peers agreed with the agent at the start. It also tests one fix aimed at sycophancy: a prompt that pays the agent for correctness and tells it to maximize that payoff. No new method is proposed. The contribution is the measurement and the account of where debate breaks.

## Evaluated on
Three tasks (CommonSenseQA, MMLU, GSM8K), 100 questions each, five seeds, three models.
- Debate often does worse than voting without debate, and on CommonSenseQA it hurt in every group tested. The largest drops are 8.0 points on CommonSenseQA and 12.0 on MMLU.
- A majority of strong agents does not protect the group: groups with more GPT-4o-mini than weak agents still lost accuracy in some cells (the paper's table marks models by icon, so the exact group per number is not recoverable from the text). A weak agent in the room can drag the stronger ones down.
- Accuracy often falls further the longer the debate runs, most visibly on MMLU and CommonSenseQA.
- Agents that change their answer more often go from correct to incorrect than the reverse. Most initially wrong agents stay wrong. In round 2, agents show less resistance than in round 1 (larger correct-to-incorrect share), which the authors read as social pressure accumulating.
- An agent is most likely to flip a correct answer when no peer agrees with it, and less likely as more peers agree. This is read as conformity. The size of the effect varies by model and task. On GSM8K, GPT and Mistral flipped far less than Llama.
- The correctness-payoff prompt does not reduce harmful flips, and in many cases they increase. So telling the model to prefer being right over agreeing does not fix sycophancy-like behaviour.
- Debate does help in some cells, mostly GSM8K, with gains up to 4.4 points. The harm is not universal.

## Limitations admitted by the authors
- No single cause is established. Sycophancy, social influence, model capability and task type all matter, and the paper only shows correlations. The flip-versus-agreement link (Figure 4) is called "strong preliminary evidence", not proof of mechanism.
- The effect varies widely by model and task. A fix tuned on one cell may not carry to another. GSM8K gains in several groups where CommonSenseQA and MMLU lose.
- The one intervention tried, the payoff prompt, failed, so the paper offers no working remedy. Its remedies (confidence or credibility weighting, rewarding independent verification, penalizing unsupported conformity in training) are suggestions only and are untested.

## Limitations found by others

## What it leaves untried
- Testing the proposed remedies: confidence-weighted votes, credibility scores, or training that penalizes conformity. Without them the paper says debate is risky but gives no safe version.
- Larger and more varied settings. Only three small models, three agents, two rounds, 100 questions per task and a single debate protocol were used, so how far the results hold for stronger models or other protocols is unsupported.
- Isolating cause by intervention, for example hiding peers' answers or planting wrong answers, rather than inferring conformity from agreement counts.

## Topics
[[Topic - multi-agent debate and consensus]] · [[Topic - agent system failure analysis]]
