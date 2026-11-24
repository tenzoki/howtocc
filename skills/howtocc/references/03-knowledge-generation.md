# Chapter 3: Knowledge Generation

From the guide *Apply Claude* by Kai Stalmann, as of November 2026. Numbers in brackets such as (8.3) refer to sections of the guide; the index in SKILL.md says which file holds each chapter.

## 3.1 Research and Synthesis of Sources

Describes how information from the web, documents and connected services can be collected, summarised and cited.

**Ways to access sources**

| Path| Function| Conditions and limitations
| :---:| :---:| :---:
| Web search| Whilst providing an answer, Claude searches the web and supports the answer with source references. It reads a specified web address in full.| All plans. In Team and Enterprise, the owner authorises web searches. Long pages take up a lot of space in the context window.
| Research| Claude carries out a series of interlinked searches, tracks open questions and incorporates enabled connectors, such as email, calendar and document storage.| Paid subscription plans; web search must be enabled. Research runs independently of the selected model on Opus and uses up the quota more quickly. In the mobile app, it only searches the web.
| Own documents| Uploaded files or a project’s knowledge base serve as the source.| Up to 20 files per chat. PDFs up to 1,000 pages. If a PDF has more than 100 pages, Claude only reads the text.
| Connected services| Connectors open storage systems and specialist systems (8.4). In Team and Enterprise, the organisation-wide search scans all connected sources.| The connector must be switched on for the conversation.

**Summarise and provide evidence**

- **State the purpose:** A summary requires a target audience, length and specific question; otherwise, Claude summarises at its own discretion.
- **Quote first, then draw conclusions:** For long documents, Claude first extracts the relevant passages verbatim and bases the summary solely on these.
- **Narrow down the material:** The instruction to use only the attached documents ensures that training-based knowledge is excluded from the response.
- **Require evidence:** Every statement must be accompanied by a source reference. Statements without a source reference should be deleted.

It remains necessary to check the sources in their original form (2.1).

## 3.2 Data and document analysis

Shows how data and documents are analysed and presented as tables, diagrams or dashboards.

**Input**

Claude reads PDF, Word, Excel, CSV, text, HTML and JSON, as well as images (JPEG, PNG, GIF, WebP), with a limit of 500 MB per file in chat. For code execution, there is a limit of 30 MB per file; however, Claude can still process larger PDFs. For documents other than PDFs, it extracts only the text; embedded images are not read. Excel files require code execution to be enabled.

**Analysis**

To carry out the analysis, Claude writes program code and executes it in a sandboxed environment. Key metrics are thus calculated rather than formulated, and the calculation process can be viewed. Typical tasks include: transferring data from reports into a table, comparing versions of a document, searching for anomalies in data series, and cleaning and merging data.

**Output formats**

| Format| Feature| Availability
| :---:| :---:| :---:
| Table or text in chat| Fastest format, linked to the conversation| All pricing plans
| Chart in chat| Interactive but ephemeral: it is not saved, but can be copied as an image, downloaded or saved as an artefact.| Beta; web and desktop, not available in the mobile apps
| File| Excel with working formulas, Word, PowerPoint or PDF for download| all plans
| Artifact| Remains preserved, can be edited further and shared (4.3)| all plans
| Dashboard| Displays continuously updated data from connected platforms such as Salesforce; Claude writes the queries.| Beta, from Pro onwards

Spot checks against the source file reveal reading errors, particularly in scanned pages and nested tables.

## 3.3 Comparison, evaluation and preparation for decision-making

Explains how options are compared according to defined criteria and validated through a critical cross-check.

Figure 4 as text: four steps alternating between human and Claude. 1 (human) Set the question and criteria: options, criteria, weights. 2 (Claude) Rate the options per criterion: a table with evidence and assumptions. 3 (Claude) Cross-check the result: strongest objections, missing information. 4 (human) Weigh up and decide; responsibility stays here. Steps 2 and 3 repeat if new objections arise.

*Figure 4: Division of labour in decision-making preparation. Claude evaluates and checks; the human sets the criteria and makes the decision.*

- **Criteria first:** Without predefined criteria and weightings, Claude selects both itself, and the result cannot be verified.
- **Withhold personal preference:** Whoever names the preferred option is more likely to receive agreement than disagreement (7.1).
- **Identify gaps:** The assessment specifies the evidence or assumption for each cell and highlights where information is missing.
- **Separate cross-checking:** The task ‘Name the strongest objections to this recommendation’ works best in a new conversation that is only aware of the result.
- **Increase the cognitive effort:** For questions with far-reaching consequences it is worth investing more cognitive effort (2.2).

For the presentation, it is sufficient to request a side-by-side comparison. Claude provides this as a table or an interactive view.

## 3.4 Education: Learning and Teaching

Describes its use in education: learners have material explained to them and practise it, whilst teachers develop curricula and assess performance.

Anthropic has analysed how students and teachers at universities use Claude. The two reports were published in 2025 and are based on accounts with university email addresses.

| Role| Most common uses| Recommended working methods
| :---:| :---:| :---:
| Learners| Creating and improving learning materials, such as practice questions, summaries and text revision (39 per cent); explanations and solutions to exercises (34 per cent); analysing and presenting data (11 per cent)| Get explanations rather than solutions: request practice questions, have your own text assessed paragraph by paragraph, and work through the solution yourself.
| Teachers| Developing curricula and course materials (57 per cent), conducting one’s own research (13 per cent), assessing performance (7 per cent)| Draw on one’s own subject expertise, design tasks that require independent thinking, and do not accept assessments without checking them first.

**Learning mode:** Claude responds like a tutor, asking questions rather than providing the solution. This is described for Claude for Education, the university-wide subscription. Claude for Teachers is available free of charge to verified teaching staff at US schools.

**Two risks:** Two of the four usage patterns among students, which occur with roughly equal frequency, focus directly on the solution or the final result. Anthropic describes examples of this as concerning and raises questions regarding the development of critical thinking. In just under half of the conversations regarding assessment, teachers largely left the task to the model, even though 22 surveyed university teachers considered AI to be least suitable for this very purpose.

## 3.5 Academic Research

Covers literature reviews, data analysis and hypothesis formulation, as well as the methodological limitations of its use.

| Work step| Support| Limitation
| :---:| :---:| :---:
| Literature review| Research identifies and synthesises sources (3.1). Claude Science searches scientific literature via connectors, and a skill helps to find, verify and consolidate papers.| Sources may be fabricated or misrepresented (2.1). Each paper must be checked against the original. Licensed literature requires its own access details.
| Hypotheses and experimental design| Claude develops hypotheses, refines the experimental design and methodology section, and identifies objections.| A plausible hypothesis is not substantiated. Only a literature review will reveal whether it is novel.
| Data analysis| Claude writes and runs code, for example in Python; in Claude Science, also in R. Claude Science saves results as versioned artefacts with provenance records and offloads complex calculations to its own computing clusters.| The reviewer, a background verification agent, compares statements with the execution log but does not perform the calculations itself. It reduces errors but does not eliminate them.
| Writing| Claude drafts manuscripts, grant applications and responses to peer reviews (4.2).| Responsibility for content and labelling lies with the authors.

**Claude Science** is a standalone desktop application (beta, available from the Pro plan onwards; in Team and Enterprise plans subject to approval by the owner) for macOS, Windows and Linux. The files remain on your own computer. Each new folder, network destination and off-site calculation must be authorised individually. The application is not limited to the life sciences and is not intended for clinical or diagnostic purposes.

**Methodological rule:** Anthropic requires results to be verified before they are incorporated into research, publications or subsequent decisions. An evaluation can only be verified via code and log; it cannot be verified via a chat response, which may differ when repeated (1.1).
