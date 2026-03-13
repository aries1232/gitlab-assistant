#  Group Direction - DataOps 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Product Stage Direction - ModelOps](https://about.gitlab.com/direction/modelops/)
  4. Group Direction - DataOps


####  Maintained by:
[ ![Taylor McCaslin](https://about.gitlab.com/images/team/taylormccaslin-crop.jpg) ](https://gitlab.com/tmccaslin) [ G ](https://gitlab.com/gl-product-leaders)
The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
# DataOps[](https://about.gitlab.com/direction/modelops/dataops/#dataops)
## On this page
  * [DataOps](https://about.gitlab.com/direction/modelops/dataops/#dataops)
    * [Overview](https://about.gitlab.com/direction/modelops/dataops/#overview)
      * [Goal](https://about.gitlab.com/direction/modelops/dataops/#goal)
      * [Categories](https://about.gitlab.com/direction/modelops/dataops/#categories)
      * [Meltano](https://about.gitlab.com/direction/modelops/dataops/#meltano)
    * [Analyst Research](https://about.gitlab.com/direction/modelops/dataops/#analyst-research)


## Overview[](https://about.gitlab.com/direction/modelops/dataops/#overview)
Today businesses are creating, moving, storing and more recently, deleting data faster than ever before. They are building applications that leverage this data. Organizations commonly have data teams to help manage the lifecycle of data and to help find value in it. Data doesn't just sit in datastores anymore, [it moves and changes](https://about.gitlab.com/direction/modelops/#data-in-motion). This is a common challenge with data science. The insights and models you built on data today, won't necessarily be accurate or useful in the future as data changes or drifts from your initial modeling. This challenge commonly leads to the dreaded "messy data" problem that makes it difficult for organizations to gain value from their data. Solving this challenge will make it easier for organizations and data science teams to find value in data and allow it to power the applications of the future. That is the focus of this group.
### Goal[](https://about.gitlab.com/direction/modelops/dataops/#goal)
This group goes beyond enhancing our existing stages and offering. DataOps will help organizations turn disparate data sources into data-driven decisions and useful workloads. This will enable new efficiencies within organizations using GitLab, and these new capabilities will be particularly attractive to a CTO, CIO, and data teams.
### Categories[](https://about.gitlab.com/direction/modelops/dataops/#categories)
  * _Extract_ → Collecting data from across organizations, applications, and data stores. Meltano today uses Singer.
  * _Load_ → Aggregating data engineering from disparate sources into a unified data lake. Compare to various data manipulation libraries and tools: Snowflake, Stitch Data, Oracle Data Integrator
  * _Transform_ → Manipulate data into standardized, cleaned, shaped, and verified data to be used for data science. Run DBT better, compare to DBT Cloud.


### Meltano[](https://about.gitlab.com/direction/modelops/dataops/#meltano)
Previously GitLab was focused on an internally developed product called [Meltano](https://meltano.com/), an [open-source platform](https://gitlab.com/meltano/meltano) for building, running & orchestrating ELT pipelines leveraging [Singer taps](https://www.singer.io/) and targets and [dbt models](https://www.getdbt.com/), that you can run locally or easily deploy in production. As of mid 2021, [Meltano was spun out of GitLab into its own startup](https://meltano.com/blog/meltano-spins-out-of-gitlab-raises-seed-round/). While we are pursuing alternative routes forward with our DataOps group, Meltano still provides a useful open source ELT platform that connects with GitLab.
## Analyst Research[](https://about.gitlab.com/direction/modelops/dataops/#analyst-research)
  * [Forrester: Feature Stores Take On The Data In Data Science](https://www.forrester.com/fn/78nWuvBkhTNOFjZC9m1z6g)


_  
Last Reviewed: 2024-10-05  
Last Updated: 2024-10-05 _
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/modelops/dataops/index.html.md.erb) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/modelops/dataops/index.html.md.erb)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fmodelops%2Fdataops%2F&_biz_t=1773331611257&_biz_i=%0AGroup%20Direction%20-%20DataOps%0A%7C%0AGitLab%0A&_biz_n=17&rnd=721546&cdn_o=a&_biz_z=1773331611632)
suggested results