# Infrastructure Product Management
## Responsibilities[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/product-management/#responsibilities)
The responsibilities of the Infrastructure Product Manager are [documented in the job-families page](https://handbook.gitlab.com/job-description-library/product/product-manager/).
## Engagement Model[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/product-management/#engagement-model)
### Inbound Requests[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/product-management/#inbound-requests)
The Infra PM can help triage and prirotize _inbound_ requests to Infrastructure from internal teams and GitLab.com customers.
Types of requests:
  1. Dogfooding requests 
     * e.g. [Runbooks](https://gitlab.com/gitlab-com/gl-infra/infrastructure/-/issues/10748)
  2. [Security and Compliance Requests](https://gitlab.com/gitlab-com/gl-infra/infrastructure/-/issues/10982)
  3. GitLab.com customer requests in remit of the Infrastructure department: 
     * GitLab.com customers, especially enterprises, may often have requests related to operational capabilities or [non-functional requirements](https://en.wikipedia.org/wiki/Non-functional_requirement) of GitLab.com (e.g. availability, security, and performance of the service). Requests related to functionality [within the application itself](https://gitlab.com/gitlab-org/gitlab/) should be directed to the appropriate stage team using the standard [feature request template](https://gitlab.com/gitlab-org/gitlab/-/blob/master/.gitlab/issue_templates/Feature%20proposal%20-%20detailed.md).


Examples of requests related to operational capabilities of GitLab.com include:
  1. Disaster Recovery SLA
  2. [Publishing an allocated range of ingress IPs](https://gitlab.com/gitlab-com/gl-infra/infrastructure/-/issues/10768)
  3. Data locality (e.g. a GitLab.eu instance)
  4. Certifications (e.g. FedRAMP)


The Infra PM can help prioritize these requests since they will likely require engineering investment from the Infrastructure department.
#### How to submit customer requests related to GitLab.com[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/product-management/#how-to-submit-customer-requests-related-to-gitlabcom)
To submit customer requests related to the operational capabilities of GitLab.com, use the [GitLab.com feature request template](https://gitlab.com/gitlab-com/gl-infra/infrastructure/-/issues/new?issuable_template=request-gitlab-com) so that we can gather the necessary opportunity size data to help prioritize this request
### Outbound Requests[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/product-management/#outbound-requests)
The Infra PM can also help drive _outbound_ requests on behalf of Infrastructure to internal teams and GitLab.com customers.
Types of requests:
  1. Changes needed within the GitLab application 
     * e.g. [Kubernetes Migration Blockers](https://gitlab.com/groups/gitlab-org/-/boards/1836252?label_name\[\]=kubernetes-migration-blocker)
  2. Outreach to GitLab.com customers 
     * e.g. [Document additional egress IP ranges for SaaS](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/37444)
  3. Driving cost efficiences across stages 
     * e.g. [Registry Cost](https://gitlab.com/gitlab-com/gl-infra/infrastructure/-/issues/8163) (internal only)


### General Questions[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/product-management/#general-questions)
For general inquiries, use the [Infrastructure PM Slack Channel](https://gitlab.slack.com/archives/infra-product).
## Workflow[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/product-management/#workflow)
To request assistance from the Infrastructure Product Manager, add the ~“infrapm” label to an issue. Next, the Infra PM will consider the issue by moving it to the ~“workflow::problem validation” phase for validation, scoping, and prioritization. After completing these steps, if the Infra PM determines the effort is worth pursuing, they will then follow the established [Infrastructure Platforms team](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/#organization-structure) workflows by adding the appropriate team label and moving the issue to the ~“workflow-infra::Triage” phase for engineering review.
## Prioritization Framework[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/product-management/#prioritization-framework)
To prioritize initiatives, the Infra PM uses the framework [documented in the Product handbook](https://handbook.gitlab.com/handbook/product/product-processes/#prioritization).
## Issue Board[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/product-management/#issue-board)
Infrastructure Product Manager Tasks are tracked on the [Infra PM Issue Board](https://gitlab.com/groups/gitlab-com/gl-infra/-/boards/1880375?label_name\[\]=infrapm)
Last modified March 4, 2026: [Rename job-families to job-description-library (`6f520606`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/6f520606)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/infrastructure-platforms/product-management.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/infrastructure-platforms/product-management.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)