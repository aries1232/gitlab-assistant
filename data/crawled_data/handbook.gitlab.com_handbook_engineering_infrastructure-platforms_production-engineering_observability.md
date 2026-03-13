# Observability Team
Observability encompasses the technical elements responsible for metrics, logging, and tracing, along with the tools and processes that leverage these components.
Observability encompasses the technical elements responsible for metrics, logging, and tracing, along with the tools and processes that leverage these components.
## Mission[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#mission)
Our mission is to deliver and maintain a world-class observability offering and frictionless operational experience for team members at GitLab.
## Common Links[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#common-links)
|   
---|---  
**Workflow** | [Team workflow](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/)  
**GitLab.com** | `@gitlab-org/production-engineering/observability`  
**Issue Trackers** |  [Observability Tracker](https://gitlab.com/gitlab-com/gl-infra/observability/team/-/issues)   
[Tamland](https://gitlab.com/gitlab-com/gl-infra/tamland/-/issues)  
**Team Slack Channels** |  [#g_observability](https://gitlab.slack.com/archives/g_observability) - Team channel  
[#infrastructure_platforms_social](https://gitlab.enterprise.slack.com/archives/C062T669RFD) - Social channel  
**Information Slack Channels** |  [#infrastructure-lounge](https://gitlab.slack.com/archives/infrastructure-lounge) (Infrastructure Group Channel),   
[#incidents](https://gitlab.slack.com/archives/incidents) (Incident Management),   
[#g_infra_observability_alerts](https://gitlab.slack.com/archives/g_infra_observability_alerts) (Observability Slack Alerts),   
[#alerts-general](https://gitlab.slack.com/archives/alerts-general) (SLO alerting),   
[#mech_symp_alerts](https://gitlab.slack.com/archives/mech_symp_alerts) (Mechanical Sympathy Alerts)  
**Documentation** | [Documentation Hub](https://gitlab-com.gitlab.io/gl-infra/observability/docs-hub/)  
## Team Members[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#team-members)
The following people are members of the Observability team:
Name | Role  
---|---  
[![Liam McAndrew](https://about.gitlab.com/images/team/liammcandrew-crop.jpg)Liam McAndrew](https://handbook.gitlab.com/handbook/company/team/#lmcandrew) | [Engineering Manager, Observability](https://handbook.gitlab.com/job-families/engineering/infrastructure/engineering-management)  
[![Andreas Brandl](https://about.gitlab.com/images/team/abrandl-crop.jpg)Andreas Brandl](https://handbook.gitlab.com/handbook/company/team/#abrandl) |  [Staff Backend Engineer](https://handbook.gitlab.com/job-families/engineering/backend-engineer/), Observability  
[![Bob Van Landuyt](https://about.gitlab.com/images/team/bob-crop.jpg)Bob Van Landuyt](https://handbook.gitlab.com/handbook/company/team/#reprazent) |  [Staff Backend Engineer](https://handbook.gitlab.com/job-families/engineering/backend-engineer/), Observability  
[![Hercules Lemke Merscher](https://about.gitlab.com/images/team/hmerscher-crop.jpg)Hercules Lemke Merscher](https://handbook.gitlab.com/handbook/company/team/#hmerscher) |  [Backend Engineer](https://handbook.gitlab.com/job-families/engineering/backend-engineer/#backend-engineer), Observability  
[![Itay Rotman](https://about.gitlab.com/images/team/itayrotman-crop.jpg)Itay Rotman](https://handbook.gitlab.com/handbook/company/team/#irotman) | [Site Reliability Engineer](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/)  
[![Calliope Gardner](https://about.gitlab.com/images/gitlab-logo-extra-whitespace.png)Calliope Gardner](https://handbook.gitlab.com/handbook/company/team/#knottos) |  [Site Reliability Engineer](https://handbook.gitlab.com/job-families/engineering/infrastructure/site-reliability-engineer/), Observability  
[![Nick Duff](https://about.gitlab.com/images/team/nduff-crop.jpg)Nick Duff](https://handbook.gitlab.com/handbook/company/team/#nduff) |  [Senior Site Reliability Engineer](https://handbook.gitlab.com/job-families/engineering/infrastructure/site-reliability-engineer/), Observability  
[![Padraig O Neill](https://about.gitlab.com/images/team/poneill-crop.jpg)Padraig O Neill](https://handbook.gitlab.com/handbook/company/team/#poneill) |  [Site Reliability Engineer](https://handbook.gitlab.com/job-families/engineering/infrastructure/site-reliability-engineer/), Observability  
[![Taliesin Millhouse](https://about.gitlab.com/images/team/tmillhouse-crop.jpg)Taliesin Millhouse](https://handbook.gitlab.com/handbook/company/team/#tmillhouse) |  [Site Reliability Engineer](https://handbook.gitlab.com/job-families/engineering/infrastructure/site-reliability-engineer/), Observability  
[![Tony Ganga](https://about.gitlab.com/images/team/tganga-crop.jpg)Tony Ganga](https://handbook.gitlab.com/handbook/company/team/#tonyganga) |  [Site Reliability Engineer](https://handbook.gitlab.com/job-families/engineering/infrastructure/site-reliability-engineer/), Observability  
The team is located all over the world in [different timezones](https://timezonewizard.com/ca-m2n).
## Technical principles, goals and responsibilities[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#technical-principles-goals-and-responsibilities)
Please see [the Technical Blueprint](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/technical_blueprint/) for details on our principles and goals.
The following gives an overview of our scope and ownership.
  1. [Monitoring fundamentals](https://gitlab.com/gitlab-com/runbooks/blob/e00eeb59937a9043c5db04314a35acb05c4e9288/docs/monitoring/README.md#L1)
    1. Metrics stack
    2. Logging stack
  2. [Error budgets](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/error_budgets/)
    1. Ownership of concept and implementation
    2. Delivery of monthly error budget report
  3. [Capacity planning](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/capacity_planning/)
    1. [Triage rotation for .com](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/capacity-planning/#gitlabcom-capacity-planning)
    2. [Operational aspects for GitLab Dedicated capacity planning](https://docs.gitlab.com/ee/architecture/blueprints/capacity_planning/)
    3. Developing [Tamland](https://gitlab.com/gitlab-com/gl-infra/tamland), the forecasting tool
    4. [Capacity reporting for GitLab Dedicated](https://gitlab.com/gitlab-com/gl-infra/capacity-planning-trackers/gitlab-dedicated)
  4. [Service Maturity model](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/service-maturity-model/) which covers GitLab.com’s production services.
  5. [GitLab.com availability reporting](https://handbook.gitlab.com/handbook/engineering/monitoring/): Provide underlying data and aggregate numbers


### Documentation[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#documentation)
We recognize the need to provide technical documentation for teams using our observability services and platforms, as well as for our team’s internal use.
Historically, we’ve provided reference documentation within the projects we own or contribute to, or in the [runbooks project](https://gitlab.com/gitlab-com/runbooks/-/tree/master/docs). As these projects are scattered around, it is rather difficult to discover the various pieces of relevant documentation for our users.
As we reshape our documentation, we follow along with the following idea and principles:
  1. The [Infrastructure Observability Documentation Hub](https://gitlab-com.gitlab.io/gl-infra/observability/docs-hub/) is the entrypoint for any observability related documentation we provide.
  2. Carefully crafted documentation is a core product for the observability platform, not an afterthought.
  3. We think of the documentation hub as a way to communicate about observability interfaces we offer as a platform with everyone in Engineering.
  4. We strive to provide documentation like guides and tutorials targeted for specific audiences - in addition to reference documentation.
  5. We use the documentation hub also to explain concepts and architecture for our team’s internal use to create a common understanding and empower everyone to contribute in all areas.


#### Where do we keep different types of documentation?[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#where-do-we-keep-different-types-of-documentation)
There are different types of documentation, which belong in different places.
What? | Where?  
---|---  
Team organisation, processes and other team level agreements | GitLab Handbook (this page)  
Technical reference documentation for standalone projects | On the project itself, and linked to the Documentation Hub  
How do we at GitLab make use of the projects we maintain? | Documentation Hub  
How does our GitLab specific architecture look like? | Documentation Hub  
Tutorials, guides, FAQs and conceptual explanations | Documentation Hub  
Documentation outside the Documentation Hub should be linked from it (that’s why we call it a _hub_) and vice versa, to help increase discoverability.
This recognizes the need to ship reference documentation with the respective project, as we would expect to see for any project (whether open source or not). The benefit here is that a change in functionality can also update reference documentation in the same merge request.
On the other hand, how we make particular use of these projects in our stack is too specific to ship with the project itself. Often, we want to understand the bigger picture and how projects play together. This is out of scope for technical documentation that ships with a certain project itself and hence we put this information on the documentation hub instead.
For our internal use, we use the documentation hub to help us reason about the services we own and how we operate them. We expect this helps everyone on the team and helps us gather a common understanding as we have different roles and perspectives on the team.
A recommended read on different types of documentation and how to organize it is the [Divio Documentation System](https://docs.divio.com/documentation-system/).
#### How do we create documentation?[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#how-do-we-create-documentation)
As we reshape and build documentation, the documentation hub benefits from each and all contributions:
  1. Explain existing concepts
  2. Link together existing documentation
  3. Consolidate existing documentation and move in the right places
  4. Writing and graphics on system architecture and operational principles


We aspire to create and maintain documentation as a primary citizen and similar to the [Handbook First](https://handbook.gitlab.com/handbook/company/culture/all-remote/handbook-first/) mindset. For example, instead of answering specific questions from team members individually (for example on Slack), we can take this as an opportunity to write a piece of documentation and ask them to review and work with that.
### Indicators[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#indicators)
The group is an owner of several performance indicators that roll up to the Infrastructure department indicators:
  1. [Service Maturity model](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/service-maturity-model/) which covers GitLab.com’s production services.
  2. [Capacity Planning](https://gitlab-com.gitlab.io/gl-infra/observability/docs-hub/capacity-planning/introduction/) uses capacity warnings to prevent incidents.


These are combined to enable us to better prioritize team projects.
An overly simplified example of how these indicators might be used, in no particular order:
  * Service Maturity - provides detail on how trustworthy the data we received from observability stack in relation to the service; the lower the level the more focus we need to improve the service observability
  * Capacity Planning - Provides a forecast for a specific service


Between these different signals, we have a relatively (im)precise view into the past, present and future to help us prioritise scaling needs for GitLab.com.
### Provisioned Services[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#provisioned-services)
The team are responsible for provisioning access to the services listed below, as per the [tech_stack.yml](https://gitlab.com/gitlab-com/www-gitlab-com/-/blob/master/data/tech_stack.yml) file.
  1. **Kibana** is accessed through Okta. Team members need to be in either of the following Okta groups: `gl-engineering` (entire Engineering department); `okta-kibana-users`. The latter group is used to manage access for team members outside of Engineering on an ad-hoc basis ([context](https://gitlab.com/gitlab-com/business-technology/change-management/-/issues/958)). Team members should be (de)provisioned through an Access Request ([example](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/28421)). If the access request is approved, the provisioner should add the user to [this group](https://groups.google.com/a/gitlab.com/g/okta-kibana-users), which will then automatically sync to its namesake group in Okta.
  2. **Elastic Cloud** is for administrative access to our Elastic stack. The login screen is available [here](https://cloud.elastic.co/) and access is through Google SSO. Team members should be (de)provisioned through an Access Request ([example](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/28457)). If approved, the provisioner can add/remove members on the [membership page](https://cloud.elastic.co/account/members) with appropriate permissions to the instances they require access to.
  3. **Grafana** is accessed through Okta. The login screen is availabile [here](https://dashboards.gitlab.net). Any GitLab team member can access Grafana. Provisioning and deprovisioning is handled through Okta.


## How we work[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#how-we-work)
We default to working inline with the GitLab [values](https://handbook.gitlab.com/handbook/values/) and by following the processes of the wider [Infrastructure Platforms section](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/project-management/). In addition to this, listed below are some processes that are specific, or particularly important, to how we work in Observability.
### Roadmap[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#roadmap)
We transparently prioritize our Roadmap in this [epic](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1295), which includes a view of how all Epics/Issues are grouped using `roadmap::` labels.
### Project Management[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#project-management)
Most projects that we work on are represented by [Epics](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/) that contain multiple Issues. Simple tasks can be worked on in [Issues](https://gitlab.com/gitlab-com/gl-infra/observability/team/-/issues) without a parent epic.
### Project Sizing[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#project-sizing)
Projects will be staffed by at least three engineers from the team, and preferably from both SRE and BE roles. This will allow us to share knowledge and keep projects moving forward when people are unavailable.
With the number of people on the team and the additional demands of KTLO and on-call, we can only have 2 projects in progress at any time.
#### Labels[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#labels)
All Epics/Issues pertaining to our team have the `~"group::Observability"` label.
We use the following `roadmap::` labels to represent the current priorities of our team:
  * `roadmap::now` items that are currently being worked on
  * `roadmap::next` items that are candidates to be picked up next
  * `roadmap::later` items that aren’t directly in our plans to be worked on
  * `roadmap::perpetual` items that are always relevant, such as version upgrades


We use `Category:` labels to represent the functional area of a work item. Examples include `Category:Logging` and `Category:Capacity Planning`.
We use `theme::` labels to group the type of work and its benefit. Labels include:
  * `theme::Operational Excellence` Operations processes that keep a system running in production
  * `theme::Performance Enablement` The ability of a system to adapt to changes in load
  * `theme::Reliability` The ability of a system to recover from failures and continue to function
  * `theme::Security` Protecting applications and data from threats
  * `theme::Cost Optimization` Managing costs to maximize the value delivered
  * `theme::Shift Left` items that encourage other stage groups to self-serve
  * `theme::Enablement & Assistance` items that require directly helping other Stage Group. We try to minimize this work by Shifting Left.


The first 5 `theme` labels cover the primary pillars covered by Well-Architected Frameworks. You can read more about this topic [here](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1350).
We also use the `workflow-infra::` labels to show where in the work cycle a particular Epic or Issue is.
In addition, all issues require either a Service label or the team-tasks, discussion, or capacity planning labels.
#### Boards[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#boards)
  * [Issues by Assignee](https://gitlab.com/groups/gitlab-com/gl-infra/-/boards/7339126)
  * [Epics by Workflow](https://gitlab.com/groups/gitlab-com/gl-infra/-/epic_boards/38727?not%5Blabel_name%5D%5B%5D=roadmap&label_name%5B%5D=group::Observability)
  * [Epics by Roadmap](https://gitlab.com/groups/gitlab-com/gl-infra/-/epic_boards/2077560?not%5Blabel_name%5D%5B%5D=roadmap&label_name%5B%5D=group::Observability)
  * [Epics by Theme](https://gitlab.com/groups/gitlab-com/gl-infra/-/epic_boards/2077564?not%5Blabel_name%5D%5B%5D=roadmap&label_name%5B%5D=group::Observability)
  * [Epics by Category](https://gitlab.com/groups/gitlab-com/gl-infra/-/epic_boards/1060230?not%5Blabel_name%5D%5B%5D=roadmap&label_name%5B%5D=group::Observability)


#### Assignees[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#assignees)
We use issue assignments to signal who is the DRI for the issue. We expect issue assignees to regularly update their issues with the status, and to be as explicit as possible at what has been done and what still needs to be done. We expect the assignee of an issue to drive the issue to completion. The assignee status typically expresses that the assigned team member is currently actively working on this or planning to come back to it relatively soon. We unassign ourselves from issues we are not actively working on or planning to revisit in a few days.
#### Group Reviews[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#group-reviews)
The Production Engineering group review happens every Thursday. We ensure that all work items with a `roadmap::now` label have a status update each Wednesday. We use [this epic](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1638) to share updates, which is generated by this [script](https://gitlab.com/gitlab-com/gl-infra/group-review-automator/).
To help improve visibility of all work in progress, it is expected that each team member is assigned to at least one project that is visible in the `roadmap::now` section of the [Group Review epic](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1638#-current-focus-roadmapnow) - either as a DRI or participant.
#### Retrospectives[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#retrospectives)
A team-level retrospective issue is created every 6 weeks, allowing the team to regularly reflect and to encourage a culture of continuous improvement. The creation of the retrospective issue is the responsibility of the Engineering Manager. You can find retrospectives [here](https://gitlab.com/gitlab-com/gl-infra/scalability/-/issues/?sort=created_date&state=all&label_name%5B%5D=team%3A%3AScalability-Observability&label_name%5B%5D=Retrospective&first_page_size=100).
### Updates in Slack[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#updates-in-slack)
We are using [GeekBot](https://app.geekbot.com/dashboard/w/184476) for weekly updates, which go to the #g_observability channel.
When posting updates, consider providing enough context (e.g. through links) so that interested team members are able to dive in on their own ([low context](https://handbook.gitlab.com/handbook/communication/#low-context)).
### Team Happiness[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#team-happiness)
Each Thursday a reminder is sent in our Slack channel asking team members to score their happiness for the week using [this form](https://forms.gle/xsToh7RzGBas2rkp8). Team members can view the results in [this spreadsheet](https://docs.google.com/spreadsheets/d/1JMYG9HCRMj6ZBMrqsRy2TCs3LwIBL3Hz44WtlbDTpQk/) (note there is also a visualization in the ‘Graph’ sheet).
### Cost Management[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#cost-management)
For details on the daily operational costs of our observability services refer to the [Cost of Observability Stack](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/cost/) documentation. This resource includes access instructions and cost breakdowns.
## History and Accomplishments[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#history-and-accomplishments)
This section contains notes on team history and our accomplishments, but is not meant to be exhaustive.
  * 2024-02, Capacity planning: [Proactive investigation of postgres CPU spike seen in saturation forecast](https://gitlab.com/gitlab-com/gl-infra/capacity-planning-trackers/gitlab-com/-/issues/1668#note_1807225359) uncovered a [database design issue](https://gitlab.com/gitlab-org/gitlab/-/issues/435250)
  * 2024-03, Capacity planning: [Tamland predicted redis CPU saturation which led to Practices proactively scaling Redis](https://gitlab.com/gitlab-com/gl-infra/capacity-planning-trackers/gitlab-com/-/issues/1712) ([slides](https://docs.google.com/presentation/d/1y58mgaUrpu1dBO_bKVLfDUez9lz-ETLE7E1yksDjAbY/edit#slide=id.g2cc1c00d163_5_4))
  * 2024-05, Metrics: [The migration from Thanos to Mimir was completed](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1107) which brought [significant improvements](https://gitlab.com/groups/gitlab-com/gl-infra/-/epics/1107#outcome) in metrics accuracy and dashboard performance.


### Year-in-Review Issues[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/#year-in-review-issues)
  * [2024](https://gitlab.com/gitlab-com/gl-infra/observability/team/-/issues/4024)


* * *
#####  [Capacity Planning](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/capacity_planning/)
We maintain and improve the Capacity Planning process that is described in the Infrastructure …
#####  [Cost of Observability Stack](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/cost/)
Elastic Cloud Costs (Snowflake) Where to Find the Views You can find the view here. Access …
#####  [Error Budgets](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/error_budgets/)
We maintain the Error Budgets process that is described in the Engineering Handbook. Issues are kept …
#####  [Technical Blueprint](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/observability/technical_blueprint/)
The purpose of this document is to detail the goals and guidelines for the Observability team. The …
Last modified February 24, 2026: [Move /infrastructure product and platform pages to /infrastructure-platforms (`f2f44b0d`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/f2f44b0d)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/infrastructure-platforms/production-engineering/observability/_index.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/infrastructure-platforms/production-engineering/observability/_index.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)