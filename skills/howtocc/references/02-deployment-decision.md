# Chapter 2: Decision on deployment

From the guide *Apply Claude* by Kai Stalmann, as of November 2026. Numbers in brackets such as (8.3) refer to sections of the guide; the index in SKILL.md says which file holds each chapter.

## 2.1 Suitability for tasks and limits of reliability

Identifies where results become unreliable and what Claude does not generate (such as photos, illustrations and realistic videos), and demonstrates how to work within these limits.

**Limits of Reliability**

Anthropic advises never to use Claude as the sole source and to verify information with significant implications. Five types of error are documented:

| Error type| How it manifests itself| Countermeasure
| :---:| :---:| :---:
| Fabricated information (hallucination)| Facts, figures and quotations sound convincing but are unsubstantiated.| Provide sources, require verbatim citations and explicitly allow the answer ‘I don’t know’.
| Outdated information| Events after June 2026 are missing or incorrectly categorised.| Enable web search or provide up-to-date documents.
| Abridged web sources| The summary omits contextual information from the original page, and its quality depends on the sources found.| Open the cited sources before reusing any information.
| Alleged actions| Claude provides links that do not work, or reports an email as having been sent when it was never sent.| Check the result at its intended destination: in the inbox, in the document, in the service.
| Inaccurate image interpretation| Counts and location details in images are approximations. Small, rotated and blurred images lead to errors.| Cross-check image analyses. Claude does not name individuals, does not recognise AI-generated images and does not replace the interpretation of CT or MRI scans.

Added to this are the effects of lengthy conversations and varying phrasing (1.1). If the answer to the same question differs in content on the second attempt, this is a warning sign.

**Level of scrutiny depending on the task**

Two questions determine how thoroughly a result should be checked: Is an error apparent, and what is the cost of that error?

Figure 3 as text: a two-by-two matrix. Axes: "What does an error cost?" (little or a lot) and "Is an error noticed?" (at once or hardly).
- Costs little, noticed at once: use freely. Ideas, outlines and drafts; rewording for your own use; explanations as an introduction to a topic.
- Costs little, hardly noticed: use, check samples. Summaries of long documents; research overviews for orientation; sorting and tagging large volumes.
- Costs a lot, noticed at once: use, check the result in full. Program code that can be tested; analyses that can be recalculated; texts that are read before sending.
- Costs a lot, hardly noticed (the top-right box): only with evidence and expert review. Legal, health and financial questions in individual cases; facts and quotations without a source to hand.

*Figure 3: Level of scrutiny based on the detectability and consequences of an error, with typical tasks for each field.*

If the subject-specific check is missing in the top-right box, the task is not suitable for Claude.

**Media**

| Medium| Possible| Not possible
| :---:| :---:| :---:
| Image| Diagrams, vector graphics (SVG), layouts and graphics calculated via code| Photos and illustrations. For image processing, there are connectors to design tools such as Adobe.
| Video| Animations generated from code using Claude Motion (Beta)| Realistic footage and people
| Audio| Spoken responses in voice mode using pre-defined voices| Voice clones. There is no documented service for generating audio freely.
| Input| Text, images and documents| Video and audio files are not documented as input.

## 2.2 Access requirements

Compares tariffs, user interfaces, models, default settings and regional availability as a basis for choosing the right package.

**Pricing plans**

Prices are quoted in US dollars per month, excluding tax (as at 5 November 2026). The plans up to Ultra each specify what is included in addition to the previous plan. The Team plan builds on the Pro plan, not the Ultra plan.

| Plan| Price| Usage volume| Intended for| Includes
| :---:| :---:| :---:| :---:| :---:
| Free| 0| limited| Trying it out| Chat with Sonnet and Haiku, web search, file creation, Memory, connectors, skills, artefacts, up to 5 projects
| Pro| 20 (17 with annual payment)| Reference| daily work| Opus, Research, Claude Code, Cowork and scheduled tasks, Claude in Chrome, Microsoft 365, Claude Science; Fable against usage credits (purchased allowance)
| Max| 100| 5 times the Pro allowance| full-day work| Fable up to half the weekly limit, priority during peak usage, 100 USD API credit
| Ultra| 200| 10 times the Pro allowance per week| long-running tasks| no 5-hour limit for automatically verified accounts, 200 USD API credit
| Team| 25 per seat (20 with annual payment); Premium seat 125 (100)| more than Pro; Premium seat: 5 times the Standard seat| teams of 2 to 150 people| central billing and management, spending limits, single sign-on (SSO), shared projects, organisation-wide search, Claude Tag, Claude Motion, API credits (US$20 per Standard seat, US$100 per Premium seat, up to a maximum of US$500)
| Enterprise| 20 per seat plus usage at API rates, from 20 seats| based on usage| large organisations| roles and permissions, audit logs, retention policies, Claude Security
| Education, Government| on request| | universities, US government agencies| see 6.4

**Usage limits**

The quota is subject to two limits: a session limit, which resets five hours after the first message, and a weekly limit. Chat, the desktop app and Claude Code all draw on the same quota. Usage increases with the length of the conversation, the size of the files, the model selected and the computational effort required. The current status is shown in the ‘Usage’ settings. Anthropic reserves the right to adjust the limits.

**Model and computational effort**

| Model series| Suitability| Available from
| :---:| :---:| :---:
| Haiku| quick, simple and frequent tasks| Free
| Sonnet| everyday tasks: texts, data analysis, code| Free
| Opus| complex and long-running tasks| Pro
| Fable| highest performance for multi-stage research and agent runs lasting hours| Pro (credit-based), Max (included)

The current versions are Haiku 5.5, Sonnet 5.5, Opus 5.5 and Fable 5.1. The computational effort has up to five levels. Low and Medium are sufficient for routine tasks and conserve the quota, whilst High offers the best balance of quality and speed. ‘Extra High’ is intended for long-running programming and agent tasks, whilst ‘Maximum’ is for the most difficult tasks where accuracy is paramount. The menu next to the send button highlights the recommended level as the default setting. The model and level can be changed whilst the conversation is in progress.

**Interfaces**

The chat runs in all plans via the browser, in the desktop app (macOS and Windows; Linux as a beta) and in the apps for iOS and Android. Cowork runs in the paid plans via the desktop app, the browser and the mobile apps. In the browser and on mobile, it is in beta for the Team plan and, for the Enterprise plan, is only available once authorised by the owner. For files on your own computer and for Computer Use, Cowork requires the desktop app (9.4). Desktop extensions are only available in the desktop app. Claude Code also works in the terminal and in the development environment (5.1).

**Basic settings**

| Setting| Effect| Further details
| :---:| :---:| :---:
| Model improvement (data protection)| Specifies, within the individual plans, whether chats are used to train the models. Regardless of this, feedback via the thumbs buttons and conversations flagged for security checks may be included in the training. Team and Enterprise exclude training by default. Incognito chats remain excluded even when this setting is enabled.| 11.1
| Personal instructions| Apply to every conversation, for example regarding language, form of address and format.| 8.3
| Memory| Determines whether Claude retains content from previous conversations.| 8.3
| Web search, code execution, connectors| Unlock capabilities, but take up space in the context window (1.1). In Team and Enterprise, the organisation decides on authorisation.| 3.1, 4.3, 8.4

**Regional availability**

Anthropic offers its products only in listed countries, including all 27 EU member states. The person’s location and the organisation’s registered office are decisive. Individual products differ: Claude Duet is available only in the USA, and Claude in Microsoft Copilot is disabled by default in the EU, EFTA and the United Kingdom, with an exception for Word, Excel and PowerPoint (10.1).
