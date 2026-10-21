# Debate, voting and cooperative reasoning among LLM agents (2023 to Oct 2026), read as incentive-and-information systems

Scope: multi-agent systems that *produce* an answer through debate, negotiation, voting or joint reasoning. Debate-as-judging, role-based teams, orchestrator-worker, generator-critic loops, topology optimisation, failure surveys and frameworks are out of scope; pointers only, at the end of the catalogue. PDFs are in `research/multiagent_llm_systems/pdfs/<arxiv-id>.pdf` (all downloads below succeeded; the Estornell & Liu paper has no arXiv id and is saved as `neurips2024-estornell-liu-multi-llm-debate.pdf`).

"Published" means a peer-reviewed venue is confirmed on the arXiv listing or the venue's site; otherwise "preprint".

## Catalogue: how each system is structured (agents, visibility, decision rule, verification, enforcement, failures, numbers)

### Takeaway
Almost every system in this family runs identical copies of one model under identical goals ("find the right answer"). Each agent sees all peers' previous-round answers. The run stops after a fixed number of rounds or at unanimity, and the answer is a majority vote or an LLM judge's pick. Nothing an agent says is checked before peers condition on it, so in the reader's terms the whole exchange is cheap talk among players whose interests are fully aligned. The harness enforces only turn order, visibility and the aggregation rule; "be stubborn", "disagree", "persuade" and "report your confidence" are prompt requests with no cost attached. The exceptions are few: verification in Tool-MAD (2026) and claim-verification debates, a ground-truth oracle used only as an upper bound (Choi et al. 2025), and calibrated escalation added after the debate (Conformal Social Choice, 2026).

### Cited Findings

**Core debate systems (homogeneous, aligned goals)**

- **Du, Li, Torralba, Tenenbaum, Mordatch, "Improving Factuality and Reasoning in Language Models through Multiagent Debate" (the "society of minds" paper).** arXiv 2305.14325, PDF https://arxiv.org/pdf/2305.14325. Published at ICML 2024; the arXiv page lists no venue, so the ICML status rests on the brief and the proceedings, not the arXiv listing. Here is how it is set up:
  - (1) Agents and goals: 3 ChatGPT instances by default, all with the same goal, run for 2 rounds.
  - (2) Visibility: each agent sees every other agent's full response; with 5 or more agents, ChatGPT summarises the responses first, which improved results.
  - (3) Stop rule and decision: the stop rule is a fixed number of rounds or convergence on a shared answer. There is no separate selection step.
  - (4) Verification: none; the exchange is pure cheap talk.
  - (5) What prompts do: prompts that make agents more "stubborn" gave longer debates and better answers, and the authors note agents were generally "agreeable".
  - (6) Failures: debates sometimes converged on wrong answers that agents then stated confidently. Gains beyond 4 rounds were about the same as at 4.
  - (7) Numbers: arithmetic 67.0 (single) / 72.1 (reflection) / 69.0 (majority of agents) / 81.8 (debate). GSM8K 77.0 / 75.0 / 81.0 / 85.0. Biographies 66.0 to 73.8 and MMLU 63.9 to 71.1 (single to debate). In mixed ChatGPT+Bard debate on 20 GSM8K problems, Bard solved 11, ChatGPT 14 and the debate 17. — [arXiv abs](https://arxiv.org/abs/2305.14325); [ar5iv full text](https://ar5iv.labs.arxiv.org/html/2305.14325)
- **Liang, He, Jiao, Wang, Wang, Wang, Yang, Shi, Tu, "Encouraging Divergent Thinking in Large Language Models through Multi-Agent Debate" (MAD).** arXiv 2305.19118, PDF https://arxiv.org/pdf/2305.19118, EMNLP 2024 main. Two debaters argue "tit-for-tat" (an assigned affirmative and negative side, so opposing goals by prompt) and a judge manages the debate and gives the final answer. The motivation is "Degeneration-of-Thought": a self-reflecting model that is confident cannot generate new ideas even when it is wrong. The authors report that ending the debate adaptively (the judge may stop it early) and keeping disagreement moderate matter. They also report the judge may not be fair when the agents are different LLMs. Tasks were commonsense machine translation and counter-intuitive arithmetic; the abstract has no numbers. — [arXiv](https://arxiv.org/abs/2305.19118)
- **Chen, Saha, Bansal, "ReConcile: Round-Table Conference Improves Reasoning via Consensus among Diverse LLMs."** arXiv 2309.13007, PDF https://arxiv.org/pdf/2309.13007, ACL 2024.
  - Agents: *different* models (API, open-source and domain-specific), all with the same goal.
  - Visibility: each round's prompt holds the answers and explanations of the previous round grouped together, each agent's *self-reported confidence*, and human explanations that correct answers, which agents use to persuade.
  - Decision: confidence-weighted vote over several rounds.
  - Results: up to +11.4% over single- and multi-agent baselines, better than GPT-4 on 3 datasets, and +8% on MATH with mixed models. The ablation says model diversity is critical.
  - Through the reader's lens: the confidence that sets the vote weight is an unverified self-report, so the scoring rule rewards the agent that claims more confidence. — [arXiv](https://arxiv.org/abs/2309.13007)
- **Yin, Sun, Chang, Guo, Dai, Huang, Qiu, "Exchange-of-Thought" (EoT).** arXiv 2312.01823, PDF https://arxiv.org/pdf/2312.01823, EMNLP 2023. There are four communication topologies (Memory, Report, Relay, Debate) plus a "confidence evaluation mechanism" meant to reduce the risk of passing on wrong reasoning chains. The authors report it beats baselines cost-effectively; the abstract gives no numbers. — [arXiv](https://arxiv.org/abs/2312.01823)
- **Sun, Yin, Li, Wu, Qiu, Kong, "Corex: Pushing the Boundaries of Complex Reasoning through Multi-Model Collaboration."** arXiv 2310.00280, PDF https://arxiv.org/pdf/2310.00280, listed as COLM 2024 / ICLR 2024 LLM-Agents workshop. It has three modes: Debate, Review and Retrieve. Retrieve has a model pick the most faithful candidate chain, so it is a selection step rather than an exchange. It is tested on 4 reasoning task types; the abstract gives no numbers. — [arXiv](https://arxiv.org/abs/2310.00280)
- **Estornell & Liu, "Multi-LLM Debate: Framework, Principals, and Interventions."** NeurIPS 2024; no arXiv id found; PDF https://proceedings.nips.cc/paper_files/paper/2024/file/32e07a110c6c6acf1afbf2bf82b614ad-Paper-Conference.pdf.
  - The paper gives a theoretical model of debate: models with similar capabilities or responses fall into "static dynamics" and converge on the majority opinion, *including a shared misconception*, which it attributes to shared training data.
  - It proposes three harness interventions: diversity-pruning (maximise the entropy of each round's responses), quality-pruning (relevance) and misconception-refutation. They improve 4 benchmarks; I did not retrieve the numbers. — [NeurIPS poster](https://neurips.cc/virtual/2024/poster/93363); [proceedings PDF](https://proceedings.nips.cc/paper_files/paper/2024/file/32e07a110c6c6acf1afbf2bf82b614ad-Paper-Conference.pdf)
- **Qian et al., "Scaling Large Language Model-based Multi-Agent Collaboration" (MacNet).** arXiv 2406.07155, PDF https://arxiv.org/pdf/2406.07155, ICLR 2025. Agents sit on a directed acyclic graph and refine artifacts along the edges, scaling to over a thousand agents. Irregular topologies beat regular ones. Performance follows a logistic "collaborative scaling law", and collaborative emergence comes earlier than neural emergence. It is cooperative refinement rather than debate, so it borders the topology-optimisation scope. — [arXiv](https://arxiv.org/abs/2406.07155)

**Critical re-evaluations (the "does debate work?" line)**

- **Smit, Duckworth, Grinsztajn, Barrett, Pretorius, "Should we be going MAD? A Look at Multi-Agent Debate Strategies for LLMs."** arXiv 2311.17371, PDF https://arxiv.org/pdf/2311.17371.
  - Status: preprint on arXiv (v3, Jul 2024). The arXiv page lists no venue; ICML 2024 publication is reported elsewhere but I did not confirm it.
  - Setup: GPT-3.5-turbo; Society of Minds, Multi-Persona, ChatEval and Ensemble Refinement against Self-Consistency and Medprompt; 7 datasets.
  - Best scores: MedQA Medprompt 0.65, SoM 0.64, SC 0.60, MP 0.58. MMLU SC 0.78, ER 0.76. CIAR SoM = SC = 0.56.
  - Conclusion: MAD "do[es] not reliably outperform" other prompting strategies.
  - Agreement prompt: a prompted "agreement intensity" gave about +15% (Multi-Persona) and about +5% (SoM) on a 376-question USMLE subset. At 90% agreement, MP went from worst to best on MedQA. On CIAR the effect reversed, and more disagreement helped.
  - Rounds: more rounds do not reliably help and always cost more. MP's built-in "devil" agent lowered accuracy below the first agent's initial answer. — [arXiv](https://arxiv.org/abs/2311.17371); [HTML v3](https://arxiv.org/html/2311.17371v3)
- **Zhang, Cui, Chen, Wang, Zhang, Wang, Wu, Hu, "If Multi-Agent Debate is the Answer, What is the Question?"** v1 title, now retitled "Stop Overvaluing Multi-Agent Debate -- We Must Rethink Evaluation and Embrace Model Heterogeneity". arXiv 2502.08788, PDF https://arxiv.org/pdf/2502.08788. It is a position-paper preprint. It evaluates 5 MAD methods × 9 benchmarks × 4 models: MAD "often fail[s] to outperform" CoT and Self-Consistency "even when consuming significantly more inference-time computation", while model heterogeneity consistently helps ("universal antidote"). — [arXiv](https://arxiv.org/abs/2502.08788)
- **Choi, Zhu, Li, "Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?"** arXiv 2508.17536, PDF https://arxiv.org/pdf/2508.17536, NeurIPS 2025.
  - Setup: 5 homogeneous agents (Qwen2.5-7B, Llama3.1-8B; Qwen2.5-32B on two tasks), simultaneous updates, each agent seeing peers' previous-round answers (decentralised, sparse or centralised). A fixed T of 2, 3 or 5 rounds, with the final answer by majority vote.
  - Qwen-7B averages: single agent 0.7205; majority vote with no debate 0.7691; decentralised MAD 0.7377 (T=2), 0.7112 (T=3), 0.7050 (T=5); centralised 0.6551 to 0.6672. Llama-8B: vote 0.7242 vs. MAD 0.6929 (T=2). Qwen-32B GSM8K: 0.9433 vote vs. 0.9400 MAD.
  - Theory: under homogeneous, fully connected agents, belief in the correct answer is a *martingale*, so debate does not raise expected correctness and voting does the work.
  - Interventions: an oracle that locks in correct answers reaches 0.8289 at T=5 (an upper bound that uses ground truth). The practical biased-update variants MAD-Conformist and MAD-Follower reach 0.7524 and 0.7577 vs. 0.7084 for vanilla MAD. — [arXiv](https://arxiv.org/abs/2508.17536); [HTML v2](https://arxiv.org/html/2508.17536v2); [NeurIPS](https://neurips.cc/virtual/2025/poster/116557)
- **Kaesberg, Becker, Wahle, Ruas, Gipp, "Voting or Consensus? Decision-Making in Multi-Agent Debate."** arXiv 2502.19130, PDF https://arxiv.org/pdf/2502.19130, ACL 2025 Findings. It compares 7 decision protocols, changing only the protocol. Voting is +13.2% on reasoning tasks and consensus is +2.8% on knowledge tasks. More agents help; *more discussion rounds before voting reduce performance*. Two diversity methods, All-Agents Drafting and Collective Improvement, give up to +3.3% and up to +7.4%. — [arXiv](https://arxiv.org/abs/2502.19130)
- **Wang, Wang, Su, Tong, Song, "Rethinking the Bounds of LLM Reasoning: Are Multi-Agent Discussions the Key?"** arXiv 2402.18272, PDF https://arxiv.org/pdf/2402.18272. Preprint per arXiv; ACL 2024 publication is reported elsewhere but unconfirmed here. A single LLM with strong prompts "nearly matches" the best discussion method, and discussion beats a single agent "only when there is no demonstration in the prompt". — [arXiv](https://arxiv.org/abs/2402.18272)
- **Wynn, Satija, Hadfield, "Talk Isn't Always Cheap: Understanding Failure Modes in Multi-Agent Debate."** arXiv 2509.05396, PDF https://arxiv.org/pdf/2509.05396, ICML 2025 MAS workshop. With agents of mixed capability, accuracy can *decline* over a debate even when stronger models outnumber weaker ones. Agents switch from correct to incorrect answers after seeing peers' reasoning, agreeing rather than challenging. The authors blame sycophancy and social conformity and conclude that agents "neither incentivized nor equipped" to resist persuasive wrong reasoning degrade the result. — [arXiv](https://arxiv.org/abs/2509.05396)
- **Yao et al., "Peacemaker or Troublemaker: How Sycophancy Shapes Multi-Agent Debate."** arXiv 2509.23055, PDF https://arxiv.org/pdf/2509.23055, preprint. It formally defines inter-agent sycophancy and finds it drives "disagreement collapse" before a conclusion. Accuracy falls below single-agent baselines, with failures coming from both debaters and judges, in decentralised and centralised designs. — [arXiv](https://arxiv.org/abs/2509.23055)
- **Wu, Li, Li, "Can LLM Agents Really Debate? A Controlled Study of Multi-Agent Debate in Logical Reasoning."** arXiv 2511.07784, PDF https://arxiv.org/pdf/2511.07784, preprint. On Knight–Knave–Spy puzzles (verifiable), reasoning strength and diversity drive success, while debate order and *confidence visibility* give limited gains. Majority pressure suppresses independent correction; effective teams overturn wrong consensus. — [arXiv](https://arxiv.org/abs/2511.07784)

**2026 successors**

- **Bertalanič & Fortuna, "The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous Multi-Agent Debate."** arXiv 2605.00914, PDF https://arxiv.org/pdf/2605.00914, listed for the ACM Conference on AI and Agentic Systems (DOI 10.1145/3786335.3813137).
  - Setup: N=10 homogeneous agents (Qwen2.5-7B, Llama-3.1-8B, Ministral-3-8B), R=3 rounds, GSM-Hard and MMLU-Hard.
  - Failure pathways: sycophantic conformity, with modal adoption up to 85.5%; contextual fragility, with correct answers overturned up to 70.0% of the time; and consensus collapse, an oracle gap of up to 32.3 percentage points, where plurality voting discards correct answers already in the pool.
  - Conformity is high even at K=2 peers seen.
  - Cost: debate spends 2.1–3.4× the tokens of self-correction (up to 28,631 per problem) for equal or lower accuracy. — [arXiv](https://arxiv.org/abs/2605.00914)
- **Hao, Wu, Qiu, Xiao, Xu, Zheng, Qin, "Not All Flips Are Conformity: Decomposing Stance Convergence in Multi-Agent LLM Debate."** arXiv 2606.00820, PDF https://arxiv.org/pdf/2606.00820, preprint.
  - Setup: 5 GPT-4o agents on MMLU-Pro questions where they disagree.
  - Baseline flips: 37% of agent-question pairs change answer even with *no* peer information.
  - Peer adoption: of the pairs stable under that control, 29.3% adopt a peer's answer after seeing stances, and these adoptions mix corrections, new errors and switches between wrong answers.
  - Cost: full reasoning exchange adds no majority-vote gain over self-reflection, at +57% tokens.
  - Intervention: an answer-agnostic intervention suppressed both good and bad adoption.
  - Conclusion: "convergence is an ambiguous signal of value." — [arXiv](https://arxiv.org/abs/2606.00820)
- **Wang et al., "From Debate to Decision: Conformal Social Choice for Safe Multi-Agent Deliberation."** arXiv 2604.07667, PDF https://arxiv.org/pdf/2604.07667, preprint (v2 Oct 20 2026).
  - Mechanism: verbalised probability distributions from heterogeneous agents are combined by a linear opinion pool and calibrated with split conformal prediction. A singleton set means act; a larger set means escalate to a human.
  - Interception: at α=0.05, 81.9% of wrong-consensus cases are flagged at the final round.
  - Accuracy: early-singleton accuracy is 90.0–96.8% on MMLU-Pro, up to +22.1 percentage points over consensus stopping, which the authors attribute to *selection, not better reasoning*.
  - Baselines: simple probability or entropy thresholds intercept comparably. — [arXiv](https://arxiv.org/abs/2604.07667)
- **"Sequential Consensus for Multi-Agent LLM Debates: A Wald-SPRT compute governor with calibration-based failure detection."** arXiv 2605.19193, PDF https://arxiv.org/pdf/2605.19193, preprint; I did not record the authors. An LLM judge emits a consensus score each round, and a Wald SPRT stops the debate or caps it at R_max. On GSM8K it uses 1.01 rounds on average (4.06 calls) for 97.0% accuracy vs. 99.0% for fixed 5 rounds (15 calls). The calibration set is small (40 items, 200 test items per benchmark). — [arXiv HTML](https://arxiv.org/html/2605.19193v1) (figures via search summary; not opened in full)
- **Jeong, Choi, Kim, Jang, "Tool-MAD: A Multi-Agent Debate Framework for Fact Verification with Diverse Tool Augmentation and Adaptive Retrieval."** arXiv 2601.04742, PDF https://arxiv.org/pdf/2601.04742, preprint. Each debater has a *different* external tool (search API, RAG), and queries adapt as the debate goes on. A judge scores responses by Faithfulness and Answer Relevance. Reported gains: "up to 5.5%" accuracy in the introduction and "up to 35%" in the conclusion. These may be different metrics; check before citing. — [arXiv](https://arxiv.org/abs/2601.04742)
- **Wu et al., "Group Perspective Matters: Regulating Debate Relationships Can Mitigate Blind Conformity in Multi-Agent Debate" (DEAR).** arXiv 2608.03648, PDF https://arxiv.org/pdf/2608.03648, preprint. The authors argue that individual-level signals (confidence, perplexity) do not track correctness and can worsen conformity. Two jointly trained MARL agents choose *which peers each agent references* and adjust generation behaviour. They report better accuracy at fewer tokens; the abstract gives no numbers. — [arXiv](https://arxiv.org/abs/2608.03648)
- **Okawa, "Emergence of Biased Consensus in Multi-Agent LLM Debates."** arXiv 2608.02827, PDF https://arxiv.org/pdf/2608.02827, ICML 2026 per the listing. A social-physics model predicts a *phase transition* to collective bias once conformity passes a threshold set by the initial bias and the sampling noise. Experiments show a finite-size crossover, and agent heterogeneity smooths it out. The effect holds on investment decisions and LLM-as-judge tasks. — [arXiv](https://arxiv.org/abs/2608.02827)
- **Jin, Ma, Zeng, Cui, Zhang, Wang, "Remember and Reweight" (R²-MAD).** arXiv 2609.03619, PDF https://arxiv.org/pdf/2609.03619, EMNLP 2026 Findings. It targets the "shared misconception" case where most agents start wrong. Memory retrieval is keyed to the current level of consensus, and per-agent reliability *estimated from past debates* (not self-report) sets influence weights. The abstract gives no numbers. — [arXiv](https://arxiv.org/abs/2609.03619)
- **"Debating Truth: Debate-driven Claim Verification with Multiple LLM Agents" (DebateCV).** arXiv 2507.19090, PDF https://arxiv.org/pdf/2507.19090, WWW 2026. Two debaters take *opposing* stances and a moderator decides. Zero-shot moderators drift toward neutral verdicts, which Debate-SFT corrects. — [arXiv](https://arxiv.org/abs/2507.19090); search summary

**Negotiation (opposing goals by construction)**

- **Fu, Peng, Khot, Lapata, "Improving Language Model Negotiation with Self-Play and In-Context Learning from AI Feedback."** arXiv 2305.10142, PDF https://arxiv.org/pdf/2305.10142, preprint. A buyer LLM and a seller LLM (opposed) bargain, and a third LLM critic gives feedback that is fed back in context over rounds. The metric is deal price. Only some models improve. Claude-instant improved less as buyer than as seller. Stronger models improve over rounds but risk breaking the deal more often. — [arXiv](https://arxiv.org/abs/2305.10142)
- **NegotiationArena** (Bianchi et al., arXiv 2402.05863, PDF https://arxiv.org/pdf/2402.05863) and **LLM-Deliberation / scoreable multi-party negotiation games** (Abdelnabi et al., arXiv 2309.17234, PDF https://arxiv.org/pdf/2309.17234) are the 2023–2024 negotiation testbeds. A 2026 reproduction of Abdelnabi et al.'s Scoreable Games found model comparison there "ambiguous" (arXiv 2602.18230). — [arXiv 2402.05863](https://arxiv.org/abs/2402.05863); [arXiv 2309.17234](https://arxiv.org/abs/2309.17234); [repro](https://www.arxiv.org/abs/2602.18230)
- 2026 negotiation benchmarks:
  - **PieArena** (arXiv 2602.05302, PDF https://arxiv.org/pdf/2602.05302): MBA-course scenarios; GPT-5 matches or beats trained business-school students; it also tracks deception and instruction compliance.
  - **AgoraBench / "MERIT Feedback Elicits Better Bargaining in LLM Negotiators"** (arXiv 2602.10467, PDF https://arxiv.org/pdf/2602.10467, ACL 2026): 9 settings including deception and monopoly, with utility-theoretic metrics.
  - **AgenticPay** (arXiv 2602.06008): finds gaps in long-horizon strategic reasoning.
  - These are benchmarks rather than answer-producing systems. — search summaries: [PieArena](https://arxiv.org/abs/2602.05302), [AgoraBench](https://www.alphaxiv.org/abs/2602.10467.md), [AgenticPay](https://arxiv.org/pdf/2602.06008)

**Game-based cooperative/competitive agents**

- **Cicero** (Meta FAIR, *Science* 2022, not arXiv; reference point only). It is the reference point for messages *bound to a planner's intended actions*: its dialogue was conditioned on intents produced by a strategic planning module. That is the structural opposite of free-form LLM debate. — [Science DOI](https://www.science.org/doi/10.1126/science.ade9097) (not re-fetched this session)
- **Guan, Kong, Zhong, Wang, "Richelieu: Self-Evolving LLM-Based Agents for AI Diplomacy."** arXiv 2407.06813, PDF https://arxiv.org/pdf/2407.06813, NeurIPS 2024. It learns through self-play with no human data. A third-party summary reports a 6.83% win rate vs. Cicero's 6.03% in press Diplomacy. On 7-player Werewolf it reaches 59.2% vs. 65% for the strongest dedicated agent. — [arXiv](https://arxiv.org/pdf/2407.06813); [alphaXiv overview](https://alphaxiv.org/overview/2407.06813v4)
- **Xu et al., "Exploring Large Language Models for Communication Games: An Empirical Study on Werewolf"** (arXiv 2309.04658, PDF https://arxiv.org/pdf/2309.04658) and **Wang et al., ReCon "Avalon's Game of Thoughts"** (arXiv 2310.01320, PDF https://arxiv.org/pdf/2310.01320). These are hidden-role games in which messages are strategically *misaligned* by design, so they are the closest LLM analogue to cheap talk with conflicting interests. I did not re-fetch details this session. — [arXiv 2309.04658](https://arxiv.org/abs/2309.04658); [arXiv 2310.01320](https://arxiv.org/abs/2310.01320)

**Pointers only (out of scope)**: Zhang et al., "Exploring Collaboration Mechanisms for LLM Agents: A Social Psychology View" (arXiv 2310.02124; conformity-style dynamics in agent societies); Subramaniam et al., "Multiagent Finetuning" (arXiv 2501.05707; training, not harness); G-Designer (arXiv 2410.11782) and sparse-topology MAD (topology optimisation); Khan et al. 2024 persuasive-debate (debate as judging); MAD-Fact (arXiv 2510.22967; evaluation); "Multi-Agent Debate for LLM Judges with Adaptive Stability Detection" (arXiv 2510.12697; judging, but its Kolmogorov–Smirnov stop rule is relevant). — [search result](https://arxiv.org/html/2510.12697v1)

### Inferences
- In contract-theory terms, the canonical MAD harness is a team with fully aligned payoffs in which every message is free and unverifiable. With aligned interests, cheap talk *can* be fully informative in principle. The empirical failure is therefore not strategic misreporting. It is that the "receiver" (the next-round copy of the same model) updates on a peer's stated answer and confidence rather than on the signal's informativeness: correlated priors (Estornell & Liu's shared misconceptions) plus a herding-like update (Choi's martingale; Bertalanič & Fortuna's 85.5% modal adoption).
- ReConcile and EoT weight by *self-reported* confidence, a pure cheap-talk signal with no scoring rule behind it. R²-MAD's history-based reliability and Conformal Social Choice's calibration are the only designs I found that replace self-report with something closer to a track record or a proper calibration step.
- Opposition is almost always *prompted* (MAD's affirmative/negative sides, Multi-Persona's "devil", DebateCV's opposing stances) rather than paid. The incentive conflict therefore lives in the prompt, and the model's prior toward agreeableness can override it.

### Gaps
- The full results tables for Zhang et al. 2502.08788 (per-method vs. SC numbers), Estornell & Liu (intervention gains), EoT, Corex, Tool-MAD and DEAR were not retrieved; the PDFs did not parse via fetch and the HTML had only the abstract.
- ICML 2024 status of Smit et al. and ACL 2024 status of Wang et al. 2402.18272 are not confirmed on the arXiv listings.
- I did not identify the authors of the SPRT paper (2605.19193), and its figures come from a search summary.
- Werewolf/Avalon/Cicero mechanism details are from the abstracts' framing and prior knowledge; I did not fetch them this session.

## Does debate beat self-consistency at equal compute, by the papers' own numbers?

### Takeaway
Mostly no. Every controlled comparison from 2023 to 2026 finds plain majority voting or self-consistency matching or beating debate at equal or lower compute for homogeneous agents. Debate's gains show up mainly when the models are heterogeneous, the base prompt is weak, or the agreement level is tuned per dataset.

### Cited Findings
- Du et al. themselves report debate beating majority-of-agents: GSM8K 85.0 vs. 81.0 and arithmetic 81.8 vs. 69.0. However, debate there uses 3 agents × 2 rounds while the majority baseline uses 3 single samples, so compute is not matched. — [ar5iv](https://ar5iv.labs.arxiv.org/html/2305.14325)
- Smit et al. (GPT-3.5): Self-Consistency 0.78 vs. ER 0.76 on MMLU and SC 0.56 = SoM 0.56 on CIAR. Medprompt is best on MedQA (0.65) and PubMedQA (0.77). MAD "do[es] not reliably outperform" SC or ensembling and costs more API calls. — [HTML v3](https://arxiv.org/html/2311.17371v3)
- Zhang et al. (5 methods × 9 benchmarks × 4 models): MAD often fails to beat CoT and Self-Consistency "even when consuming significantly more inference-time computation". — [arXiv](https://arxiv.org/abs/2502.08788)
- Choi et al.: majority vote of 5 agents with no debate scores 0.7691 vs. 0.7377 / 0.7112 / 0.7050 for 2/3/5-round decentralised debate (Qwen-7B), and 0.7242 vs. 0.6929 on Llama-8B. Debate costs strictly more because round 0 is the vote. — [HTML v2](https://arxiv.org/html/2508.17536v2)
- Kaesberg et al.: more discussion rounds *before* voting reduce performance; more agents help. — [arXiv](https://arxiv.org/abs/2502.19130)
- Bertalanič & Fortuna: debate uses 2.1–3.4× the tokens of isolated self-correction for equal or lower accuracy at the 7–8B scale. — [arXiv](https://arxiv.org/abs/2605.00914)
- Hao et al.: exchanging full reasoning gives no majority-vote gain over self-reflection, at +57% tokens. — [arXiv](https://arxiv.org/abs/2606.00820)
- Wang et al. 2024: a strongly prompted single LLM nearly matches the best discussion method; discussion wins only without demonstrations. — [arXiv](https://arxiv.org/abs/2402.18272)
- Counter-evidence: ReConcile reports up to +11.4% over multi-agent baselines, driven by *model diversity*. Zhang et al. find heterogeneity a "universal antidote". Smit et al. find that tuning the agreement level lifts Multi-Persona to the top on MedQA. — [ReConcile](https://arxiv.org/abs/2309.13007); [Zhang](https://arxiv.org/abs/2502.08788); [Smit](https://arxiv.org/html/2311.17371v3)

### Inferences
- What survives is diversity of *initial samples* (different models), which is the same thing that makes a vote informative. Per Choi's martingale result, the exchange itself adds no expected correctness for homogeneous agents. For a model-invariant harness, this suggests spending compute on independent heterogeneous draws plus an aggregation rule, not on rounds.

### Gaps
- No paper I found reports a strict FLOP- or token-matched debate-vs-SC sweep across model scales above about 32B. Choi's 32B check (0.9433 vote vs. 0.9400 MAD) is the largest controlled point found.

## Which papers show agents converging on confidence rather than correctness, and what mechanism do they blame?

### Takeaway
Many do. The blamed mechanisms fall into four groups: (a) sycophancy and conformity, meaning models adopt the peer or majority answer without scrutiny; (b) shared priors and correlated errors from shared training data; (c) noise-driven phase transitions into collective bias; and (d) confidence or persuasiveness signals that do not track correctness.

### Cited Findings
- Du et al.: debates sometimes converge on wrong answers that agents then state confidently; agents are generally "agreeable". — [ar5iv](https://ar5iv.labs.arxiv.org/html/2305.14325)
- Liang et al.: "Degeneration-of-Thought": a model confident in its answer stops generating alternatives even when wrong. The judge may be unfair when the agents are different LLMs. — [arXiv](https://arxiv.org/abs/2305.19118)
- Estornell & Liu: similar models converge on the majority opinion, including a shared misconception rooted in shared training data. — [NeurIPS](https://neurips.cc/virtual/2024/poster/93363)
- Wynn, Satija, Hadfield: agents flip from correct to incorrect after seeing peers' reasoning, and accuracy declines even when strong models are the majority. Blamed on sycophancy and social conformity, i.e. agents "neither incentivized nor equipped" to resist persuasive wrong reasoning. — [arXiv](https://arxiv.org/abs/2509.05396)
- Yao et al.: inter-agent sycophancy causes "disagreement collapse" and sub-single-agent accuracy, coming from both debaters and judges. — [arXiv](https://arxiv.org/abs/2509.23055)
- Bertalanič & Fortuna: modal adoption up to 85.5%, correct answers overturned up to 70.0%, and plurality voting discarding correct answers already present (oracle gap up to 32.3 percentage points). Conformity grows with initial diversity. — [arXiv](https://arxiv.org/abs/2605.00914)
- Wu, Li, Li: majority pressure suppresses independent correction. — [arXiv](https://arxiv.org/abs/2511.07784)
- DEAR: confidence and perplexity signals "do not reflect" whether reasoning is correct and may worsen blind conformity. — [arXiv](https://arxiv.org/abs/2608.03648)
- Okawa (ICML 2026): a phase transition to biased consensus once conformity passes a threshold set by initial bias and sampling noise. — [arXiv](https://arxiv.org/abs/2608.02827)
- R²-MAD: "shared misconception", where a majority starting wrong is reinforced. — [arXiv](https://arxiv.org/abs/2609.03619)
- Conformal Social Choice: "agreement among agents does not show the answer is correct". Consensus stopping sends wrong consensus into automated action. — [arXiv](https://arxiv.org/abs/2604.07667)
- Hao et al.: caution against over-attribution. 37% of flips happen with *no* peer information, so not all convergence is conformity. — [arXiv](https://arxiv.org/abs/2606.00820)

### Inferences
- None of these papers frames the problem as missing incentives, except in passing: Wynn et al.'s "not incentivized". In cheap-talk language, the receivers treat the sender's message as more informative than it is, because a message from a copy of yourself is correlated with your own error. The remedy suggested across the 2026 papers is to break correlation (heterogeneity: Zhang, Okawa) or to weight messages by an *external* reliability estimate (R²-MAD, Conformal Social Choice).

### Gaps
- No paper found isolates "the most confident agent wins regardless of correctness" with a direct measurement, e.g. win rate of the highest-stated-confidence agent conditioned on being wrong. ReConcile's confidence weighting invites exactly this failure, but I found no measurement of it.

## Is there any system where what an agent says is checked against something before other agents act on it?

### Takeaway
Rarely. Most systems are pure cheap talk. The partial exceptions:
- tool-grounded debaters (Tool-MAD; courtroom/RAG claim-verification debates), where evidence is fetched per agent;
- judge-side scoring of faithfulness (Tool-MAD);
- a ground-truth oracle used only as an upper bound (Choi et al.);
- Cicero-style binding of messages to planned actions (outside the LLM-debate family);
- post-hoc calibration that decides whether the consensus is acted on at all (Conformal Social Choice).

I found no LLM debate system that verifies each claim *before* it is broadcast to peers.

### Cited Findings
- Tool-MAD: each agent has a distinct external tool (search API or RAG) with adaptive queries, and the judge scores Faithfulness and Answer Relevance. — [arXiv](https://arxiv.org/abs/2601.04742)
- Contestable MAD for multimedia verification (arXiv 2605.14495) turns tool evidence into structured support/attack arguments in a quantitative bipolar argumentation framework. PROClaim (arXiv 2603.28488) adds progressive retrieval to courtroom-style debate. — [search summary](https://arxiv.org/html/2605.14495); [PROClaim](https://arxiv.org/html/2603.28488v1)
- Choi et al.'s MAD-oracle locks in an answer once it is verified correct (0.8289 vs. 0.7084 at T=5), which shows the value of verification but needs ground truth. — [HTML v2](https://arxiv.org/html/2508.17536v2)
- Conformal Social Choice checks the *aggregate* against a calibration set, not individual messages, and routes uncertain cases to a human. — [arXiv](https://arxiv.org/abs/2604.07667)
- Corex's "Retrieve" mode has a model score the faithfulness of candidate chains, i.e. an LLM check rather than an external one. — [arXiv](https://arxiv.org/abs/2310.00280)
- Malenfant's Dialogue Moral Hazard Game makes *information acquisition* costly: an agent pays a query cost to reveal a hidden safety fact. The revealed fact is ground truth, so what is checked is whether the agent passes it on. — [arXiv](https://arxiv.org/abs/2607.23982)

### Inferences
- The open design slot for a contract-theoretic harness is message-level verification with consequences: a claim gets a verifiable tag (tool result, executed code, retrieved citation) before broadcast, and unverifiable claims are discounted. The literature has the components (tools, calibrated pooling, history-based reliability) but has not assembled them into a pre-broadcast checker.

### Gaps
- I could not confirm Tool-MAD's exact headline numbers (5.5% vs. 35%), and I did not inspect whether its tool outputs are shown to peers before they respond.

## What stop rule do the systems use, and did fixed-round systems report degradation after round N?

### Takeaway
Stop rules come in four kinds. Fixed rounds is the dominant kind, typically 2–5 (Du, Smit, Choi, Bertalanič & Fortuna). The others are unanimity or convergence (Du, ReConcile's consensus), a judge's adaptive stop (Liang's MAD), and, newly in 2026, statistical stop rules (Wald SPRT; conformal first-singleton). Several fixed-round studies report flat or *declining* accuracy past 2 rounds.

### Cited Findings
- Du et al.: 3 agents × 2 rounds by default; gains beyond 4 rounds about the same as at 4 (saturation, no degradation reported). — [ar5iv](https://ar5iv.labs.arxiv.org/html/2305.14325)
- Liang et al.: adaptive termination by the judge is reported as important. — [arXiv](https://arxiv.org/abs/2305.19118)
- Smit et al.: rounds do not reliably help. Multi-Persona on PubMedQA goes 0.68 to 0.67 at 4 rounds, ChatEval on MedQA 0.70–0.71 at 2 rounds vs. 0.67 at 3, and SoM-4 0.73 at 2 vs. 0.72 at 3; cost always rises. — [HTML v3](https://arxiv.org/html/2311.17371v3)
- Choi et al.: decentralised and sparse MAD mostly decline as T rises (Qwen-7B 0.7377 → 0.7112 → 0.7050 for T=2/3/5). — [HTML v2](https://arxiv.org/html/2508.17536v2)
- Kaesberg et al.: more rounds before voting lower performance. — [arXiv](https://arxiv.org/abs/2502.19130)
- Wynn et al.: accuracy can decline over the course of a debate. — [arXiv](https://arxiv.org/abs/2509.05396)
- Bertalanič & Fortuna: at R=3, debate costs 2.1–3.4× the tokens of self-correction for equal or lower accuracy. — [arXiv](https://arxiv.org/abs/2605.00914)
- SPRT governor: stops at 1.01 average rounds (4.06 calls) for 97.0% on GSM8K vs. 99.0% at a fixed 5 rounds (15 calls). — [arXiv HTML](https://arxiv.org/html/2605.19193v1)
- Conformal Social Choice: the guarantee holds at a pre-specified fixed round; adaptive first-singleton stopping is evaluated but not covered. — [arXiv](https://arxiv.org/abs/2604.07667)

### Inferences
- Since convergence is "an ambiguous signal of value" (Hao et al.) and wrong consensus is common, *stop-at-unanimity* rewards exactly the conformity failure. Both statistical stop rules treat consensus as evidence to be weighed rather than as a terminal state.

### Gaps
- No paper found reports per-round degradation curves past round 5 for any system.

## What does the cheap-talk literature on LLM agents say, as it applies to these systems?

### Takeaway
The small 2025–2026 literature studies LLMs in classical games with a costless pre-play message. A one-word channel can take Stag Hunt cooperation from 0% to 96.7%, and cheap talk mostly stabilises play in repeated games. However, the channel is exploitable (Byzantine signallers), meta-reasoning about the topology matters, and team moral hazard shows that agents fail to *acquire and pass on* information that helps others.

### Cited Findings
- **Madmoun & Lahlou, "Communication Enables Cooperation in LLM Agents: A Comparison with Curriculum-Based Approaches."** arXiv 2510.05748, PDF https://arxiv.org/pdf/2510.05748, EACL 2026 (short).
  - Result: in a 4-player Stag Hunt, a one-word cheap-talk channel raises cooperation from 0% to **96.7%**.
  - Correction: v3 (Mar 2026) fixed a denominator bug; v1 and v2 reported 48.3% and 50.0%, now 96.7% and 100.0%. Older citations carry the wrong number.
  - Curriculum: a curriculum of progressively harder games *cut* payoffs by 27.4% in an Iterated Public Goods Game with Punishment ("learned pessimism"). — [arXiv](https://arxiv.org/abs/2510.05748); [ACL Anthology](https://aclanthology.org/2026.eacl-short.23)
- **El Mir, Takáč, Lahlou, "Byzantine Cheap Talk: Adversarial Resilience and Topology Effects in LLM Coordination Games."** arXiv 2606.07790, PDF https://arxiv.org/pdf/2606.07790, NETYS 2026. The setup is 6 model families and 720 trials.
  - Byzantine agents: honest agents detect agents that signal cooperation and then defect within one round, yet often keep cooperating and fail to recover collectively.
  - Topology: *announcing* a restricted communication topology collapses cooperation, while the same restriction left silent keeps it near-perfect. The authors attribute this to agents' meta-reasoning about hidden information.
  - Archetypes: models split into Defection-Prone and Cooperation-Persistent. — [arXiv](https://arxiv.org/abs/2606.07790)
- **Lorè & Heydari, "Communication Enhances LLMs' Stability in Strategic Thinking."** arXiv 2602.06081, PDF https://arxiv.org/pdf/2602.06081, preprint. Models of 7–9B parameters play a 10-round repeated Prisoner's Dilemma. Pre-play messages reduce trajectory noise in most model–context pairs; models with higher baseline volatility gain most; a few context-specific harms are reported. — [arXiv](https://arxiv.org/abs/2602.06081)
- **Lorè, Zhu, Heydari, "Cheap Talk Stabilizes Strategic Interaction in LLM Agents."** arXiv 2609.16270, PDF https://arxiv.org/pdf/2609.16270, preprint (Sep 2026).
  - Setup: 4 open-weight 7–9B models; Prisoner's Dilemma, Snowdrift, Stag Hunt and Harmony; 6 framing contexts.
  - Result: cheap talk is mostly stabilising, with 5 corrected reversals, mostly in social or team framings.
  - Mechanism in Qwen: the effect works through lower action uncertainty and less round-to-round drift.
  - Representation: a late-layer "policy-content direction" in Qwen and Falcon; ablating it increases switching.
  - History: recent partner behaviour decides whether mutual-benefit language increases persistence. — [arXiv](https://arxiv.org/abs/2609.16270)
- **Malenfant, "Moral Hazard in Multi-Agent Language Models."** arXiv 2607.23982, PDF https://arxiv.org/pdf/2607.23982. Preprint (v7, Sep 2026); a NeurIPS 2026 listing appears on neurips.cc but I did not confirm it.
  - Game: the Dialogue Moral Hazard Game, built on Holmström team moral hazard. An agent keeps a local reward or pays a query cost to reveal a hidden safety fact that mainly helps another agent's later decision.
  - Scale: 14 open-weight and 4 frontier models, 3,015 decisions per model.
  - Frontier results: three frontier models track the derived private-share boundary across 9 query costs, with mean absolute errors of 0.013, 0.030 and 0.024.
  - GEPA prompt optimisation: one model's team success rose from 22.2% to 100.0% while query use fell from 51.1% to 0.3%. That success came from a learned rank-label mapping rather than revelation; perturbing the mapping dropped success to 12.5% and then 0.0%.
  - CREDIT: a new method that rewards counterfactual causal contribution rather than query frequency.
  - Conclusion: the same team outcome can come from direct revelation or a learned information structure, so evaluate mechanisms rather than team success. — [arXiv](https://arxiv.org/abs/2607.23982); [NeurIPS listing](https://neurips.cc/virtual/2026/165349)

### Inferences
- Applied to debate harnesses, three lessons carry over.
  - Cheap talk helps most where the problem is *coordination* (Stag Hunt), which is the aligned-interest case debate already sits in. Debate's problem is not coordination failure but over-coordination on a wrong answer.
  - Signalling channels are an injection surface (Byzantine). A debate harness with no message verification has the same exposure to one confidently wrong or adversarial agent.
  - Malenfant shows aggregate success can hide the wrong mechanism. That mirrors Choi's and Hao's finding that debate "wins" are often vote or selection effects. Harness evaluation should measure what each message contributed (CREDIT-style counterfactual replay) rather than final accuracy.

### Gaps
- None of the cheap-talk papers tests a debate-for-answers harness directly; the transfer is by analogy.
- Lorè/Zhu/Heydari use 7–9B open models only.
- Malenfant's model names, counts and venue changed across 7 versions; cite v7 specifically.
