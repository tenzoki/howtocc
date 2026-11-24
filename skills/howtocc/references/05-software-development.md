# Chapter 5: Software Development

From the guide *Apply Claude* by Kai Stalmann, as of November 2026. Numbers in brackets such as (8.3) refer to sections of the guide; the index in SKILL.md says which file holds each chapter.

## 5.1 Setting up and exploring existing codebases

Describes the configuration of Claude Code and shows how it analyses the structure and interrelationships of existing systems.

Claude Code operates as an agent within the project folder: it reads files, modifies them and executes commands, such as tests and Git (version control). Unlike assistants that can only see the file that is currently open, it has an overview of the entire project.

**Set-up**

| Interface| Feature| Prerequisites
| :---:| :---:| :---:
| Terminal (command line)| Offers the full range of functions. A single installation command is sufficient (0.2), after which `claude` launches in the project folder.| Pro or higher; alternatively, an API account or cloud provider
| IDE (VS Code, Cursor, JetBrains)| Displays changes as a comparison in the editor.| same as Terminal
| Desktop app, ‘Code’ tab| Runs multiple sessions side by side and requires no separate installation.| paid plan
| Web and mobile| The session runs in the cloud. This is suitable for long tasks and for repositories (code repositories with version history) that are not available locally.| paid plan; for Enterprise, depending on the seat type

**Permissions:** New sessions in the terminal and in VS Code start in Auto mode. Claude then works without prompting, whilst a second model checks and pauses risky steps before execution, such as deployments to production. In manual mode, Claude prompts the user before almost every change, every shell command and every network access. In Plan mode, Claude reads files, executes commands to explore the code, makes no changes, and submits a plan for approval.

**Onboarding:** Claude reads the code itself at the start of each task. You only need to explain what isn’t in the repository.

- **From overview to workflow:** First ask about structure and architectural patterns, then about data models, then have it trace a workflow – for example, the login process from the user interface to the database.
- **Use technical terminology:** Questions phrased in the project’s terminology are more precise. Claude can create a glossary of these terms on request.
- **Offloading searches:** Claude delegates broad searches to a sub-agent (an auxiliary agent with its own context window), which simply reports back the result. In typed languages, a code intelligence plugin leads directly to the definition of a symbol.
- **Saving results:** `/init` generates an initial CLAUDE.md file from the codebase. This records what Claude would otherwise have to determine anew in every session (5.3).

## 5.2 Modification and Quality Assurance

Shows how new features, bug fixes and refactoring (restructuring without changing behaviour) are validated through tests, automated code review and security checks.

Claude completes a task as soon as the result appears to be ready. Only an executable test that reports ‘pass’ or ‘fail’ enables it to find and rectify its own errors.

Figure 5 as text: five stages. In the session: 1 Request and plan (human): state the goal, location and test criterion; approve larger changes as a plan first. 2 Change and check (Claude): edit files, run the check, read the error output, correct, until the check passes. 3 Cross-check (Claude and checking tools): a fresh context with no knowledge of the history, using /code-review and /security-review. At the pull request: 4 Check automatically: Code Review and CI. 5 Approve: a human decides.

*Figure 5: The path of a change from request to approval. Checks are carried out during the session and again at the pull request stage (the request to incorporate a change into the shared code).*

**Assignment by task**

| Task| Request| Review
| :---:| :---:| :---:
| Bug fixing| State the symptom, suspected location and command to reproduce the issue. First, have a test written that demonstrates the bug.| The test passes after the correction.
| New function| Refer to an existing pattern in the code and define the scope. For open requirements, Claude asks for clarification and draws up a specification.| Tests for normal and edge cases, review against the specification
| Refactoring| Rewrite in small, individually testable steps and require the same behaviour.| The existing tests continue to pass.

**Testing tools**

| Timing| Tool| Availability
| :---:| :---:| :---:
| During the change| Tests, type checking and linter (tool for style and error rules) for the project. The ‘security-guidance’ plugin allows Claude to check its own changes for common vulnerabilities.| Plugin from the Anthropic catalogue
| Before the pull request| `/code-review` checks the change in a fresh context. `/security-review` checks the branch once for security vulnerabilities.| `/code-review` available on all plans
| If required| The “Claude Security” plugin uses multiple agents to scan a repository or a change, checks each finding independently and suggests corrections.| paid plan or API access
| On the pull request| Code review: Several agents check the change; a further step filters out false positives, and the findings are displayed as comments on the line of code.| Team and Enterprise, GitHub only
| Ongoing| Claude Security monitors repositories as a managed service.| Enterprise, Public Beta

**Rules**

- **Require proof:** Display the command executed along with its output. The statement ‘all tests passed’ proves very little.
- **Narrow down the review:** Limit findings to correctness and exclude style. Anyone who implements every finding ends up with superfluous abstractions and tests for cases that never occur.
- **Approval remains with the human:** Code Review reads the code without executing it and does not approve any pull requests. A review with no findings does not prove the code is error-free.
- **Reset rather than fix:** `/rewind` reverts the code and conversation to an earlier state. It does not revert files that have only been changed by a shell command. After two failed corrections, a new session with a more precise brief leads to the goal more quickly (8.2).

## 5.3 Teamwork and the toolchain

Explains how teams establish common rules, extend Claude Code and integrate it into CI (automated testing and deployment pipelines).

Claude Code recognises two types of specifications. An instruction is read by the model and is generally followed. A configuration is enforced by Claude Code itself, regardless of what the model decides.

**Shared Rules**

| Means| Content| Binding nature
| :---:| :---:| :---:
| CLAUDE.md in the repository| Knowledge not contained in the code: commands for testing and type checking, conventions, pitfalls. The file loads into every session and therefore remains short – as a guideline, under 200 lines. Further rules can be found at `.claude/rules/` and are also loaded into every session. Rules marked with `paths` are loaded only when Claude reads or edits a relevant file.| Instruction
| Skills| Team workflows, such as releases or troubleshooting. Claude only loads their content when the task requires it (9.1).| Instruction
| Hooks| User-defined actions that Claude executes in response to specific events, usually a shell command: format after each edit, reject changes in protected folders, only allow completion after a successful type check.| enforced, with limits
| Prohibition rules and sandbox| Prohibitions apply in every mode, for example when reading files containing login credentials. The sandbox (isolated environment) restricts the file and network access of shell commands. On Windows, it is only available with WSL 2.| enforced
| Managed settings| Organisational policies that no personal setting can override (11.1).| enforced

Anything that allows no exceptions belongs in a hook or a prohibition rule; everything else goes in CLAUDE.md. The set of enforced rules remains small because each rule must be maintained and may occasionally be triggered incorrectly. Files in the repository apply to the whole team; personal guidelines are stored in `CLAUDE.local.md` or in your own user folder. If a repository already contains an AGENTS.md for other coding agents, Claude Code will read this as long as no CLAUDE.md is present.

**Limitations of hooks**

- **Only two types are enforced:** Hooks that execute a command or call a web service work reliably. Hooks of the types `prompt` and `agent` allow a model to decide and therefore remain a matter of discretion.
- **Errors are allowed to pass:** If a hook fails, for example due to an incorrect path or a timeout, the action continues regardless. Only the setting `onFailure: "block"` stops it. This setting is only available for hooks using a command or web service, and not for every event. It requires Claude Code version 2.1.295 or later.
- **Time limits terminate hooks:** By default, hooks using a command, web service or MCP tool abort after 10 minutes; model queries after 30 seconds; and sub-agents after 60 seconds. Shorter time limits apply to individual events, such as 30 seconds when submitting a job. The `timeout` field changes the value for each hook.
- **The process cannot be indefinitely delayed:** after eight consecutive blocks by default, Claude Code will still terminate the task.
- **Mods can override blocks:** a mod (a plugin with its own program code) can authorise a call that was previously blocked by a hook or a restriction rule. This applies to computers without managed settings and without logging in via a Team or Enterprise plan. An organisation can specifically authorise mods to override restriction rules.
- **Hooks themselves pose a risk:** command hooks run with the full privileges of the user account. In interactive sessions, they only start once the folder has been confirmed as trustworthy. In scripted mode, this prompt is omitted; hooks from an external repository run there without prompting.
- **The organisation takes precedence:** individual users cannot disable centrally defined hooks. Administrators can block all other hooks (11.1).

**Extension**

- **Integrating tools:** Claude utilises existing command-line tools directly, such as `gh` for GitHub. Systems without such tools, such as ticketing systems or error monitoring, are integrated via an MCP server (8.4).
- **Defining sub-agents:** A dedicated agent is provided only with the tools it needs, such as a reviewer with read-only access (9.2).
- **Distributing as a plugin:** A plugin bundles skills, sub-agents, hooks and MCP servers into a single installable unit. A marketplace (catalogue) distributes it, including internally (11.2).

**Integration into the toolchain**

| Method| Function
| :---:| :---:
| GitHub Actions, GitLab CI/CD| Claude Code runs within your own CI. On GitHub, it responds to `@claude` in issues and pull requests, implements changes and converts issues into pull requests.
| Script operation| `claude -p "task"` runs once and then terminates. Tools are authorised in advance; an upper limit on steps or costs restricts the run.
| Schedule and event| `/loop` repeats a job within the active session. Scheduled cloud tasks run without a dedicated computer (9.3).
| Parallel sessions| Worktrees (separate working copies for each branch) prevent sessions from overwriting one another.

Before every unattended run, five questions must be clarified: Does the run know its acceptance criteria? Can it check the result itself? What is it permitted to change? What stops it? Who approves the result?
