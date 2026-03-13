#  Product Section Direction - Platforms 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. Product Section Direction - Platforms


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Mission](https://about.gitlab.com/direction/platforms/#mission)
  * [Platforms section overview](https://about.gitlab.com/direction/platforms/#platforms-section-overview)
    * [Why use SaaS?](https://about.gitlab.com/direction/platforms/#why-use-saas)
    * [DevSecOps using a single Platform](https://about.gitlab.com/direction/platforms/#devsecops-using-a-single-platform)
    * [Target personas](https://about.gitlab.com/direction/platforms/#target-personas)
    * [Why a Platforms section?](https://about.gitlab.com/direction/platforms/#why-a-platforms-section)
    * [How does Product Management support this direction?](https://about.gitlab.com/direction/platforms/#how-does-product-management-support-this-direction)
    * [Metrics](https://about.gitlab.com/direction/platforms/#metrics)
    * [Competitive space and position](https://about.gitlab.com/direction/platforms/#competitive-space-and-position)
  * [3-year strategy](https://about.gitlab.com/direction/platforms/#3-year-strategy)
  * [Themes](https://about.gitlab.com/direction/platforms/#themes)
    * [Move towards self-service frameworks](https://about.gitlab.com/direction/platforms/#move-towards-self-service-frameworks)
    * [Easily assess the impact of changes](https://about.gitlab.com/direction/platforms/#easily-assess-the-impact-of-changes)
    * [Scalable architectures for single-tenant and multi-tenant platforms](https://about.gitlab.com/direction/platforms/#scalable-architectures-for-single-tenant-and-multi-tenant-platforms)
    * [Drive cost efficiency](https://about.gitlab.com/direction/platforms/#drive-cost-efficiency)
  * [What we're not doing](https://about.gitlab.com/direction/platforms/#what-were-not-doing)
  * [Sections](https://about.gitlab.com/direction/platforms/#sections)
  * [Categories](https://about.gitlab.com/direction/platforms/#categories)
  * [What's Next](https://about.gitlab.com/direction/platforms/#whats-next)


Last reviewed: 2024-03-31
## Mission[](https://about.gitlab.com/direction/platforms/#mission)
**Everyone can access the best version of GitLab that meets their needs.**
Platforms provides the best version of GitLab to our customers. We create multi- and single-tenant GitLab platforms - with a focus on compliance, security, and performance. We also empower GitLab product development groups to deploy, monitor and operate their code reliably across all of our platforms, with the ultimate goal of increased efficiency and productivity.
Using capabilities built by the Platforms section, customers and internal product development can focus on delivering customer value at any scale and have a great experience with GitLab.
## Platforms section overview[](https://about.gitlab.com/direction/platforms/#platforms-section-overview)
### Why use SaaS?[](https://about.gitlab.com/direction/platforms/#why-use-saas)
GitLab is available in three deployment methods: Self-managed, multi-tenant SaaS (commonly referred to as GitLab.com), and our single-tenant SaaS solution GitLab Dedicated.
Our multi-tenant SaaS platform, GitLab.com, provides the easiest and quickest way to adopt GitLab and the lowest overall total cost of ownership. GitLab.com is targeted at early adopting Mid Market, SMB and ICs.
GitLab Dedicated, our single-tenant SaaS platform, provides strong tenant isolation, private networking, and is available in specific regions. GitLab Dedicated is targeted at large enterprises in regulated industries with strict compliance needs.
Our SaaS offerings make up an [increasing percentage of revenue](https://ir.gitlab.com/node/7861/html) and we see further growth opportunities because of the benefits of SaaS for our customers. For this reason, we continue to advance our [GitLab-hosted first](https://about.gitlab.com/direction/#gitlab-hosted-first) theme.
### DevSecOps using a single Platform[](https://about.gitlab.com/direction/platforms/#devsecops-using-a-single-platform)
For our product development community, including the wider GitLab community, developing the single DevSecOps Platform poses specific challenges depending on the deployment platform. For SaaS platforms, it is critical that code can run reliably and at different types of scale. This is also becoming more important for self-managed deployments as our [reference architectures can support tens of thousands of users](https://docs.gitlab.com/ee/administration/reference_architectures/).
Software developers, however, cannot easily reproduce the same scale in their developer environments, nor is it feasible for them to anticipate all workload variations found in production environments. Other personas may also struggle. For example, Software Engineers in Test may not be able to identify the root causes of problems because of a lack of visibility and monitoring. This can lead to slower iterations, and unexpected behaviors. Ultimately, this has a negative impact on our customers because we can't provide value to them fast enough.
GitLab the product, is the leading DevSecOps Platform, but GitLab as a company still uses a number of DIY solutions for DevSecOps in combination with our own product. The Platforms section aims to create tools, services, and frameworks that make building and deploying GitLab a delightful experience on any hardware at any scale. Once added, these tools will push GitLab as a company from [Phase 3 to Phase 4](https://about.gitlab.com/topics/devops/) of DevSecOps. This creates a virtuous cycle where the capabilities developed in the Platforms section will ultimately benefit all of our customers - also known as [dogfooding](https://handbook.gitlab.com/handbook/values/#dogfooding).
![Virtuous development cycle](https://about.gitlab.com/direction/platforms/platform-virtous-cycle.png)
Developers should be empowered to roll out their changes themselves frequently, with a minimal lead time for change, short time to recover and a low change failure rate. Without great frameworks and services, developers have no way to operate their code and take ownership of the entire DevSecOps lifecycle. This in turn also creates a number of process inefficiencies, such as increased need for handoffs with other stakeholders (e.g. Infrastructure, Security, etc.).
One side-effect of a growing number of handoffs is that this requires that the Infrastructure, and Security teams grows in lockstep with the organizational growth. While that investment needs to continue, this should support an increase in efficiency and productivity over the long term.
At GitLab, we know the solution already because we build it: DevSecOps using a single Platform approach.
### Target personas[](https://about.gitlab.com/direction/platforms/#target-personas)
We target product development tools with the most important personas being:
  * Site Reliability engineers (tools, services, frameworks)
  * Software developers (tools, services, frameworks)
  * Engineering Managers, Product Managers, Executive Leadership (metrics and roll ups)


### Why a Platforms section?[](https://about.gitlab.com/direction/platforms/#why-a-platforms-section)
GitLab has a number of delivery channels. Apart from customer-managed setups, GitLab manages a multi-tenant (GitLab.com) and single-tenant ([GitLab Dedicated](https://docs.gitlab.com/ee/subscriptions/gitlab_dedicated/)) customer facing platforms.
This means that customers can be operators, administrators, or simply consumers of GitLab's feature set. This creates different expectations, and Product Development at GitLab needs to develop code that can run successfully on any platform.
For GitLab-managed offerings, there are two dimensions of scale with slightly different expectations:
  1. For GitLab.com, a single GitLab instance needs to receive rapid changes, features that scale with a large number of requests, and serve significantly varied workflows. This requires a more hands on approach because issues need to be mitigated as they happen, and rolled forward or back as required.
  2. For GitLab Dedicated, a large number of independent GitLab instances need to receive changes in a more predictably paced environment, with focus on stability and predictability to match the type of workloads expected with a single tenant offering.


These requirements for GitLab.com and GitLab Dedicated make it critical that teams can take full ownership of features and utilize DevSecOps best practices. This in turn requires fully utilizing GitLab as the One DevSecOps Platform - and improving it where it falls short.
The Platforms section is needed to empower our own development groups and drive a virtuous improvement cycle for GitLab. Platforms put a great product development experience front and center and aims to reduce costly hand-offs to the infrastructure department.
Creating a minimal viable platform is also cost-efficient. By moving towards DevSecOps, we should be able to better drive efficiencies in how we develop and deliver changes to SaaS over the long term. Platform teams should scale sub-linearly to the rest of GitLab product development.
### How does Product Management support this direction?[](https://about.gitlab.com/direction/platforms/#how-does-product-management-support-this-direction)
We strongly believe that the Platforms stage is a product stage. [Platforms teams are product teams](https://www.linkedin.com/pulse/platform-teams-product-niels-talens), with their own product development cycles. When building out developer tools/services e.g. error budgets we should treat this first and foremost as product development. The users are GitLab's product development groups first. When these services become part of GitLab they will service all of our customers.
By adopting a product-focused mindset, we avoid building out solutions that don't address our users' needs and can utilize our [established product development framework](https://handbook.gitlab.com/handbook/product-development-flow/).
### Metrics[](https://about.gitlab.com/direction/platforms/#metrics)
As one of Platforms missions is to help GitLab's product development groups to deploy, monitor and operate code at scale, the well known DORA 4 metrics are what measures success:
[DORA 4 metrics](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance):
  1. Deployment Frequency - how often can we deploy to production
  2. Lead time for changes - time from commit to production
  3. Change Failure rate - Percentage of failed deployments
  4. Time to Restore Service - How long it takes to recover from failure


GitLab already [implements DORA metrics](https://docs.gitlab.com/ee/user/analytics/#devops-research-and-assessment-dora-key-metrics)
### Competitive space and position[](https://about.gitlab.com/direction/platforms/#competitive-space-and-position)
The Platforms section is expected to roll out valuable changes to customers at a rapid pace without introducing instability. By allowing product groups to take full ownership of their code and improving our DORA metrics, we ensure that GitLab does not fall behind other competitors in the space. Aligning all parts of GitLab's Development teams with DevSecOps best practices will ensure our competitiveness.
## 3-year strategy[](https://about.gitlab.com/direction/platforms/#3-year-strategy)
In three years, we want to move GitLab's Product Development groups to utilize GitLab as the single DevSecOps Platform to deploy, monitor and operate any changes on our platforms. This means, for example, that functionalities provided by runbooks should become part of the one DevSecOps Platform.
## Themes[](https://about.gitlab.com/direction/platforms/#themes)
### Move towards self-service frameworks[](https://about.gitlab.com/direction/platforms/#move-towards-self-service-frameworks)
Without product development groups able to self-service, they can get blocked and require other teams to support them. To avoid this, Platforms focuses on creating better frameworks.
Moving towards self-service delivery. Backporting changes to prior GitLab self-managed releases should not require input from the Delivery group. Instead, developers should be able to manage the entire backporting lifecycle for their changes, and Delivery group would ensure that this process is executed smoothly.
Moving towards utilizing pre-built frameworks. Developers should utilize existing building blocks that ensure their code is production ready, like uniformly using a pre-made logging framework, or importing the existing code necessary for their feature to interact with uploads storage layer.
### Easily assess the impact of changes[](https://about.gitlab.com/direction/platforms/#easily-assess-the-impact-of-changes)
Deploying changes at scale means that many things can go wrong that were not easy to test locally. By providing automatic reports, error budgets and other tools it should be simple for developers to understand the impact changes have on productions.
Defining SLIs and SLOs is also critical to ensure that incentives are aligned and developers understand how much failure is acceptable.
### Scalable architectures for single-tenant and multi-tenant platforms[](https://about.gitlab.com/direction/platforms/#scalable-architectures-for-single-tenant-and-multi-tenant-platforms)
GitLab's SaaS platforms are growing rapidly. By evolving our SaaS architectures we ensure that we can keep up with [GitLab's expected growth (internal)](https://internal.gitlab.com/handbook/product/investment/scaling-model/).
### Drive cost efficiency[](https://about.gitlab.com/direction/platforms/#drive-cost-efficiency)
Deploying features can be very costly on production. We aim to make it simpler for product teams to evaluate and measure the cost impact of their features. This ensure that we remain [efficient](https://handbook.gitlab.com/handbook/values/#efficiency) at scale.
## What we're not doing[](https://about.gitlab.com/direction/platforms/#what-were-not-doing)
  * Building micro-services outside of GitLab
  * Creating more processes and hand-off points.


## Sections[](https://about.gitlab.com/direction/platforms/#sections)
  * [Tenant Scale](https://about.gitlab.com/direction/runtime/)


## Categories[](https://about.gitlab.com/direction/platforms/#categories)
  * [GitLab.com](https://about.gitlab.com/direction/platforms/dotcom/)
  * [GitLab Delivery](https://about.gitlab.com/direction/gitlab_delivery/)
  * [Scalability](https://about.gitlab.com/direction/production_engineering/)
  * [GitLab Dedicated](https://about.gitlab.com/direction/gitlab_dedicated/)
  * [Switchboard](https://about.gitlab.com/direction/platforms/switchboard/)


## What's Next[](https://about.gitlab.com/direction/platforms/#whats-next)
[See the Platforms section page lists for currently active initiatives](https://handbook.gitlab.com/handbook/engineering/infrastructure/platforms/).
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/platforms/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/platforms/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fplatforms%2F&_biz_t=1773332159587&_biz_i=%0AProduct%20Section%20Direction%20-%20Platforms%0A%7C%0AGitLab%0A&_biz_n=133&rnd=84679&cdn_o=a&_biz_z=1773332159747)
suggested results