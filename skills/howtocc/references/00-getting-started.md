# Chapter 0: Getting Started

From the guide *Apply Claude* by Kai Stalmann, as of November 2026. Numbers in brackets such as (8.3) refer to sections of the guide; the index in SKILL.md says which file holds each chapter.

## 0.1 Access, Account and Pricing Plan

Explains where to find Claude, how to set up an account and payment, and what the free plan offers.

One account applies to all access points: the browser, desktop app and mobile app all display the same conversations. Getting started is free.

**Access methods**

| Access| Where to find it and how to set it up| Prerequisites
| :---:| :---:| :---:
| Browser| Visit claude.ai, no installation required| Account
| Desktop app for macOS| claude.ai/download, open the file, launch from the ‘Applications’ folder| macOS version 13 or later
| Desktop app for Windows| claude.ai/download, run the installation file, launch via the Start menu| Windows version 10 and later, versions for x64 and ARM64
| Desktop app for Linux (Beta)| Set up the Anthropic package repository, then `sudo apt install claude-desktop`; the commands can be found in the Claude Code documentation on the ‘Claude Desktop on Linux’ page| Ubuntu 22.04 or later, or Debian 12 or later
| Mobile app| App Store (iOS) or Google Play (Android)| Account

A browser is all you need for the chat; in paid plans, this also applies to Cowork. The desktop app comes into play as soon as you want Claude to run on your own computer: working with local files in Cowork, using desktop extensions, or using Claude Code without a terminal (0.2).

**Registration**

1. **Sign up:** On claude.ai or in an app, enter your email address or choose to sign up using your Google account.
2. **Confirm:** Open the sign-up link from the email. There is no password; any subsequent logins will be via the link or Google.
3. **Verify:** Enter your mobile number and the six-digit code from the text message.

You must be at least 18 years old, be based in a supported country (2.2) and have a mobile number from such a country. Landlines and internet telephony are not accepted. The number cannot be changed later and can be used to verify a maximum of three accounts.

**Free plan (Free)**

- **Included:** Chat with the Sonnet and Haiku model series, web search, file creation, artefacts, Memory, connectors, skills and up to five projects.
- **Not included:** Claude Code, Cowork, Research and the Opus and Fable model series (2.2).
- **Limit:** The quota is reset every five hours. Anthropic does not specify a fixed number of messages. The limit varies depending on system load and decreases during long conversations and when handling large files. Claude will notify you when the limit has been reached.

**Paid plan**

You can switch plans in the settings under ‘Billing’ or directly at claude.ai/upgrade: select a plan and enter your payment details. Pro and Team plans can be paid for monthly or annually; Max and Ultra plans are available on a monthly basis only.

| Point| Rule
| :---:| :---:
| Payment methods| On the web, Anthropic only accepts credit and debit cards. Those who sign up via the mobile app pay via the App Store or Google Play and manage their subscription there.
| Price| Pro costs 20 USD per month. The price is displayed in local currency where Anthropic supports it, with or excluding tax depending on the region. A comparison of all plans can be found in section 2.2.
| Term| The subscription renews automatically for one month or one year and can be cancelled at any time. Invoices can also be found under ‘Billing’.
| API| The API is billed separately via the Claude Console on a pay-as-you-go basis (10.2). Max, Ultra and Team include a monthly credit balance which must be used and expires at the end of the billing period (2.2).

The Free plan is sufficient for trying it out. A paid plan is worthwhile as soon as the limit disrupts your work or you need Claude Code and Cowork.

## 0.2 Installing Claude Code

Lists the requirements for Claude Code, describes the installation process on macOS, Windows and Linux, and shows how the running Claude application assists with this.

Claude Code is available in two ways: pre-installed in the ‘Code’ tab of the desktop app, or as the command `claude` in the terminal (the command line). The first method requires no separate installation, whilst the second offers the full range of features (5.1).

**Prerequisites**

| Prerequisite| Rule
| :---:| :---:
| Plan| Pro, Max, Ultra, Team or Enterprise; alternatively, an account with the Claude Console or a cloud provider offering pay-as-you-go billing. The Free plan is not sufficient.
| Operating system| macOS 13 or later, Windows 10 or later (version 1809), Ubuntu 20.04 or later, Debian 10 or later, or Alpine 3.19 or later
| Computer| 4 GB RAM, x64 or ARM64 processor, internet connection
| Git (version control)| Git is not mandatory. On Windows, Anthropic recommends ‘Git for Windows’ (git-scm.com), as Claude Code then uses the Bash shell instead of PowerShell. Git is required for separate working copies of parallel sessions (worktrees) and for uploading local projects to cloud sessions. Most Macs come with Git pre-installed; you can check this with `git --version`.
| Node.js| Node.js is not required. Only the alternative method via npm requires it, from version 22 onwards.

**Method 1: Desktop app.** Install the app and log in (0.1), open the ‘Code’ tab, select a project folder and enter your task. If the app prompts you to upgrade, you do not have a paid subscription.

**Method 2: Terminal**

| System| Open Terminal| Alternative to the installation command
| :---:| :---:| :---:
| macOS| Cmd + Space, type ‘Terminal’| `brew install --cask claude-code`
| Windows| Win + X, then ‘Terminal’ or ‘Windows PowerShell’| `winget install Anthropic.ClaudeCode`
| Linux and WSL (Linux on Windows)| Linux: usually Ctrl + Alt + T. WSL: open the installed Linux distribution| Repositories for apt, dnf and apk

The recommended installation command for macOS, Linux and WSL:

```
curl -fsSL https://claude.ai/install.sh | bash
```

The command for Windows PowerShell:

```
irm https://claude.ai/install.ps1 | iex
```

This is followed by three steps:

1. **Check:** Open a new terminal window. `claude --version` displays the version number; `claude doctor` provides a diagnostic report on the installation.
2. **Start:** Navigate to the project folder and enter `claude`.
3. **Log in:** The first session opens the browser to log in with your Claude account.

Four tips to save you the trouble of troubleshooting:

- **No progress visible:** The installation command does not display anything whilst loading. The window remains open until the success message appears.
- **Windows:** Administrator rights are not required. You can recognise PowerShell by the `PS` before the path. The older Command Prompt (CMD) requires a different command.
- **Updates:** The recommended installation updates itself automatically. With Homebrew, WinGet and the Linux package repositories, you can update manually.
- **Billing:** If an API key is stored on the computer in the variable `ANTHROPIC_API_KEY`, Claude Code can bill usage through it on a pay-as-you-go basis rather than via a subscription.

**Claude as an installation assistant**

- **In the chat, even with the free version:** Claude guides you through the steps, explains each command and interprets error messages. It cannot execute anything on your computer: you must copy the commands into the terminal yourself and copy error messages verbatim back into the chat.
- **Task for this:** “I’m using Windows 11 and have never used a terminal before. Guide me step by step through the installation of Claude Code, following the official instructions (code.claude.com/docs/en/setup). For each step, state a command and wait for my feedback.” The reference to the instructions is important because commands change and training knowledge becomes outdated (1.1).
- **In the ‘Code’ tab, with a paid subscription:** There, Claude executes commands directly on the computer. For example, it uses `git --version` to check whether Git is installed and, on request, sets up any missing components, including the `claude` command for the terminal. In the event of Git errors, Anthropic itself refers users to the help provided by Claude in Cowork.
- **For beginners:** Anthropic provides a guide for people with no terminal experience (code.claude.com/docs/en/terminal-guide).
