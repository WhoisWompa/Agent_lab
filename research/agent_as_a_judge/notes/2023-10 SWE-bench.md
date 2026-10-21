---
title: SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
authors: Carlos E. Jimenez et al.
date: 2023-10
arxiv: 2310.06770
url: https://arxiv.org/abs/2310.06770
venue: ICLR 2024
category: agent-evaluation-benchmarks
topics: ["agent evaluation benchmarks", "alternative evaluation paradigms"]
---
# SWE-bench: Can Language Models Resolve Real-World GitHub Issues?

## One line
Outcome benchmark of 2,294 real GitHub issues from 12 Python repos, graded by running the repo's FAIL_TO_PASS / PASS_TO_PASS unit tests on the agent's patch.

## Method
Verifier = the tests from the merged human PR. Only the final patch is judged; the trajectory is not looked at. Hidden tests are not shown to the agent.

## Evaluated on
At release the best model (Claude 2 with retrieval) resolved 1.96%.

## Limitations admitted by the authors
- Tests come from the original PR, so they can be narrower or broader than the issue text implies.

## Limitations found by others
- (added by alternative-paradigms researcher) Repository-level issue resolution judged by executing the repository's fail-to-pass and pass-to-pass tests.
- Solution leakage: 32.67% of passing patches had the fix in the issue text or comments; 31.08% passed on weak tests; SWE-Agent+GPT-4 dropped 12.47% -> 3.97% after filtering (SWE-Bench+, 2410.06992).
- 7.8% of 'resolved' patches fail the full developer test suite; 29.6% of plausible patches diverge behaviourally from gold; resolution inflated ~6.2 pp (Wang, Pradel, Liu, 2503.15223).
- Insufficient tests in 36 instances, 345 wrongly passing patches; 40.9% of Lite and 24.4% of Verified leaderboard entries affected (UTBoost, 2506.09289).
- Memorisation: models name the buggy file from the issue alone with up to 76% accuracy vs ~53% on unseen repos (SWE-Bench Illusion, 2506.12286).
- ~Half of test-passing agent PRs would not be merged by maintainers, ~24 pp gap (METR note, 2026-03-10).

## What it leaves untried
- Grading on maintainer acceptance or code review rather than tests.
- Judging the trajectory (did the agent read the tests, did it test at all).

## Topics
[[Topic - agent evaluation benchmarks]] · [[Topic - alternative evaluation paradigms]]
