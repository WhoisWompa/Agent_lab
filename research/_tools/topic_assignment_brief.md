# Topic assignment brief

You classify paper notes into topics. Read every note on your list in full (they are 700 to 1,000 words each), then write ONE JSON file. Do nothing else: no other files, no edits to the notes.

## The topics

A paper belongs to every topic whose definition it satisfies, not only the one it was filed under. Most papers belong to two or three. Use these five names exactly:

- "agent as a judge": the paper is about evaluating agents or LLM outputs with an LLM or agent as the judge, or about judges themselves: their biases, their calibration, their reliability, benchmarks for judges, user simulators used to evaluate agents, replacing judges with cheaper models. If the paper's use case is judging, grading, verifying or evaluating, it belongs here.
- "decision models": the paper is about typed / System One / single-pass decision models (Jev and its kin: Laya, Kev, Clef, Decider, Bongard, etc.): their architecture, theory, interface, properties, or their use inside agents. Any paper whose subject is such a model belongs here.
- "open models": the paper builds, trains, distils, adapts, reproduces or releases an open-weight decision model, or gives a recipe for getting one from an existing LLM or encoder. The paper's contribution must include a model or recipe, not only measurements of a hosted model.
- "evaluations": the paper's main contribution is an audit, benchmark or empirical study of how decision models or judges behave: bias, calibration, coherence, robustness to wording or presentation, rejection behaviour, cost, failures in agent loops. Measurement is the contribution.
- "stopping rules": the paper is about when to stop sampling, testing or evaluating: sequential tests (SPRT, group sequential), adaptive testing, Bayesian optimal stopping, sample-size reduction with valid error control. Strict: a confidence threshold that gates escalation to a bigger model is NOT a stopping rule unless the paper frames it as sequential testing.

## Output

Write to the output path you were given a JSON object:

{
  "assignments": [
    {"note": "<filename without .md>", "topics": ["...", "..."], "why": "one sentence naming what in the note satisfies each topic"}
  ],
  "suggested_topics": [
    {"name": "<short topic name>", "definition": "one sentence", "notes": ["<filename without .md>", ...]}
  ]
}

- "assignments" has one entry per note on your list, in the order given, every topic list non-empty.
- "suggested_topics": up to five cross-cutting themes you saw in at least four of your notes that none of the five topics captures (for example a technique, a failure mode, a deployment pattern). Only themes a reader would want to walk to from a paper. Empty list if none.

Reply with only: the output path and the count of assignments.
