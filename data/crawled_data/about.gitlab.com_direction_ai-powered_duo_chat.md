#  Category Direction - GitLab Duo Chat 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Stage Direction - AI-powered](https://about.gitlab.com/direction/ai-powered/)
  4. Category Direction - GitLab Duo Chat


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
## On this page
  * [GitLab Duo Chat](https://about.gitlab.com/direction/ai-powered/duo_chat/#gitlab-duo-chat)
    * [Introduction and how you can help](https://about.gitlab.com/direction/ai-powered/duo_chat/#introduction-and-how-you-can-help)
    * [Overview](https://about.gitlab.com/direction/ai-powered/duo_chat/#overview)
    * [Strategy and Themes](https://about.gitlab.com/direction/ai-powered/duo_chat/#strategy-and-themes)
    * [1 year plan](https://about.gitlab.com/direction/ai-powered/duo_chat/#1-year-plan)
      * [What is next for us](https://about.gitlab.com/direction/ai-powered/duo_chat/#what-is-next-for-us)
      * [What we are currently working on](https://about.gitlab.com/direction/ai-powered/duo_chat/#what-we-are-currently-working-on)
      * [What we recently completed](https://about.gitlab.com/direction/ai-powered/duo_chat/#what-we-recently-completed)
      * [What is Not Planned Right Now](https://about.gitlab.com/direction/ai-powered/duo_chat/#what-is-not-planned-right-now)
    * [Best in Class Landscape](https://about.gitlab.com/direction/ai-powered/duo_chat/#best-in-class-landscape)
      * [Key Capabilities](https://about.gitlab.com/direction/ai-powered/duo_chat/#key-capabilities)
      * [Roadmap](https://about.gitlab.com/direction/ai-powered/duo_chat/#roadmap)
      * [Top Competitive Solutions](https://about.gitlab.com/direction/ai-powered/duo_chat/#top-competitive-solutions)
    * [Target Audience](https://about.gitlab.com/direction/ai-powered/duo_chat/#target-audience)
    * [Pricing and Packaging](https://about.gitlab.com/direction/ai-powered/duo_chat/#pricing-and-packaging)
    * [Analyst Landscape](https://about.gitlab.com/direction/ai-powered/duo_chat/#analyst-landscape)


## GitLab Duo Chat[](https://about.gitlab.com/direction/ai-powered/duo_chat/#gitlab-duo-chat)
|   
---|---  
Stage | [AI-powered](https://about.gitlab.com/direction/ai-powered/)  
Group | [Duo Chat](https://about.gitlab.com/direction/ai-powered/duo_chat)  
Maturity | [Available](https://about.gitlab.com/direction/#maturity)  
Content Last Reviewed | `2024-10-05`  
### Introduction and how you can help[](https://about.gitlab.com/direction/ai-powered/duo_chat/#introduction-and-how-you-can-help)
Thanks for visiting this category direction page on GitLab Duo Chat. This page belongs to the [Duo Chat group](https://handbook.gitlab.com/handbook/engineering/development/data-science/ai-powered/duo-chat/) of the AI-powered stage and is maintained by [Dasha Adushkina](https://gitlab.com/dashaadu) (email).
This direction page is a work in progress, and everyone can contribute to our vision, architecture, and designs by commenting on the epic for the [GitLab Duo Chat](https://gitlab.com/groups/gitlab-org/-/epics/10219) and its sub-epics and issues.
  * Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
  * Alternatively, feel free to share feedback directly via email, or on a video call. If you're a GitLab user and have direct knowledge of your need for AI support, we'd especially love to hear from you.


### Overview[](https://about.gitlab.com/direction/ai-powered/duo_chat/#overview)
The recent advent of very capable large language models presents an opportunity to improve the way users interact with data. It is now possible to employ such AI models to let users interactively explore data via natural language.
The vision: GitLab Duo Chat is a conversational AI assistant that simplifies tasks and reducing context switches to empower users to achieve their DevSecOps goals faster and streamlined.
Initially, Chat will be limited in the types of queries it can answer. Long-term we intend for Chat to also be able to carry out tasks for the user.
### Strategy and Themes[](https://about.gitlab.com/direction/ai-powered/duo_chat/#strategy-and-themes)
Let's face it DevSecOps tasks are hard and complex. Understanding code that others have written, comprehending reported vulnerabilities, reading through tons of comments, understanding why a pipeline failed. And this is just the beginning, ultimately one wants to contribute to such code, fix the vulnerability, draw conclusions from the comments, and fix the pipeline.
Yes, such work is being done every day by developers, security professionals, product managers, and all the other personas that work in the DevSecOps space. However, they could do all these tasks much more efficiently and with less context switching with the help of AI.
GitLab Duo Chat aims to do just that and is a cornerstone in our [FY25 Investment theme to make DevSecOps more efficient with AI](https://about.gitlab.com/direction/#enable-aiml-efficiencies-across-devsecops).
Our Duo Chat strategy is to assist users with AI in ideation and creation tasks as well as in learning tasks across the entire Software Development Lifecycle (SDLC) to make them faster and more efficient.
We aim to employ the Chat for all use cases and workflows that can benefit from a conversational interaction between a user and an AI that is driven by a large language model (LLM). Typically, these are:
  * Complex creation and learning tasks that are more effectively and more efficiently solved through iteration than through a one-shot interaction.
  * Tasks that are typically satisfiable with one-shot interactions but that might need refinement or could turn into a conversation.
  * Among the latter are tasks where the AI may not get it right the first time but where users can easily course correct by telling the AI more precisely what they need. For instance, "Explain this code" is a common question that most of the time would result in a satisfying answer, but sometimes the user will have additional questions.
  * Tasks that benefit from the history of a conversation, so neither the user nor the AI need to repeat themselves.


The Chat shall be context aware and ultimately have access to all the resources in GitLab that the user has access to. Initially, this context is limited to code files, code selections, the content of individual issues and epics, as well as the GitLab documentation.
To scale the context awareness and the supported use cases across the entire DevSecOps domain, Duo Chat aims to be a platform, that other GitLab teams and the wider community can contribute to. They are the experts for the use cases and workflows to accelerate.
### 1 year plan[](https://about.gitlab.com/direction/ai-powered/duo_chat/#1-year-plan)
Over the next 12 months, we will focus on the following prioritized themes, which represent broad categories of user needs that evolve as the market and our product mature. While these themes may extend beyond the 12-month horizon, we will continuously iterate and deliver improvements within each theme:
  * Support use cases that require automatically fetching relevant content. The initial use case is [chatting with your code base](https://gitlab.com/groups/gitlab-org/-/epics/16910).
  * Enabling custom rules that applied for every conversation starting with supporting [custom style guides for Duo Chat](https://gitlab.com/gitlab-org/gitlab/-/issues/481841).
  * Support use cases that require access to multiple GitLab resources starting with [enabling the planner persona to create status updates for work items in Duo Chat](https://gitlab.com/groups/gitlab-org/-/epics/16695).


#### What is next for us[](https://about.gitlab.com/direction/ai-powered/duo_chat/#what-is-next-for-us)
  * [GitLab Duo Chat on GitLab Duo Agent Platform for more context, better answers, editing capabilities](https://gitlab.com/groups/gitlab-org/-/epics/17182)
  * [Provide means for users to add context to their chat conversations](https://gitlab.com/groups/gitlab-org/-/epics/15181)
  * [Observability and Stability initiative for Duo Chat](https://gitlab.com/groups/gitlab-org/-/epics/16125)
  * [Multi-threaded conversations in the chat](https://gitlab.com/groups/gitlab-org/-/epics/11449)
  * [Evaluate the quality of answers to follow-up questions and potentially improve the experience with conversations](https://gitlab.com/groups/gitlab-org/modelops/ai-model-validation-and-research/ai-evaluation/-/epics/33)


#### What we are currently working on[](https://about.gitlab.com/direction/ai-powered/duo_chat/#what-we-are-currently-working-on)
  * [Planning issue for GitLab Duo Chat 17.10](https://gitlab.com/gitlab-org/ai-powered/duo-chat/planning/-/issues/11)


#### What we recently completed[](https://about.gitlab.com/direction/ai-powered/duo_chat/#what-we-recently-completed)
  * [Experimental release of Gitlab Duo Agentic Chat](https://about.gitlab.com/blog/gitlab-duo-chat-gets-agentic-ai-makeover/) (29 May 2025)
  * [GitLab Duo Core: Duo Chat in IDEs available for free to users on Ultimate or Premium plan](https://docs.gitlab.com/subscriptions/subscription-add-ons/#gitlab-duo-core) (18.0)
  * [Llama 3 models generally available for GitLab Duo Chat and Code Suggestions](https://about.gitlab.com/releases/2025/04/17/gitlab-17-11-released/#llama-3-models-generally-available-for-gitlab-duo-chat-and-code-suggestions) (17.11)
  * [GitLab Duo Chat now uses Anthropic Claude Sonnet 3.7](https://about.gitlab.com/releases/2025/04/17/gitlab-17-11-released/#gitlab-duo-chat-now-uses-anthropic-claude-sonnet-37) (17.11)
  * [Manage multiple conversations in GitLab Duo Chat in the GitLab web application](https://about.gitlab.com/releases/2025/04/17/gitlab-17-11-released/#manage-multiple-conversations-in-gitlab-duo-chat) (17.11)
  * [GitLab Eclipse plugin available in beta](https://about.gitlab.com/releases/2025/04/17/gitlab-17-11-released/#gitlab-eclipse-plugin-available-in-beta) (17.11)
  * [GitLab Duo Chat is now resizable](https://about.gitlab.com/releases/2025/03/20/gitlab-17-10-released/#gitlab-duo-chat-is-now-resizable) (17.10)
  * [New insights into GitLab Duo Code Suggestions and GitLab Duo Chat trends](https://about.gitlab.com/releases/2025/03/20/gitlab-17-10-released/#new-insights-into-gitlab-duo-code-suggestions-and-gitlab-duo-chat-trends) (17.10)
  * [Select models for AI-powered features on GitLab Duo Self-Hosted](https://about.gitlab.com/releases/2025/03/20/gitlab-17-10-released/#select-models-for-ai-powered-features-on-gitlab-duo-self-hosted) (17.10)
  * [Add project files to Duo Chat in VS Code and JetBrains IDEs](https://gitlab.com/groups/gitlab-org/-/epics/15183) (rolled out to .com; expected (but not committed) to be released in 17.10)
  * [Chat can be resized in the GitLab UI to help users interact with chat and page content at the same time](https://gitlab.com/gitlab-org/gitlab/-/issues/499849) (rolled out to .com; expected (but not committed) to be released in 17.10)
  * [New /help command in GitLab Duo Chat](https://gitlab.com/gitlab-org/gitlab/-/issues/462122) (17.7)
  * [Slash commands picker in GitLab UI shows relevant commands only depending on the page](https://gitlab.com/groups/gitlab-org/-/epics/15371) (17.7)
  * [Use self-hosted model for GitLab Duo Chat](https://gitlab.com/gitlab-org/gitlab/-/issues/501267) (17.6)
  * [Have a conversation with GitLab Duo Chat about your pipeline job](https://gitlab.com/gitlab-org/gitlab/-/issues/468461) (17.6)
  * [Have a conversation with GitLab Duo Chat about your commit](https://gitlab.com/gitlab-org/gitlab/-/issues/468460) (17.6)
  * [AI Impact Analytics API for GitLab Duo Pro including Chat usage](https://gitlab.com/gitlab-org/gitlab/-/issues/498497#release-notes) (17.6)
  * [Query user-level GitLab Duo Enterprise usage metrics including Chat usage](https://gitlab.com/gitlab-org/gitlab/-/issues/483049#release-notes) (17.6)
  * [Have a conversation with GitLab Duo Chat about your merge request](https://gitlab.com/gitlab-org/gitlab/-/issues/464587) (17.5)
  * [Duo Quick Chat: operates directly on the lines you’re editing](https://gitlab.com/groups/gitlab-org/-/epics/15218) (17.5)
  * [Summarize issue discussions with GitLab Duo Chat](https://gitlab.com/gitlab-org/gitlab/-/issues/454550) (17.4)
  * [Troubleshoot failed jobs with root cause analysis](https://gitlab.com/groups/gitlab-org/-/epics/13080) (17.3)
  * [Gitlab Duo (including Duo Chat) disabling input and output logging by default](https://about.gitlab.com/releases/2024/07/18/gitlab-17-2-released/#gitlab-duo-disabling-input-and-output-logging-by-default) (17.2)
  * [Vulnerability Explanation](https://gitlab.com/groups/gitlab-org/-/epics/10642) (17.2)
  * [GitLab Duo Chat and Code Suggestions available in workspaces](https://gitlab.com/groups/gitlab-org/-/epics/12780) (17.2)
  * [Moving chat from Anthropic Claude Sonnet 3 to 3.5](https://gitlab.com/gitlab-org/gitlab/-/issues/468936) (17.2)
  * [Moving chat from Anthropic Claude 2.1 to Claude Sonnet 3](https://gitlab.com/gitlab-org/gitlab/-/issues/444629) (17.0)
  * [How-to questions in GitLab Duo Chat supported on self-managed deployments](https://gitlab.com/gitlab-org/gitlab/-/issues/451215) (17.0)
  * [GitLab Duo Chat GA release](https://gitlab.com/groups/gitlab-org/-/epics/13516) (16.11)
  * [GitLab Duo Chat available in JetBrains IDEs](https://gitlab.com/gitlab-org/editor-extensions/gitlab-jetbrains-plugin/-/issues/307) (16.11)


#### What is Not Planned Right Now[](https://about.gitlab.com/direction/ai-powered/duo_chat/#what-is-not-planned-right-now)
More details soon.
### Best in Class Landscape[](https://about.gitlab.com/direction/ai-powered/duo_chat/#best-in-class-landscape)
Details coming soon.
#### Key Capabilities[](https://about.gitlab.com/direction/ai-powered/duo_chat/#key-capabilities)
Details coming soon.
#### Roadmap[](https://about.gitlab.com/direction/ai-powered/duo_chat/#roadmap)
Details coming soon.
#### Top Competitive Solutions[](https://about.gitlab.com/direction/ai-powered/duo_chat/#top-competitive-solutions)
Competitors in the space include Android Studio Bot, GitHub Copilot Chat, Tabnine Chat, and Sourcegraph Cody AI Assistant.
### Target Audience[](https://about.gitlab.com/direction/ai-powered/duo_chat/#target-audience)
GitLab Duo Chat aims to support across all there DevSecOps workflows. Therefore, all of GitLab's users are a target audience for the Chat. The initial focus is however on:
  1. [Sasha, Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
  2. [Parker, Product Manager](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager)
  3. [Delaney, Development Team Lead](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)
  4. [Simone, Software Engineer in Test](https://handbook.gitlab.com/handbook/product/personas/#simone-software-engineer-in-test)
  5. [Amy, Application Security Engineer](https://handbook.gitlab.com/handbook/product/personas/#amy-application-security-engineer)
  6. [Alex, Security Operations Engineer](https://handbook.gitlab.com/handbook/product/personas/#alex-security-operations-engineer)


### Pricing and Packaging[](https://about.gitlab.com/direction/ai-powered/duo_chat/#pricing-and-packaging)
Duo Chat is availible as part of both [Duo Pro and Duo Enterprise addons](https://about.gitlab.com/direction/ai-powered/duo_chat/). Learn about how different [Duo Chat features are tiered between the Duo addons](https://about.gitlab.com/direction/ai-powered/duo_chat/).
### Analyst Landscape[](https://about.gitlab.com/direction/ai-powered/duo_chat/#analyst-landscape)
Details coming soon.
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/ai-powered/duo_chat/index.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/ai-powered/duo_chat/index.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fai-powered%2Fduo_chat%2F&_biz_t=1773331624618&_biz_i=%0ACategory%20Direction%20-%20GitLab%20Duo%20Chat%0A%7C%0AGitLab%0A&_biz_n=20&rnd=44044&cdn_o=a&_biz_z=1773331624766)
suggested results