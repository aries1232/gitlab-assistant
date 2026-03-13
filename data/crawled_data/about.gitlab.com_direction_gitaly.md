#  Category Direction - Gitaly 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. Category Direction - Gitaly


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Gitaly](https://about.gitlab.com/direction/gitaly/#gitaly)
    * [Introduction and how you can help](https://about.gitlab.com/direction/gitaly/#introduction-and-how-you-can-help)
    * [Gitaly Overview](https://about.gitlab.com/direction/gitaly/#gitaly-overview)
      * [Gitaly within GitLab](https://about.gitlab.com/direction/gitaly/#gitaly-within-gitlab)
    * [Gitaly Development](https://about.gitlab.com/direction/gitaly/#gitaly-development)
  * [Analyst Landscape](https://about.gitlab.com/direction/gitaly/#analyst-landscape)
    * [Sales Enablement](https://about.gitlab.com/direction/gitaly/#sales-enablement)
      * [What is Gitaly?](https://about.gitlab.com/direction/gitaly/#what-is-gitaly)
      * [Why we built Gitaly Cluster](https://about.gitlab.com/direction/gitaly/#why-we-built-gitaly-cluster)
      * [How is Gitaly Cluster differentiator for GitLab](https://about.gitlab.com/direction/gitaly/#how-is-gitaly-cluster-differentiator-for-gitlab)
      * [When should customers use Gitaly Cluster](https://about.gitlab.com/direction/gitaly/#when-should-customers-use-gitaly-cluster)
      * [When should customers not use Gitaly Cluster](https://about.gitlab.com/direction/gitaly/#when-should-customers-not-use-gitaly-cluster)
      * [Resources](https://about.gitlab.com/direction/gitaly/#resources)
    * [Deprecations and Changes](https://about.gitlab.com/direction/gitaly/#deprecations-and-changes)
    * [Maturity Plan](https://about.gitlab.com/direction/gitaly/#maturity-plan)
    * [Target Audience](https://about.gitlab.com/direction/gitaly/#target-audience)


## Gitaly[](https://about.gitlab.com/direction/gitaly/#gitaly)
|   
---|---  
Section | Data Access  
Maturity | Non-marketable  
Content Last Reviewed | 2025-04-01  
### Introduction and how you can help[](https://about.gitlab.com/direction/gitaly/#introduction-and-how-you-can-help)
The Gitaly direction page belongs to the [Data Access](https://handbook.gitlab.com/handbook/product/categories/#data-access-stage) within the [Infrastructure Platforms](https://handbook.gitlab.com/handbook/product/categories/#infrastructure-platforms-section) section, and is maintained by [Mark Wood](https://gitlab.com/mjwood). The Gitaly Engineering team and stable counterparts can be found on the [Engineering team page](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/data-access/gitaly/).
This strategy is a work in progress, and everyone can contribute. Please comment and contribute in the linked issues and epics. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
  * [Issue List](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name\[\]=group%3A%3Agitaly)
  * [Epic list](https://gitlab.com/groups/gitlab-org/-/epics?label_name\[\]=group%3A%3Agitaly)


If you would like support from the Gitaly team, please see the team's page detailing [How to contact the Gitaly team](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/data-access/gitaly/#how-to-contact-the-team).
### Gitaly Overview[](https://about.gitlab.com/direction/gitaly/#gitaly-overview)
Gitaly is the service responsible for the storage and maintenance of all Git repositories in GitLab for both our GitLab.com customers, as well as self-managed customers. Git repositories are essential to GitLab, for [Source Code Management](https://about.gitlab.com/direction/create/source_code_management/), [Wikis](https://about.gitlab.com/direction/plan/knowledge/wiki/), [Snippets](https://about.gitlab.com/direction/create/source_code_management/), Design Management, and [Web IDE](https://about.gitlab.com/direction/create/remote_development/web_ide/). Every stage of the DevOps lifecycle to the right of Create - Verify, Package, Release, Configure, Govern, Monitor and Secure - depends on the project repositories. Because the majority of GitLab capabilities depend on information stored in Git repositories, performance and availability are of primary importance.
GitLab is used to store Git repositories by small teams of a few people all the way up to large enterprises with many terabytes of data. For this reason, Gitaly has been built to scale from small single server GitLab instances, to large high availability architectures.
Gitaly provides multiple interfaces to read and write Git data:
  * Git protocol over SSH, through the [GitLab Shell](https://gitlab.com/gitlab-org/gitlab-shell) component.
  * Git protocol over HTTP, through the [GitLab Workhorse](https://gitlab.com/gitlab-org/gitlab/-/blob/master/doc/development/workhorse/index.md) component.
  * gRPC internally to GitLab components. The public REST and GraphQL APIs to Git data are implemented using these RPCs.


#### Gitaly within GitLab[](https://about.gitlab.com/direction/gitaly/#gitaly-within-gitlab)
While GitLab is the largest user of the Gitaly project, it is important to note that Gitaly is a standalone project that can be adopted separately from GitLab. As such, we strive to ensure that all business specific decisions are made within the GitLab application. Our belief is that Gitaly should provide the ability for management interfaces, but not make any specific management decisions.
For example, some users may want the ability to move repositories between different storage nodes for either cost savings or performance reasons. While Gitaly should provide an easy to use interface to efficiently move repositories, the calling application should be making the decisions around which repositories to move where.
Processes requiring no business data or inputs should be fully contained within Gitaly. These types of processes include repository maintenance and storage maintenance type tasks. We believe that these types of features provide substantial value for projects utilizing Gitaly and provide a compelling reason to choose Gitaly as a repository storage architecture.
### Gitaly Development[](https://about.gitlab.com/direction/gitaly/#gitaly-development)
The Gitaly team's goal is to provide a durable, performant, and reliable Git storage layer for GitLab. This team will tightly collaborate with the Git team as they will build directly upon the Git tooling. Areas where the Gitaly team will focus on is High Availability Git storage (Gitaly Cluster), scalability of Gitaly storage mechanisms, and improved user and administrative experiences.
For more information, please see the [team page](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/data-access/gitaly/).
## Analyst Landscape[](https://about.gitlab.com/direction/gitaly/#analyst-landscape)
  * [Native support for large files](https://gitlab.com/groups/gitlab-org/-/epics/773) is important to companies that need to version large binary assets, like game studios. These companies primarily use Perforce because Git LFS provides poor experience with complex commands and careful workflows needed to avoid large files entering the repository. GitLab has been supporting work to provide a more native large file workflow based on promiser packfiles which will be very significant to analysts and customers when the feature is ready.


### Sales Enablement[](https://about.gitlab.com/direction/gitaly/#sales-enablement)
This section contains messaging, questions, and resources for our sales counterparts to successfully position and sell Gitaly Cluster. It is important to note that Gitaly Cluster is not perfect for every installation. Our goal is to provide options for our customers so they can choose the best repository storage mechanism for their particular business needs.
#### What is Gitaly?[](https://about.gitlab.com/direction/gitaly/#what-is-gitaly)
Gitaly is a centralized service which handles all access to files to file storage for GitLab. Gitaly services Git requests from the GitLab web application, command line, and via the API. Gitaly is highly configurable and can utilize one or more storage locations to read / write repository data.
The Gitaly service is required for all GitLab installs, and is a separate product from Gitaly Cluster. While Gitaly handles accessing repository storage, Gitaly Cluster provides a highly available repository storage solution for our customers.
#### Why we built Gitaly Cluster[](https://about.gitlab.com/direction/gitaly/#why-we-built-gitaly-cluster)
Gitaly Cluster was built to address the industry-wide difficulty around expanding Git repository storage in addition to the lack of high availability (HA) Git storage for critical applications. A prominent theme in industry is the idea of an ever expanding NFS storage location for repository storage. While this can work, over time performance degrades, and management becomes increasingly complex. Additionally, while the NFS file system is ideal for many types of files, it's well documented that the types of file accesses created by Git repository access can cause performance issues.
Our goal with Gitaly cluster is to build a Git repository storage system capable of scaling with our users needs, and providing a configurable level of redundancy to keep businesses operating, iterating, and growing.
#### How is Gitaly Cluster differentiator for GitLab[](https://about.gitlab.com/direction/gitaly/#how-is-gitaly-cluster-differentiator-for-gitlab)
Gitaly Cluster is a unique open-core project aimed at providing a scalable and high availability platform for Git repository storage. Gitaly Cluster enable horizontal scalability, allowing our customers to grow their storage in a simple, and well defined manner. We also capitalize on the redundant copies of data needed for HA by increasing read performance through read-distribution.
#### When should customers use Gitaly Cluster[](https://about.gitlab.com/direction/gitaly/#when-should-customers-use-gitaly-cluster)
Customers should utilize Gitaly Cluster in a few key situations:
  * **There is a need for high availability** - Customers who wish to ensure that losing a single node does not induce downtime are ideally suited to a Gitaly Cluster installation.
  * **There is a need for expandable storage** - Customers whose repository storage size continues to grow and want to be able to horizontally scale their storage infrastructure.
  * **There is a large read demand on Git data** - Environments where there is a large read demand on data can benefit greatly from the distributed read functionality provided by Gitaly Cluster.


#### When should customers not use Gitaly Cluster[](https://about.gitlab.com/direction/gitaly/#when-should-customers-not-use-gitaly-cluster)
Customers may not desire to utilize Gitaly Cluster for the following reasons:
  * **Cost** - Having data stored in a highly available / redundant manner requires more infrastructure and therefore incurs higher storage / hosting costs.
  * **Very low RPO / RTO needs** - Recognize that restoration of an entire cluster & Praefect database will naturally take longer than a single node. However, this is mostly mitigated by the fact that loss of a single node should not require restoration, and therefore should be an unlikely scenario.
  * **Require snapshot backups** - It is very difficult to backup the Gitaly Cluster nodes & Praefect database at the exact same time, which will result in a non-congruent backup. Therefore, Gitaly Cluster does not support snapshot backups. However, we are making progress on releasing an [incremental backup solution](https://gitlab.com/groups/gitlab-org/-/epics/2094) that will be fully compatible with Gitaly Cluster.


#### Resources[](https://about.gitlab.com/direction/gitaly/#resources)
**Documentation Resources**
  * [Gitaly Cluster Recommendations](https://docs.gitlab.com/ee/administration/configure.html#gitaly-capabilities)
  * [Gitaly Cluster documentation](https://docs.gitlab.com/ee/administration/gitaly/)
  * [FAQ](https://docs.gitlab.com/ee/administration/gitaly/faq.html)


**Enablement Presentation** (Internal GitLab Only)
  * [Video: Gitaly Cluster Enablement Presentation](https://youtu.be/zI1t0IyHayM)
  * [Deck: Self-hosted options for GitLab](https://docs.google.com/presentation/d/1RV-dOah-EO4D4VZvSwEVxaXEXbVSlc6FzjZjQIYSre8/edit#slide=id.g29a70c6c35_0_68)


### Deprecations and Changes[](https://about.gitlab.com/direction/gitaly/#deprecations-and-changes)
As Gitaly and Gitaly Cluster evolve, it is sometimes necessary to deprecate features. When this occurs, we will follow the documented [Deprecations, removals and breaking changes](https://handbook.gitlab.com/handbook/marketing/blog/release-posts/#deprecations-removals-and-breaking-changes) procedure. This ensures that all stable counterparts within GitLab are informed, and that the [GitLab Documentation](https://docs.gitlab.com/ee/update/deprecations) is also updated to keep our customers informed.
### Maturity Plan[](https://about.gitlab.com/direction/gitaly/#maturity-plan)
Gitaly is a **non-marketable** category, and is therefore not assigned a maturity level.
### Target Audience[](https://about.gitlab.com/direction/gitaly/#target-audience)
**Systems Administrators** directly interact with Gitaly when installing, configuring, and managing a GitLab server, particularly when high availability is a requirement. In the past, systems administrators needed to create and manage an NFS cluster to configure a high availability GitLab instance, and manually manage the failover to new Gitaly nodes mounted on the same NFS cluster. In order to scale such a solution individual storage nodes needed to be re-sized, or a sharded Gitaly approach was required. Now that Gitaly Cluster is available, is possible to eliminate the NFS cluster from architecture and rely on Gitaly for replication. Gitaly Cluster brings with it automatic failover, horizontal scaling, and read access across replicas will deliver 99.999% uptime (five 9's) and improved performance without regular intervention. Systems administrators will have fewer applications to manage, as the last projects are migrated to GitLab and other version control systems are retired.
**Developers** will benefit from increasing performance of repositories of all shapes and sizes, on the command line and in the GitLab application, as performance improvements continue. Once support for monolithic repositories reaches minimal and continues maturing, developers will no longer be split between Git and legacy version control systems, as projects consolidate increasingly on Git. Developers that heavily use binary assets, like **Game Developers** , will at long last be able to switch to Git and eliminate Git LFS by adopting native large file support in Git.
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/gitaly/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/gitaly/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fgitaly%2F&_biz_t=1773332150809&_biz_i=%0ACategory%20Direction%20-%20Gitaly%0A%7C%0AGitLab%0A&_biz_n=131&rnd=899613&cdn_o=a&_biz_z=1773332150987)
suggested results