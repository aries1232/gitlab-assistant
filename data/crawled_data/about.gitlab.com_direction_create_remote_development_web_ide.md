#  Category Direction - Web IDE 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Product Stage Vision - Create](https://about.gitlab.com/direction/create/)
  4. [Group Direction - Remote Development](https://about.gitlab.com/direction/create/remote_development/)
  5. Category Direction - Web IDE


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Web IDE](https://about.gitlab.com/direction/create/remote_development/web_ide/#web-ide)
    * [Introduction and how you can help](https://about.gitlab.com/direction/create/remote_development/web_ide/#introduction-and-how-you-can-help)
    * [Overview](https://about.gitlab.com/direction/create/remote_development/web_ide/#overview)
    * [Strategy and Themes](https://about.gitlab.com/direction/create/remote_development/web_ide/#strategy-and-themes)
      * [GitLab Workflow for Visual Studio Code](https://about.gitlab.com/direction/create/remote_development/web_ide/#gitlab-workflow-for-visual-studio-code)
    * [1 year plan](https://about.gitlab.com/direction/create/remote_development/web_ide/#1-year-plan)
      * [What is next for us](https://about.gitlab.com/direction/create/remote_development/web_ide/#what-is-next-for-us)
      * [What we are currently working on](https://about.gitlab.com/direction/create/remote_development/web_ide/#what-we-are-currently-working-on)
      * [What we recently completed](https://about.gitlab.com/direction/create/remote_development/web_ide/#what-we-recently-completed)
      * [What is Not Planned Right Now](https://about.gitlab.com/direction/create/remote_development/web_ide/#what-is-not-planned-right-now)
    * [Target Audience](https://about.gitlab.com/direction/create/remote_development/web_ide/#target-audience)
    * [Pricing and Packaging](https://about.gitlab.com/direction/create/remote_development/web_ide/#pricing-and-packaging)


## Web IDE[](https://about.gitlab.com/direction/create/remote_development/web_ide/#web-ide)
|   
---|---  
Stage | [Create](https://about.gitlab.com/direction/create/)  
Maturity | [Complete](https://about.gitlab.com/direction/#maturity)  
Content Last Reviewed | `2025-04-28`  
### Introduction and how you can help[](https://about.gitlab.com/direction/create/remote_development/web_ide/#introduction-and-how-you-can-help)
Thanks for visiting the category direction page for the GitLab Web IDE. This page belongs to the [Remote Deveopment group](https://handbook.gitlab.com/handbook/product/categories/#remote-development-group) of the [Create stage](https://handbook.gitlab.com/handbook/engineering/development/dev/create/) and is maintained by Senior Product Manager, Michelle Chen ([@michelle-chen](https://gitlab.com/michelle-chen)).
This direction page is a work in progress, and everyone can contribute:
  * Please comment and contribute to issues linked througout this page or contained in our [category strategy epic](https://gitlab.com/groups/gitlab-org/-/epics/170). Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
  * If you would like to share your feedback directly or schedule a video call, please reach out directly to Michelle Chen via email.


### Overview[](https://about.gitlab.com/direction/create/remote_development/web_ide/#overview)
A code editor is one of the most important tools in a software developer's toolkit. With the Web IDE, we want to meet the developers where they are and offer a mature, feature-rich editing experience in the browser. By replacing the current Web IDE with a browser-based instance of VS Code, the [most popular code editor](https://insights.stackoverflow.com/survey/2021#section-most-popular-technologies-integrated-development-environment), we can enable developers to complete more complex tasks and work more efficiently inside GitLab.
Software development is an iterative process that involves requesting and responding to feedback from Developers, Designers, Product Managers, or other peers. While a desktop editor is often optimized with extensions to support specific programming languages, coding standards, or frameworks, they are often not ideal for the frequent context switching and rapid feedback cycles in the review phase. GitLab's Web IDE offers a familiar workflow to developers while remaining easy to use for designers, product managers and more. It brings editing capabilities into the context of their current task in GitLab, by providing an editing experience designed for the workflow they're trying to accomplish.
### Strategy and Themes[](https://about.gitlab.com/direction/create/remote_development/web_ide/#strategy-and-themes)
There are three critical workflows we aim to support in the Web IDE.
**Configuration**
Users who configure projects or GitLab need editing tools to help them be efficient at this process. Creating specialized configuration files for working with GitLab CI or other areas of GitLab benefit from feedback provided directly in the editor.
Configuration files are common to software development and the tools of the DevSecOps life cycle. Files like `gitlab-ci.yml` or `CODEOWNERS` can be difficult to manage because they need to be both syntactically (correct commas, quotes, value types etc) and semantically valid (expresses what you intended it to). Local development environments can be configured with syntax checkers, and schemas to help verify syntactic correctness, but lack the context for deeper features.
Once your GitLab CI configuration has been created and validated, it may be responsible for providing review applications for previewing changes, code quality and coverage reports or vulnerability information. As an engineer who is working on a contribution information contained on these reports must be reconciled within their editor.
**Contribution**
Developers who work on contributing directly to the code in projects need to action feedback from the review process. This often involves leaving MR feedback open in one window while working in an editor in a different window. Feedback in the form of suggestions and patch files needs to be handled outside of the MR interface and back in the local development environment. At the same time some feedback requires manually updating comments and threads that feedback has been actioned after the changes have been pushed back to the MR. Having easy access to the feedback from reviewers and CI jobs inside of the editor should ensure that it's easy to action.
**Feedback & Review**
The code review process encompasses both engineering personas and non-engineering personas who contribute through design, product and other feedback.
A developer reviewing a merge request often needs to check the code out locally and create an environment for that review. Sometimes this process can be complicated by conflicts with local dependencies, their own local development branch, database migrations and other issues which prevent just cleanly changing branches.
A designer or product manager may not have the time or experience required to set up and maintain an environment to perform reviews. Reviewing these changes inside of a review application is valuable, but it can be hard to provide as actionable comments back to the MR.
In solving for both these users and workflows, it will be important to make sure that people who want to give feedback are able to easily accomplish that.
**Strategic Focus Areas** To address these themes, we will focus on the following strategic areas, which will resemble phases of the product and work prioritization:
![Web IDE Strategic Focus Areas](https://about.gitlab.com/images/remote_development/webide-strategic-areas.png)
#### GitLab Workflow for Visual Studio Code[](https://about.gitlab.com/direction/create/remote_development/web_ide/#gitlab-workflow-for-visual-studio-code)
The [GitLab Workflow extension for VS Code](https://docs.gitlab.com/ee/editor_extensions/visual_studio_code/) is available on the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=GitLab.gitlab-workflow) and enables you to interact with merge request discussions, issues, and pipelines directly from VS Code.
One of the benefits of [replacing the Web IDE with a VS Code instance](https://gitlab.com/groups/gitlab-org/-/epics/7683) is that you will be able to install compatible extensions in the browser-based Web IDE. By [bundling the GitLab Workflow extension in the Web IDE](https://gitlab.com/gitlab-org/gitlab/-/issues/355054), we will enable new functionality and provide consistency across the desktop and web editing experience. Functionality contributed by the community and additional investments in the capabilities of the extension will then be available on both platforms. The GitLab Workflow extension is maintained by the [Editor Extensions](https://about.gitlab.com/direction/create/editor_extensions/) group.
### 1 year plan[](https://about.gitlab.com/direction/create/remote_development/web_ide/#1-year-plan)
  * [Don't require accepting third-party cookies to run Web IDE](https://gitlab.com/gitlab-org/gitlab-web-ide/-/issues/270)
  * [1st Class Editing Experiences for GitLab features](https://gitlab.com/groups/gitlab-org/-/epics/2707)
  * [Add additional source control operations to the Web IDE](https://gitlab.com/groups/gitlab-org/-/epics/11142)


#### What is next for us[](https://about.gitlab.com/direction/create/remote_development/web_ide/#what-is-next-for-us)
  * [Search across all files in a project from within the Web IDE](https://gitlab.com/groups/gitlab-org/-/epics/9466)
  * [Consistent UI for Web IDE Loader and Error State](https://gitlab.com/groups/gitlab-org/-/epics/14944)
  * [Fix: Theme images are broken on the VS Code welcome page](https://gitlab.com/groups/gitlab-org/-/epics/14997)


#### What we are currently working on[](https://about.gitlab.com/direction/create/remote_development/web_ide/#what-we-are-currently-working-on)
  * [Host the Web IDE on a new domain or subdomain](https://gitlab.com/groups/gitlab-org/-/epics/11972)
  * [Update VSCode to >= 1.96.x](https://gitlab.com/groups/gitlab-org/-/epics/16132)


#### What we recently completed[](https://about.gitlab.com/direction/create/remote_development/web_ide/#what-we-recently-completed)
  * [Prevent different Web IDE Extensions Marketplace contexts from overwriting Settings Sync store](https://gitlab.com/groups/gitlab-org/-/epics/15216)
  * [Enable Web IDE Extension Marketplace for Self-Managed](https://gitlab.com/groups/gitlab-org/-/epics/11770)
  * [Settings Sync for the Web IDE](https://gitlab.com/groups/gitlab-org/-/epics/11147)
  * [Enable Web IDE Extension Marketplace for GitLab.com](https://gitlab.com/groups/gitlab-org/-/epics/11769)
  * [Enable OAuth authentication by default on the Web IDE](https://gitlab.com/groups/gitlab-org/-/epics/14941)
  * [Investigate hosting Web IDE on new domain](https://gitlab.com/gitlab-org/gitlab/-/issues/464082)


#### What is Not Planned Right Now[](https://about.gitlab.com/direction/create/remote_development/web_ide/#what-is-not-planned-right-now)
While our [complete maturity](https://about.gitlab.com/direction/create/remote_development/web_ide/#maturity) plan also aims to ensure some [compatibility with the iPad](https://gitlab.com/groups/gitlab-org/-/epics/756). We won't be focusing on making the iPad or other mobile devices 1st class devices due to our upstream dependencies on VS Code. We also do not have sufficient evidence to support mobile devices as code creation devices inside the Web IDE. As our research in this area continues to expand we may revisit mobile support.
We do not have plans to bring real-time collaborative coding features to the Web IDE at this time. We'll continue to evaluate the space and may revisit this use case at a later date, especially as it relates to [workspaces](https://about.gitlab.com/direction/create/remote_development/workspaces/).
### Target Audience[](https://about.gitlab.com/direction/create/remote_development/web_ide/#target-audience)
The Web IDE primarily serves engineering personas who are contributing to development, configuring or interacting with continuous integration and reviewing contributions from other team members. Personas like [Sasha (Software Developer)](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer) and [Devon (DevOps Engineer)](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer) need tools that allow them to deeply understand the changes and provide meaningful feedback of both comments and code suggestions.
The Web IDE also serves non-engineer personas who are focused on reviewing and providing feedback for contributions. Personas like [Parker (Product Manager)](https://handbook.gitlab.com/handbook/product/personas/#parker-product-manager), [Presley (Product Designer)](https://handbook.gitlab.com/handbook/product/personas/#presley-product-designer), and [Delaney (Development Team Lead)](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead) need tools and features that help them preform reviews of code, documentation and interfaces without requiring local environments or complex configurations. Feedback should be easy to leave and actionable by engineers within their editor.
### Pricing and Packaging[](https://about.gitlab.com/direction/create/remote_development/web_ide/#pricing-and-packaging)
The Web IDE is available to everyone on SaaS and Self-managed as part of the Free tier.
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/create/remote_development/web_ide/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/create/remote_development/web_ide/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fcreate%2Fremote_development%2Fweb_ide%2F&_biz_t=1773331735448&_biz_i=%0ACategory%20Direction%20-%20Web%20IDE%0A%7C%0AGitLab%0A&_biz_n=41&rnd=175588&cdn_o=a&_biz_z=1773331735551)
suggested results