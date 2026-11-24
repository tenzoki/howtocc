# howtocc

A Claude Code plugin with one skill that answers what Claude can and cannot do, and which building block, plan or working method fits a task. It is built from the guide *Apply Claude: Fundamentals, fields of application, and working models* by Kai Stalmann (November 2026).

Ask it things like:

- Can Claude generate images? Read a 600-page PDF? Send my emails?
- Should this be a project, a skill or a connector?
- Which plan includes Cowork and Claude Code?
- Why is my result so generic, and how do I fix the prompt?
- What happens to my data, and what can an administrator control?

The skill reads only the chapter that covers the question, answers in your language, and cites the section of the guide. Prices, limits, model versions and beta labels are given with their date (November 2026), because they change.

## Use in Claude Code

```bash
/plugin marketplace add tenzoki/claude-plugins
/plugin install howtocc@tenzoki-plugins
```

Claude loads the skill by itself when a question matches. To call it directly, type `/howtocc:howtocc` followed by your question.

## Use in the Claude apps (chat and Cowork)

1. Run `python3 tools/build.py`. It writes `dist/howtocc.zip`.
2. In Claude, open Settings, then Capabilities, then Skills, and upload the zip.

Skills need code execution to be enabled. The folder `skills/howtocc/` is a plain skill in the open Agent Skills format, so it also works copied to `~/.claude/skills/howtocc/` without the plugin.

## Contents

```
skills/howtocc/
├── SKILL.md         how to answer, the index, and the core of the guide in brief
└── references/      one file per chapter of the guide (0 to 11)
tools/build.py       regenerates references/ from the manuscript and builds the zip
```

## Updating from a new edition of the guide

```bash
python3 tools/build.py "/path/to/Apply Claude.md"
```

The script splits the manuscript at its chapter headings. Figures are images in the manuscript, so the script replaces each with a text description from its `FIGURES` table; update that table when a figure changes. Then review `SKILL.md`: the index, the "core in brief" and the date in the section on changing facts are written by hand.

## Licence

The guide content is © 2026 Kai Stalmann, all rights reserved; you may use it as a skill but not republish it. The tooling is MIT. See `LICENSE`.
