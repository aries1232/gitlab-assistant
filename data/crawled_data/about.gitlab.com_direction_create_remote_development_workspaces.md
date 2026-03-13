#  Category Direction - Workspaces 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Product Stage Vision - Create](https://about.gitlab.com/direction/create/)
  4. [Group Direction - Remote Development](https://about.gitlab.com/direction/create/remote_development/)
  5. Category Direction - Workspaces


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Workspaces](https://about.gitlab.com/direction/create/remote_development/workspaces/#workspaces)
    * [Introduction and how you can help](https://about.gitlab.com/direction/create/remote_development/workspaces/#introduction-and-how-you-can-help)
    * [Overview](https://about.gitlab.com/direction/create/remote_development/workspaces/#overview)
    * [Vision](https://about.gitlab.com/direction/create/remote_development/workspaces/#vision)
    * [Strategy and Themes](https://about.gitlab.com/direction/create/remote_development/workspaces/#strategy-and-themes)
    * [1 year plan](https://about.gitlab.com/direction/create/remote_development/workspaces/#1-year-plan)
      * [What is next for us](https://about.gitlab.com/direction/create/remote_development/workspaces/#what-is-next-for-us)
      * [What we are currently working on](https://about.gitlab.com/direction/create/remote_development/workspaces/#what-we-are-currently-working-on)
      * [What we recently completed](https://about.gitlab.com/direction/create/remote_development/workspaces/#what-we-recently-completed)
      * [What is Not Planned Right Now](https://about.gitlab.com/direction/create/remote_development/workspaces/#what-is-not-planned-right-now)
    * [Target Audience](https://about.gitlab.com/direction/create/remote_development/workspaces/#target-audience)
    * [Pricing and Packaging](https://about.gitlab.com/direction/create/remote_development/workspaces/#pricing-and-packaging)
    * [Analyst Landscape](https://about.gitlab.com/direction/create/remote_development/workspaces/#analyst-landscape)


## Workspaces[](https://about.gitlab.com/direction/create/remote_development/workspaces/#workspaces)
|   
---|---  
Stage | [Create](https://about.gitlab.com/direction/create/)  
Content Last Reviewed | `2025-07-22`  
### Introduction and how you can help[](https://about.gitlab.com/direction/create/remote_development/workspaces/#introduction-and-how-you-can-help)
Thanks for visiting the category direction page for Workspaces in GitLab. This page belongs to the [Remote Development group](https://handbook.gitlab.com/handbook/product/categories/#editor-group) of the [Create stage](https://handbook.gitlab.com/handbook/engineering/development/dev/create/) and is maintained by Principal Product Manager, Michelle Chen ([@mmichelle-chen](https://gitlab.com/michelle-chen)).
This direction page is a work in progress, and everyone can contribute:
  * Please comment and contribute to issues linked througout this page or contained in our [category strategy epic](https://gitlab.com/groups/gitlab-org/-/epics/7419). Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
  * If you would like to share your feedback directly or schedule a video call, please reach out directly to Michelle Chen via email.


### Overview[](https://about.gitlab.com/direction/create/remote_development/workspaces/#overview)
A common obstacle faced by developers when first contributing to a project is the setup of their local development environment. The time-consuming process of managing interrelated dependencies and fixing version compatibility issues can be demotivating, especially for those who only contribute occasionally or switch between multiple projects frequently. In complicated environments, development teams may also impose restrictions, authentication credentials, build procedures, and standards that add to the fragile nature of the development environment.
At the end of the day, developers want to spend less time managing their development environment and more time contributing high-quality code. And at GitLab, our mission is to ensure _everyone can contribute_. With Workspaces, our goal is to eliminate the responsibility of configuring and maintaining a local development environment.
### Vision[](https://about.gitlab.com/direction/create/remote_development/workspaces/#vision)
Ephemeral, cloud-based workspaces will be configured in a single file stored in a repository, allowing you to provision a new environment with a single click and connect securely from the GitLab Web IDE or your desktop editor of choice. Monitoring tools and dashboards will be available in GitLab to manage running and suspended environments, ensuring efficient usage of resources. This will free up valuable development time, streamline onboarding of new developers, and increase security across an increasingly remote workforce.
A cloud-based development environment also enables organizations working in regulated industries to enforce a zero-trust policy that prevents source code from ever being stored locally while maintaining a high quality developer experience. GitLab workspaces contribute to our [vision for managing Software Supply Chain Security](https://about.gitlab.com/direction/supply-chain/) by providing a single place where dependencies and tools can be audited and verified, and access to those environments can be controlled through strong authentication.
Our initial iterations for Workspaces will be focused on a "bring your own cloud" solution, letting developers on both GitLab.com and Self-managed GitLab instances provision workspaces on their existing cloud platforms like Amazon Web Services, Google Cloud Platform, or Azure Cloud Services. We will eventually offer a fully-managed option within GitLab, provided as a service billed based on consumption, much like our [Runner SaaS](https://about.gitlab.com/direction/verify/hosted_runners/) offering.
### Strategy and Themes[](https://about.gitlab.com/direction/create/remote_development/workspaces/#strategy-and-themes)
Our strategy for Workspaces is centered around three main themes:
  1. Simplifying Development Environment Setup 
     * Provide a seamless, one-click solution for provisioning development environments
     * Eliminate the need for manual configuration and dependency management
     * Enable quick onboarding for new team members and contributors
  2. Enhancing Collaboration and Productivity 
     * Offer consistent development environments across teams
     * Facilitate easy sharing and replication of workspace configurations
     * Supporting development workflows end-to-end
  3. Improving Security and Compliance 
     * Implement zero-trust security policies for regulated industries
     * Centralize control over development environments and access
     * Enable auditing and verification of dependencies and tools


To address these themes, we will focus on the following strategic areas, which will resemble phases of the product and work prioritization:
![Workspaces Strategic Areas](https://about.gitlab.com/images/remote_development/workspaces-strategic-areas.png)
### 1 year plan[](https://about.gitlab.com/direction/create/remote_development/workspaces/#1-year-plan)
In the next year, we are focused on reducing "time to first workspace" through making it easier to manage the configuration and resource management associated with running workspaces, and removing any barriers of entry into adoption of workspaces.
  * [Shared workspaces](https://gitlab.com/groups/gitlab-org/-/epics/11310)
  * [Investigation: Automatically suspend a workspace after a period of inactivity](https://gitlab.com/groups/gitlab-org/-/epics/10710)
  * [Workspaces Settings Configuration Infrastructure in GitLab](https://gitlab.com/groups/gitlab-org/-/epics/14186)


#### What is next for us[](https://about.gitlab.com/direction/create/remote_development/workspaces/#what-is-next-for-us)
  * [Simplify Workspaces setup by removing GitLab Workspaces Proxy](https://gitlab.com/groups/gitlab-org/-/epics/16785)
  * [Show workspace ports in VS Code Panel](https://gitlab.com/groups/gitlab-org/-/epics/15732)
  * [Support SSH for Workspaces](https://gitlab.com/groups/gitlab-org/-/epics/13984)
  * [Workspaces on CI Runners](https://gitlab.com/groups/gitlab-org/-/epics/16650)
  * [Inject JetBrains Editors into a workspace](https://gitlab.com/groups/gitlab-org/-/epics/9836)


#### What we are currently working on[](https://about.gitlab.com/direction/create/remote_development/workspaces/#what-we-are-currently-working-on)
  * [Improve Workspace Creation Failure Visibility and Troubleshooting](https://gitlab.com/groups/gitlab-org/-/epics/16787)
  * [Simplify freezing of Kubernetes resources for workspaces to avoid inadvertent workspace restart issues](https://gitlab.com/groups/gitlab-org/-/epics/17483)
  * [Simplify Workspaces setup by removing GitLab Workspaces Proxy](https://gitlab.com/groups/gitlab-org/-/epics/16785)
  * [Show message if devfile is invalid before creating a workspace](https://gitlab.com/groups/gitlab-org/-/epics/17853)


#### What we recently completed[](https://about.gitlab.com/direction/create/remote_development/workspaces/#what-we-recently-completed)
  * [Startup scripts for Remote Development workspaces](https://gitlab.com/groups/gitlab-org/-/epics/15602)
  * [Instance level agent authorization](https://gitlab.com/groups/gitlab-org/-/epics/16485)
  * [Create a workspace from MR](https://gitlab.com/gitlab-org/gitlab/-/issues/426568)
  * [Shared namespace for workspaces](https://gitlab.com/groups/gitlab-org/-/epics/12327)


#### What is Not Planned Right Now[](https://about.gitlab.com/direction/create/remote_development/workspaces/#what-is-not-planned-right-now)
Workspaces are personal and ephemeral. We anticipate developers will want to collaboarte within workspaces but we are not currently focused on providing a real-time collaborative editing environment suitable for pair programming.
### Target Audience[](https://about.gitlab.com/direction/create/remote_development/workspaces/#target-audience)
The term "Workspaces" speaks to the challenges faced by software developers and those who lead or support their teams. By providing a mature workspaces solution, the technical barriers to collaboration are lowered, allowing non-developers to make effective contributions as well. This enables us to cater to all [user personas](https://handbook.gitlab.com/handbook/product/personas/#user-personas) described in our handbook, with a focus on:
  * **[Sasha (Software Developer):](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)** targets full time contributors to all types of projects (commercial, OSS, data science, etc.). These users expect and need a high level of reliability and speed in their interactions with both project files and Git.
  * **[Delaney (Development Team Lead):](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)** targets users who often times have elevated roles which allow for the management of project settings, such as access control, security, commit strategies, and mirroring.
  * **[Priyanka (Platform Engineer)](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)** targets users who define pipelines, templates, and processes to improve developer efficiency across an organization.


### Pricing and Packaging[](https://about.gitlab.com/direction/create/remote_development/workspaces/#pricing-and-packaging)
Remote Developement is currently a Premium+ offering. However, the goal is to provide a multi-level offering, providing value across all tiers and distributions.
**Free tiers** is not currently available, but we aim to provide one in the future to make our features more accessible and valuable to a broader audience.
With **GitLab Premium** , organizations will have the ability to specify development environments in a `devfile` and create remote environments on existing cloud infrastructure. This will allow team leads or DevOps engineers to monitor multiple environments from a centralized GitLab dashboard and standardize the environment across the organization, improving team efficiency.
Eventually, **Ultimate tiers** will have access to advanced monitoring and auditing tools, providing insight into usage across the organization and enforcing security best practices through development tooling.
### Analyst Landscape[](https://about.gitlab.com/direction/create/remote_development/workspaces/#analyst-landscape)
Several analysts have recently published reports highlighting the rapid adoption of cloud-based development workflows.
**Gartner®**
Gartner report titled, **Hype® Cycle for Agile and DevOps, 2021** discusses "Browser-based integrated development environments (IDEs) are consumed “as a service.” They enable browser-based remote access to a complete development environment, which obviates the need for local installation/configuration."*
Further, it states "Browser-based IDEs provide consistent, secure access to preconfigured development workflows to developers. This frees them from setting up their own environments, eliminating the need to install and maintain prerequisites, software development kits (SDKs), security updates and workstation plug-ins."*
"Gartner predicts that, by 2026, 60% of cloud workloads will be built and deployed using browser-based IDEs". The report adds, “Five factors are driving their increased adoption":
  1. "Remote work and remote onboarding of software developers create a need for a frictionless onboarding experience."
  2. "Environment setup issues can impede productivity and hurt the onboarding experience."
  3. "Cloud-native (e.g., Kubernetes) deployments require new tooling that either isn't available or is inconvenient to set up on-premises."
  4. "Browser-based IDEs make it easier to support and secure bring your own PC (BYOPC) use cases."
  5. "Automating DevOps workflows introduces more plug-ins, extensions and API integrations, which make it cumbersome to manage on local machines."*


*_Gartner, Hype Cycle for Agile and DevOps, 2021, George Spafford, Joachim Herschmann, 12 July, 2021. GARTNER and HYPE CYCLE are a registered trademark and service mark of Gartner, Inc. and/or its affiliates in the U.S. and internationally and are used herein with permission._
GitLab's Web IDE already addresses some of Gartner's recommendations, by providing a platform from which anyone can contribute. By [migrating the Web IDE to VSCode](https://gitlab.com/groups/gitlab-org/-/epics/7143), we can rapidly increase the complexity of work and meet the needs of more serious development tasks. Pairing that with a [Server Runtime](https://gitlab.com/gitlab-org/gitlab/-/issues/329602), GitLab is positioned well to meet our customers' expectations when it comes to security, agility, and flexibility.
_451 Research_
451 Research published an analysis of [Coder](https://coder.com/) and their approach to moving development workspaces to the cloud. 451 Research recognizes that "by moving developers, IT operators and others to the cloud, organizations can drive faster releases, productivity and efficiency by automating and abstracting IT environments and their management. The idea is that developers have more time to focus on new features, applications and innovation when they are unencumbered with setting up and running their own environments."
In the analysis, 451 Research cites results from their 2021 report, **Voice of the Enterprise: DevOps, Workloads & Key Projects**, that reveal a significant shift in the primary DevOps implementation environment, moving away from On-premise and Hosted Private Cloud workspaces to SaaS and Public Cloud over the next two years.
451 Research's recommendation to stay competitive in this space is to "focus on enabling simplicity, speed and productivity for developers," something GitLab's single platform for DevOps is positioned well to deliver.
_Source: 451 Research, a part of S &P Global Market Intelligence, Coverage Initiation: Coder moves development to the cloud with workspaces-as-code, September 2021, All Rights Reserved_
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/create/remote_development/workspaces/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/create/remote_development/workspaces/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fcreate%2Fremote_development%2Fworkspaces%2F&_biz_t=1773331850590&_biz_i=%0ACategory%20Direction%20-%20Workspaces%0A%7C%0AGitLab%0A&_biz_n=66&rnd=618500&cdn_o=a&_biz_z=1773331850756)
suggested results