#  Category Direction - Infrastructure as Code 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Delivery Direction](https://about.gitlab.com/direction/delivery/)
  4. Category Direction - Infrastructure as Code


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Infrastructure as Code](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#infrastructure-as-code)
    * [Market overview](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#market-overview)
  * [Vision](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#vision)
  * [Strategy](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#strategy)
    * [Pricing Strategy](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#pricing-strategy)
    * [Today](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#today)
      * [Terraform/OpenTofu strategy](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#terraformopentofu-strategy)
    * [Next up](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#next-up)
    * [Later up](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#later-up)
  * [Target User](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#target-user)
    * [Jobs](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#jobs)
    * [Interaction with Policy as Code](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#interaction-with-policy-as-code)
    * [Current status and what's next](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#current-status-and-whats-next)
      * [Collaboration support](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#collaboration-support)
      * [Managed Terraform state](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#managed-terraform-state)
      * [Terraform module registry](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#terraform-module-registry)
    * [Analyst Landscape](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#analyst-landscape)
    * [Top Customer Success/Sales issue(s)](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#top-customer-successsales-issues)
    * [Top user issue(s)](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#top-user-issues)
    * [Top internal customer issue(s)](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#top-internal-customer-issues)
    * [Competitors](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#competitors)
      * [CloudSkiff](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#cloudskiff)
      * [HashiCorp Terraform Enterprise](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#hashicorp-terraform-enterprise)
      * [env0](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#env0)
    * [Examples](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#examples)


## Infrastructure as Code[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#infrastructure-as-code)
[Infrastructure as code](https://about.gitlab.com/topics/gitops/infrastructure-as-code/) (IaC) is the practice of managing and provisioning infrastructure through machine-readable definition files, rather than managing physical hardware configuration or interactive configuration tools. The IT infrastructure managed by IaC can range from physical equipment such as bare-metal servers to virtual machines to other associated configuration resources. The definitions of the infrastructure are stored in a version control system, and changes are often applied automatically. IaC takes proven coding techniques and extends them to your infrastructure directly, effectively blurring the line between what is an application and what is the environment.
  * [Issue List](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name%5B%5D=Category%3AInfrastructure%20as%20Code)
  * [Overall Vision](https://about.gitlab.com/direction/delivery/)
  * [UX Research](https://gitlab.com/groups/gitlab-org/-/epics/595)


### Market overview[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#market-overview)
According to [Gartner](https://drive.google.com/file/d/1DjsnkQxozkOONAFNLlZaJ5QHzaaY3Lcx/view), Infrastructure and Operations (I&O) automation was the second most common investment target in 2021. Adoption is often led by a move to the cloud. Furthermore, IaC provisioning of **on-prem** infrastructure is also gaining momentum, with an expected rise from 5% to 40% between 2020 and 2023.
Despite the intention, one large obstacle remains for widespread adoption: the lack of skilled developers in the area.
By providing easy-to-use primitives and with a focus on good developer experience, GitLab is well-positioned to break down the obstacles of infrastructure as code adoption.
## Vision[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#vision)
Every software runs on some type of infrastructure. This infrastructure needs to be provisioned, secured, managed and finally destroyed. GitLab users receive an integrated solution for all their infrastructure oriented tasks and processes in a single application.
We imagine GitLab to provide outstanding support for the most often used Infrastructure as Code tools (Terraform and Crossplane) for Platform Engineers, Application Operators and Software Developers. GitLab provides different abstractions for each persona, as a result, Platform Engineers can create infrastructure stacks templates that are easy and straightforward to use by Application Operators and Software Developers.
Once an infrastructure is provisioned, GitLab users can observe their stacks within GitLab and get notified about insecure components.
## Strategy[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#strategy)
### Pricing Strategy[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#pricing-strategy)
We focus most of our features in GitLab Free. Non-Free features are focused around reporting, access rights, security and compliance requirements.
### Today[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#today)
GitLab already offers strong integrations with Terraform in the form of the GitLab Managed Terraform state backend, the Merge Request widget, the Terraform module registry and the GitLab Terraform provider.
**We don't work actively on this category given other priorities.** We are still encouraging community contributions, especially around [Open Policy Agent integration](https://gitlab.com/gitlab-org/gitlab/-/issues/205913) for Policy as Code and the [GitLab Terraform provider](https://github.com/gitlabhq/terraform-provider-gitlab).
We are in the [process of checking the category maturity](https://gitlab.com/gitlab-com/Product/-/issues/3651) and [moving the Terraform registry over to the Package team](https://gitlab.com/gitlab-org/gitlab/-/issues/364718).
#### Terraform/OpenTofu strategy[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#terraformopentofu-strategy)
We aim to support current and future Terraform users as much as possible following the Terraform license changes. This means that the following features remain supported with Terraform:
  * GitLab Managed Terraform States
  * Terraform module registry with a helper CI/CD template
  * Terraform plan Merge Request integration
  * GitLab Terraform provider


At the same time, we added support to OpenTofu. As in its current form OpenTofu is a drop-in replacement for Terraform, all the previously mentioned features are supported with OpenTofu as well. Moreover, we are offering an OpenTofu CI/CD component to simplify all the supported Infrastructure as Code workflows through GitLab pipelines.
We are going to revisit our Terraform strategy when there are breaking changes in either solution that require us to either invest more into these areas or to remove one of them.
### Next up[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#next-up)
We want to improve all the existing features:
  * by providing [more granular control of Terraform states](https://gitlab.com/gitlab-org/gitlab/-/issues/227108)
  * by providing [more information about expected infrastructure changes in Merge Requests](https://gitlab.com/groups/gitlab-org/-/epics/3441)
  * by providing [usage insights about modules and supporting module upgrades driven by module authors](https://gitlab.com/groups/gitlab-org/-/epics/5639)


### Later up[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#later-up)
Beside Terraform, as our Kubernetes features strenghten, we consider adding [support for Crossplane](https://gitlab.com/gitlab-org/gitlab/-/issues/346186) to manage cloud infrastructure in a fully declarative way.
## Target User[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#target-user)
With GitLab's Infrastructure as Code support - in the order of importance - we are targeting:
  * Platform Engineers, who are in charge of providing the infrastructure for production and non-production environments
  * Application Operators and Software Engineers who focus on a few applications and want those to be deployed, monitored and integrated into their infrastructure following company standards
  * Development Team Leaders, who want low-friction tools in their development processes and have to fulfill various reporting needs


### Jobs[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#jobs)
During our customer interviews, we identified the following core jobs:
### Interaction with Policy as Code[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#interaction-with-policy-as-code)
As Infrastructure as Code usage scales across teams [collaboration pain points around security, compliance and adopting best practices arise](https://www.youtube.com/watch?v=Vy8s7AAvU6g&amp=&feature=youtu.be). Traditionally these pain points are solved by written documentation. Modern infrastructure as code applications have implemented Policy as Code tools to enable automated checking of infrastructure definitions against easy to write policy definitions. One prime example of this is [Hashicorp's Sentinel](https://www.hashicorp.com/sentinel/).
The principles of Policy as Code are closely aligned with Infrastructure as Code. Within GitLab our existing primitives of integrated CI with _CI job definition in-code_ model similar behavior to modern Policy as Code frameworks. At present our existing CI approach allows easy integration of special Policy as Code tools and GitLab. The primary difference with policy as code is the separation of duties, namely the appearance of a new persona, the compliance manager.
### Current status and what's next[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#current-status-and-whats-next)
Today, GitLab's infrastructure as code support is at "Viable" maturity, and we are in the process of validating for "Complete" maturity. We offer deep integrations with Terraform in the form of
#### Collaboration support[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#collaboration-support)
Collaboration around Infrastructure as Code is more involved than generic collaboration around code is, because every code change has a direct effect on the underlying infrastructure. To support IaC collaboration workflows, we have developed the Terraform Merge Request widget.
We plan to [extend the widget with more insights](https://gitlab.com/groups/gitlab-org/-/epics/3441) and have it integrated with the Managed Terraform state.
#### Managed Terraform state[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#managed-terraform-state)
We would like to provide GitLab users with an unmatched Terraform experience. This involves a Terraform backend that integrates with GitLab pipelines without any setup from the user, and allows advanced state management from within GitLab. GitLab provides a versioned, encrypted Terraform state backend and templates to get started with it. The state backend removes every friction around starting a new Terraform project, and streamlines the complexity of infrastructure to manage.
We have many ideas planned to provide even more funtionality and a better experience around the GitLab Managed Terraform state.
  * [Protected state files support](https://gitlab.com/gitlab-org/gitlab/-/issues/227108) will allow a fine tuned access to various state files managed in a project.
  * [Management interfaces](https://gitlab.com/gitlab-org/gitlab/-/issues/271591) are planned to support debugging infrastructure issues on the UI.


Please contribute to [our plans in the related epic](https://gitlab.com/groups/gitlab-org/-/epics/2673).
#### Terraform module registry[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#terraform-module-registry)
For larger infrastructures, re-usable modules are a call part of the IaC codebase. We provide a Terraform module registry as part of GitLab by extending the current module registries. We plan to add insights into modules usage for module owners. This should help around deprecations and risk management of modules.
Please, contribute to our plans around the registry in the [Terraform registry Epic](https://gitlab.com/groups/gitlab-org/-/epics/3221)
### Analyst Landscape[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#analyst-landscape)
We don't consider GitLab a replacement of IaC tools, but rather a complement. Based on several discussions, we consider Terraform the _de facto_ standard of infrastructure provisioning, and we want to support Terraform based workflows.
Given the trends around containerization, ephemeral and immutable infrastructures, we expect the relevance of configuration management tools to decrease, and infrastructure provisioning to gain more market share.
### Top Customer Success/Sales issue(s)[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#top-customer-successsales-issues)
As already mentioned, we've several customers using IaC solutions with GitLab. The following list shows our primary points of contacts for customer interviews around IaC.
  * Wag!
  * kiwi.com
  * Ooma
  * GitLab


### Top user issue(s)[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#top-user-issues)
[The most popular user issues are listed in GitLab](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name\[\]=Category%3AInfrastructure%20as%20Code).
### Top internal customer issue(s)[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#top-internal-customer-issues)
  * [Use the GitLab Managed Terraform state for gitlab.com](https://gitlab.com/gitlab-com/gl-infra/infrastructure/-/issues/10179)


### Competitors[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#competitors)
#### CloudSkiff[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#cloudskiff)
CloudSkiff describes itself as a CI/CD for Terraform, on steroids.
#### HashiCorp Terraform Enterprise[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#hashicorp-terraform-enterprise)
We consider HashiCorp to be a partner, not a competitor, and we do not support many advanced features offered by Terraform Enterprise.
#### env0[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#env0)
env0 describes itself as a way to manage, deploy, and scale Terraform and other infrastructure as code frameworks
### Examples[](https://about.gitlab.com/direction/delivery/infrastructure_as_code/#examples)
  * [How GitLab uses Terraform](https://about.gitlab.com/topics/gitops/gitlab-enables-infrastructure-as-code/) internally
  * [Kiwi.com on Infrastructure as Code](https://www.youtube.com/watch?v=Un2mJrRFSm4) at GitLab Commit London, 2019
  * Presenting [code.siemens.com](https://www.youtube.com/watch?v=4Y8zv1TJRlM) at GitLab Commit London, 2019


[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/delivery/infrastructure_as_code/index.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/delivery/infrastructure_as_code/index.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fdelivery%2Finfrastructure_as_code%2F&_biz_t=1773331726614&_biz_i=%0ACategory%20Direction%20-%20Infrastructure%20as%20Code%0A%7C%0AGitLab%0A&_biz_n=39&rnd=921286&cdn_o=a&_biz_z=1773331726819)
suggested results