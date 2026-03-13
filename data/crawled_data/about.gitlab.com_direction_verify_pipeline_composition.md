#  Category Direction - Pipeline Composition 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Verify Stage Direction](https://about.gitlab.com/direction/verify/)
  4. Category Direction - Pipeline Composition


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Pipeline Composition](https://about.gitlab.com/direction/verify/pipeline_composition/#pipeline-composition)
    * [Introduction and how you can help](https://about.gitlab.com/direction/verify/pipeline_composition/#introduction-and-how-you-can-help)
    * [Overview](https://about.gitlab.com/direction/verify/pipeline_composition/#overview)
    * [Strategy and Themes](https://about.gitlab.com/direction/verify/pipeline_composition/#strategy-and-themes)
      * [What is next for us](https://about.gitlab.com/direction/verify/pipeline_composition/#what-is-next-for-us)
      * [What we are currently working on](https://about.gitlab.com/direction/verify/pipeline_composition/#what-we-are-currently-working-on)
      * [What we recently completed](https://about.gitlab.com/direction/verify/pipeline_composition/#what-we-recently-completed)
      * [What is Not Planned Right Now](https://about.gitlab.com/direction/verify/pipeline_composition/#what-is-not-planned-right-now)
    * [Best in Class Landscape](https://about.gitlab.com/direction/verify/pipeline_composition/#best-in-class-landscape)
      * [Key Capabilities](https://about.gitlab.com/direction/verify/pipeline_composition/#key-capabilities)
      * [Roadmap](https://about.gitlab.com/direction/verify/pipeline_composition/#roadmap)
      * [Top [1/2/3] Competitive Solutions](https://about.gitlab.com/direction/verify/pipeline_composition/#top-123-competitive-solutions)
        * [Github Actions](https://about.gitlab.com/direction/verify/pipeline_composition/#github-actions)
        * [Circle CI](https://about.gitlab.com/direction/verify/pipeline_composition/#circle-ci)
        * [Gitea Actions](https://about.gitlab.com/direction/verify/pipeline_composition/#gitea-actions)
    * [Target Audience](https://about.gitlab.com/direction/verify/pipeline_composition/#target-audience)
    * [Analyst Landscape](https://about.gitlab.com/direction/verify/pipeline_composition/#analyst-landscape)


## Pipeline Composition[](https://about.gitlab.com/direction/verify/pipeline_composition/#pipeline-composition)
|   
---|---  
Stage | [verify](https://about.gitlab.com/direction/verify/)  
Maturity | [Minimal](https://about.gitlab.com/direction/#maturity)  
Content Last Updated | `2026-01-26`  
### Introduction and how you can help[](https://about.gitlab.com/direction/verify/pipeline_composition/#introduction-and-how-you-can-help)
Thanks for visiting this category direction page on Pipeline Composition in GitLab. This page belongs to the [Pipeline Authoring](https://handbook.gitlab.com/handbook/product/categories/#pipeline-authoring-group) group of the Verify stage and is maintained by Dov Hershkovitch (E-Mail).
This direction page is a work in progress, and everyone can contribute:
  * Please comment and contribute in the linked [issues](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=updated_desc&state=opened&label_name%5B%5D=developer%20automations&first_page_size=20) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
  * Please share feedback directly via email, Twitter, or on a video call. If you're a GitLab user and want to discuss how GitLab can improve Variables, we'd especially love to hear from you.


### Overview[](https://about.gitlab.com/direction/verify/pipeline_composition/#overview)
GitLab CI is the platform that you use to ship your software to your customers as fast as possible. As outlined in our 3 year strategy, we want to enable platform teams to share operational definitions (infrastructure, environments, deployment pipelines, monitoring configuration) with development teams, and for development teams to easily contribute improvements. The Developer Automation category is the backbone to eliminating the user friction for authoring those pipeline configurations throughout the GitLab CI/CD journey.
### Strategy and Themes[](https://about.gitlab.com/direction/verify/pipeline_composition/#strategy-and-themes)
Pipeline Composition is born from the need to solve how nearly 80% of a developer's time is spent on non-coding tasks, as shown in GitLab's [2024 Global DevSecOps Report](https://about.gitlab.com/resources/developer-survey/). Our strategy focuses on two interconnected approaches to reduce pipeline configuration complexity:
  1. **AI-Powered Pipeline Intelligence** : Leverage GitLab Duo to reduce manual configuration through intelligent authoring assistance, real-time debugging, and automated optimization recommendations.
  2. **Visual Pipeline Understanding** : Provide advanced visualization tools that help users understand pipeline structure, identify failures quickly, and navigate complex multi-stage workflows without editing YAML directly.


These themes work together to address the full pipeline lifecycle: AI assists with creation and debugging, while visualization aids understanding and troubleshooting complex workflows.
#### What is next for us[](https://about.gitlab.com/direction/verify/pipeline_composition/#what-is-next-for-us)
For the next quarter, we have the following strategic initiatives planned:
  1. **Visual Pipeline Intelligence Platform** - Pivoting from a bidirectional YAML editing tool to an AI-first visualization and debugging platform. This shift addresses technical constraints (YAML normalization destroys comments and formatting) while aligning with user research showing highest satisfaction scores (4.75-5.0/5) for visualization and debugging use cases versus lower scores (3.2/5) for UI-based authoring.
  2. **IDE-First Pipeline Authoring** - Consolidating pipeline authoring capabilities into the IDE experience (both web-based and local IDEs) with plans to deprecate the standalone pipeline editor in the future. This strategy will: 
     * Leverage Language Server Protocol (LSP) for advanced editing capabilities including auto-completion, validation, and go-to-definition
     * Integrate GitLab Duo AI assistance directly into the editing workflow
     * Provide unified experience across Web IDE, VS Code, and other local IDEs
     * Bring visualization capabilities into the IDE alongside editing
     * Enable developers to author pipelines in their preferred development environment without context switching
  3. **GitLab Duo Integration** - Deeply embedding AI capabilities throughout the pipeline authoring experience: 
     * AI-powered pipeline generation with teaching mode for novice users
     * Intelligent debugging and root cause analysis for failed pipelines
     * Automated optimization recommendations based on execution patterns
     * Context-aware suggestions during YAML editing


#### What we are currently working on[](https://about.gitlab.com/direction/verify/pipeline_composition/#what-we-are-currently-working-on)
Currently the team is focusing on providing solutions for critical customer requests:
  1. [Inputs Enhancements](https://gitlab.com/groups/gitlab-org/-/epics/10603) - This epic supports the feature release of [introduce inputs for pipeline](https://gitlab.com/groups/gitlab-org/-/epics/16321). This epic holds a series of technical debt issues and feature enhancements that we want to make to polish the CI inputs experience.
  2. [Introduce CI Job inputs](https://gitlab.com/groups/gitlab-org/-/epics/17833) - The feature aims to make CI jobs more configurable, secure, and easier to debug, with a primary initial objective of allowing users to retry CI jobs with new input values - addressing a critical customer need that's currently blocking Jenkins migration efforts.
  3. **Visual Pipeline Intelligence MVC** - Engineering feasibility assessment and UX design for AI-first pipeline visualization platform targeting GitLab 18.11 (May 2026) launch as BETA.
  4. **Language Server Protocol (LSP) Integration** - Developing advanced pipeline editing capabilities through LSP to enable rich IDE experiences across multiple editors.


#### What we recently completed[](https://about.gitlab.com/direction/verify/pipeline_composition/#what-we-recently-completed)
  * [Dynamic Input Selection in GitLab Pipelines](https://gitlab.com/gitlab-org/gitlab/-/issues/520094) - Delivered dropdown selection for pipeline inputs with cascading functionality where options in one dropdown change based on selections made in previous inputs


#### What is Not Planned Right Now[](https://about.gitlab.com/direction/verify/pipeline_composition/#what-is-not-planned-right-now)
  1. Pipeline editor improvements
  2. Enhancements to existing keywords or introducing new keywords
  3. Migration tooling for other pipeline syntax


### Best in Class Landscape[](https://about.gitlab.com/direction/verify/pipeline_composition/#best-in-class-landscape)
BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.
#### Key Capabilities[](https://about.gitlab.com/direction/verify/pipeline_composition/#key-capabilities)
#### Roadmap[](https://about.gitlab.com/direction/verify/pipeline_composition/#roadmap)
#### Top [1/2/3] Competitive Solutions[](https://about.gitlab.com/direction/verify/pipeline_composition/#top-123-competitive-solutions)
##### Github Actions[](https://about.gitlab.com/direction/verify/pipeline_composition/#github-actions)
Our main competitor doing innovative things in terms of pipeline authoring is GitHub, who have evolved Actions into more and more of a standalone CI/CD solution. GitLab remains far ahead in a lot of areas of CI/CD that they are going to have to catch up on, but Microsoft and GitHub have a lot of resources and have a large user base excited to use their product, especially when given away as part of a package. Actions has a more event-driven and community plugin-based approach than GitLab, whereas we take community contributions directly into the product where they can be maintained.
GitHub actions are a seemingly powerful toolkit with a high potential for low maintainability with community contributions as we have seen with Jenkins. We are monitoring to swiftly incorporate the best of their innovation into our product. We've already had some successes [running GitHub Actions directly in GitLab CI](https://gitlab.com/snippets/1988376) and will continue to explore that. We are also working on a [migration guide](https://gitlab.com/gitlab-org/gitlab/-/issues/228937) to help teams we're hearing from who are looking to move over to GitLab have an easier time. Features like [making the script section in containers optional](https://gitlab.com/gitlab-org/gitlab/-/issues/223203) would make it easier to build reusable plugins within GitLab that would behave more like Actions and [Allow `needs:` to refer to a job in the same stage](https://gitlab.com/gitlab-org/gitlab/-/issues/30632) to enable users to run an entire pipline without defining stages.
A limitation of the [GitHub Actions API](https://docs.github.com/en/rest/reference/actions) is the exclusiveness interaction with the service via a workflow YAML checked into a repository. By contrast, GitLab enables users to define units of work to execute as a service, for example, via [mutli-project pipelines](https://docs.gitlab.com/ee/ci/multi_project_pipelines.html), [dynamic child pipelines](https://docs.gitlab.com/ee/ci/parent_child_pipelines.html#dynamic-child-pipelines) and [parent-child pipelines](https://docs.gitlab.com/ee/ci/parent_child_pipelines.html).
Watch this walkthrough video of Github actions
##### Circle CI[](https://about.gitlab.com/direction/verify/pipeline_composition/#circle-ci)
Circle CI is a Continuous Integration platform that builds a robust process for using and contributing Orbs. Circle CI Orbs are reusable snippets of code packages as YAML configuration condenses repeated pieces of config into a single line of code. Once an orb is created, it could be published to the orb registry, which becomes available to any of the Circle CI user base.
Watch this walkthrough video of the different contribution frameworks available by GitHub Marketplace, Circle CI and CodeFresh.io.
##### Gitea Actions[](https://about.gitlab.com/direction/verify/pipeline_composition/#gitea-actions)
[Gitea Actions](https://blog.gitea.io/2022/12/feature-preview-gitea-actions/) implements a similar event based system like GitHub Actions for CI/CD. The infrastructure features a runner, actions orchestration subsystem, and the action definition.
### Target Audience[](https://about.gitlab.com/direction/verify/pipeline_composition/#target-audience)
Check out our [CI Section Direction "Who is it for?"](https://about.gitlab.com/direction/ci/#who-is-it-for) for an in depth look at the our target personas across Ops. For Pipeline Authoring, our "What's Next & Why" are targeting the following personas, as ranked by priority for support:
  1. [Priyanka - Platform engineer](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)
  2. [Devon - DevOps Engineer](https://handbook.gitlab.com/handbook/product/personas/#devon-devops-engineer)
  3. [Sasha - Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)


### Analyst Landscape[](https://about.gitlab.com/direction/verify/pipeline_composition/#analyst-landscape)
The Gartner Magic Quadrant evaluates leadership of Continuous Integration offerings within the [DevOps Platforms](https://about.gitlab.com/gartner-magic-quadrant/) landscape. GitLab is a leader in this space and this category aims to sustain our position in this by defending our strong hold in the following spaces:
  * Parallel builds
  * Multistage pipelines
  * Container Native CI
  * Build Caching


[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/verify/pipeline_composition/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/verify/pipeline_composition/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fverify%2Fpipeline_composition%2F&_biz_t=1773332005208&_biz_i=%0ACategory%20Direction%20-%20Pipeline%20Composition%0A%7C%0AGitLab%0A&_biz_n=100&rnd=464386&cdn_o=a&_biz_z=1773332005324)
suggested results