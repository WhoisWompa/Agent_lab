---
name: paper-ingest
description: Turn a folder of PDFs into paper notes, topic links and the graphify knowledge graph. Use when the user says "ingest <folder>", "add these papers", "note these PDFs", or when a research run has downloaded papers that need notes. One paper-reader agent per paper, five at a time; the main session rules on proposed new topics.
---

# Paper ingest

A PDF becomes a note (the idea and the limitations, with evidence), the note carries its topics from `research/topics.md`, the topic notes are regenerated, and the graph is rebuilt. The reader is `.claude/agents/paper-reader.md`; this skill is the main session's side.

## Steps

1. **Extract text once.** `uv run --with pypdf python -I research/_tools/extract_pdf_text.py "<pdf folder>" <scratchpad>/pdftext`. One `.txt` per PDF, same relative path, plus `index.json` with page and token counts. Readers read the text, never the PDF.
2. **Skip what exists.** For each PDF, Glob the notes folder for its title's main words. A matching note means no new note; add `pdf:` and `folder:` to it if missing.
3. **Spawn readers, five at a time.** One `paper-reader` per paper, `model: opus`. Each brief is four lines: paper text path, source PDF path, notes folder, folder chain as a JSON list. Wait for the five, then the next five. The user sets the batch size; five is the default they chose.
4. **Rule on proposals.** A reader that finds no fitting topic returns a proposal instead of topics. Read `research/topics.md` in full. If the proposal names a real gap, add a row to the registry (name, definition in the registry's style, in the right group) and tell the reader `added <name>` with SendMessage. If an existing topic fits, tell it `use <names>`. A reader never edits the registry.
5. **Rebuild.** From the repo root: `python -I -X utf8 research/_tools/build_topics.py` (topic notes, overview, Topics sections), then `graphify update . --force` and `graphify cluster-only . --no-label`.
6. **Report.** Notes written, notes skipped as existing, topics added to the registry, and anything a reader flagged (a PDF whose content does not match its filename, a missing date).

## Rules

- A new topic exists only after step 4 says so. Readers propose, the main session decides.
- Never run graphify's semantic (LLM) pass without the user's word; the quick-scan is enough for topic traversal and costs nothing.
- Nothing from the papers' text comes into the main session. Readers read; the session reads their reports and the registry.
