#!/usr/bin/env python3
"""Rebuild the skill's reference files from the guide manuscript, and the upload zip.

Usage:
    python3 tools/build.py "/path/to/Apply Claude.md"   # regenerate references/ and the zip
    python3 tools/build.py                              # only rebuild the zip

The manuscript is split at its "### Chapter N:" headings into one file per chapter
under skills/howtocc/references/. Figures are images in the manuscript; each is
replaced by the text description in FIGURES below, so update that table when a
figure changes. The zip (dist/howtocc.zip) is the form the Claude apps accept
under Settings > Capabilities > Skills.
"""
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "howtocc"
REFS = SKILL / "references"

SLUGS = {
    0: "getting-started",
    1: "fundamentals",
    2: "deployment-decision",
    3: "knowledge-generation",
    4: "content-creation",
    5: "software-development",
    6: "operational-processes",
    7: "personal-matters",
    8: "output-quality",
    9: "standardisation-delegation",
    10: "integration",
    11: "responsibility-organisation",
}

FIGURES = {
    1: """Figure 1 as text: the language model draws on two sources. (a) Training knowledge: fixed, cannot be changed, as of June 2026, no internal data. (b) The context window: working memory, controllable, around 1 million tokens. The context window holds instructions (personal, in the project, from skills), knowledge provided (files, project knowledge, Memory), tool results (web search, connectors, code execution), the conversation history and the current prompt. The response is generated token by token and becomes part of the conversation history.""",
    2: """Figure 2 as text: Task (prompt, instructions), Knowledge (projects, files, Memory, web search) and Integration (connectors to services and data) feed the language model, which reads the context window. The Result is a response in the chat, an artefact or file, or an action in a service or program. Reuse (skills, plugins, templates) captures what works (proven tasks, procedures and integrations) and is loaded for a matching task. Delegation (Cowork, scheduled tasks, agents) means Claude carries out the process itself, in several steps or on a schedule.""",
    3: """Figure 3 as text: a two-by-two matrix. Axes: "What does an error cost?" (little or a lot) and "Is an error noticed?" (at once or hardly).
- Costs little, noticed at once: use freely. Ideas, outlines and drafts; rewording for your own use; explanations as an introduction to a topic.
- Costs little, hardly noticed: use, check samples. Summaries of long documents; research overviews for orientation; sorting and tagging large volumes.
- Costs a lot, noticed at once: use, check the result in full. Program code that can be tested; analyses that can be recalculated; texts that are read before sending.
- Costs a lot, hardly noticed (the top-right box): only with evidence and expert review. Legal, health and financial questions in individual cases; facts and quotations without a source to hand.""",
    4: """Figure 4 as text: four steps alternating between human and Claude. 1 (human) Set the question and criteria: options, criteria, weights. 2 (Claude) Rate the options per criterion: a table with evidence and assumptions. 3 (Claude) Cross-check the result: strongest objections, missing information. 4 (human) Weigh up and decide; responsibility stays here. Steps 2 and 3 repeat if new objections arise.""",
    5: """Figure 5 as text: five stages. In the session: 1 Request and plan (human): state the goal, location and test criterion; approve larger changes as a plan first. 2 Change and check (Claude): edit files, run the check, read the error output, correct, until the check passes. 3 Cross-check (Claude and checking tools): a fresh context with no knowledge of the history, using /code-review and /security-review. At the pull request: 4 Check automatically: Code Review and CI. 5 Approve: a human decides.""",
    6: """Figure 6 as text: a customer enquiry (chat, email, form) is 1 classified by Claude (topic, urgency, responsibility). Routine questions are 2 answered directly, backed by the knowledge base; the response carries its source and is in the language of the enquiry. If uncertain, Claude 3 prepares the case (summary and draft reply) and 4 staff check, decide and reply. The knowledge base holds policies, product knowledge and articles from resolved cases.""",
    7: """Figure 7 as text: three levels as distress increases.
- Everyday strain (annoyance, stress, a hard day): Claude is suitable, to sort out thoughts, prepare a conversation, gain distance. People: trusted people such as friends, family, colleagues.
- Persistent distress (for weeks, daily life suffers): Claude only as a supplement, to collect questions for the appointment and find support services. People: professional help such as a GP, psychotherapy, a counselling service.
- Acute crisis (suicidal thoughts, acute danger): Claude is not suitable and should itself point to human help. People: immediate help. In Germany: emergency number 112, helpline 0800 111 0 111 or 116 123.""",
    8: """Figure 8 as text: three nested scopes, all of which must fit inside the limited context window. Account (applies in every conversation): personal instructions (working style, tone; set by the human) and Memory (topics from earlier conversations; created by Claude). Project (applies only there): project instructions (role, goal, rules; set by the human), project knowledge (files for the project) and project memory (created by Claude). Conversation: the prompt (task, files, images) and the history (responses and tool results).""",
    9: """Figure 9 as text: three forms, with cost and coordination effort increasing from first to last. Chain: step 1, check, step 2, check, step 3; a fixed sequence with checkable interim results. Agent with sub-agents: the main agent distributes work to sub-agents, each with its own context window, and brings the results together. Agent team: a lead session and several sessions share one task list and coordinate directly.""",
    10: """Figure 10 as text: prompt injection becomes a risk where two conditions meet. Condition 1: Claude reads third-party content (web pages, emails, third-party files). Condition 2: Claude can take far-reaching action (send, pay, delete, change). Countermeasure for 1, limit reading: only trusted sources and extensions. Countermeasure for 2, limit action: approval before far-reaching actions.""",
}


def split(manuscript: Path) -> None:
    lines = manuscript.read_text(encoding="utf-8").splitlines()
    chapters, current, figure = {}, None, 0
    for line in lines:
        m = re.match(r"### Chapter (\d+): (.+)", line)
        if m:
            current = int(m.group(1))
            chapters[current] = [f"# Chapter {current}: {m.group(2)}"]
            continue
        if current is None or line.startswith("## Part") or line.strip() == "---":
            continue
        if line.startswith("!["):
            figure += 1
            chapters[current].append(FIGURES[figure])
            continue
        if line.startswith("#### "):
            line = "## " + line[5:]
        chapters[current].append(line.rstrip())
    if figure != len(FIGURES):
        sys.exit(f"manuscript has {figure} figures, FIGURES describes {len(FIGURES)}")
    if set(chapters) != set(SLUGS):
        sys.exit(f"chapters found {sorted(chapters)}, expected {sorted(SLUGS)}")
    REFS.mkdir(parents=True, exist_ok=True)
    for old in REFS.glob("*.md"):
        old.unlink()
    for n, body in chapters.items():
        note = ("\nFrom the guide *Apply Claude* by Kai Stalmann, as of November 2026. "
                "Numbers in brackets such as (8.3) refer to sections of the guide; "
                "the index in SKILL.md says which file holds each chapter.\n")
        text = "\n".join([body[0], note] + body[1:])
        text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
        (REFS / f"{n:02d}-{SLUGS[n]}.md").write_text(text, encoding="utf-8")
        print(f"{n:02d}-{SLUGS[n]}.md  {len(text):>6} chars")


def pack() -> None:
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    target = dist / "howtocc.zip"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(SKILL.rglob("*")):
            if f.is_file() and f.name != ".DS_Store":
                z.write(f, Path("howtocc") / f.relative_to(SKILL))
    print(f"wrote {target}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        split(Path(sys.argv[1]))
    pack()
