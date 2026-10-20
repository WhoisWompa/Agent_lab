# Game theory: the full map of branches and subfields

Written 2026-10-20. Purpose: a reference map of every kind of game theory and its subfields, so that specific areas can be picked later for focus on multi-agent system design. No papers yet; this is the index, not the reading list.

No source has one canonical taxonomy (the Yale Cowles paper calls the boundaries fuzzy), so the grouping below is by what each branch studies. Branches marked ★ are the ones most directly about designing systems of interacting agents.

## The classification axes

Every game is a cell in this grid. Any branch below sits somewhere in it.

| Axis | Values |
|---|---|
| Binding agreements | Non-cooperative vs cooperative |
| Players | 2-player, n-player, population (continuum), 1-player-vs-nature |
| Payoff structure | Zero-sum (strictly competitive), general-sum, common-payoff (team games), potential games |
| Timing | Simultaneous (normal/strategic form) vs sequential (extensive form) vs continuous time |
| Information | Perfect vs imperfect; complete vs incomplete (Bayesian); symmetric vs asymmetric |
| Repetition | One-shot, finitely repeated, infinitely repeated, stochastic/Markov |
| Chance | Deterministic vs stochastic |

## 1. The classical core

| Branch | Subfields and key objects |
|---|---|
| **Non-cooperative game theory** ★ | Normal-form games (Nash equilibrium, mixed strategies, dominance, rationalizability, correlated equilibrium). Extensive-form games (subgame perfection, backward induction, sequential and perfect Bayesian equilibrium, trembling-hand and proper equilibrium). Equilibrium refinement and equilibrium selection (risk dominance, Harsanyi-Selten). Zero-sum and minimax theory. Potential games and congestion games. Supermodular games. |
| **Games of incomplete information** ★ | Bayesian games and Bayesian Nash equilibrium (Harsanyi). Signaling games (Spence) and screening. Cheap talk and strategic communication (Crawford-Sobel). Global games (Carlsson-van Damme). Reputation models. Hypergames (players hold different models of the game itself). Psychological games (payoffs depend on beliefs). |
| **Repeated games** ★ | Folk theorems, trigger strategies, discounting. Repeated games with imperfect public or private monitoring. Reputation and bounded-memory play. |
| **Cooperative game theory** ★ | Transferable-utility games (core, Shapley value, nucleolus, kernel, bargaining set, Banzhaf index). Non-transferable-utility games. Coalition formation and coalition structure generation. Hedonic games. Partition-function (externality) games. Voting and weighted-voting power indices. Cost-sharing and surplus-division. |
| **Bargaining theory** | Axiomatic bargaining (Nash, Kalai-Smorodinsky, egalitarian solutions). Strategic bargaining (Rubinstein alternating offers). Multilateral and coalitional bargaining. Bargaining under incomplete information. |
| **Epistemic game theory** | Formal models of knowledge and belief (Aumann structures, type spaces). Common knowledge, common belief in rationality, agreement theorems. Epistemic foundations of equilibrium concepts. Interactive epistemology, modal and dynamic epistemic logic of games. |
| **Combinatorial game theory** | Two-player, perfect-information, no-chance games (Nim, Go, chess). Sprague-Grundy theory, surreal numbers, partizan and impartial games, misère play. Mostly a math branch, little to do with agents. |

## 2. Dynamic, population and learning branches

| Branch | Subfields and key objects |
|---|---|
| **Evolutionary game theory** ★ | Evolutionarily stable strategies (Maynard Smith). Replicator and other deterministic dynamics; stochastic evolutionary dynamics and stochastic stability. Population games and revision protocols (Sandholm). Evolution of cooperation (Axelrod, reciprocity, indirect reciprocity, punishment). Games on graphs and networks (spatial evolutionary games). Cultural evolution and evolutionary signaling. |
| **Dynamic and differential games** | Differential games (Isaacs): pursuit-evasion, zero-sum and nonzero-sum, open-loop vs feedback Nash, Hamilton-Jacobi-Isaacs equations. Stackelberg differential games. Linear-quadratic games. Robust and H-infinity control as a game. |
| **Stochastic (Markov) games** ★ | Shapley's stochastic games, discounted and average-reward criteria. Markov perfect equilibrium. Partially observable stochastic games (POSGs) and decentralized POMDPs (Dec-POMDPs, team case). |
| **Mean field games** ★ | Large-population limit (Lasry-Lions, Huang-Malhamé-Caines). Mean field equilibria, master equation. Mean field control (cooperative version). Mean field type games, Stackelberg mean field games, graphon games (heterogeneous populations). |
| **Learning in games** ★ | Fictitious play, best-response dynamics, regret matching. No-regret and online learning in games; convergence to coarse correlated equilibrium. Counterfactual regret minimization (CFR) for imperfect information. Double oracle and policy-space response oracles (PSRO). Opponent modeling, theory of mind, level-k and cognitive hierarchy reasoning. Game-theoretic foundations of multi-agent reinforcement learning (Nash-Q, minimax-Q, self-play, population-based training, open-ended learning). |
| **Behavioral and experimental game theory** | Bounded rationality, quantal response equilibrium, level-k models. Social preferences (fairness, inequity aversion, reciprocity). Learning models fit to lab data. Experimental economics methods. Neuroeconomics. Increasingly applied to LLM agents as test subjects. |
| **Network and graphical games** ★ | Graphical games (payoffs depend on neighbours). Network formation games. Games on networks, contagion and coordination on networks. Strategic network diffusion. |

## 3. Design, computation and applied branches

| Branch | Subfields and key objects |
|---|---|
| **Mechanism design** ★ | Revelation principle, incentive compatibility, individual rationality. Dominant-strategy vs Bayesian implementation. VCG mechanisms. Optimal auction theory (Myerson). Implementation theory (Maskin). Mechanism design without money. Dynamic mechanism design. Robust mechanism design. |
| **Auction theory and market design** | Single-item auctions (English, Dutch, first/second price), revenue equivalence. Combinatorial auctions. Multi-unit and spectrum auctions. Ad auctions. Double auctions and exchanges. |
| **Matching theory** ★ | Stable matching (Gale-Shapley), two-sided markets, school choice, kidney exchange, roommates and one-sided matching, matching with contracts, stable allocations. |
| **Social choice and voting** | Arrow's theorem, Gibbard-Satterthwaite, voting rules, judgment aggregation, fair division (cake cutting, envy-freeness, proportionality), apportionment. Computational social choice adds complexity of manipulation, preference elicitation, and algorithmic fair division. |
| **Contract theory** ★ | Principal-agent models, moral hazard (hidden action), adverse selection (hidden information), multi-task and multi-agent contracting, relational contracts, incomplete contracts. Algorithmic contract design is the recent CS version. |
| **Information design** ★ | Bayesian persuasion (Kamenica-Gentzkow), information disclosure, Bayes correlated equilibrium (Bergemann-Morris), information design with multiple receivers, algorithmic persuasion. The "inverse" of mechanism design: control what agents know instead of what they are paid. |
| **Algorithmic game theory** ★ | Complexity of computing equilibria (PPAD, Nash hardness). Price of anarchy and price of stability (selfish routing, congestion). Algorithmic mechanism design (truthful approximation, computational efficiency). Equilibrium computation (Lemke-Howson, support enumeration, sequence form). Learning-based equilibrium finding. |
| **Security and adversarial games** ★ | Stackelberg security games (leader commits, follower best-responds). Attacker-defender and interdiction games. Cyber-security games, moving-target defense. Adversarial ML as a game (GANs, robust learning). Deception games. |
| **Games in formal methods** | Games on graphs for verification and synthesis: reachability, safety, Büchi, parity games. Reactive synthesis from temporal logic. Rational synthesis and rational verification (multi-agent synthesis with Nash constraints). Alternating-time temporal logic (ATL) and strategy logic. Concurrent and timed games. |
| **Team theory and distributed decision making** ★ | Common-payoff games, Dec-POMDPs, information structures (Witsenhausen), consensus and coordination, decentralized control, credit assignment. |
| **Quantum game theory** | Quantum strategies and entangled games (Eisert-Wilkens-Lewenstein), non-local games, quantum correlated equilibrium. Niche. |
| **Applied game theory families** | Industrial organization (oligopoly, Cournot, Bertrand, Stackelberg, entry deterrence). Political economy (voting, lobbying, conflict, deterrence). Biology (animal conflict, signaling, kin selection). Law and economics. Blockchain and cryptoeconomics (consensus incentives, MEV, token mechanisms). Search and rendezvous games. Resource allocation and sharing games (water, spectrum, cloud). |

## Notes relevant to LLM multi-agent systems

- A January 2026 survey, "Game-Theoretic Lens on LLM-based Multi-Agent Systems" (arXiv 2601.15047), organises LLM multi-agent work around players, strategies, payoffs and information. It concludes that LLM agents reason and communicate well but still fail at equilibrium selection and incentive compatibility in partially observable settings.
- A February 2025 survey, "Game Theory Meets Large Language Models" (arXiv 2502.09053), proposes a taxonomy of the intersection and names game-theoretic reasoning as the next target for agents.
- "A Survey on LLM-Based Social Agents in Game-Theoretic Scenarios" (arXiv 2412.03920, TMLR May 2025) covers LLM agents as subjects in game settings.
- The MARL surveys all reduce the algorithm zoo to the stochastic-game and extensive-form frameworks plus the learning-in-games families, so those two rows are where most of the engineering literature lives.

## Sources

- [Game theory (Wikipedia)](https://en.wikipedia.org/wiki/Game_theory)
- [What is game theory (CASRAI)](https://casrai.org/guides/what-is-game-theory)
- [Saylor Academy game theory course page](https://s-saylor-academy-moodle.catalyst-ca.net/mod/page/view.php?id=62227)
- [Cowles Foundation discussion paper](https://cowles.yale.edu/sites/default/files/2022-08/d1808.pdf)
- [Algorithmic game theory (Wikipedia)](https://en.wikipedia.org/wiki/Algorithmic_game_theory)
- [Oxford ALGAME project](https://www.cs.ox.ac.uk/projects/ALGAME)
- [Waterloo algorithmic game theory course flyer](https://math.uwaterloo.ca/~cswamy/courses/co759/sp15/courseflyer.pdf)
- [Game-Theoretic Lens on LLM-based Multi-Agent Systems (arXiv 2601.15047)](https://arxiv.org/abs/2601.15047v1)
- [Game Theory Meets Large Language Models survey (arXiv 2502.09053)](https://arxiv.org/pdf/2502.09053)
- [Survey on LLM-based social agents in game-theoretic scenarios (arXiv 2412.03920)](https://arxiv.org/pdf/2412.03920v2)
- [Handbook of Dynamic Game Theory table of contents](https://ersearch2.cvtisr.sk/vufind/Record/275952/TOC)
- [Sandholm, Evolutionary Game Theory survey](https://users.ssc.wisc.edu/~whs/research/egt.pdf)
- [Advances in Dynamic and Evolutionary Games](https://cris.maastrichtuniversity.nl/en/publications/advances-in-dynamic-and-evolutionary-games-theory-applications-an)
- [Coalition formation in n-person games (Shenoy)](https://pshenoy.ku.edu/Papers/IJGT79.pdf)
- [Core lecture notes (Hart)](https://math.huji.ac.il/hart/papers/core-lk.pdf)
- [Coalition formation review](https://kam.mff.cuni.cz/~ryzak/data/coal_formation.pdf)
- [Epistemic Foundations of Game Theory (Stanford Encyclopedia)](https://plato.stanford.edu/entries/epistemic-game/)
- [Epistemic Game Theory handbook chapter (Dekel and Siniscalchi)](https://ideas.repec.org/h/eee/gamchp/v4y2015icp619-702.html)
- [Bayesian rational agents in iterated quantum games (arXiv 2408.02058)](https://arxiv.org/pdf/2408.02058)
- [Multi-agent Reinforcement Learning: A Comprehensive Survey (arXiv 2312.10256)](https://arxiv.org/pdf/2312.10256)
- [MARL: A Selective Overview of Theories and Algorithms (arXiv 1911.10635)](https://awesomepapers.io/ai-agents/papers/1911.10635)
- [Distributed no-regret learning in multi-agent systems (arXiv 2002.09047)](https://arxiv.org/abs/2002.09047?context=cs)
- [Algorithms in Multi-Agent Systems: RL and Game Theory (arXiv 2001.06487)](https://arxiv.org/abs/2001.06487v1)
- [Generalized Principal-Agency: Contracts, Information, Games and Beyond (arXiv 2209.01146)](https://arxiv.org/pdf/2209.01146)
- [Persuasion and Incentives Through the Lens of Duality (arXiv 1909.10584)](https://arxiv.org/pdf/1909.10584)
- [Opaque Contracts (arXiv 2301.13404)](https://arxiv.org/pdf/2301.13404)
- [Moral Hazard in Delegated Bayesian Persuasion (arXiv 2604.10006)](https://arxiv.org/pdf/2604.10006)
- [Stackelberg Security Games: Looking Beyond a Decade of Success (IJCAI 2018)](https://www.ijcai.org/proceedings/2018/775)
- [Stackelberg Security Games: Models, Applications and Computational Aspects](https://jtit.pl/jtit/article/view/749)
- [Extensions of Mean Field Games beyond homogeneity and anonymity (arXiv 2511.04929)](https://arxiv.org/pdf/2511.04929)
- [Stackelberg mean field games master equation (arXiv 2201.05959)](https://arxiv.org/pdf/2201.05959.pdf)
- [Linear-Quadratic Stackelberg Mean Field Games (arXiv 2412.16203)](https://arxiv.org/pdf/2412.16203)
- [Partial Solvers for Generalized Parity Games](https://orbi.umons.ac.be/bitstream/20.500.12907/30042/1/RP2019_Partial_Solvers_for_Generalized_Parity_Games.pdf)
- [Parity games and mu-calculus model checking](https://content.iospress.com/articles/fundamenta-informaticae/fi1235)
- [ltlsynt reactive synthesis tool](https://www.lre.epita.fr/publications/michaud.18.synt)
- [Knor parity game solver](https://www.tvandijk.nl/pdf/2024knor.pdf)

## Focus areas

Picked on 2026-10-20. One subfolder per area in this directory.

| Subfolder | Why |
|---|---|
| `information design/` | The orchestrator controls what agents know. |
| `mechanism design/` | The orchestrator controls what agents are paid. Applies when agents have divergent objectives. |
| `contract theory/` | Hidden effort and hidden type among foreign agents. |
| `team theory and distributed decision making/` | Agents with a shared objective but split information; the communication protocol is the lever. |
| `social choice/` | Aggregating several agents' outputs is a voting rule. |
| `cooperative game theory/` | Shapley value for credit assignment across a pipeline. |
| `stackelberg games/` | Leader commits, follower responds: the orchestrator-worker relationship. |
| `preference learning/` | The judge learns the payoff from the user's binary feedback. |
| `inverse reinforcement learning/` | Recovering the goal from behaviour and corrections; assistance games. |
