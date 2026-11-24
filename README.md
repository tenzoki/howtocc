# howtocc

A Claude Code plugin with one skill that answers what Claude can and cannot do, and which building block, plan or working method fits a task. It is built from the guide *Apply Claude: Fundamentals, fields of application, and working models* by Kai Stalmann (November 2026).

## Install

**Claude Code.** Run these two commands inside Claude Code:

```bash
/plugin marketplace add tenzoki/claude-plugins
/plugin install howtocc@tenzoki-plugins
```

Then run `/reload-plugins` or start a new session. `/howtocc:howtocc` should now appear when you type `/howto`.

**Claude apps (chat and Cowork).**

1. Run `python3 tools/build.py`. It writes `dist/howtocc.zip`.
2. In Claude, open Settings, then Capabilities, then Skills, upload the zip and switch the skill on.

Skills need code execution to be enabled. The folder `skills/howtocc/` is a plain skill in the open Agent Skills format, so it also works copied to `~/.claude/skills/howtocc/` without the plugin.

## Use

There are two ways to use it, and both work in any project folder.

**Just ask.** Put a question about Claude in plain words, in any language. Claude recognises the topic and loads the skill by itself:

```
Can Claude read a 600-page PDF?
Should this be a project, a skill or a connector?
Which plan includes Cowork and Claude Code?
```

**Call it by name.** Type the command followed by your question. Use this when you want to be sure the answer comes from the guide and not from Claude's general knowledge:

```
/howtocc:howtocc Why is my result so generic, and how do I fix the prompt?
/howtocc:howtocc Was passiert mit meinen Daten im Team-Plan?
```

In the Claude apps there is no command; ask the question, or write "use the howtocc skill" in front of it.

### What you get back

- **A direct answer first:** yes, no, or which option, followed by the condition that matters (plan, platform, beta status, a setting that must be on).
- **The limit along with the capability:** for example that web summaries need the sources opened before you reuse the information.
- **A section number** such as "(section 8.3)", so you can read further in the guide.
- **Dates on facts that change:** prices, usage limits, model versions and beta labels are given "as of November 2026". Where a decision depends on one of them and web search is available, Claude checks the current Anthropic page and tells you if the guide is out of date.
- **A plain statement when the guide does not cover the question,** with the rest of the answer marked as not from the guide.

### Questions it handles well

| You want to know | Example |
|---|---|
| Whether Claude can do something | "Can Claude generate images or video?" |
| Which building block to use | "I do the same report every Monday. Skill, project or scheduled task?" |
| What a plan includes or costs | "What do I get with Max that Pro does not have?" |
| How far to trust a result | "How much do I need to check a contract summary?" |
| Why a result is poor | "Claude keeps suggesting changes but does not make them." |
| How to give Claude your knowledge | "What is the difference between Memory and project instructions?" |
| How to work with code | "How do I make Claude Code run the formatter after every edit?" |
| What is safe to delegate | "Can I let Cowork send emails without asking me?" |
| What happens to your data | "Are my chats used for training?" |
| How to get started | "How do I install Claude Code on Windows?" |

### Keeping it current

```bash
/plugin marketplace update tenzoki-plugins
```

This fetches a new version when the guide has been revised. To remove the plugin, run `/plugin uninstall howtocc@tenzoki-plugins`.

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
