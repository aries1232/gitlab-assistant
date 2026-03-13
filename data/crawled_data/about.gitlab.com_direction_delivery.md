#  Delivery Direction 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. Delivery Direction


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Overview](https://about.gitlab.com/direction/delivery/#overview)
    * [What is Continuous Delivery?](https://about.gitlab.com/direction/delivery/#what-is-continuous-delivery)
    * [What is Continuous Deployment?](https://about.gitlab.com/direction/delivery/#what-is-continuous-deployment)
  * [GitLab's Delivery Vision](https://about.gitlab.com/direction/delivery/#gitlabs-delivery-vision)
  * [Jobs To Be done](https://about.gitlab.com/direction/delivery/#jobs-to-be-done)
    * [Market](https://about.gitlab.com/direction/delivery/#market)
  * [Product principles](https://about.gitlab.com/direction/delivery/#product-principles)
  * [Strategy](https://about.gitlab.com/direction/delivery/#strategy)
  * [Key Capabilities for Delivery](https://about.gitlab.com/direction/delivery/#key-capabilities-for-delivery)
  * [GitLab Current Delivery Capabilities](https://about.gitlab.com/direction/delivery/#gitlab-current-delivery-capabilities)
    * [Focus for Q4 FY26 (Through January 2026)](https://about.gitlab.com/direction/delivery/#focus-for-q4-fy26-through-january-2026)


DevSecOpsPlanCodeBuildTestReleaseDeployOperateMonitorSecurityCompliance
Configure
Release
## Overview[](https://about.gitlab.com/direction/delivery/#overview)
The delivery direction covers the deployment and release features and capabilities in GitLab and two related concepts, Continuous Delivery and Continuous Deployment. Delivery is composed of two parts, deployment and release. Deployment covers the processes and actions needed to deploy a new version of the software to a target infrastructure. This includes both production and non-production infrastructures. Release includes the processes and actions needed to make a deployed application available to users. This encompasses both the packaging of code artifacts with associated metadata and the orchestration of making those changes accessible to end users.
### What is Continuous Delivery?[](https://about.gitlab.com/direction/delivery/#what-is-continuous-delivery)
Continuous Delivery(CD) tools automate the process of delivering code changes to target environments (development, test, production) reliably and efficiently, typically after passing quality or compliance checks when the target is a production environment.
### What is Continuous Deployment?[](https://about.gitlab.com/direction/delivery/#what-is-continuous-deployment)
Continuous Deployment goes one step further than Continuous Delivery. In Continuous Deployment, every change that goes through a deployment pipeline is automatically promoted to production, resulting in many production deployments every day.
## GitLab's Delivery Vision[](https://about.gitlab.com/direction/delivery/#gitlabs-delivery-vision)
GitLab's Delivery vision is to make sophisticated deployment automation accessible to every developer, for every - platform, everywhere.
We will accomplish this by
  1. Empowering [Priyanka (Platform Engineer)](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer) and [Ingrid (Infrastructure Operator)](https://handbook.gitlab.com/handbook/product/personas/#allison-application-ops) to define and automate DevOps practices that have security and compliance guard rails built directly into the process.
  2. Provide integrations, tools and frameworks for Priyanka and Ingrid that they can use without customizations or can fine-tune to provide a delivery platform for their users.
  3. The delivery platform managed by Priyanka and Ingrid should enable developers to own their specific deployment operations without toil, increase their confidence in their delivery processes and support Day-2 operations.
  4. Taking advantage of the data available in the connected GitLab platform, from planning input, artifact storage to observability and incident data, to make release operations, such as scaling rollouts or rollbacks automatic.


## Jobs To Be done[](https://about.gitlab.com/direction/delivery/#jobs-to-be-done)
For Developers:
  * When using the development platform, I want to be more productive by not having to spend time figuring out how to deploy yet enable them to comply with security and compliance requirements.
  * When releasing updates, I feel confident my changes will not disrupt the existing environment and I know exactly what will be impacted.
  * When delivering my application, it doesn't matter if I am delivering to legacy servers or to Kubernetes, it all just works.


For Platform Engineers:
  * When operating the development platform, I do not want to slow down the development teams and limit what they need to do to improve and deploy their service so that there's no downside to using the platform.
  * When operating the development platform, I empower engineers while retaining control with RBAC, Audit trails, secret management, progressive delivery, and auto-scaling deployments and rollbacks.
  * When configuring my delivery pipelines I can decide the people and teams with rights to deploy and release, so the pipeline can adhere to my organization's policies and regulatory requirements.
  * When looking for improvements in the delivery process, I can understand how my organization is performing, so that I can pinpoint actionable improvement areas.


For Operations:
  * When managing my environments, I want to see and understand what is currently running, so that I can make decisions on what I need to do.


We created [a glossary](https://about.gitlab.com/direction/delivery/glossary.html) to discuss related terms in a consistent way.
### Market[](https://about.gitlab.com/direction/delivery/#market)
The delivery tooling market is evolving and expanding. There are now many more options than just adding a deployment job to your CI/CD pipeline. Release Orchestration, advanced releases, GitOps, infrastructure provisioning, platform as a service, progressive delivery, and feature flags are all methodologies that help teams deliver software more easily, frequently, and confidently. Completeness of feature sets from vendors is becoming increasingly important as teams want the benefits from all worlds; traditional, table stakes deployment features alongside modern, differentiating features.
To increase deployment frequency and be competitive in the market, enterprises have turned to [centralized cloud teams or cloud center of excellence](https://gitlab.com/gitlab-com/Product/-/issues/2287#note_526578502) that are responsible for helping [development teams be more efficient and productive](https://gitlab.com/gitlab-com/Product/-/issues/2287#note_526579050). These teams have centralized buying power for DevOps and delivery tools. They may also have organizational support to build a DIY DevOps platform. For cloud-native DIY platforms, we've found (through customer interviews) that open-source point deployment solutions (such as [Flux](https://fluxcd.io/) or [ArgoCD](https://argoproj.github.io/argo-cd/)) are the primary options because of their focus on cloud-native principles and early adoption of pull-based deployment. These tools often come with auxiliary tooling for release management, like [Flagger](https://fluxcd.io/flagger/) and [Argo Rollouts](https://argoproj.github.io/argo-rollouts/) Otherwise, enterprises, even existing GitLab customers, sometimes buy commercial tools for deployment, such as Octopus, Harness, and CloudBees electric flow.
The market leading enterprise CD platforms of the future must include the following core capabilities: automated deployment pipeline orchestration, compliance frameworks, automated approval gates, integration with multiple artifact repositories, environment management, integration with Agentic AI systems, support for easily configured advanced deployment strategies (blue-green, canary, rolling updates) feature flag support, observability, comprehensive audit trails and audit logging.
## Product principles[](https://about.gitlab.com/direction/delivery/#product-principles)
**Modern, Developer-Friendly Experience**
  * We aim to simplify deployment configuration and management, reducing the hundreds of lines of custom YAML that platform engineers currently maintain while preserving flexibility for advanced use cases.


**Compliance-Ready by Design**
  * Security and compliance guardrails are built into the process from the start, enabling teams to meet regulatory requirements without sacrificing velocity.


**First-Class Auditing and Accountability**
  * With AI agents increasingly initiating deployments, comprehensive audit trails showing which entity (human or agent) triggered each production deployment become critical for organizations of all sizes.


**Enterprise ready
  * While we want to provide supporting products for every company size, we expect enterprise users to have special needs that our integrated approach can serve well.


## Strategy[](https://about.gitlab.com/direction/delivery/#strategy)
In Delivery, our primary persona is [Priyanka (Platform Engineer)](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer). They are responsible for setting up the systems that development teams use to develop, test, **ship** , and **operate** their applications. They - likely - work at an enterprise where there is a mix of delivery targets from VMs to Kubernetes and bare metal to cloud infrastructure. They also face the challenges of ever-increasing complexity; as more contributors, more services, more infrastructure, more databases, and a mix of technologies are added to their applications. They are looking for ways to create a system to manage the complexity at scale, and especially to present the necessary parts of this complexity to their users, the application operators.
In line with Priyanka's users, our most important secondary persona is [Allison (Application Operator)](https://handbook.gitlab.com/handbook/product/personas/#allison-application-ops).
As our primary target customers are enterprise customers, we want to make sure that regulatory and compliance requirements related to application delivery are covered from the start. As a result, we pay special attention to the needs of [Cameron (Compliance Manager)](https://handbook.gitlab.com/handbook/product/personas/#cameron-compliance-manager) and [Rachel (Release Manager)](https://handbook.gitlab.com/handbook/product/personas/#rachel-release-manager).
and [Ingrid (Infrastructure Operator)](https://handbook.gitlab.com/handbook/product/personas/#ingrid-infrastructure-operator).
## Key Capabilities for Delivery[](https://about.gitlab.com/direction/delivery/#key-capabilities-for-delivery)
Enterprises are increasingly choosing to have a [cloud-first strategy](https://gitlab.com/gitlab-com/Product/-/issues/2287#note_526573920). Furthermore, with the increasing adoption of microservices architecture and infrastructure as code, traditional release tools are inadequate. This, coupled with the traditional delivery requirements of governance, compliance, and security, means that delivery tools have to meet a high bar and address a set of evolving technology and compliance requirements. The primary themes for these capabilities are that first organizations need **collaboration and transparency** , then **control and compliance** and before requiring **measurement and advanced patterns**. We list these key capabilities of deployment platforms in **priority order of user need** :
**Collaboration and Transparency**
  1. **Environment management:** Organizations typically operate multiple [environments](https://docs.gitlab.com/ee/ci/environments/), each serving different needs. Delivery tools should help to make managing environments easy and intuitive.
  2. **Everything as code:** Delivery tooling, including pipelines, releases, infrastructure, environments, and monitoring tools, are constantly evolving. If they can be stored as code and version-controlled, it will enable organizations to more effectively collaborate and avoid costly mistakes.


**Control and Compliance**
  1. **GitOps:** Simply checking code into a repository will not prevent drift to occur between code and what is deployed. [GitOps](https://about.gitlab.com/topics/gitops/) solves this problem by automatically managing changes using the single source of truth reflected in the source repository providing more control by preventing drift.
  2. **Release Orchestration & Quality gates:** Organizations need to control what can be deployed and in which sequence. Enabling reviews and approvals built right into the deployment workflow and supporting policy tools is a critical requirement. The ability to perform automatic rollback, environment freeze, and scaling deployment also enables organizations to be more in control.


**Measurement and Advanced Patterns**
  1. **Feedback:** Delivery is a critical part of the DevOps feedback loop. A successful release depends on immediate feedback from Monitoring and Observability tools to ensure a healthy rollout. Furthermore, knowing that a delivery was successful is not just about knowing whether the application deployed is healthy, it also requires understanding the impact to downstream neighbors and the environment as a whole.
  2. **Reporting:** Understanding how the DevOps team and the entire organization is performing, such as using the DORA metrics, is important to enable iteration towards stronger performance.
  3. **Progressive delivery:** Delivery can be risky. To mitigate risks, progressive delivery techniques, such as using feature flags, canary and rolling deployments can help mitigate the risk by limiting the impact until the delivery teams are confident that their changes are good to go.


## GitLab Current Delivery Capabilities[](https://about.gitlab.com/direction/delivery/#gitlab-current-delivery-capabilities)
GitLab has a market-leading CI/CD solution. Deployments and releases using GitLab's CI/CD pipelines work well for many use cases. GitLab users love the developer enablement provided by our robust pipeline definition language, but they find it painful to write and manage hundreds of lines of code to describe their custom delivery logic. Similarly, orchestrating large deployments across projects is painful with GitLab. This complexity is exacerbated by the complexity of infrastructure and the delivery domain. Customers today look for alternative solutions, like FluxCD to hide some of the complexity from software engineering teams.
**Independent software deliveries** - for the delivery of individual projects that can be deployed in an automated fashion without coordination, developers deploy using CI/CD pipelines in the following ways:
  * Writing [customized pipeline definitions](https://docs.gitlab.com/ee/ci/yaml/gitlab_ci_yaml.html)
    * Custom pipeline can take advantage of functionalities made available in containers, including [ones published by GitLab](https://about.gitlab.com/blog/deploy-aws/)
  * [Including](https://docs.gitlab.com/ee/ci/yaml/includes.html) pipeline definitions provided by their platform teams
  * Using GitLab provided deployment [templates](https://docs.gitlab.com/ee/ci/examples/#cicd-templates) (such as Pages, AWS, Fastlane, Serverless, 5 Minute App, etc)
  * Utilizing GitLab's [AutoDevOps](https://docs.gitlab.com/ee/topics/autodevops/) defined deployment process
  * Relying on offered [Terraform support](https://docs.gitlab.com/ee/user/infrastructure/iac/)


**Kubernetes deployments** - for deployments to Kubernetes, we have support for pull-based GitOps via the [Kubernetes Agent and FluxCD](https://docs.gitlab.com/ee/user/clusters/agent/), while push-based GitOps is supported by [CI/CD tunnel](https://docs.gitlab.com/ee/user/clusters/agent/ci_cd_workflow.html). Supporting both push- and pull-based deployments, GitLab can be used to migrate to full GitOps approaches of Kubernetes management and can support even dynamic use cases that pull-based only approaches struggle supporting.
**Visualising deployment status** - once a deployment reaches its target infrastructure, application operators want to make sure that it's running smoothly and serves its users, and they want to be able to troubleshoot issues if needed. GitLab offers a minimal UI to show the status of deployments in Kubernetes.
**Orchestrated delivery** - for complex releases, particularly those that require [orchestration](https://about.gitlab.com/direction/delivery/) across multiple projects, release managers use [Releases](https://docs.gitlab.com/ee/user/project/releases/) to gather artifacts. Sometimes release managers collaborate on the delivery process using GitLab's release.
**Continuous Delivery** - many industries have strict regulatory requirements to follow that direct them to Continuous Delivery practices. GitLab supports Continuous Delivery via [Protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html) and [Deployment approval rules](https://docs.gitlab.com/ee/ci/environments/deployment_approvals.html).
None of these methods are duplicative and each serves different use cases.
### Focus for Q4 FY26 (Through January 2026)[](https://about.gitlab.com/direction/delivery/#focus-for-q4-fy26-through-january-2026)
To build toward the future vision, we're first ensuring our existing capabilities are stable and reliable. For Q4 FY26 (November 2025 - January 2026), we're focused on critical maintenance work including reducing severity 1-2 bugs and addressing technical debt in the Deploy stage.
Simultaneously, we're incorporating enterprise customer feedback to refine our delivery roadmap and ensure our next phase of development addresses the most pressing market needs.
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/delivery/index.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/delivery/index.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fdelivery%2F&_biz_t=1773331840187&_biz_i=%0ADelivery%20Direction%0A%7C%0AGitLab%0A&_biz_n=64&rnd=984121&cdn_o=a&_biz_z=1773331840383)
suggested results