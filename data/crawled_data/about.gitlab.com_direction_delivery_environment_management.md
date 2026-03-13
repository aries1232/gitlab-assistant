#  Category Direction - Environment Management 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Delivery Direction](https://about.gitlab.com/direction/delivery/)
  4. Category Direction - Environment Management


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Environment Management](https://about.gitlab.com/direction/delivery/environment_management/#environment-management)
    * [Introduction and how you can help](https://about.gitlab.com/direction/delivery/environment_management/#introduction-and-how-you-can-help)
    * [Overview](https://about.gitlab.com/direction/delivery/environment_management/#overview)
    * [Strategy and Themes](https://about.gitlab.com/direction/delivery/environment_management/#strategy-and-themes)
    * [1 year plan](https://about.gitlab.com/direction/delivery/environment_management/#1-year-plan)
      * [What is next for us](https://about.gitlab.com/direction/delivery/environment_management/#what-is-next-for-us)
      * [What we are currently working on](https://about.gitlab.com/direction/delivery/environment_management/#what-we-are-currently-working-on)
      * [What we recently completed](https://about.gitlab.com/direction/delivery/environment_management/#what-we-recently-completed)
      * [What is Not Planned Right Now](https://about.gitlab.com/direction/delivery/environment_management/#what-is-not-planned-right-now)
    * [Best in Class Landscape](https://about.gitlab.com/direction/delivery/environment_management/#best-in-class-landscape)
      * [Key Capabilities](https://about.gitlab.com/direction/delivery/environment_management/#key-capabilities)
      * [Roadmap](https://about.gitlab.com/direction/delivery/environment_management/#roadmap)
      * [Top [1/2/3] Competitive Solutions](https://about.gitlab.com/direction/delivery/environment_management/#top-123-competitive-solutions)
    * [Target Audience](https://about.gitlab.com/direction/delivery/environment_management/#target-audience)
    * [Pricing and Packaging](https://about.gitlab.com/direction/delivery/environment_management/#pricing-and-packaging)
    * [Analyst Landscape](https://about.gitlab.com/direction/delivery/environment_management/#analyst-landscape)


## Environment Management[](https://about.gitlab.com/direction/delivery/environment_management/#environment-management)
|   
---|---  
Stage | [Deploy](https://about.gitlab.com/direction/delivery/)  
Maturity | [Viable](https://about.gitlab.com/direction/#maturity)  
Content Last Reviewed | `2023-04-06`  
### Introduction and how you can help[](https://about.gitlab.com/direction/delivery/environment_management/#introduction-and-how-you-can-help)
Welcome to the direction page of the Environment Management product category of GitLab. This page is part of the bigger [Delivery direction](https://about.gitlab.com/direction/delivery/). It is owned by the Environments group and is maintained by Viktor Nagy (Email).
Your feedback helps us building a world-class environment management offering in GitLab. We welcome your feedback in [issues](https://gitlab.com/groups/gitlab-org/-/issues/?sort=updated_desc&state=opened&label_name%5B%5D=Category%3AEnvironment%20Management&first_page_size=20), [epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name\[\]=Category:Environment+Management) and are always open to user interviews to learn more about your use cases or share more details about our roadmap. You can register a call with us through your GitLab account manager or through customer support.
### Overview[](https://about.gitlab.com/direction/delivery/environment_management/#overview)
Environments are at the heart of DevSecOps. From the application developers' perspective, environments are where the application gets deployed. Environments can differ in terms of lifespan, related change management processes, and policies. Some environments are short-lived, ephemeral, while others are long lived. Production environments are the place where your applications meet your users.
Environments are the culmination of the work of several teams and are the place where the application will finally serve its users. As a result, they should present their current state and related artifacts to support critical decisions in security, rollout and troubleshooting.
The key aspects of environments are:
  * Ops users and organizations can easily see and take action on deployments
  * Deep integration with target infrastructure e.g. Kubernetes
  * Compatible with all types of application architectures (e.g. monorepo, microservices, etc)
  * Answers key questions such as: 
    * What is deployed to production?
    * Who deployed to production?
    * What deployments to production happened in the past 30 days?
    * What is deployed to other environments?
    * What is the health and status of my deployment environments?
  * Easily execute key actions such as: 
    * Rollbacks / Rollouts
    * Deployment / Feature Flag toggling
    * Promote from lower environments to higher environments such as production
  * Benefits 
    * Tool consolidation
    * Connect to other capabilities in GitLab. Note: Deployment relies on nearly all upstream activities in GitLab so this is an important place for these types of connections.


### Strategy and Themes[](https://about.gitlab.com/direction/delivery/environment_management/#strategy-and-themes)
Environments are as central to a DevSecOps organization as Merge requests are to a Dev organization. We envision GitLab environments to serve as the single entry point to every information and action related to a given environment from status data to security reports and actions related to new release rollouts and troubleshooting.
As GitLab offers solutions for the whole DevSecOps lifecycle, we want to visualise data to environments on the environment pages. The environment page should show
  * the deployment status
  * the application metrics


related to the running deployment(s) together with information about
  * the artifacts behind these deployments
  * related security scans.


Release managers should be able to rely on environment pages to gather all the information they need to block or move a release forward. Moreover, they should be able to do it from within the environment pages. The rollout might involve running a dedicated CI/CD job in a pipeline or changing a feature flag. Either should be supported. The GitLab [Continuous delivery direction](https://about.gitlab.com/direction/delivery/continuous_delivery/) provides more details on our plans to support release managers, and the [Feature flags direction](https://about.gitlab.com/direction/delivery/feature_flags/) descibes our strategy and plans related to feature flags.
As Environments typically include deployments, this direction is best read together with the [Deployment management direction](https://about.gitlab.com/direction/delivery/deployment_management/).
While Environments can be best interacted with through the GitLab UI, we see that highly efficient teams prefer chat-based, integrated solutions for at least some of the functionality. While ChatOps is not a priority now, it partially falls under the environment management category.
### 1 year plan[](https://about.gitlab.com/direction/delivery/environment_management/#1-year-plan)
We are in the process of [building up our roadmap](https://gitlab.com/groups/gitlab-org/ci-cd/deploy-stage/environments-group/-/epics/1) to work towards the vision described above. Some items we already know to be on this roadmap are
  * Add support for [group-level environments](https://gitlab.com/groups/gitlab-org/-/epics/7558).
  * Provide a [Kubernetes dashboard](https://gitlab.com/groups/gitlab-org/-/epics/2493) in GitLab
  * [Deployment detail page MVC](https://gitlab.com/gitlab-org/gitlab/-/issues/374538)
  * [Connect Releases with Environments and Deployments](https://gitlab.com/gitlab-org/gitlab/-/issues/332103)
  * [Log auto stop environment actions](https://gitlab.com/gitlab-org/gitlab/-/issues/36047)


#### What is next for us[](https://about.gitlab.com/direction/delivery/environment_management/#what-is-next-for-us)
  * We want to [run a design sprint](https://gitlab.com/groups/gitlab-org/ci-cd/deploy-stage/environments-group/-/epics/1) to drive our roadmap forward.
  * We are [adding Environments support to the GitLab Agent](https://gitlab.com/groups/gitlab-org/-/epics/9859).


#### What we are currently working on[](https://about.gitlab.com/direction/delivery/environment_management/#what-we-are-currently-working-on)
  * We are [adding Environments support to the GitLab Agent](https://gitlab.com/groups/gitlab-org/-/epics/9859).
  * We are working on modernizing the environment page frontend by [moving from HAML to Vue](https://gitlab.com/groups/gitlab-org/-/epics/9489).


#### What we recently completed[](https://about.gitlab.com/direction/delivery/environment_management/#what-we-recently-completed)
  * We switched the approval rules settings UI from universal approval rules to [multiple approval rules](https://docs.gitlab.com/ee/ci/environments/deployment_approvals.html#multiple-approval-rules). We found multiple approval rules to better serve our users and we are in the process of deprecating universal approval rules.


#### What is Not Planned Right Now[](https://about.gitlab.com/direction/delivery/environment_management/#what-is-not-planned-right-now)
We don't plan to
  * extend our chatops support


### Best in Class Landscape[](https://about.gitlab.com/direction/delivery/environment_management/#best-in-class-landscape)
BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.
#### Key Capabilities[](https://about.gitlab.com/direction/delivery/environment_management/#key-capabilities)
The key capabilities of environment management applications are
  * provide up-to-date information about environment status, including 
    * which deployments are currently running
    * related infromation to deployments, like attestations, scan results, milestones
  * support troubleshooting with entry points to 
    * logs
    * metrics
    * traces
  * create and tear-down ephemeral environments, including the related infrastructure
  * visualize the deployment and roll-out related processes in a pipeline
  * allow to describe the delivery process and environments as declarative code (aka YAML)
  * provide interfaces to release managers for continuous delivery practices


#### Roadmap[](https://about.gitlab.com/direction/delivery/environment_management/#roadmap)
**This section is work in progress.**
#### Top [1/2/3] Competitive Solutions[](https://about.gitlab.com/direction/delivery/environment_management/#top-123-competitive-solutions)
  * [Harness.io](https://www.harness.io/)
  * [Kubevela](https://kubevela.io/) built on the [Open Application Model](https://oam.dev/)
  * [Release](https://release.com/)


### Target Audience[](https://about.gitlab.com/direction/delivery/environment_management/#target-audience)
Primary persona:
  * [Allison, application operator](https://handbook.gitlab.com/handbook/product/personas/#allison-application-ops)


Secondary personas:
  * [Rachel, release manager](https://handbook.gitlab.com/handbook/product/personas/#rachel-release-manager)


### Pricing and Packaging[](https://about.gitlab.com/direction/delivery/environment_management/#pricing-and-packaging)
**This section is work in progress.**
### Analyst Landscape[](https://about.gitlab.com/direction/delivery/environment_management/#analyst-landscape)
**This section is work in progress.**
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/delivery/environment_management/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/delivery/environment_management/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fdelivery%2Fenvironment_management%2F&_biz_t=1773332036558&_biz_i=%0ACategory%20Direction%20-%20Environment%20Management%0A%7C%0AGitLab%0A&_biz_n=107&rnd=435772&cdn_o=a&_biz_z=1773332036706)
suggested results