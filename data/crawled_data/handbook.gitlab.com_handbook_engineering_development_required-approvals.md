# Development Required Approvals
## Overview[](https://handbook.gitlab.com/handbook/engineering/development/required-approvals/#overview)
There are specific scenarios we are identifying that will require additional approval before moving forward. At GitLab we value [freedom and responsibility over rigidity](https://handbook.gitlab.com/handbook/values/#freedom-and-responsibility-over-rigidity), however in the [examples requiring approval](https://handbook.gitlab.com/handbook/engineering/development/required-approvals/#examples-requiring-approval) section below we outline which decisions will need to go through the approval process before proceeding.
### Approval Process[](https://handbook.gitlab.com/handbook/engineering/development/required-approvals/#approval-process)
Each section requiring approvals will have a considerations section. If you answered yes to all of the questions in the considerations section, then you will need to get approval for your proposal before proceeding with implementation. Steps for the approval process:
  * Submit an issue with your design proposals
  * Make the issue visible to the CEO and all Fellow Engineers. 
    * Label with ~“CEO Interest”
  * You will need to gain approval from the CEO and one Fellow Engineer
  * Use the issue created in the first step to coordinate how to gain approval


### Examples Requiring Approval[](https://handbook.gitlab.com/handbook/engineering/development/required-approvals/#examples-requiring-approval)
#### Proposing a separate database[](https://handbook.gitlab.com/handbook/engineering/development/required-approvals/#proposing-a-separate-database)
As we’ve learned from our discussions around [defining the container registry database schema](https://gitlab.com/gitlab-org/gitlab/-/issues/207147) there are times when it makes sense to separate the data out into its own database. The following sections will describe what data points you should consider and how you would move forward in gaining approval to create a separate database.
##### Considerations[](https://handbook.gitlab.com/handbook/engineering/development/required-approvals/#considerations)
  * Was the feature written in a completely separate code base? Again, using the Container Registry example, this was written in Go and is separate from the main GitLab Rails application. 
    * Only do a separate database when it has a completely separate codebase, and that is the only codebase querying the data. For example, [Analytics Instrumentation](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/27730) isn’t fit for it since the Rails codebase touches it.
  * Will the feature incur a heavy write load? Writes are harder to scale than reads who can be scaled with replicas.
  * Will the feature not need any access to the main Rails database? Example, the data is completely isolated from the main Rails database and will not need to share data across databases.
  * Are there existing APIs that we need to support? For example, the container registry has a full set of APIs (<https://docs.docker.com/registry/>) that we already use in the existing GitLab Rails application to retrieve tags, etc.


#### Proposing the creation of microservices[](https://handbook.gitlab.com/handbook/engineering/development/required-approvals/#proposing-the-creation-of-microservices)
The [trouble with microservices](https://handbook.gitlab.com/handbook/engineering/data-engineering/database-excellence/database-frameworks/doc/strategy/#the-trouble-with-microservices) is not a new topic to GitLab. With our company strategy of a Flywheel with two turbos we default to delivering GitLab as a [single application](https://handbook.gitlab.com/handbook/product/categories/gitlab-the-product/single-application/). However, we are not opposed to adopting the right architecture to solve our problems at scale, in this case microservices. When submitting your proposal for the creation of microservices for [approval](https://handbook.gitlab.com/handbook/engineering/development/required-approvals/#approval-process) please be sure to include the following considerations.
##### Considerations[](https://handbook.gitlab.com/handbook/engineering/development/required-approvals/#considerations-1)
  * Given that our direction indicates we are [Saas First](https://about.gitlab.com/direction/#saas-first) how will this change improve our SaaS first offering? 
    * How can these improvements be measured going forward?
  * How will this impact our self-managed customers?
  * Can this problem be solved in our current monolithic environment?
  * Are the ongoing deployment considerations listed in your proposal?


Last modified November 19, 2025: [Bulk move of Database teams to Database Excellence (`c578076b`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/c578076b)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/development/required-approvals.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/development/required-approvals.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)