#  Category Direction - Hosted runners 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Verify Stage Direction](https://about.gitlab.com/direction/verify/)
  4. Category Direction - Hosted runners


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
## Hosted runners[](https://about.gitlab.com/direction/verify/hosted_runners/#hosted-runners)
Stage | [Verify](https://about.gitlab.com/direction/verify/)  
---|---  
Maturity | [Viable](https://about.gitlab.com/direction/#maturity)  
Content Last Reviewed | `2025-12-01`  
### Introduction[](https://about.gitlab.com/direction/verify/hosted_runners/#introduction)
Thanks for visiting this direction page on the Hosted runners category at GitLab. This page is maintained by Gabriel Engel.
### Strategy and Themes[](https://about.gitlab.com/direction/verify/hosted_runners/#strategy-and-themes)
With the adoption of a DevSecOps approach and the resulting gains in developer and delivery efficiency, organizations are seeing an increased demand for computing power to run CI/CD pipelines.
Our **vision** is to provide a fully managed, best-in-class hosted CI/CD build infrastructure that is fast and secure by default. We want to eliminate the overhead of hosting and maintaining your build infrastructure, ultimately enabling you to deliver software faster. Our platform approach will allow you to run cross-platform (Docker containers on Linux, Windows, macOS) builds in one CI/CD pipeline. With GitLab-hosted runners, we aim to help you realize increased cost savings and efficiency by providing a reliable service for running all CI/CD builds to eliminate the need to maintain infrastructure.
Today, the [GitLab-hosted runners](https://docs.gitlab.com/ee/ci/runners/) product offerings are:
  * [Hosted runners on Linux - GA](https://docs.gitlab.com/ee/ci/runners/hosted_runners/linux.html)
  * [GPU-enabled hosted runners - GA](https://docs.gitlab.com/ee/ci/runners/hosted_runners/gpu_enabled.html)
  * [Hosted runners on macOS - Beta](https://docs.gitlab.com/ee/ci/runners/hosted_runners/macos.html)
  * [Hosted runners on Windows - Beta](https://docs.gitlab.com/ee/ci/runners/hosted_runners/windows.html)
  * [Hosted runners for GitLab Dedicated - Limited availability](https://docs.gitlab.com/ee/administration/dedicated/hosted_runners.html)


### 1 year plan[](https://about.gitlab.com/direction/verify/hosted_runners/#1-year-plan)
The primary FY2026 runner themes focus on building a competitive and complete CI/CD offering that allows customers to build for all common platforms.
  * [Hosted runners for GitLab Dedicated](https://about.gitlab.com/blog/hosted-runners-for-gitlab-dedicated-available-in-beta/) transition to General Availability
  * [Hosted runners on macOS](https://gitlab.com/groups/gitlab-org/-/epics/8267) transition to General Availability
  * [Hosted runners on Windows](https://gitlab.com/groups/gitlab-org/-/epics/2162) transition to General Availability
  * [Outbound network control of hosted runners for GitLab Dedicated](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/583)
  * [Hosted runners on macOS for GitLab Dedicated - Beta](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/392)
  * [Hosted runners on Windows for GitLab Dedicated - Beta](https://gitlab.com/groups/gitlab-com/gl-infra/gitlab-dedicated/-/epics/397)
  * [GitLab Runner Infrastructure Toolkit (GRIT)](https://gitlab.com/gitlab-org/ci-cd/runner-tools/grit) to General Availability


### 3 year plan[](https://about.gitlab.com/direction/verify/hosted_runners/#3-year-plan)
In the next three years, we want to enable enterprises, to fully focus on developing software without the hassle of managing infrastructure and make GitLab-hosted runners, to be the most widely adopted CI solution by enterprises in the market. We want to achieve this, by focusing on [speed](https://about.gitlab.com/company/team/structure/working-groups/ci-build-speed/), security, and cost efficiency.
Our flagship offering will be [custom-hosted runners](https://gitlab.com/groups/gitlab-org/-/epics/10073), allowing users to create [custom GitLab-hosted runners via GitLab UI](https://gitlab.com/gitlab-org/ci-cd/shared-runners/infrastructure/-/issues/148), fully dedicated to their project, with more advanced features such as [dedicated IP-range](https://gitlab.com/gitlab-org/gitlab/-/issues/364425), or [SSH access for debugging](https://gitlab.com/groups/gitlab-org/-/epics/10423). Combined with a new pricing model, it should be a superior choice for the enterprise hosting needs.
#### What we are currently working on[](https://about.gitlab.com/direction/verify/hosted_runners/#what-we-are-currently-working-on)
  * [Hosted runners for GitLab Dedicated](https://about.gitlab.com/blog/hosted-runners-for-gitlab-dedicated-available-in-beta/) transition to General Availability


#### What is next for us[](https://about.gitlab.com/direction/verify/hosted_runners/#what-is-next-for-us)
In the next three months we plan to complete the following projects:
  * [Transition hosted runners on Linux to new Autoscaler and GRIT](https://gitlab.com/groups/gitlab-org/ci-cd/shared-runners/-/epics/17)
  * [GRIT - Linux Docker scenarios (Beta)](https://gitlab.com/groups/gitlab-org/ci-cd/runner-tools/-/epics/13)


### Best in Class Landscape[](https://about.gitlab.com/direction/verify/hosted_runners/#best-in-class-landscape)
BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.
#### Key Capabilities[](https://about.gitlab.com/direction/verify/hosted_runners/#key-capabilities)
Cloud-native CI/CD solutions, such as GitLab.com, Harness.io, CircleCI, and GitHub, allow to run CI/CD pipelines on a fully managed runner fleet with no setup required.
In addition to eliminating CI build server maintenance costs, there are other critical considerations for organizations that can migrate 100% of their CI/CD processes to a cloud-native solution. These include security, reliability, performance, compute types, and on-demand scale.
CI build speed or time-to-result, and the related CI build infrastructure cost efficiency are critical competitive vectors. [CircleCI](https://circleci.com/circleci-versus-github-actions/) and [Harness.io](https://www.harness.io/blog/announcing-speed-enhancements-and-hosted-builds-for-harness-ci) are promoting CI-build performance in their go-to-market strategy. Both [GitHub](https://github.blog/2022-12-08-experiment-the-hidden-costs-of-waiting-on-slow-build-times/) and [Harness.io](https://www.harness.io/blog/fastest-ci-tool) explored the cost impact of CI build performance measured by build times on hosted solutions.
#### Top Competitive Solutions[](https://about.gitlab.com/direction/verify/hosted_runners/#top-competitive-solutions)
##### Hosted Linux Compute[](https://about.gitlab.com/direction/verify/hosted_runners/#hosted-linux-compute)
Size | Machine Specs | GitLab | GitHub | CircleCI  
---|---|---|---|---  
small | 2 vCPUs, 8GB RAM | Available | Available | Available  
medium | 4 vCPUs, 16GB RAM | Available | Available | Available  
large | 8 vCPUs, 32GB RAM | Available | Available | Available  
x-large | 16 vCPUs, 64GB RAM | Available | Available | Available  
2x-large | 32 vCPUs, 128GB RAM | Available | Available | Available  
3x-large | 48 vCPUs, 192GB RAM | Not available | Available | Not available  
4x-large | 64 vCPUs, 256GB RAM | Not available | Available | Not available  
##### Hosted GPU Compute[](https://about.gitlab.com/direction/verify/hosted_runners/#hosted-gpu-compute)
Size | Machine Specs | GitLab | GitHub | CircleCI  
---|---|---|---|---  
lite | Nvidia Tesla P4 | Not available | Not available | Available  
standard | Nvidia Tesla T4 | Available | Available | Available  
premium | Nvidia Tesla V100 | Not available | Not available | Available  
##### macOS - Offer Positioning and Hosted Build Machines[](https://about.gitlab.com/direction/verify/hosted_runners/#macos---offer-positioning-and-hosted-build-machines)
| GitLab | GitHub | Xcode Cloud | CircleCI | Bitrise.io  
---|---|---|---|---|---  
Positioning statement | Hosted runners on macOS provide an on-demand macOS build environment fully integrated with GitLab CI/CD. | A GitHub-hosted runner is VM hosted by GitHub with the GitHub actions runner application installed. | A CI/CD service built into Xcode, designed expressly for Apple developers. | Industry-leading speed. No other CI/CD platform takes performance as seriously as we do. | Build better mobile applications, faster.  
Value proposition | You can take advantage of all the capabilities of the GitLab single DevOps platform and not have to manage or operate a build environment. | When you use a GitHub-hosted runner, machine maintenance and upgrades are taken care of. | Build your apps in the cloud and eliminate dedicated build infrastructure. | The macOS execution environment allows you to test, build, and deploy macOS and iOS apps on CircleCI. | CI for mobile - save time spent on testing, onboarding, and maintenance with automated workflows and triggers  
Available machines | M1: medium; M2 Pro: large | M1: small+, medium+ | n/a | M1, M2Pro, M4Pro: medium, large | M1: medium, large; M2 Pro: medium, large, x-large; M4 Pro: large, x-large  
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/verify/hosted_runners/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/verify/hosted_runners/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fverify%2Fhosted_runners%2F&_biz_t=1773332100622&_biz_i=%0ACategory%20Direction%20-%20Hosted%20runners%0A%7C%0AGitLab%0A&_biz_n=120&rnd=607027&cdn_o=a&_biz_z=1773332100737)
suggested results