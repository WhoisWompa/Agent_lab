---
title: Moral Hazard in Multi-Agent Language Models
authors: Dane Malenfant et al.
date: 2026-07
arxiv: 2607.23982
url: https://arxiv.org/abs/2607.23982
venue: arXiv (preprint, under review)
category: failure-analysis-survey
pdf: research/multiagent_llm_systems/pdfs/2607.23982.pdf
folder: ["multiagent_llm_systems"]
topics: ["contract theory", "strategic play among LLM agents", "automated pipeline and topology search"]
---
# Moral Hazard in Multi-Agent Language Models

## One line
A text game built on Holmström's moral hazard in teams shows that LLM agents differ in whether they pay to help a teammate, that optimisation can reach full team success while skipping the costly help, and a counterfactual prompt optimiser (CREDIT) that rewards the help itself.

## Method
- **Problem.** Checking a claim or flagging a risk costs the agent and mostly benefits another agent. Team success hides whether anyone acquired the information, passed it on or used it.
- **Dialogue Moral Hazard Game.** Agents sit in a directed ring. Each owns a case with one hidden unsafe option that only its predecessor can reveal, by paying query cost k and giving up a local payoff. The querier may post an anonymous warning, and every agent then picks a final action. The stages (query, warning, downstream use, team success) are scored separately. Team reward is all-or-nothing, so no individual query earns marginal credit.
- **Theory prediction.** Querying pays privately only when the agent's share of team output exceeds a threshold. With the paper's weights (n=2) the threshold is alpha*(k) = 0.35 + k. Varying k and the share tests whether a model follows its stated private payoff.
- **Learned shortcut.** By design the unsafe option is the highest-public-utility one. A prompt optimiser (GEPA, which sees only scalar scores) can learn "avoid the top-utility option" and drop querying. The authors change this rank-label mapping (balanced, reversed) on frozen prompts to expose such shortcuts.
- **CREDIT.** For each training case it builds "matched hidden-state twins": identical visible text, different hidden unsafe options. A fixed observable rule cannot solve all twins, so credit is taken at the worst hidden state. It replays the query and the best no-query continuation and credits a query only by its net value of information after the query cost and forgone local reward. Prompts are optimised in four stages (query discovery, exact communication, information use, joint), with GEPA only proposing candidate instructions.

## Evaluated on
- **Incentive response is model-specific.** GPT-5.6 Sol, Claude Opus 4.8 and Nemotron-3 Ultra track the boundary across nine query costs with mean absolute errors of 0.013, 0.030 and 0.024. Muse Spark 1.1 and Fable 5 never drop below 50% querying. Fable queries in 97.9% of privately dominated decisions and Opus in 46.3%, though payoff comprehension is 100% for both, so the authors read this as safety-prioritising, not arithmetic error.
- **Failures separate by stage.** Gemma-2-2B IT and OLMo-7B query often but transfer only 9.2% and 11.2% of the information. Qwen3-0.6B learns to query under SFT (0.4% to 74.5%) but reaches only 0.7% team success. SFT lifts SmolLM3-3B team success from 0.9% to 64.7%.
- **Success can bypass the mechanism.** GEPA takes Muse from 22.2% to 100% team success while query use falls from 51.1% to 0.3%. Frozen, these prompts drop to 12.5% (balanced) and 0.0% (reversed), while the base policy gets 89.1% and 100% there, so the collapse is not a broken environment. One Opus prompt that kept querying stays at 100%.
- **CREDIT restores query-mediated success.** All three Muse CREDIT prompts reach 100% query use, transfer and team success on all three mappings. CREDIT raises realized transfer over GEPA for all five models (25.7 points for Gemma up to 99.7 for Muse). On OLMo-7B team success goes from 2.9% to 42.2%.
- **Executing the pathway is not the same as helping.** For Opus, query use stays at 100% as the mapping changes, but positive net value falls from 100% to 25% to 0%, because a no-query continuation reaches the same outcome.

## Limitations admitted by the authors
- The game fixes private information, effort cost, communication access and payoff accounting, which buys clean attribution but leaves open how far results carry to settings where these vary. The paper only claims results for observable policies under explicit reward contracts.
- Evidence is thin per model: CREDIT has three optimisation seeds each for five models, and the optimised-prompt comparisons have no matched-objective optimiser contrast. SFT, RLOO and GEPA use different objectives, so contrasts show policy responses, not a ranking of optimisers.
- Open-weight models stay limited by communication and downstream use after CREDIT (OLMo transfer about 72-73% but team success 52-54%), so CREDIT fixes acquisition more than use.
- The Qwen3-4B IT shortcut effect is not established: the original-minus-balanced interaction is +9.6 points with 95% CI [-7.0, 31.0].
- The cue-competition and blocking motivation is an analogy; the authors leave the models' cognitive implementation unspecified.

## Limitations found by others

## What it leaves untried
- Games with more than two agents in the CREDIT experiments and costs that are not fixed. The group-size sweeps go to n=10 only for base incentive response, not for optimisation.
- Showing that CREDIT's gains hold when the shortcut is not planted by the generator. The rank-label link is built in, so how often real tasks hold such shortcuts is unmeasured.
- Using CREDIT credit to design the payoff contract itself (for example, giving a query individual credit), which the Holmström framing suggests but the paper does not test.

## Topics
[[Topic - contract theory]] · [[Topic - strategic play among LLM agents]] · [[Topic - automated pipeline and topology search]]
