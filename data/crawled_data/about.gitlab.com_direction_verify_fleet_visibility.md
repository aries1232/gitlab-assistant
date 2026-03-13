#  Category Direction - Fleet Visibility 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Verify Stage Direction](https://about.gitlab.com/direction/verify/)
  4. Category Direction - Fleet Visibility


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
## Navigation & Settings[](https://about.gitlab.com/direction/verify/fleet_visibility/#navigation--settings)
|   
---|---  
Stage | [Verify](https://about.gitlab.com/direction/verify/)  
Maturity | Complete  
Content Last Reviewed | `2025-09-05`  
## Introduction and how you can help[](https://about.gitlab.com/direction/verify/fleet_visibility/#introduction-and-how-you-can-help)
Thanks for visiting this direction page on the Fleet Visibility category at GitLab. This page belongs to the [Runner Group](https://handbook.gitlab.com/handbook/product/categories/#runner-group) within the Verify Stage and is maintained by Darren Eastman.
## Strategy and Themes[](https://about.gitlab.com/direction/verify/fleet_visibility/#strategy-and-themes)
As the GitLab AI native DevSecOps transforms development workflows, GitLab Fleet Visibility empowers organizations to manage CI/CD infrastructure at scale through intelligent, unified observability that eliminates operational blind spots and accelerates software delivery.
## The Challenge We Solve[](https://about.gitlab.com/direction/verify/fleet_visibility/#the-challenge-we-solve)
Development teams struggle with CI/CD performance issues buried in fragmented tooling, while platform administrators lack the visibility needed to optimize build infrastructure costs and reliability. This disconnect creates developer friction, inflated cloud costs, and time wasted on custom observability solutions.
### Our Solution[](https://about.gitlab.com/direction/verify/fleet_visibility/#our-solution)
Fleet Visibility delivers comprehensive CI/CD observability through two integrated dashboards:
**[Fleet Dashboard](https://docs.gitlab.com/ci/runners/runner_fleet_dashboard/)** provides platform administrators with:
  * Real-time runner fleet status (online, offline, stale) across all build servers
  * Runner utilization patterns, queue performance, and failure rate analytics
  * Runner compute minutes usage by group and projects for cost optimization


**[CI/CD Analytics](https://docs.gitlab.com/user/analytics/ci_cd_analytics/)** gives developers project-level visibility into:
  * Pipeline execution metrics (duration, failure rates, queue times)
  * Job-level performance trends and bottleneck identification
  * Build environment correlation for faster troubleshooting


### The Impact[](https://about.gitlab.com/direction/verify/fleet_visibility/#the-impact)
**For Development Teams:** Faster issue resolution and optimized CI/CD performance through actionable insights that eliminate guesswork in pipeline optimization.
**For Platform Teams:** Data-driven infrastructure decisions that reduce costs, improve reliability, and deliver exceptional developer experiences without custom dashboard development.
**For Executives:** Operational confidence that your AI-powered DevSecOps platform scales efficiently across any cloud infrastructure while maximizing development velocity and controlling costs.
### 1 year plan[](https://about.gitlab.com/direction/verify/fleet_visibility/#1-year-plan)
**Runner Fleet Dashboard**
The [Runner Fleet Dashboard - Admin View: Starter Metrics](https://gitlab.com/gitlab-org/gitlab/-/issues/424495) was released in 16.5. The included metrics widgets for the initial release are as follows:
  * Fleet Health (Postgres DB)
  * Top Active Runners (Postgres DB)
  * Wait Time to Pick up a Job (Clickhouse DB)


We followed this up by releasing the [Runner Fleet Dashboard for Groups](https://docs.gitlab.com/ee/ci/runners/runner_fleet_dashboard_groups.html) in the GitLab 17.1 release. With this release, customers on GitLab.com and Self Managed can manage runner fleets at the group level. We have heard from many customers that they need this capability and related APIs to augment the current observability tooling and custom dashboards they rely on to monitor and operate GitLab CI/CD and Runners. Therefore, we will enable access to the data via GraphQL APIs for those customers who need to integrate the CI metrics with data from their internal systems to enable organization-specific analytics.
We plan to [gather and analyze customer feedback](https://gitlab.com/gitlab-org/gitlab/-/issues/421737) over the next few months based on the current features in the Fleet Dashboard. That feedback will guide the next evolution of the Fleet Dashboard strategy into calendar year 2025. While we have already identified additional metrics, such as runner failure trends, that could be valuable to include in the dashboard, it is also likely, based on recent customer feedback, that simply extending the metrics data model and enabling customers to create their reports and visualizations is the most valuable future iteration.
Regarding prediction, one prevalent theme in customer conversations is determining when there may be a slowdown in runner queue performance. Another critical problem and pain point often cited by customers is configuring the Runner Fleet to find the optimal balance between compute costs and developer efficiency as measured by reduced CI/CD job durations. These are classic prediction problems, so we aim to explore if we can reduce the cost of prediction and fleet operational costs for our customers by incorporating ML/AI into the Fleet Dashboard. With Clickhouse as the database layer and a new analytics database table structure for Runner Fleet, we believe the foundational elements are in place to make this next evolution a reality in FY26.
Also, based on many customer conversations, operating a CI/CD build fleet on Kubernetes can be complex. Platform engineering teams sometimes must spend months configuring and optimizing the Kubernetes environment to reliably run their organization's CI/CD jobs. For new users of GitLab, this configuration and optimization effort can be a critical blocker to CI adoption.
In Runner Core, we have seen the immense value to platform teams of simply enabling the printing of Kubernetes events directly in the CI/CD job log. So, we are exploring the following questions:
  * How can we expose the right metrics for the Kubernetes CI/CD build infrastructure in the Fleet Dashboard?
  * Will exposing the right Kubernetes stack infrastructure metrics and associating that data with the CI/CD job metrics reduce the operational burden for customers who use Kubernetes as the CI/CD build infrastructure?


We aim to explore these questions in depth in planning the Fleet Dashboard's future roadmap.
Our vision is that the next evolution of cloud-native CI/CD will automatically self-optimize across the entire workflow—from the GitLab CI pipeline configuration to the Runner Kubernetes CI/CD build infrastructure stack.
**CI/CD Analytics**
The first phase in the unified Developer Efficiency strategy is solving the critical visibility problems developers and platform administrators have with using GitLab CI/CD. Those visibility problems include the fact that there is no built-in report in [GitLab CI/CD analytics](https://docs.gitlab.com/ee/user/analytics/ci_cd_analytics.html) for a developer to determine if a CI job is running as expected from a duration perspective or whether a CI job is unhealthy, as represented by an increase in job failures. As a result, customers have had to create custom reporting systems or implement third-party observability tools using data exposed in the GitLab jobs API.
Our objective for the second half of FY26 is to further enhance the newly updated GitLab CI/CD analytics view by incorporating CI/CD job performance metrics. Providing visibility into all aspects of CI/CD job performance is only the foundation. We intend to develop solutions using this data that eliminate developer pain and frustration related to slow CI/CD job start times and suboptimal CI/CD job durations. Another critical goal is to eliminate lost developer productivity from troubleshooting CI/CD job failures that are not a result of code changes
#### What is next for us[](https://about.gitlab.com/direction/verify/fleet_visibility/#what-is-next-for-us)
In the next three months (September - November 2025) we are focused on the following:
**CI/CD Analytics**
#### What we are currently working on[](https://about.gitlab.com/direction/verify/fleet_visibility/#what-we-are-currently-working-on)
  * We are currently working on adding the CI/CD job metrics to the [GitLab CI/CD analytics view](https://gitlab.com/gitlab-org/gitlab/-/issues/453956).


#### What we recently completed[](https://about.gitlab.com/direction/verify/fleet_visibility/#what-we-recently-completed)
  * In GitLab 18.0, we released the new [GitLab CI/CD analytics view](https://docs.gitlab.com/ee/user/analytics/ci_cd_analytics.html) that provides a unified view of CI/CD job performance metrics, including job duration and job failure rates. This is the first step in our strategy to provide developers with insights into their CI/CD jobs and enable them to optimize their workflows.


#### What is Not Planned Right Now[](https://about.gitlab.com/direction/verify/fleet_visibility/#what-is-not-planned-right-now)
In calendar year 2025, our priority is enhancing [CI pipeline observability at the project level](https://gitlab.com/groups/gitlab-org/-/epics/18548). Throughout this period, we'll actively collect customer feedback to identify the most valuable metrics and features for our Fleet Dashboard FY27+ roadmap for [Admins](https://docs.gitlab.com/ci/runners/runner_fleet_dashboard/) and [Groups](https://docs.gitlab.com/ci/runners/runner_fleet_dashboard_groups/).
### Best in Class Landscape[](https://about.gitlab.com/direction/verify/fleet_visibility/#best-in-class-landscape)
BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.
At GitLab, a critical challenge is simplifying the administration and management of a CI/CD build fleet at an enterprise scale and enabling developer efficiency. This effort is one foundational pillar to realizing the vision of GitLab Duo AI-optimized DevSecOps. Competitors are also investing in this general category. Earlier this year GitHub announced a new management experience that provides a summary view of GitHub-hosted runners. This is a signal that there will be a focus on reducing maintenance and configuration overhead for managing a CI/CD build environment at scale across the industry.
We also now see additional features on the GitLab public roadmap signaling an increased investment in the category we coined here at GitLab, 'Runner Fleet.' These features suggest that GitHub aims to provide a first-class experience for managing GitHub Actions runners and include features in the UI to simplify runner queue management and resolve performance bottlenecks. With this level of planned investment, it is clear that there is recognition in the market that simplifying the administrative maintenance and overhead of the CI build fleet is critical for large customers and will help enable deeper product adoption.
Indirect competitor Actutated is the first solution that we have seen whose product includes a [dashboard for Runners and build queue](https://docs.actuated.dev/dashboard/#runners) visibility. This is another strong signal that providing solutions that reduce the CI/CD build infrastructure's management overhead is valuable for organizations with mature DevOps practices.
In the CI Insights arena, a few startups, for example, [Trunk.io](https://trunk.io/ci-analytics), are providing CI visibility solutions for GitHub actions. The [Datadog CI Visbility product](https://www.datadoghq.com/product/ci-cd-monitoring/) is a mature, full-featured offering that provides CI/CD insights for GitLab CI/CD using the GitLab jobs API as the foundational layer.
To ensure that our GitLab customers can fully realize the value of GitLab's one DevSecOps platform vision, we must provide solutions that eliminate the complexities, manual tasks, and operational overhead and reduce the costs of delivering a CI build environment at scale. Our goal in FY25 is to introduce the basic building blocks for in-product developer efficiency visibility. These solutions will be good enough for customers who are not fully invested in third-party observability or custom tooling, allowing them to observe, analyze, optimize, or troubleshoot CI job failures natively in GitLab. However, the end state is that we will deliver GitLab native solutions that eliminate the impact on developer efficiency related to all aspects of reliable CI/CD job execution.
#### Key Capabilities[](https://about.gitlab.com/direction/verify/fleet_visibility/#key-capabilities)
The key capabilities that we hear from customers describing fleet management and CI insights pain points are as follows:
  * What is the root cause of a CI pipeline failure?
  * CI/CD job failure rate trends
  * CI/CD job duration trends
  * CI/CD job retry rate trends
  * Determine when test jobs started failing.
  * Diagnose whether a test is Flaky versus failing consistently.
  * Runner queue visibility (wait time)
  * Frictionless upgrades
  * Security
  * Cost visibility for runners hosted on public cloud infrastructure
  * Fleet autoscaling
  * Fleet cost management while maintaining internal service level objectives (SLOs)
  * Automatic fleet configuration optimization
  * Managing runner sprawl
  * Configuring and managing a heterogeneous runner fleet (container builds on Linux, container builds on Windows, shell builds on Windows, shell builds on macOS)
  * Self-service runner creation for the developer persona
  * Automating choosing the right cloud and compute to host a Runner based on CI/CD build performance


#### Top [1/2/3] Competitive Solutions[](https://about.gitlab.com/direction/verify/fleet_visibility/#top-123-competitive-solutions)
Runner Fleet is still a nascent category; competitors like GitHub are beginning to invest in this area. On their future roadmap, GitHub plans to introduce [seamless management of GitHub-hosted and self-hosted runners](https://github.com/github/roadmap/issues/504). This feature aims to deliver a "single management plane to manage all runners for a team using GitHub." GitHub also plans to offer [Actions Performance Metrics](https://github.com/github/roadmap/issues/561) to provide organizations with deep insights into critical CI/CD performance metrics.
One example of how the cloud infrastructure market can evolve is [Active Assist for Google Cloud](https://cloud.google.com/solutions/active-assist) - a solution to optimize cloud operations cost reduction. Another is the recently [announced Komodor product - KlaudiaAI](https://komodor.com/blog/introducing-klaudiaai-redefining-kubernetes-troubleshooting/), which uses generative AI models to generate root cause analysis automatically and recommended fixes for issues on Kubernetes. Therefore we can imagine a future where Microsoft and GitHub bring to market AI-based solutions that use AI to more efficiently run GitHub Actions Runners on Azure infrastructure.
Our GitLab competitive position is solid in that we will continue to invest in features and capabilities to ensure that customers can use GitLab Runners efficiently on any cloud provider.
In the insights space DataDog has a [CI and Test Visibility](https://docs.datadoghq.com/continuous_integration/) offering and [CircleCI](https://circleci.com/docs/insights/) has had an insights offering for some time. While there is no main GitHub actions functionality there are several offerings in the marketplace for collecting test/run data and displaying it on a dashboard.
[Harness.io, Software Engineering Insights](https://developer.harness.io/docs/software-engineering-insights) includes several configurable [CI/CD job](https://developer.harness.io/docs/software-engineering-insights/sei-metrics-and-reports/velocity-metrics-reports/ci-cd-reports) and pipeline metric widgets. The [CI/CD job count](https://developer.harness.io/docs/software-engineering-insights/sei-metrics-and-reports/velocity-metrics-reports/ci-cd-reports#job-count-reports) metric category aims to provide developers with insights into CI/CD job success and failure rates. We also see additional investment planned by [Harness.io](https://developer.harness.io/roadmap/#platform) with their Pipeline Analytics feature slated for Q3 2024 (August 2024+).
CloudBees has the [CI Workload Insights dashboard](https://docs.cloudbees.com/docs/cloudbees-cd/latest/dashboards-built-in/workload-insights) that includes `workload deviation`, `mean wait time`, `mean wait time deviation`, `job failure rate deviation`, and `job duration deviation` metrics.
In the Test Reduction area Sealights offers a [CutTests](https://www.sealights.io/solutions/cut-end-to-end-tests-cycle-time/) solution and [Redefine.dev](https://www.redefine.dev/product) is a new player in the space taking advantage of AI to reduce future test runs for faster pipelines.
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/verify/fleet_visibility/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/verify/fleet_visibility/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fverify%2Ffleet_visibility%2F&_biz_t=1773332013319&_biz_i=%0ACategory%20Direction%20-%20Fleet%20Visibility%0A%7C%0AGitLab%0A&_biz_n=102&rnd=397665&cdn_o=a&_biz_z=1773332013448)
suggested results