# Chapter 9: Standardisation and Delegation

From the guide *Apply Claude* by Kai Stalmann, as of November 2026. Numbers in brackets such as (8.3) refer to sections of the guide; the index in SKILL.md says which file holds each chapter.

## 9.1 Reusable Work Instructions

Shows how prompt templates and skills define roles, rules, processes, examples and formats, and how plugins bundle them for sharing.

Anything that is repeated is recorded once: as a template, as a skill or bundled as a plugin. The three forms differ in terms of who triggers them and how far their scope extends.

| Form| Content| Effect| Suitable for
| :---:| :---:| :---:| :---:
| Prompt template| Task text with placeholders| The person inserts them or files them in the project instructions (8.3).| Individual, simple tasks
| Skill| Folder containing instructions (`SKILL.md`), plus examples, templates and scripts as required| Claude initially reads only the name and description and loads the rest as soon as a task matches.| Recurring processes with a fixed outcome
| Plugin| A bundle of skills, connectors and commands; in Cowork and Claude Code, this also includes agents and hooks| It is installed as a single unit. Paid plans.| Sharing within the team (11.2)

**Structure of a skill**

- **Name and description:** The description (maximum 200 characters) explains what the skill does and when it applies. Claude uses this to decide whether to invoke the skill.
- **Instructions:** These set out the role, rules and step-by-step procedure.
- **Examples and format:** Examples show the expected result; templates define its format.
- **Scripts:** These are optional and handle tasks that can be calculated.

**Paths to the skill**

| Path| Description
| :---:| :---:
| Ready to use| Skills from Anthropic generate Excel, Word, PowerPoint and PDF files. The Directory lists skills from partners such as Notion, Figma and Atlassian.
| Writing| A guide written in Markdown is sufficient; no programming is required.
| Recording| In Cowork on a Mac, Claude records your screen and voice for around 10 minutes and suggests a skill based on this (Pro, Max, Ultra and Team).

Skills are available on all plans. They require code execution to be enabled. The format is an open standard that can also be adopted by other tools.

**Rules**

- **One skill, one purpose:** several specialised skills work more reliably than a single ‘jack-of-all-trades’ skill.
- **Note the distinction:** project knowledge is available to every conversation within the project, whereas a skill is only loaded when needed and applies universally.
- **Testing:** A new skill is tested using several different tasks.
- **Check the source:** A skill may contain program code and load further code. Its files must be read before activation, even if it originates from colleagues (11.1).

## 9.2 Multi-stage and agent-based processes

Describes how chained prompts and agents are designed, coordinated and extended to agents working in parallel, and identifies their performance limits.

Anthropic advises choosing the simplest solution and only adding stages if they demonstrably improve the outcome. Multi-stage processes come at the cost of time and money to achieve better results.

Figure 9 as text: three forms, with cost and coordination effort increasing from first to last. Chain: step 1, check, step 2, check, step 3; a fixed sequence with checkable interim results. Agent with sub-agents: the main agent distributes work to sub-agents, each with its own context window, and brings the results together. Agent team: a lead session and several sessions share one task list and coordinate directly.

*Figure 9: Three forms of multi-stage processes. From left to right, the degree of autonomy increases, and with it the effort required.*

| Form| Working method| Suitable when| Price
| :---:| :---:| :---:| :---:
| Chain| Fixed sequence of tasks. Each processes the result of the previous one, with a check in between.| the task can be neatly broken down into fixed steps| Longer runtime
| Agent| Claude determines steps and tools itself.| The number and type of steps are unpredictable| Higher costs. Errors can propagate.
| Agent with sub-agents| The main agent distributes subtasks. Each sub-agent works in its own context window and reports back only the result.| Sub-tasks are independent or involve reviewing a large amount of material| Each sub-agent consumes additional tokens from the same quota.
| Team of agents| Multiple sessions with a leader and a shared task list coordinate directly with one another.| Participants are required to exchange findings and review each other’s work| Significantly higher consumption. In Claude Code, this is experimental and disabled by default.

In Chat and Cowork, Claude distributes such work itself. In Claude Code, sub-agents can be set up specifically (5.3).

**Design**

- **Start with the chain:** The most common pattern is to draft, check against criteria, and revise.
- **Separate the evaluator:** A separate step or sub-agent that merely reads the output assesses the result more independently than its creator.
- **Define the scope:** Each sub-agent receives a clear description and only the tools it needs.
- **Limit delegation:** Current models deploy sub-agents automatically, sometimes more frequently than necessary. The brief therefore specifies when they are appropriate: for parallel, mutually independent subtasks.

**Performance limits**

- **Dependent work:** For steps that build on one another, changes to the same file, and tasks with many dependencies, a single session works more effectively.
- **Error propagation:** An early error carries through to all subsequent steps. Anthropic recommends testing in an isolated environment and fixed guardrails (11.1).
- **Trust:** An agent runs through many steps without seeking confirmation. This presupposes that its result can be verified (2.1).

## 9.3 Recurring and long-running tasks

Covers schedules, repetitions and progress monitoring, as well as the benefits for personal work organisation.

A scheduled task is a saved instruction with a cycle. Claude executes it without further intervention and saves the result for review.

| Path| Interval| Execution| Note
| :---:| :---:| :---:| :---:
| Scheduled task in Cowork| Hourly, daily, weekly, on weekdays or on demand| In the cloud, even when the computer is switched off| Paid plans. Tasks that require local files or programs only run on your own computer.
| Cloud task in Claude Code| Freely selectable, at least hourly| In the cloud, with a fresh copy of the repository| In auto-mode by default (5.1)
| Desktop task in Claude Code| Freely selectable| On your own computer, which must be awake and have the app open| Access to local files
| `/loop` in Claude Code| From one minute| In the open session| Ends with the session, after seven days at the latest

**Set-up:** In Cowork, a single sentence specifying the task and frequency is sufficient, for example: “Every Monday at 9 am, summarise the previous week’s messages in my team’s channels”. Claude will ask for clarification, specify the name, schedule and content of the task, and schedule it once confirmed. The task uses the same connectors, skills and plugins as a standard session.

**Benefits for work organisation:** Anthropic cites typical uses such as daily briefings from messages, emails and appointments; weekly reports from connected sources; recurring research on topics or competitors; and organising files and status updates from project management tools.

**Progress monitoring**

- **Overview:** The ‘Scheduled’ view displays upcoming and past runs. Tasks can be modified, paused, resumed, deleted or executed immediately from there.
- **Each run is a separate session:** the result and work steps remain individually traceable.
- **Long tasks:** Cowork works on a task over a long period without the context window’s limit interrupting the run. The user describes the result and reviews it later.

**Rules**

- **Defining the result:** The task specifies the format, scope and storage location of the result so that runs can be compared.
- **Checking initial runs:** A new task initially runs on demand and only subsequently on a scheduled basis.
- **Restricting permissions:** Unsupervised runs are granted read-only access where possible. The approval mode is defined for each task (9.4).
- **Clean-up:** Tasks whose results are no longer being read are paused or deleted.

## 9.4 Working on the computer and in the browser

Shows how Claude works directly with files, programs and web pages via Cowork, Computer Use, Claude in Chrome and Claude Duet.

Claude interacts in four ways. The more directly it interacts with the screen, the slower, more error-prone and riskier the work becomes.

| Method| Activity| Availability| Special feature
| :---:| :---:| :---:| :---:
| Cowork| Carries out multi-step tasks with files, connectors and skills and delivers finished results| Paid plans. Desktop app, web and mobile. Web and mobile in Team as a beta, in Enterprise following approval by the owner| Sessions run in the cloud; in Team and Enterprise, they also run locally in the desktop app. Claude only deletes files with explicit permission.
| Claude in Chrome| Reads webpages, clicks and fills in forms| Paid plans. Google Chrome only; not on mobile devices| The sidebar runs as a Cowork session.
| Computer Use| Operates programs via screenshots, mouse clicks and keyboard| Beta. Pro, Max and Ultra. Desktop app for macOS and Windows; Claude Code in Terminal only on macOS| There is no isolation between Claude and the programs. Each program is authorised individually; trading and crypto platforms are blocked.
| Claude Duet| Acts as a constantly available assistant on its own computer in the cloud and gets in touch on its own initiative| Research Preview with a waiting list. Pro, Max and Ultra, available in the USA only| Asks for confirmation before sending, paying, signing and deleting

**Order of tools:** Cowork first selects a connector, then the browser, and only finally the screen control. Access via a connector takes seconds, whilst screen control takes considerably longer.

**Approval modes in Cowork**

| Mode| Behaviour
| :---:| :---:
| Manual| Claude pauses before actions and waits for confirmation. Default in Enterprise
| Automatic| Claude carries on, checks every action for security and blocks anything it classifies as unsafe. Default in Pro, Max, Ultra and Team
| No approvals| Claude does not ask for confirmation, and nothing checks the actions. Only to be used when there is complete trust in all sources involved

**Rules**

- **Choose the most precise method:** If you use a service frequently, integrate it as a connector rather than operating it via the screen (8.4).
- **What is visible is readable:** When using the computer, Claude sees everything on the screen. Confidential windows must be closed beforehand. Programs for banking, healthcare and government agencies are not authorised.
- **External content may contain instructions:** Websites, emails and files may contain hidden commands (prompt injection). According to Anthropic’s own statement, the security checks are not foolproof (11.1).
- **Supervision:** Get started with familiar programs and under supervision. A session can be stopped at any time.
