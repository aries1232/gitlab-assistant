#  Verify Stage Direction 
[ ](https://about.gitlab.com/direction/verify/) [ ](https://about.gitlab.com/direction/verify/) [ ](https://about.gitlab.com/direction/verify/)
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. Verify Stage Direction


####  Maintained by:
[ ![Manav Khurana](https://about.gitlab.com/images/team/manav_khurana-crop.jpg) Manav Khurana  @manav-gl  ](https://gitlab.com/manav-gl)
  * [Overview](https://about.gitlab.com/direction/verify/#overview)
    * [What is Verify?](https://about.gitlab.com/direction/verify/#what-is-verify)
    * [Vision](https://about.gitlab.com/direction/verify/#vision)
      * [Verify Stage Categories](https://about.gitlab.com/direction/verify/#verify-stage-categories)
        * [Continuous Integration (CI)](https://about.gitlab.com/direction/verify/#continuous-integration-ci)
        * [Pipeline Composition](https://about.gitlab.com/direction/verify/#pipeline-composition)
        * [GitLab Runner Core](https://about.gitlab.com/direction/verify/#gitlab-runner-core)
        * [Fleet Visibility](https://about.gitlab.com/direction/verify/#fleet-visibility)
        * [Code Testing and Coverage](https://about.gitlab.com/direction/verify/#code-testing-and-coverage)
        * [Job Artifacts](https://about.gitlab.com/direction/verify/#job-artifacts)
        * [Merge Trains](https://about.gitlab.com/direction/verify/#merge-trains)
        * [Review Apps](https://about.gitlab.com/direction/verify/#review-apps)
        * [Environment Management](https://about.gitlab.com/direction/verify/#environment-management)
        * [Auto DevOps](https://about.gitlab.com/direction/verify/#auto-devops)
        * [Deployment Management](https://about.gitlab.com/direction/verify/#deployment-management)
        * [Infrastructure as Code](https://about.gitlab.com/direction/verify/#infrastructure-as-code)
        * [Mobile DevOps](https://about.gitlab.com/direction/verify/#mobile-devops)
        * [Component Catalog](https://about.gitlab.com/direction/verify/#component-catalog)


## Overview[](https://about.gitlab.com/direction/verify/#overview)
DevSecOpsPlanCodeBuildTestReleaseDeployOperateMonitorSecurityCompliance
Verify
### What is Verify?[](https://about.gitlab.com/direction/verify/#what-is-verify)
The Verify Stage is responsible for executing on the market needs for continuous integration.
[Continuous integration](https://handbook.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/usecase-gtm/ci/#continuous-integration) is a critical practice in modern software development. High-performing software development teams check in code to a shared GitLab repository multiple times daily, leveraging automated and repeatable tests and build workflows to produce secure, functional, and deployment-ready software.
### Vision[](https://about.gitlab.com/direction/verify/#vision)
GitLab CI/CD, a core component of our DevSecOps, platform, is the market-leading enterprise solution for CI/CD workflow automation and orchestration. Our powerful orchestration engine addresses the needs of both software developers and the administrators who manage the critical tooling that empowers high-performing development teams to excel. Our strategy focuses on delivering advanced CI/CD capabilities while providing enterprise-grade solutions that scale with your organizations needs. We believe in making automation accessible to all teams, then delivering advanced capabilities that promote greater efficiency and governance without compromising on security as your DevSecOps maturity grows.
We will execute this vision by:
  1. Building a comprehensive component ecosystem that makes advanced CI/CD patterns accessible to all teams through free CI/CD inputs, reusable components, and our CI/CD Catalog, while delivering premium enterprise features for organizations requiring advanced governance, security, and scalability.
  2. Continuing developing [CI/CD inputs](https://docs.gitlab.com/ci/inputs/) features to address enterprise needs for pipeline input validation, reusability, dynamic parameterization, scalability, self-documenting workflows, and flexibility.
  3. Significantly investing in improving the [CI/CD Catalog](https://docs.gitlab.com/ci/components/#cicd-catalog). Key themes include: 
     * Enterprise accessibility: Enable self-managed customers to access GitLab.com components with automated synchronization and air-gapped environment support
     * Advanced analytics and visibility: Comprehensive component analytics dashboards for usage insights, version tracking, and lifecycle governance
     * Security and governance: Developer security workflows and administrative controls for component publishing and usage
     * Competitive maturity: Comprehensive user experience improvements, including enhanced search, filtering, and navigation
  4. Reimagining a holistic new user experience for CI/CD.
  5. Focusing on scalability, quality and reliability so that customers can trust GitLab CI/CD to work as expected when they need it most.


#### Verify Stage Categories[](https://about.gitlab.com/direction/verify/#verify-stage-categories)
##### Continuous Integration (CI)[](https://about.gitlab.com/direction/verify/#continuous-integration-ci)
Streamline your software development lifecycle with continuous, automated building, testing, and deploying of iterative code changes. This ensures the early detection of integration issues, bugs, and security vulnerabilities before deploying to production. This category is planned, but not yet available.
[Learn more](https://about.gitlab.com/solutions/continuous-integration/) • [Documentation](https://docs.gitlab.com/ci/) • [Direction](https://about.gitlab.com/direction/verify/continuous_integration/)
##### Pipeline Composition[](https://about.gitlab.com/direction/verify/#pipeline-composition)
Advanced features enable you to edit/compose a highly flexible CI/CD pipeline configuration to boost efficiency across a variety of projects.
[Learn more](https://about.gitlab.com/solutions/continuous-integration/) • [Documentation](https://docs.gitlab.com/ci/) • [Direction](https://about.gitlab.com/direction/verify/pipeline_composition/)
##### GitLab Runner Core[](https://about.gitlab.com/direction/verify/#gitlab-runner-core)
GitLab Runner is an application to run the GitLab CI/CD jobs in a pipeline.
[Documentation](https://docs.gitlab.com/runner/) • [Direction](https://about.gitlab.com/direction/verify/runner_core/)
##### Fleet Visibility[](https://about.gitlab.com/direction/verify/#fleet-visibility)
Evaluate the status and performance of your runner fleet.
[Documentation](https://docs.gitlab.com/administration/admin_area/#administering-runners) • [Direction](https://about.gitlab.com/direction/verify/fleet_visibility/)
##### Code Testing and Coverage[](https://about.gitlab.com/direction/verify/#code-testing-and-coverage)
Code testing and coverage are important parts of a Continuous Integration framework, ensuring that source code is validated by test suites and individual pipeline components perform as expected. This category is planned, but not yet available.
[Documentation](https://docs.gitlab.com/ci/testing) • [Direction](https://about.gitlab.com/direction/verify/code_testing/)
##### Job Artifacts[](https://about.gitlab.com/direction/verify/#job-artifacts)
This category focuses on user needs of artifacts which are created as an output of a pipeline or job. This includes both the job’s artifacts, job logs and pipeline artifacts.
[Documentation](https://docs.gitlab.com/ci/jobs/job_artifacts/) • [Direction](https://about.gitlab.com/direction/verify/job_artifacts/)
##### Merge Trains[](https://about.gitlab.com/direction/verify/#merge-trains)
Coordinate frequent merge requests and avoid merge conflicts with Merge Trains, preventing code commits from breaking default and main branches. This category is planned, but not yet available.
[Documentation](https://docs.gitlab.com/ci/pipelines/merge_trains/) • [Direction](https://about.gitlab.com/direction/verify/merge_trains/)
##### Review Apps[](https://about.gitlab.com/direction/verify/#review-apps)
Gain access to a live instance of your application for every commit, allowing you and stakeholders to ensure thorough validation and collaboration before changes are merged into the main codebase. This category is planned, but not yet available.
Priority: low • [Documentation](https://docs.gitlab.com/ci/review_apps/) • [Direction](https://about.gitlab.com/direction/verify/review_apps/)
##### Environment Management[](https://about.gitlab.com/direction/verify/#environment-management)
Environments are at the center of DevSecOps, bringing the results of application development in front of the users. They provide traceability of deployments, visualisation of workload states, and support advanced rollout strategies, feature flag management, and when necessary rollbacks. This category is planned, but not yet available.
Priority: high • [Documentation](https://docs.gitlab.com/ci/environments/) • [Direction](https://about.gitlab.com/direction/delivery/environment_management/)
##### Auto DevOps[](https://about.gitlab.com/direction/verify/#auto-devops)
Automatically discover, build, test, and scan source code, and deploy and monitor built applications using an opinionated but highly customizable set of CI/CD templates and integrations. Enable teams to focus on writing business code and better collaboration while delivering software faster. This category is planned, but not yet available.
Priority: medium • [Documentation](https://docs.gitlab.com/topics/autodevops/) • [Direction](https://about.gitlab.com/direction/delivery/auto_devops/)
##### Deployment Management[](https://about.gitlab.com/direction/verify/#deployment-management)
Deploying applications from testing environments to multi-region production servers is a core requirement of DevSecOps. Deployments should be easy to codify for platform engineers and simple to interact with for engineers and release managers. Moreover, they should follow company requirements in terms of compliance and security. Deployment management supports multi-cloud, cloud-native, and legacy infrastructures and unifies the platform experience by integrating tools and frameworks, such as Flux for GitOps. This category is planned, but not yet available.
Priority: high • [Learn more](https://about.gitlab.com/solutions/kubernetes/) • [Documentation](https://docs.gitlab.com/topics/release_your_application/) • [Direction](https://about.gitlab.com/direction/delivery/)
##### Infrastructure as Code[](https://about.gitlab.com/direction/verify/#infrastructure-as-code)
Automate the provisioning of infrastructure resources through Infrastructure-as-Code, use Terraform/OpenTofu with zero-configuration from CI/CD pipelines, and apply GitOps best practices to deliver software faster. This category is planned, but not yet available.
Priority: high • [Documentation](https://docs.gitlab.com/user/infrastructure/iac/) • [Direction](https://about.gitlab.com/direction/delivery/infrastructure_as_code/)
##### Mobile DevOps[](https://about.gitlab.com/direction/verify/#mobile-devops)
This category is planned, but not yet available.  
[Direction](https://about.gitlab.com/direction/mobile/mobile-devops)
##### Component Catalog[](https://about.gitlab.com/direction/verify/#component-catalog)
A collaborative platform for developers who can easily share, build, and maintain high-quality CI/CD configurations.
[Learn more](https://about.gitlab.com/solutions/continuous-integration/) • [Documentation](https://docs.gitlab.com/ci/) • [Direction](https://about.gitlab.com/direction/verify/component_catalog/)
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/verify/index.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/verify/index.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fverify%2F&_biz_t=1773331711203&_biz_i=%0AVerify%20Stage%20Direction%0A%7C%0AGitLab%0A&_biz_n=36&rnd=761464&cdn_o=a&_biz_z=1773331714065)
suggested results