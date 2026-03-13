#  Category Direction - Runner Core 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Verify Stage Direction](https://about.gitlab.com/direction/verify/)
  4. Category Direction - Runner Core


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
## Navigation & Settings[](https://about.gitlab.com/direction/verify/runner_core/#navigation--settings)
|   
---|---  
Stage | [Verify](https://about.gitlab.com/direction/verify/)  
Maturity | Lovable  
Content Last Reviewed | `2025-12-05`  
### Introduction and how you can help[](https://about.gitlab.com/direction/verify/runner_core/#introduction-and-how-you-can-help)
Thanks for visiting this direction page on the Runner Core category at GitLab. This page belongs to the [Runner Group](https://handbook.gitlab.com/handbook/product/categories/#runner-group) within the Verify Stage and is maintained by Gabriel Engel.
### Strategy and Themes[](https://about.gitlab.com/direction/verify/runner_core/#strategy-and-themes)
#### Vision[](https://about.gitlab.com/direction/verify/runner_core/#vision)
  * Our vision is to deliver a universal GitLab CI/CD build agent that seamlessly operates across any compute architecture and technology stack. We empower platform administrators and developers with effortless installation and configuration of GitLab Runner, enabling them to execute CI/CD workloads at any scale on infrastructure perfectly aligned with their unique software development requirements.


#### Context[](https://about.gitlab.com/direction/verify/runner_core/#context)
  * GitLab Runner - the near-ubiquitous build agent that executes CI jobs on a target compute platform is a critical foundational pillar of GitLab's [one DevSecOps platform vision](https://about.gitlab.com/direction/#vision). The fundamental problems customers must solve in this product category include installing, [configuring](https://gitlab.com/groups/gitlab-org/-/epics/17592), and scaling CI/CD build agents (runners) on public or private cloud infrastructure and securely executing CI/CD jobs on heterogeneous computing architectures, x86-64, ARM, and s390x.
  * For customers that run millions of CI/CD jobs monthly, the primary GitLab Runner autoscaling options for CI/CD builds in ephemeral, isolated environments are Kubernetes and public cloud or on-premise virtual machine environments. Therefore, critical needs for this customer segment include consistently fast start times for builds, fast build times as measured by total wall clock time, low CI build failure rates due to runner or runner host infrastructure issues, and minimal operational overhead. Other customers require seamless support for multi-platform and architecture builds, while others need the flexibility to install a build agent according to their organization's security and compliance policies


### 1 year plan[](https://about.gitlab.com/direction/verify/runner_core/#1-year-plan)
Our major investment themes for GitLab Fiscal Year 2026 are as follows:
  * Improved SLO attainment for GitLab Runner bug resolution.
  * [GitLab Runner Kubernetes Executor enhancements](https://gitlab.com/groups/gitlab-org/-/epics/12691).


### What is next for us[](https://about.gitlab.com/direction/verify/runner_core/#what-is-next-for-us)
In the next three months we plan to deliver these features or capabilities:
  * Quality initative -reduce overdue bugs assigned to `group::runner`
  * [Add fault tolerance to the Runner K8s executor - attach strategy](https://gitlab.com/gitlab-org/gitlab-runner/-/issues/36951)
  * [Phase 1: GitLab Runner Job Router - Admission Control](https://gitlab.com/groups/gitlab-org/-/work_items/19607)


### What we are currently working on[](https://about.gitlab.com/direction/verify/runner_core/#what-we-are-currently-working-on)
We are working on the [fault tolerance feature](https://gitlab.com/gitlab-org/gitlab-runner/-/issues/36951) for the Runner Kubernetes executor.
### What we recently completed[](https://about.gitlab.com/direction/verify/runner_core/#what-we-recently-completed)
  * [Expose a duration histogram for the runner prepare stage](https://gitlab.com/gitlab-org/gitlab-runner/-/issues/37471)
  * [Autoscaler: Healthcheck prior to using instance](https://gitlab.com/gitlab-org/gitlab-runner/-/issues/38271)
  * [Internal Dogfooding - Use the fault tolerance feature branch for our own k8s runners](https://gitlab.com/gitlab-org/gitlab-runner/-/issues/38458)


### What is Not Planned Right Now[](https://about.gitlab.com/direction/verify/runner_core/#what-is-not-planned-right-now)
We are not actively working on the following features:
  * [Sticky Runners](https://gitlab.com/gitlab-org/gitlab/-/issues/17497) - For this feature, the problem to solve is that users need to improve CI job performance in scenarios where each job can generate intermediate build elements with hundreds of GBs in size. In the current GitLab CI model, a significant amount of pipeline execution time is due to the uploading and downloading of intermediate build elements between jobs in a pipeline. Given the current Runner executor implementation, i.e., we support several executor types out of the box (shell, docker, Kubernetes), changing the CI job execution paradigm in GitLab is a significant architectural change. The Sticky Runners MVC feature is not in the near-term roadmap due to higher priority features in the Runner core and the Verify stage.


### Best in Class Landscape[](https://about.gitlab.com/direction/verify/runner_core/#best-in-class-landscape)
BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.
#### Key Capabilities[](https://about.gitlab.com/direction/verify/runner_core/#key-capabilities)
When you run a continuous integration pipeline job or workflow, the code in that pipeline must execute on some computing platform to complete your software's building, testing, and deployment. Terms used to describe the software that handles the pipeline code execution include worker, agent, or runner.
So while the basic functionality of pipeline code execution is table stakes in the industry, the ability to efficiently build software on multiple compute platforms with low operational maintenance overhead are critical features for a best-in-class solution.
#### GitLab Runner Value Proposition[](https://about.gitlab.com/direction/verify/runner_core/#gitlab-runner-value-proposition)
  1. Autoscaling on Kubernetes or VM's: GitLab Runner includes a fully mature Kubernetes autoscaling solution where CI builds run in one-time use, runner worker pods or the GitLab Runner autoscaling technology for public cloud virtual machine instances where CI builds by default run in ephemeral, one-time use virtual machine instances.
  2. Scalability and Flexibility: GitLab Runner is highly scalable, allowing you to run multiple concurrent jobs across different environments. Whether you have a small personal project or a large-scale enterprise application, GitLab Runner can adapt to your needs, providing flexibility in managing your CI/CD workflows.
  3. Multi-platform Support: GitLab Runner can be installed on various operating systems, enabling developers to build and test their projects across different platforms and environments. This versatility ensures consistency and reliability throughout the development and deployment pipeline.
  4. Distributed Execution: GitLab Runner allows distributed job execution across multiple machines, enabling faster and more efficient CI/CD pipelines. Jobs can be parallelized, reducing overall execution time and improving developer productivity.
  5. Easy Configuration: GitLab Runner is seamlessly integrated with GitLab CI/CD and is straightforward to configure. The `.gitlab-ci.yml` file provides a declarative syntax for defining jobs, stages, and dependencies, making it easy for developers to set up and manage their pipelines.
  6. Docker Integration: GitLab Runner has native Docker integration, allowing you to leverage the power of containerization for your CI/CD workflows. Docker images can be used as execution environments for jobs, providing consistency and reproducibility in building and testing applications. Red Hat's daemonless Podman container engine is fully supported as a drop-in replacement.
  7. Extensibility: GitLab Runner supports various executors, including Shell, Docker, Kubernetes, and more. This extensibility enables integration with different tools and platforms, empowering developers to leverage their preferred technology stack and infrastructure.
  8. Security and Isolation: GitLab Runner ensures secure and isolated execution of jobs. Each job runs in its own environment, preventing interference between different jobs and maintaining data privacy and security.


#### Top [1/2/3] Competitive Solutions[](https://about.gitlab.com/direction/verify/runner_core/#top-123-competitive-solutions)
Solution | CI/CD Agent naming convention/brand | Self-Managed Option Availablity | Notes  
---|---|---|---  
GitHub Actions | Runners | Available | At its core, GitHub Action Runners are similar to GitLab Runners in that they communicate to a central server via a REST API, execute jobs, and send the logs and artifacts back to the server when finished. However, multi-platform support, native autoscaling on cloud instances, support for Kubernetes as a build environment, concurrency, and parallel CI/CD job execution are more mature in GitLab Runner. As expected, GitHub has continued to invest in features and capabilities to improve the maturity of GitHub Action Runners. For instance, the recently released [Actions Runner Controller (ARC)](https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners-with-actions-runner-controller/quickstart-for-actions-runner-controller) enables GitHub Actions Runners to autoscale on Kubernetes clusters. However, as noted by others, there is operational overhead involved in the setup and configuration of ARC. On the GitHub public roadmap, we also notice similar investment themes regarding multi-platform support as GitHub continues to target market segments requiring a self-managed platform.  
Harness.io | Harness Delegate | Available | Harness currently provides the following types of Delegate: Kubernetes, Shell Script, AWS ECS, Helm, Docker. Though the Delegates perform a similar essential function as GitLab Runner, i.e., executes tasks provided by the Harness Manager, the Delegates' primary purpose is to deploy software to the target platform. In this regard, the value proposition of the [GitLab Agent for Kubernetes](https://docs.gitlab.com/ee/user/clusters/agent/) is a critical consideration when evaluating capabilities in GitLab for developer frictionless cloud-native deployment.  
Nx Cloud | Nx Agents | Available |  [Nx Cloud](https://nx.dev) a build system for optimizing CI performance and scaling for monorepos,includes [Nx agents](https://nx.dev/ci/features/distribute-task-execution) which dynamically distributes the CI/CD jobs across multiple buiild machines.  
Jenkins | Agents | Available | In Jenkins, an agent is a software executable that runs a task under the direction of the Jenkins controller. Like GitLab Runner, a Jenkins agent can run on different computing environments (bare metal, virtual machines, containers, Kubernetes clusters). Java must be supported and installed on the host OS to run a Jenkins agent.  
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/verify/runner_core/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/verify/runner_core/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fverify%2Frunner_core%2F&_biz_t=1773332009680&_biz_i=%0ACategory%20Direction%20-%20Runner%20Core%0A%7C%0AGitLab%0A&_biz_n=101&rnd=433075&cdn_o=a&_biz_z=1773332009781)
suggested results