#  Category Direction - Continuous Integration 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Verify Stage Direction](https://about.gitlab.com/direction/verify/)
  4. Category Direction - Continuous Integration


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Continuous Integration](https://about.gitlab.com/direction/verify/continuous_integration/#continuous-integration)
    * [Overview](https://about.gitlab.com/direction/verify/continuous_integration/#overview)
    * [Strategy and Themes](https://about.gitlab.com/direction/verify/continuous_integration/#strategy-and-themes)
    * [1 year plan](https://about.gitlab.com/direction/verify/continuous_integration/#1-year-plan)
      * [What is next for us](https://about.gitlab.com/direction/verify/continuous_integration/#what-is-next-for-us)
      * [What we are currently working on](https://about.gitlab.com/direction/verify/continuous_integration/#what-we-are-currently-working-on)
      * [What we recently completed](https://about.gitlab.com/direction/verify/continuous_integration/#what-we-recently-completed)
      * [What is Not Planned Right Now](https://about.gitlab.com/direction/verify/continuous_integration/#what-is-not-planned-right-now)
    * [Best in Class Landscape](https://about.gitlab.com/direction/verify/continuous_integration/#best-in-class-landscape)
      * [Key Capabilities](https://about.gitlab.com/direction/verify/continuous_integration/#key-capabilities)
    * [Target Audience](https://about.gitlab.com/direction/verify/continuous_integration/#target-audience)


## Continuous Integration[](https://about.gitlab.com/direction/verify/continuous_integration/#continuous-integration)
|   
---|---  
Stage | [Verify](https://about.gitlab.com/direction/verify/)  
Maturity | Competitive  
Content Last Reviewed | `2025-10-31`  
Maintained By | Rutvik Shah (rutshah@gitlab.com)  
### Overview[](https://about.gitlab.com/direction/verify/continuous_integration/#overview)
Continuous Integration is an important part of any software development lifecycle. We recognize a key advantage of GitLab CI is that we can define pipelines as code, while making CI easy to use, reliable, and accurate in terms of its results. We are very proud that we are recognized as [a leader in DevOps Platforms](https://about.gitlab.com/gartner-magic-quadrant) in the Gartner Magic Quadrant, as well as a leader in [Forrester's Wave: DevOps Platform](https://about.gitlab.com/blog/gitlab-named-a-leader-in-the-forrester-wave-devops-platforms-q2-2025/).
For specific information and features related to authoring pipelines, check out [Pipeline Authoring](https://about.gitlab.com/direction/verify/pipeline_composition/).
You may also be looking for one of the following related product direction pages: [Overall Vision of the Verify stage](https://about.gitlab.com/direction/ops/#verify) and [GitLab Runner](https://about.gitlab.com/direction/verify/runner_core/).
### Strategy and Themes[](https://about.gitlab.com/direction/verify/continuous_integration/#strategy-and-themes)
Our strategy focuses on delivering advanced CI/CD capabilities while providing enterprise-grade solutions that scale with your organization's needs. We believe in making automation accessible to all teams, then delivering advanced capabilities that promote greater efficiency and governance without compromising on security as your DevSecOps maturity grows.
### 1 year plan[](https://about.gitlab.com/direction/verify/continuous_integration/#1-year-plan)
For FY26 (ending February 2026):
We will be maintaining our Continuous Integration functionality with a focused approach:
  * Bug Resolution: Prioritizing critical S1/S2 issues that have exceeded their service level objectives
  * Community Collaboration: Actively supporting community contributions that enhance this category.
  * Feature Development: We will focus on delivering the following capabilities
    * [Improve parent/child pipeline experience with the ability to show security reports from a child pipelines in Merge Request Widget](https://gitlab.com/gitlab-org/gitlab/-/issues/504109)
    * [Real time pipeline/jobs status update](https://gitlab.com/groups/gitlab-org/-/epics/16394)


#### What is next for us[](https://about.gitlab.com/direction/verify/continuous_integration/#what-is-next-for-us)
  * Critical S1/S2 issues that have exceeded their service level objectives
  * Continue rolling out real time pipeline/jobs status updates.


#### What we are currently working on[](https://about.gitlab.com/direction/verify/continuous_integration/#what-we-are-currently-working-on)
We are currently focusing on:
  1. Critical S1/S2 issues that have exceeded their service level objectives
  2. Investigating why [job timeouts are not working](https://gitlab.com/gitlab-org/gitlab-runner/-/issues/27040#top) in some cases


#### What we recently completed[](https://about.gitlab.com/direction/verify/continuous_integration/#what-we-recently-completed)
The top deliverables from the Pipeline Execution group over the last quarter are:
  1. [Ability to filter by [job name](https://gitlab.com/gitlab-org/gitlab/-/issues/387547#top) and [trigger jobs](https://gitlab.com/gitlab-org/gitlab/-/issues/555434)
  2. [Ability to be notified for failed scheduled pipelines when an owner is deactivated](https://gitlab.com/gitlab-org/gitlab/-/issues/36806#top)


#### What is Not Planned Right Now[](https://about.gitlab.com/direction/verify/continuous_integration/#what-is-not-planned-right-now)
  * CI related [notifications](https://gitlab.com/groups/gitlab-org/-/issues?label_name%5B%5D=notifications&label_name\[\]=group%3A%3Apipeline%20execution) (by email or via integration with other tools)
  * CI related [API endpoints](https://gitlab.com/gitlab-org/gitlab/-/issues?label_name%5B%5D=api&label_name%5B%5D=group%3A%3Apipeline+execution&state=opened) (unless related to features on the roadmap)
  * CI related [permissions](https://gitlab.com/gitlab-org/gitlab/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name\[\]=CI%20permissions&label_name\[\]=group%3A%3Apipeline%20execution&not\[label_name\]\[\]=bug) (non-bug issues)
  * [Configure CI/CD Quotas by project](https://gitlab.com/gitlab-org/gitlab/-/issues/357760) going forward we will work with the community to review and merge contributions but are not planning active development on new features.


### Best in Class Landscape[](https://about.gitlab.com/direction/verify/continuous_integration/#best-in-class-landscape)
BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.
#### Key Capabilities[](https://about.gitlab.com/direction/verify/continuous_integration/#key-capabilities)
  * [Pipelines as code](https://about.gitlab.com/solutions/continuous-integration/)
  * [Scheduled triggering of pipelines](https://docs.gitlab.com/ee/ci/pipelines/schedules.html)
  * [Trigger pipeline on any event in code repository](https://docs.gitlab.com/ee/ci/triggers/)
  * [CI/CD Horizontal Autoscaling](https://docs.gitlab.com/runner/configuration/autoscale.html#overview)
  * [Live streaming of logs from running pipeline](https://docs.gitlab.com/ee/ci/jobs/#expand-and-collapse-job-log-sections)
  * [CI/CD for external repo](https://docs.gitlab.com/ee/ci/ci_cd_for_external_repos/)


### Target Audience[](https://about.gitlab.com/direction/verify/continuous_integration/#target-audience)
For Continuous Integration, our "What's Next & Why" are targeting the following personas, as ranked by priority for support:
  1. [Sasha - Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
  2. [Priyanka - Platform Engineer](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)
  3. [Delaney - Development Team Lead](https://handbook.gitlab.com/handbook/product/personas/#delaney-development-team-lead)


[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/verify/continuous_integration/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/verify/continuous_integration/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fverify%2Fcontinuous_integration%2F&_biz_t=1773331722404&_biz_i=%0ACategory%20Direction%20-%20Continuous%20Integration%0A%7C%0AGitLab%0A&_biz_n=38&rnd=530151&cdn_o=a&_biz_z=1773331722554)
suggested results