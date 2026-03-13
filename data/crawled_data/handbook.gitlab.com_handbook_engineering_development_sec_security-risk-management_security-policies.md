# Security Risk Management, Security Policies
The Security Policies team at GitLab is responsible for creating solutions that enforce scans, and require security approvals once vulnerabilities are detected.
## Mission[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#mission)
The Security Policies group’s mission is to provide security and compliance teams with a way to enforce security controls globally in their organization. With tools developed by our team, customers can prevent security risks by enforcing and automating security scans and requiring security approvals for proposed changes in their repository. For a comprehensive understanding of our vision and direction, we invite you to visit the Direction page at <https://about.gitlab.com/direction/security_risk_management/security_policies/security_policy_management/>.
## Top Priorities FY25[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#top-priorities-fy25)
  * Integrate Security Policies with other Security Risk Management feature categories by allowing users to scope policies to selected Compliance Frameworks or Projects.
  * Allow for complex and customized Scan Execution Policies by introducing Pipeline Execution Action with the ability to enforce Custom CI YAML for selected projects and groups.
  * Help users understand why we require merge request approvals in their MRs by displaying Security Policy Violation details as a comment with helpful information.
  * Help customers with the slow rollout of features from the Security Policies team by customizing their policy configuration to allow them to select if they want to fail open or fail closed in case the policy or project is misconfigured.
  * Decrease performance impact on runners when enforcing scheduled Scan Execution Policies.
  * Ability to enforce policies on Organization Level.


### Customer Outcomes we are driving for GitLab[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#customer-outcomes-we-are-driving-for-gitlab)
  1. Increase usage of Merge Request Approval Policies with detailed information explaining why we require approvals for given MR.
  2. Speed up adoption time in enabling Security Policies by providing a way to enforce them gradually without blocking their current workflows for selected projects or projects with given Compliance Frameworks only.
  3. Increase the flexibility of Scan Execution Policies and allow users limitless possibilities with enforcing any job with Pipeline Execution Action for selected projects and groups.
  4. Help other groups introduce new types of policies to help customers automate and manage their security controls on group and organization levels.


## Common Links[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#common-links)
  * Slack channel: `#g_srm_security_policies`
  * Slack alias: @govern_security_policies_be, @govern_security_policies_fe
  * Google groups: sec-govern-security-policies@gitlab.com


## How we work[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#how-we-work)
### Prioritization[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#prioritization)
We use our [Security Policies Priorities](https://about.gitlab.com/direction/security_risk_management/security_policies/security_policy_management/#security-policies) list in our direction page to track what we are doing, and what order to do it in. Each initiative includes these fields:
  1. Name - Description and link to the epic
  2. BE DRI / FE DRI - indicates the backend and frontend [DRIs](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/srm-planning/#epic-engineering-dri) who will be actively involved.
  3. Size
  4. Target Release


Complete items are removed from the table once the code is in production without a feature flag, and a release post, if applicable, has been merged. The epic is closed at this point.
### Workflow[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#workflow)
The Security Policies group largely follows GitLab’s [Product Development Flow](https://handbook.gitlab.com/handbook/product-development/how-we-work/product-development-flow/).
Additional information about how we operate can be found on the [Planning page](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/srm-planning/).
Our current workflow is visualized as flowchart on the [Workflow page](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/workflow/).
Our current process on how we work on features is on the [Feature process page](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/feature_process/)
#### MR Reviews[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#mr-reviews)
We follow these guidelines when submitting MRs for review when the change is within the Security Policies domain:
  1. The initial review should be performed by a member of the team, stage, or section. This helps the team by: 
     * Faster reviews, as the reviewer is already familiar with the domain
     * Additional awareness of changes taking place within the domain
     * Identifying changes that don’t align with what is happening with the domain
  2. For GraphQL changes, the MR should be reviewed by a frontend engineer as soon as possible. This helps to validate the interface, and allows changes to be made before tests are written.


### Issue Boards[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#issue-boards)
  * [Security Policies Delivery Board](https://gitlab.com/groups/gitlab-org/-/boards/1754674?milestone_title=Started)
    * Primary board for engineers from which engineers can work. It’s stripped down to only include the workflow labels we use when delivering software.
  * [Security Policies Planning Board](https://gitlab.com/groups/gitlab-org/-/boards/1420731?label_name%5B%5D=group%3A%3Asecurity%20policies)
    * Milestone-centric board primarily used by product management to gauge work in current and upcoming milestones.
  * [Security Policies EM Board](https://gitlab.com/groups/gitlab-org/-/boards/4738985)
    * Engineer-centric board used by engineering management to gauge how heavy a load engineer is carrying. Judged by the number of issues assigned to them.


#### Issue and Merge Requests labels[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#issue-and-merge-requests-labels)
GitLab has a labeling convention for issues and Merge Requests. We follow this convention, though there are specific labels required to route artifacts to us. We use these labels to filter issues meant for us on our issue boards. They are also used for metrics and KPI reporting.
Label | Meaning  
---|---  
~“section::sec” | Identifies the issue or MR as belonging to the Sec Section’s roadmap.  
~devops::govern | Identifies the issue or MR as belonging to the Security Risk Management Stage’s roadmap.  
~“group::security policies” | Identifies the Security Policies group as the collection of individuals who will work on the issue or MR.  
~“Category:Security Policy Management” | Identifies the issue or MR as being part of the Security Policy Management feature category.  
~backend | Identifies the issue or MR as being part of GitLab’s backend.  
~frontend | Identifies the issue or MR as being part of GitLab’s frontend.  
When creating a new issue, use the `/copy_metadata #373191` quick command to copy required labels.
## Quality[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#quality)
### How to classify MRs which need to run Package and QA?[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#how-to-classify-mrs-which-need-to-run-package-and-qa)
It is advisable to manually trigger the `Package and QA` downstream [E2E](https://docs.gitlab.com/ee/development/testing_guide/end_to_end/) job in an MR and review the results when there are changes in:
  * GraphQL (API response, query parameters, schema etc)
  * Gemfile (version changes, adding/removing gems)
  * Vue files which contain “data-qa-selector” attribute because these are used in identifying UI elements in E2E tests
  * Database schema/query changes
  * Any frontend changes which directly impact vulnerability report page, MR security widget, pipeline security tab, security policies, configuration, license compliance page


To manually trigger the QA job:
  1. Navigate to the pipelines tab of the MR.
  2. Click the `>` arrow on the right of the `Stages` and click the `package-and-qa` item.


It’s advisable to run the QA job on the latest pipeline at least once during the MR review cycle.
## Monitoring[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#monitoring)
  * [Stage Group dashboad on Grafana](https://dashboards.gitlab.net/d/stage-groups-security_policies/stage-groups-security-policies-group-dashboard?orgId=1)


### Metrics the team tracks[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#metrics-the-team-tracks)
#### Engineering productivity metrics[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#engineering-productivity-metrics)
  * Total Open Bug by Severity
  * Overall MRs by Type %
  * Group MR Rate
  * Flaky Test Issues
  * Slow RSpec Tests Issues


#### Product metrics[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#product-metrics)
Adoption of Security Policies features:
  * Number of projects with an assigned security policy project
  * Number of groups with an assigned security policy project
  * Number of open merge requests with at least one applicable scan result policy
  * Number of projects with at least one scan result policy
  * Number of users who have created merge requests with at least one applicable scan result policy
  * Number of users who have created merge requests in Projects that have an assigned security policy project
  * Unique count of Security Risk Management actions in a given timeframe
  * Unique count of the Security Policies actions in a given timeframe
  * Unique count of the Security Policies visits in a given timeframe
  * Unique count of users creating merge requests with security policies in a given timeframe


## Contributing[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#contributing)
### Local testing of licensed features[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#local-testing-of-licensed-features)
When a feature needs to check the current license tier, it’s important to make sure this also works on GitLab.com.
To emulate this locally, follow these steps:
  1. Export an environment variable: `export GITLAB_SIMULATE_SAAS=1`[1](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#fn:1)
  2. Within the same shell session run `gdk restart`
  3. Admin > Settings > General > “Account and limit”, enable “Allow use of licensed EE features”


See the [related handbook entry](https://docs.gitlab.com/ee/development/ee_features.html#act-as-saas) for more details.
### Cross-stack collaboration[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#cross-stack-collaboration)
We encourage frontend engineers to contribute to the backend and vice versa. In such cases we should work closely with a domain expert from within our group and also keep the initial review internal.
This will help ensure that the changes follow best practice, are well tested, have no unintended side effects, and help the team be across any changes that go into the Security Policies codebase.
### Community Contributions[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#community-contributions)
The Security Policies group welcomes community contributions. Any community contribution should get prompt feedback from one of the Security Policies engineers. All engineers on the team are responsible for working with community contributions. If a team member does not have time to review a community contribution, please tag the Engineering Manager, so that they can assign the community contribution to another team member.
## Footnotes[](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#footnotes)
* * *
  1. Please refer to the [Environment variables](https://gitlab-org.gitlab.io/gitlab-development-kit/configuration/#environment-variables) section in the GitLab Development Kit (GDK) configuration page for the up-to-date steps to set up your environment variables. [↩︎](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/#fnref:1)


* * *
#####  [Security Policies - How we prioritize our current work?](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/workflow/)
How do we prioritize our current work? Please refer to the flowchart provided below to understand …
#####  [Security Policies - Working on features](https://handbook.gitlab.com/handbook/engineering/development/sec/security-risk-management/security-policies/feature_process/)
Process Feature development is organized in an epic that collects feature related issues. Features …
Last modified December 15, 2025: [Update the Environment Variable setup helper foot (`0c4fec21`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/0c4fec21)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/development/sec/security-risk-management/security-policies/_index.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/development/sec/security-risk-management/security-policies/_index.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)