---
title: Peacemaker or Troublemaker: How Sycophancy Shapes Multi-Agent Debate
authors: Binwei Yao et al.
date: 2025-09
arxiv: 2509.23055
url: https://arxiv.org/abs/2509.23055
venue: arXiv
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2509.23055.pdf
folder: ["multiagent_llm_systems"]
topics: ["multi-agent debate and consensus", "judge and decision-model audits"]
---
# Peacemaker or Troublemaker: How Sycophancy Shapes Multi-Agent Debate

## One line
Defines and measures inter-agent sycophancy in multi-agent debate, then shows with persona-controlled agents that it drives debates to wrong consensus and that a mix of agreeable and contrarian debaters works best.

## Method
The problem: debate is supposed to work because agents disagree productively, but LLMs trained to please may drop a correct answer to match a peer (debater form) or echo the most polished answer (judge form). Prior sycophancy work looked at user-to-model, not agent-to-agent.

The paper contributes three things.
- **Definition.** Sycophancy in debate is excessive agreement that puts harmony above the agent's communication objective.
- **Metrics.** Each debate state is labelled positive or negative agreement or disagreement (correct answer held by at least one agent or none). Disagreement Collapse Rate (DCR) is the share of cases that start with a correct answer in play but do not end in correct consensus. Negative Agreement Rate (NAR) is the per-agent share of correct positions abandoned. Sycophancy Score (SS, 0 to 100) comes from an LLM grader (GPT-5-mini) rating whether a reply reasons independently or just mirrors peers.
- **Control.** Eight system-prompt personas run from level 1 ("troublemaker", disagrees when warranted) to level 8 ("peacemaker", tells peers what they want to hear). A grid search over every combination of levels across debaters finds the best and worst setups. The judge is varied separately.

Two structures are tested: decentralized Society-of-Minds (peers, no judge) and centralized two-debater-plus-judge debate. The assumption is that the prompt persona changes the sycophancy level, and SS is used to check this.

## Evaluated on
Qwen3-32B and Llama3.3-70B, alone and mixed, on MMLU Pro and CommonsenseQA with two or three agents.
- **Debate often does not beat one model, and collapse is common.** Two-Llama decentralized debate on CommonsenseQA has 86.36% DCR and no accuracy gain (83.70 vs 85.01 single). The authors say gains elsewhere are modest next to the extra compute.
- **A judge reduces collapse in two-agent debate.** Qwen-Qwen on CommonsenseQA goes from 83.62% to 86.65% accuracy, and DCR drops from 81.71% to 41.27%. With three agents the judge gains are smaller and collapse is higher.
- **Sycophancy is linked to collapse.** Debater NAR against SS has Pearson r = 0.902 (CommonsenseQA). Judge DCR against SS has r = 0.639, so about 0.4 of the variance is explained, which is weaker.
- **Persona choice matters more across models.** Same-model Qwen debates vary only from 81.98% to 83.87%. Qwen-Llama debates vary from 78.95% to 82.06% across 81 persona pairs. The best pairs mix peacemaker and troublemaker; the worst are mostly both highly sycophantic.
- **Judge persona barely matters.** Accuracy stays around 86 to 87% on CommonsenseQA across levels 1 to 8.
- **Sycophancy rises with rounds.** SS is lowest in round 1 and climbs in later rounds. The authors conclude that more rounds can hurt, and recommend capping at 2 to 3.

## Limitations admitted by the authors
- Only two model families and two debate frameworks were tested, so the results may not carry to other LLMs, scales or system designs.
- The metrics may miss other forms of sycophancy in other domains, interaction styles or cultures.
- The proposed design rules were checked only in controlled benchmark settings. Long-term effects and side effects in deployment are untested.
- New training methods may produce sycophancy the current taxonomy does not cover.

## Limitations found by others

## What it leaves untried
- The 2 to 3 round cap and the "terminate when positions converge without better reasoning" rule are recommended but never run. Round effects are only observed, not compared against a stopping rule.
- SS depends on one LLM grader, and the paper gives no human agreement for it. Whether the prompt personas actually produce graded sycophancy levels is only indirectly supported, through the NAR to SS correlation.
- The judge sees only the debaters' answers and reasoning. Its insensitivity is not tested with judges that must work from stylistic or confidence cues, or in settings with more than three agents (cost limited the study to two or three).

## Topics
[[Topic - multi-agent debate and consensus]] · [[Topic - judge and decision-model audits]]
