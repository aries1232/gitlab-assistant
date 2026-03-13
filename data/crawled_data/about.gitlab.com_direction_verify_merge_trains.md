#  Category Direction - Merge Trains 
  1. You are here:
  2. [GitLab Direction](https://about.gitlab.com/direction/)
  3. [Verify Stage Direction](https://about.gitlab.com/direction/verify/)
  4. Category Direction - Merge Trains


The following page may contain information related to upcoming products, features and functionality. It is important to note that the information presented is for informational purposes only, so please do not rely on the information for purchasing or planning purposes. Just like with all projects, the items mentioned on the page are subject to change or delay, and the development, release, and timing of any products, features or functionality remain at the sole discretion of GitLab Inc. 
  * [Merge Trains](https://about.gitlab.com/direction/verify/merge_trains/#merge-trains)
    * [Introduction and how you can help](https://about.gitlab.com/direction/verify/merge_trains/#introduction-and-how-you-can-help)
    * [Overview](https://about.gitlab.com/direction/verify/merge_trains/#overview)
    * [1 year plan](https://about.gitlab.com/direction/verify/merge_trains/#1-year-plan)
      * [What we are currently working on](https://about.gitlab.com/direction/verify/merge_trains/#what-we-are-currently-working-on)
      * [What we recently completed](https://about.gitlab.com/direction/verify/merge_trains/#what-we-recently-completed)
    * [Best in Class Landscape](https://about.gitlab.com/direction/verify/merge_trains/#best-in-class-landscape)
      * [Key Capabilities](https://about.gitlab.com/direction/verify/merge_trains/#key-capabilities)
      * [Roadmap](https://about.gitlab.com/direction/verify/merge_trains/#roadmap)
      * [Top Competitive Solutions](https://about.gitlab.com/direction/verify/merge_trains/#top-competitive-solutions)
    * [Target Audience](https://about.gitlab.com/direction/verify/merge_trains/#target-audience)
    * [Top Internal Customer Issue(s)](https://about.gitlab.com/direction/verify/merge_trains/#top-internal-customer-issues)


## Merge Trains[](https://about.gitlab.com/direction/verify/merge_trains/#merge-trains)
|   
---|---  
Stage | [Verify](https://about.gitlab.com/direction/verify/)  
Maturity | [Viable](https://about.gitlab.com/direction/#maturity)  
Content Last Reviewed | 2025-11-09  
Author | Rutvik Shah  
### Introduction and how you can help[](https://about.gitlab.com/direction/verify/merge_trains/#introduction-and-how-you-can-help)
Thanks for visiting this category direction page on Merge Trains in GitLab. This page belongs to the [Pipeline Execution](https://handbook.gitlab.com/handbook/product/categories/#pipeline-execution-group) group of the Verify stage and is maintained by Rutvik Shah (E-Mail).
This direction page is a work in progress, and everyone can contribute:
  * Please comment and contribute in the linked [issues](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=updated_desc&state=opened&label_name%5B%5D=Category%3AMerge%20Trains&first_page_size=50) and [epics](https://gitlab.com/groups/gitlab-org/-/epics?state=opened&page=1&sort=start_date_desc&label_name\[\]=Category:Merge+Trains) on this page. Sharing your feedback directly on GitLab.com is the best way to contribute to our strategy and vision.
  * Please share feedback directly via email, Twitter, or on a video call. If you're a GitLab user and want to discuss how GitLab can improve Review Apps, we'd especially love to hear from you.


### Overview[](https://about.gitlab.com/direction/verify/merge_trains/#overview)
We aim to help you balance speed with reliability, keeping your pipelines green. This ultimately supports the stability of collaboration across branches and GitLab has introduced Merge Trains as the mechanism to accomplish this. When merge trains are used, each merge request joins as the last item in that train. Each merge request is processed in order and is added to the merge result of the last successful merge request. The merge request adds its changes, and starts the pipeline immediately under the assumption that everything is going to pass. If the merge request fails, it is kicked out of the train and the next merge request continues the pipeline of the last successful merge result.
  * [Issue List](https://gitlab.com/groups/gitlab-org/-/issues?scope=all&utf8=%E2%9C%93&state=opened&label_name\[\]=Category%3AMerge%20Trains)
  * [Documentation](https://docs.gitlab.com/ee/ci/pipelines/merge_trains.html)


### 1 year plan[](https://about.gitlab.com/direction/verify/merge_trains/#1-year-plan)
For FY26 (ending February 2026):
We will be maintaining our Merge Trains functionality with a focused approach:
  * Bug Resolution: Prioritizing critical S1/S2 issues that have exceeded their service level objectives
  * Community Collaboration: Actively supporting community contributions that enhance this category
  * Feature Development: We will add additional [API support for Merge Trains](https://gitlab.com/groups/gitlab-org/-/epics/5864)


This strategic decision allows us to strengthen the core functionality while ensuring a dependable experience for current users.
#### What we are currently working on[](https://about.gitlab.com/direction/verify/merge_trains/#what-we-are-currently-working-on)
We are adding a UX improvement that will [allow users to re-add an MR back to Merge Train with a single click](https://gitlab.com/gitlab-org/gitlab/-/issues/451302) when an MR is dropped from the train due to an unexpected pipeline failure.
#### What we recently completed[](https://about.gitlab.com/direction/verify/merge_trains/#what-we-recently-completed)
  * When closing a merge request on a merge train, [all pipelines including child pipelines are now canceled](https://gitlab.com/gitlab-org/gitlab/-/issues/382065), saving CI resources.
  * Merge train commits now [maintain their links back to the original merge request even after rebasing during fast-forward merges](https://gitlab.com/gitlab-org/gitlab/-/issues/436943), ensuring accurate changelog generation and complete commit traceability for all merged requests.


### Best in Class Landscape[](https://about.gitlab.com/direction/verify/merge_trains/#best-in-class-landscape)
BIC (Best In Class) is an indicator of forecasted near-term market performance based on a combination of factors, including analyst views, market news, and feedback from the sales and product teams. It is critical that we understand where GitLab appears in the BIC landscape.
#### Key Capabilities[](https://about.gitlab.com/direction/verify/merge_trains/#key-capabilities)
  * Queue merge requests and verify their changes work together before they are merged to the target branch
  * Support fast-forward and semi-linear merge requests
  * Provide marge train visualization and administration capabilities


#### Roadmap[](https://about.gitlab.com/direction/verify/merge_trains/#roadmap)
This category is currently at the "Viable" maturity level, and our next maturity target is "Competitive" in future milestones. See our [Merge Train Maturity - Competitive Epic](https://gitlab.com/groups/gitlab-org/-/epics/2219) on the proposed plan
Key deliverables to achieve this are:
  * Completed - [Simplify merge strategies with Auto-merge](https://gitlab.com/groups/gitlab-org/-/epics/6687)
  * Completed - [Merge Trains should support fast-forward merge](https://gitlab.com/groups/gitlab-org/-/epics/4911)
  * [API support for merge trains](https://gitlab.com/groups/gitlab-org/-/epics/5864)
  * [Resolving Severity 1 and 2 bugs](https://gitlab.com/gitlab-org/gitlab/-/issues?sort=milestone_due_desc&state=opened&label_name\[\]=Category:Merge+Trains&label_name\[\]=type::bug&not\[label_name\]\[\]=severity::3&not\[label_name\]\[\]=severity::4)


#### Top Competitive Solutions[](https://about.gitlab.com/direction/verify/merge_trains/#top-competitive-solutions)
GitLab pioneered Merge Train functionality for CI/CD establishing early market leadership. While there are multiple solutions offering similar capabilities, GitLab's solution offers a more mature implementation that has been proven scalable for large development teams and complex CI/CD workflows.
[GitHub's Merge Queue](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue#about-merge-queues) is a feature that automates the process of merging pull requests into a repository by placing them in a queue and running checks against the latest version of the codebase.
[Aviator](https://www.aviator.co/) is the most comparable offering against Merge Trains, promising to "keep builds green forever", much like how we [positioned Merge Trains in 2020](https://about.gitlab.com/blog/all-aboard-merge-trains/) during their release.
[marge-bot](https://github.com/smarkets/marge-bot) is a popular open source program that works with GitLab to manage merge requests.
[Mergify](https://mergify.com/features/merge-queue) is another offering that integrates with GitHub repositories and multiple CI providers to supporty queued pull requests.
[Graphite](https://graphite.dev/features#merge-queue) offers similar capabilities as Merge Trains
### Target Audience[](https://about.gitlab.com/direction/verify/merge_trains/#target-audience)
Check out our [Ops Section Direction "Who's is it for?"](https://about.gitlab.com/direction/ops/#who-is-it-for) for an in depth look at the our target personas across Ops. For Merge Trains, our "What's Next & Why" are targeting the following personas, as ranked by priority for support:
  1. [Sasha - Software Developer](https://handbook.gitlab.com/handbook/product/personas/#sasha-software-developer)
  2. [Priyanka - Platform Engineer](https://handbook.gitlab.com/handbook/product/personas/#priyanka-platform-engineer)


### Top Internal Customer Issue(s)[](https://about.gitlab.com/direction/verify/merge_trains/#top-internal-customer-issues)
In an effort to dogfood our own features, we are actively working on using [merge trains internally on gitlab-org](https://gitlab.com/gitlab-org/quality/engineering-productivity/team/-/issues/513).
[Edit this page](https://gitlab.com/-/ide/project/gitlab-com/www-gitlab-com/edit/master/-/source/direction/verify/merge_trains/index.html.md) [View source](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/source/direction/verify/merge_trains/index.html.md)
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=800054037&_biz_u=5d8b0a8c77f548e88eadc0ccfbfc5a2b&_biz_l=https%3A%2F%2Fabout.gitlab.com%2Fdirection%2Fverify%2Fmerge_trains%2F&_biz_t=1773332027414&_biz_i=%0ACategory%20Direction%20-%20Merge%20Trains%0A%7C%0AGitLab%0A&_biz_n=105&rnd=74279&cdn_o=a&_biz_z=1773332027548)
suggested results