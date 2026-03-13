#  Category Direction - Code Suggestions 
  1. You are here:
  2. Category Direction - Code Suggestions


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
## On this page
  * [Code Suggestions](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#code-suggestions)
    * [Introduction and how you can help](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#introduction-and-how-you-can-help)
    * [Overview](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#overview)
    * [Vision](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#vision)
    * [Strategy & themes](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#strategy--themes)
      * [Latency](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#latency)
      * [Quality](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#quality)
      * [Expand use cases](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#expand-use-cases)
      * [Enterprise & administrator controls](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#enterprise--administrator-controls)
    * [1 year plan](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#1-year-plan)
    * [Target audience](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#target-audience)
    * [Success metrics](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#success-metrics)
    * [Competitive landscape](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#competitive-landscape)


# Code Suggestions[](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#code-suggestions)
|   
---|---  
Stage | [Create](https://about.gitlab.com/direction/create/)  
Maturity | [viable](https://about.gitlab.com/direction/#maturity)  
Content Last Reviewed | `2024-10-15`  
### Introduction and how you can help[](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#introduction-and-how-you-can-help)
Thanks for visiting this category direction page on Code Suggestions in GitLab. This page belongs to the [Code Creation](https://handbook.gitlab.com/handbook/product/categories/#code-creation-group) group of the Create stage, and is maintained by Jordan Janes ([@jordanjanes](https://gitlab.com/jordanjanes)).
## Overview[](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#overview)
The Code Creation team focuses on helping developers create & maintain code more efficiently. We strive to help GitLab customers deliver value to their customers more quickly through an accelerated software development lifecycle.
We help developers understand, write, test, fix, refactor, and document code:
  * Help developers understand and navigate their codebase, and plan changes.
  * Reduce the time spent writing code by generating code based on natural language instructions and suggesting code completions.
  * Automate and accelerate development tasks by explaining and documenting code, generating unit tests, and fixing code.
  * Improve code quality by refactoring inefficient code.


We believe there’s an opportunity to help developers with both narrowly scoped tasks - such as generating unit tests - and with broadly scoped tasks - such as evaluating and updating all tests across a codebase.
## Vision[](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#vision)
GitLab Duo Code Suggestions helps teams accelerate code creation throughout their software development lifecycle, without sacrificing security, privacy, and enterprise control.
## Strategy & themes[](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#strategy--themes)
We plan to improve the quality and latency of code suggestions, expand the breadth of customer use cases we support, and ensure our customers have sufficient administrative controls. To make progress towards our vision, our investments are organized into these primary themes:
### Latency[](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#latency)
Code suggestions, and specifically inline code completions, have to keep up with the pace of the user. Delays in presenting useful suggestions often result in the user manually continuing their workflow, and this impairs our opportunity to help our customers accelerate their development. 
Code generation is often less latency sensitive, though we still strive to quickly deliver generated code to the user. We will often stream the responses so the developer can start to assess the results, and this also improves the latency when generating large blocks of code. 
GitLab has customers across the globe, and we’re committed to optimizing latency for all customers. We’ve invested in globally distributed infrastructure, and we prioritize model providers who can mitigate network latency with globally deployed models. 
We consider fast latency a tablestakes expectation from our customers, and we carefully manage latency tradeoffs when considering larger and more capable models. 
### Quality[](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#quality)
Improving the quality of code suggestions is a primary focus. We think of quality as providing useful suggestions, which our users accept to accelerate their workflow. For code completion, this could be 1 line of code that perfectly matches what the user wanted. For code generation, this could be dozens of lines of code, and the user may sometimes edit a few specifics before moving forward. Over time, we want to provide exactly what the user needs. 
We plan to make progress on this goal by leveraging context throughout the customer’s codebase, continuing to invest in our internal evaluation suite, and continually assessing new AI models. 
**Context**
Managing and providing relevant context - from relevant dependencies, files, and throughout a codebase - is the main tactic to improve code suggestion quality. We can greatly improve the quality of code suggestions by ensuring responses are aware of key dependencies, libraries, and systems. We plan to find the right portions of content, provide that as context to our AI models, and generate a better response.
**Internal evaluations**
We must be confident that we’re improving quality as we broaden Code Suggestions to include more context and support more customer use cases. We use a broad evaluation dataset to internally quantify quality before rolling out changes to our customers. We’ll continue to extend our evaluation dataset by curating and creating test scenarios that will help us confidently assess quality. 
**Models**
We continuously monitor and evaluate the latest AI models for opportunities to improve quality and latency. We provide full transparency to our customers on the models used within GitLab Duo, and we gladly take responsibility for keeping up to date on all of the latest breakthroughs in AI models and technology. With Duo Code Suggestions, our customers can focus on accelerating their software development lifecycle and not spend time reviewing the latest AI models. 
### Expand use cases[](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#expand-use-cases)
With the breadth of the GitLab DevSecOps platform, expanding to support more customer goals is a long term opportunity for differentiation.
**Broadly scoped tasks**
Today, most of our user interactions center around specifically scoped tasks. As an example, a user can select portions of code and use Duo Code Suggestions to create tests, or refactor the code. We will support more broadly scoped tasks from our users to further accelerate their workflow. An example might be helping a developer add a field to an existing API, then updating all queries to match the new schema. These broadly scoped tasks require more context and reasoning, and the ability to make edits among multiple files and locations within the files.
**Increase automation**
We will help developers further accelerate their workflow through increased automation. This might include searching an entire codebase to find code that needs improvement, or continuously scanning for bugs and surfacing those to our users. Duo can intelligently help our users find areas to improve, along with efficiently implementing the improvements.
### Enterprise & administrator controls[](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#enterprise--administrator-controls)
Enterprise customers often have more needs for admin controls and auditing. We want to ensure Duo Code Suggestions meets our customers’ goals for compliance and administration. GitLab Duo has a strict [data privacy and data retention policy](https://docs.gitlab.com/ee/user/gitlab_duo/data_usage.html) to ensure customers can be confident in our data protection agreements. Customers don’t need to manage administrator controls to ensure there’s data privacy. 
## 1 year plan[](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#1-year-plan)
**What we recently completed**
  * [Migrate Repository X-Ray to a background job](https://gitlab.com/groups/gitlab-org/-/epics/14100)
  * [Improving quality through context: Imports](https://gitlab.com/groups/gitlab-org/editor-extensions/-/epics/58)
  * [Accelerate code completion latency with prompt caching](https://gitlab.com/groups/gitlab-org/-/epics/17489)


**What we are currently working on**
  * [Duo content exclusion](https://gitlab.com/groups/gitlab-org/-/epics/17124)
  * [Full codebase/project context](https://gitlab.com/groups/gitlab-org/-/epics/16910)
  * [Improve code base understanding & context - Knowledge Graph](https://gitlab.com/groups/gitlab-org/-/epics/16210)


**What is next for us**
  * [Duo custom instructions for code suggestions](https://gitlab.com/groups/gitlab-org/-/epics/16938)
  * [Next edit suggestions](https://gitlab.com/gitlab-org/gitlab/-/issues/518714)


## Target audience[](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#target-audience)
People who code:
  1. [Sasha (Software Developer)](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
  2. [Priyanka (Platform Engineer)](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)
  3. [Simone (Software Engineer in Test)](https://handbook.gitlab.com/handbook/product/personas/#simone-software-engineer-in-test)


## Success metrics[](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#success-metrics)
Success metrics & signals are organized around 2 broad goals:
  1. Increasing developer productivity
  2. Improving developer satisfaction


**Increasing developer productivity**
Signal: reduced time from task start to task finish
  * Merge request throughput


Signal: more coding tasks are automated or accelerated
  * % of code provided by AI
  * Number of accepted suggestions per user
  * Acceptance rate


**Improve developer satisfaction**
Signal: Developers consistently use code suggestions
  * MAU
  * MAU / Billable users
  * Code completion usage
  * Code generation usage


## Competitive landscape[](https://about.gitlab.com/direction/create/code_creation/code_suggestions/#competitive-landscape)
Please see the content in our [internal handbook](https://internal.gitlab.com/handbook/product/best-in-class/create/code_suggestions/).
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/create/code_creation/code_suggestions/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/create/code_creation/code_suggestions/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fcreate%2Fcode_creation%2Fcode_suggestions%2F&_biz_t=1773331914301&_biz_i=%0ACategory%20Direction%20-%20Code%20Suggestions%0A%7C%0AGitLab%0A&_biz_n=79&rnd=901326&cdn_o=a&_biz_z=1773331914303)
suggested results