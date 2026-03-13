#  Category Strategy - Omnibus Package 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Product Direction - Distribution](https://about.gitlab.com/direction/distribution/)
  4. Category Strategy - Omnibus Package


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Omnibus](https://about.gitlab.com/direction/distribution/omnibus/#omnibus)
    * [Introduction and how you can help](https://about.gitlab.com/direction/distribution/omnibus/#introduction-and-how-you-can-help)
    * [Overview](https://about.gitlab.com/direction/distribution/omnibus/#overview)
      * [Target Audience](https://about.gitlab.com/direction/distribution/omnibus/#target-audience)
      * [Challenges to address](https://about.gitlab.com/direction/distribution/omnibus/#challenges-to-address)
    * [Direction](https://about.gitlab.com/direction/distribution/omnibus/#direction)
      * [What's Next & Why](https://about.gitlab.com/direction/distribution/omnibus/#whats-next--why)
      * [What is Not Planned Right Now](https://about.gitlab.com/direction/distribution/omnibus/#what-is-not-planned-right-now)
      * [Maturity Plan](https://about.gitlab.com/direction/distribution/omnibus/#maturity-plan)


## Omnibus[](https://about.gitlab.com/direction/distribution/omnibus/#omnibus)
Stage | Enablement  
---|---  
Maturity | [Lovable](https://about.gitlab.com/direction/#maturity)  
Content Last Reviewed | `2022-02-07`  
### Introduction and how you can help[](https://about.gitlab.com/direction/distribution/omnibus/#introduction-and-how-you-can-help)
Thanks for visiting this category strategy page for Omnibus GitLab. This page belongs to the [Distribution](https://handbook.gitlab.com/handbook/product/categories/#distribution-group) group of the Enablement stage and is maintained by Dilan Orrino (E-Mail).
Your ideas and feedback are important to us and play a major part in shaping the product direction. The best way to provide feedback on work that is planned or in the backlog is through the Omnibus [epics](https://gitlab.com/groups/gitlab-org/-/epics?scope=all&utf8=%E2%9C%93&state=opened&label_name\[\]=group%3A%3Adistribution&not\[label_name\]\[\]=Category%3ACloud%20Native%20Installation) and [deliverable issues board](https://gitlab.com/groups/gitlab-org/-/boards/1282058?scope=all&utf8=%E2%9C%93&state=opened&label_name\[\]=Deliverable&label_name\[\]=group%3A%3Adistribution) in GitLab.com.
We are always looking for opportunities to interview GitLab users and learn more about your experiences using the Omnibus package to deploy a self-managed instance of GitLab. If you would like to share your experience and provide feedback through a video call, please email Dilan.
### Overview[](https://about.gitlab.com/direction/distribution/omnibus/#overview)
Omnibus GitLab is a downloadable package that contains all the components needed to run, configure, and scale a self-managed instance of GitLab on prem or in the cloud. It provides a quick and easy way to install a standard instance of GitLab and keep it updated to the latest version. It also provides the tools and flexibility to
  * Set up a highly available architecture that suits your scale
  * Fine tune your instance by enabling, disabling, and customizing GitLab features
  * Monitor and troubleshoot your instance
  * Bring your own databases


With Omnibus GitLab we aim to reduce the time it takes to administer GitLab, regardless of your scale, so that your users can have the best possible experience.
#### Target Audience[](https://about.gitlab.com/direction/distribution/omnibus/#target-audience)
  * Organizations or teams that prefer to run their own instance of GitLab rather than use the hosted gitlab.com offering
  * System Administrators and DevOps Engineers responsible for providing development teams with a fast and reliable development environment that allows them to work efficiently
  * Development teams that need to deliver software quickly and efficiently with minimal disruption


#### Challenges to address[](https://about.gitlab.com/direction/distribution/omnibus/#challenges-to-address)
Installing GitLab
  * My company recently purchased GitLab. I want to quickly deploy it and make it available to my end users in the fewest steps possible
  * I want to install GitLab on my preferred operating system and platform, and know that it will be a fully functioning, high performing instance with all of the features and functionality that GitLab offers.


Upgrading GitLab
  * I always want to be on a recent version of GitLab so that I have access to new features and I am running a supported version of GitLab.
  * I want to upgrade GitLab with no downtime for my end users
  * I want my instance to be automatically updated when GitLab releases a patch release
  * I need to approve upgrades to a new major or minor version so it's not okay for GitLab to automatically update without my approval, but I would like to be notified when a new minor release is available and opt in to an automated upgrade process after I've had a chance to review the details of the release.
  * I want to minimize the effort required to upgrade my highly complex, large-scale deployment of GitLab


Scaling GitLab
  * As usage of GitLab expands at my organization, I would like to easily expand from a single node deployment to an architecture that is more appropriate for our scale so that my end users don't experience delays when using GitLab.
  * I need to deploy GitLab at large-scale with zero disruption in the event that a server goes down. I would like it to be easy and quick to set up this highly available deployment with clear documentation that guides me through the process for the cloud platform of my choosing. Even better would be if the process is automated through an interactive script that makes recommendations based on my scale and preferences.


Configuring GitLab
  * I want to configure GitLab in a secure way that satisfies compliance requirements at my organization
  * Omnibus bundles many components. I want to clearly understand the purpose of each component so I can understand how GitLab works and how to get the most out of it


Getting started with GitLab
  * Once I have installed GitLab, I would like guidance on next steps to get value out of my deployment as quickly as possible.


### Direction[](https://about.gitlab.com/direction/distribution/omnibus/#direction)
GitLab's Omnibus package is a mature product that provides a straightforward and quick way to deploy GitLab on a single node. It also includes a well-proven High Availability solution for distributing components of GitLab across multiple nodes and keeping the system accessible in the event of a node failure. GitLab is being deployed at increasingly larger scale as organizations realize the value of having all projects across their organizations available within a single instance.
To support larger scale deployments, we have developed [reference architectures](https://docs.gitlab.com/ee/administration/reference_architectures/index.html) for deploying GitLab with an appropriately sized, highly available architecture. We also plan to support the GitLab Environment Toolkit (GET) on the Omnibus side, for VM and hybrid reference architectures. GET will be the best and easiest way to deploy multi-node production instances of GitLab, and operate them with very high service levels. The collaboration will ensure users can continue to easily grow with GitLab. GET uses Terraform to provision machines and adding specific labels / tags to each machine for Ansible to then use to identify, and Ansible to configure them. This helps users who maintain applications like GitLab have a reliable and automated way of deploying, upgrading, and performing maintenance tasks across multiple nodes. Check out the [GET documentation](https://gitlab.com/gitlab-org/gitlab-environment-toolkit) to learn more.
We want to take the worry out of upgrading GitLab so you can upgrade more regularly, with less impact on your end users, and with less time spent by your administrators. Our goal is to reduce the checklist you need to follow when upgrading multi-node GitLab, and enable more customers to leverage truly zero downtime upgrades. For example, this might mean eliminating some of the upgrade steps, and addressing some of the potential scenarios that presently require downtime.
As a new user, you install GitLab. Then what? Our goal is to guide you through to the next steps of running a fully functioning deployment of GitLab that meets the needs of your organization so you can spend less time wading through documentation and more time putting GitLab to good use.
The Omnibus package will also undergo foundational changes to how the package is built. Our direction of [splitting and paralleling the components in the Omnibus project](https://gitlab.com/gitlab-org/distribution/team-tasks/-/issues/596) will help reduce overall package size, making upgrades quicker and benefiting instances with memory constraints. Another project we will work towards is better repo signing key management via keyring packages, which will make is easier for users to rotate keys.
#### What's Next & Why[](https://about.gitlab.com/direction/distribution/omnibus/#whats-next--why)
The Omnibus installation will be benefitting from overall efficiency work the team is planning to work on in the next 3 milestones (15.9-15.11). We have identified these [contributor experience issues](https://gitlab.com/groups/gitlab-org/-/epics/9711) and [build efficiency issues](https://gitlab.com/groups/gitlab-org/-/epics/9712).
Improving our contributor experience is very impactful for the Distribution team because we typically work on a large number of reviews and are asked to contribute to and complete a wide range of work items from customers and internal teams at GitLab. By improving our contributor experience we can reduce the amount of time we spend on reviews. Contributor experience might also mean another team at GitLab is completely enabled to do work, where in the past they may have been required to request assistance from Distribution team members.
In our efficiency work we hope to reduce the amount of maintenance we need to do regularly, as well as, reduce the time it takes to build tests and implement features. Our efficiency work is focused on reducing the effort to maintain two distinct code bases, for Omnibus and Cloud-native GitLab. This will ideally reduce the time it takes to implement any issue, maintenance work or feature work.
#### What is Not Planned Right Now[](https://about.gitlab.com/direction/distribution/omnibus/#what-is-not-planned-right-now)
We get many requests to support running GitLab on different platforms. While we wish we could support all of these requests, we simply don't have the capacity given all of the goals we want to achieve. AWS is the most popular cloud platform for deploying GitLab. We have committed to providing an outstanding experience for deploying in AWS with up-to-date images, a range of marketplace listings, and great documentation. If time permits, we will provide this same level of commitment for other platforms that are in high demand by our users. We know we won't get to all of them, and for some platforms we will rely on community support to get there.
#### Maturity Plan[](https://about.gitlab.com/direction/distribution/omnibus/#maturity-plan)
This category is currently at the Lovable maturity level. This is the highest maturity level. Our goal is to stay Lovable by making it even easier to manage a GitLab instance and continuing to provide the best possible experience when deploying GitLab with Omnibus. For more information on maturity levels, see our [definitions in the handbook](https://about.gitlab.com/direction/#maturity).
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/distribution/omnibus/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/distribution/omnibus/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fdistribution%2Fomnibus%2F&_biz_t=1773331984667&_biz_i=%0ACategory%20Strategy%20-%20Omnibus%20Package%0A%7C%0AGitLab%0A&_biz_n=95&rnd=349861&cdn_o=a&_biz_z=1773331984847)
suggested results