# Package
## Mission and Vision[](https://handbook.gitlab.com/handbook/engineering/devops/package/#mission-and-vision)
The Package stage creates a secure environment where both source code and dependencies can live by allowing you to publish, consume, and discover packages across a variety of languages and platforms all in one place. Our vision is to be our customers’ single source of truth for storing and distributing packages and container images across the entire DevOps lifecycle.
## Team Structure[](https://handbook.gitlab.com/handbook/engineering/devops/package/#team-structure)
The Package stage consists of two groups:
  1. Package:Container Registry - Backend Go service for OCI-compliant container image storage
  2. Package:Package Registry - Package management features within GitLab Rails application


### Team Members[](https://handbook.gitlab.com/handbook/engineering/devops/package/#team-members)
The following teams make up the Package stage:
Name | Role  
---|---  
[![Crystal Poole](https://about.gitlab.com/images/team/crystalpoole-crop.jpg)Crystal Poole](https://handbook.gitlab.com/handbook/company/team/#crystalpoole) | [Senior Engineering Manager, Package](https://handbook.gitlab.com/job-families/engineering/development/management/senior-manager/)  
[![Jaime Martínez](https://about.gitlab.com/images/team/jaimemartinez-crop.jpg)Jaime Martínez](https://handbook.gitlab.com/handbook/company/team/#jaime) | [Engineering Manager, Container Registry](https://handbook.gitlab.com/job-families/engineering/development/management/engineering-manager/)  
[![João Pereira](https://about.gitlab.com/images/team/joaopereira-crop.jpg)João Pereira](https://handbook.gitlab.com/handbook/company/team/#jdrpereira) | [Staff Backend Engineer, Package:Container Registry](https://handbook.gitlab.com/job-families/engineering/development/backend/staff/)  
[![Rahul Chanila](https://about.gitlab.com/images/gitlab-logo-extra-whitespace.png)Rahul Chanila](https://handbook.gitlab.com/handbook/company/team/#rchanila) | [Senior Frontend Engineer, Package:Container Registry](https://handbook.gitlab.com/job-families/engineering/development/frontend/)  
Name | Role  
---|---  
[![Crystal Poole](https://about.gitlab.com/images/team/crystalpoole-crop.jpg)Crystal Poole](https://handbook.gitlab.com/handbook/company/team/#crystalpoole) | [Senior Engineering Manager, Package](https://handbook.gitlab.com/job-families/engineering/development/management/senior-manager/)  
[![David Fernandez](https://about.gitlab.com/images/team/davidfernandez-crop.jpg)David Fernandez](https://handbook.gitlab.com/handbook/company/team/#10io) | [Staff Backend Engineer, Package:Package Registry](https://handbook.gitlab.com/job-families/engineering/development/backend/staff/)  
[![Dzmitry Meshcharakou](https://about.gitlab.com/images/team/dmeshcharakou-crop.jpg)Dzmitry Meshcharakou](https://handbook.gitlab.com/handbook/company/team/#dmeshcharakou) | [Senior Backend Engineer, Package:Package Registry](https://handbook.gitlab.com/job-families/engineering/development/backend/senior/)  
[![Moaz Khalifa](https://about.gitlab.com/images/team/moazkhalifa-crop.jpg)Moaz Khalifa](https://handbook.gitlab.com/handbook/company/team/#mkhalifa3) | [Backend Engineer, Package:Package Registry](https://handbook.gitlab.com/job-families/engineering/development/backend/intermediate/)  
[![Rad Batnag](https://about.gitlab.com/images/team/radbatnag-crop.jpg)Rad Batnag](https://handbook.gitlab.com/handbook/company/team/#radbatnag) | [Senior Backend Engineer, Package:Package Registry](https://handbook.gitlab.com/job-families/engineering/development/backend/senior/)  
### Stable Counterparts[](https://handbook.gitlab.com/handbook/engineering/devops/package/#stable-counterparts)
Name | Role  
---|---  
[![Senior Backend Engineer](https://about.gitlab.com/images/gitlab-logo-extra-whitespace.png)Senior Backend Engineer](https://handbook.gitlab.com/handbook/company/team/#adiepo) | [Backend Engineer, Package:Container Registry](https://handbook.gitlab.com/job-families/engineering/development/backend/intermediate/)  
[![Fi McCawley](https://about.gitlab.com/images/team/fionamccawley-crop.jpg)Fi McCawley](https://handbook.gitlab.com/handbook/company/team/#fmccawley) | [Fullstack Engineer, Package:Package Registry](https://handbook.gitlab.com/job-families/engineering/development/backend/senior/)  
[![Hayley Swimelar](https://about.gitlab.com/images/team/hayleyswimelar-crop.jpg)Hayley Swimelar](https://handbook.gitlab.com/handbook/company/team/#hswimelar) | [Senior Backend Engineer, Package:Container Registry](https://handbook.gitlab.com/job-families/engineering/development/backend/senior/)  
[![Senior Backend Engineer](https://about.gitlab.com/images/team/pawelrozlach-crop.jpg)Senior Backend Engineer](https://handbook.gitlab.com/handbook/company/team/#vespian_gl) | [Senior Backend Engineer, Package:Container Registry](https://handbook.gitlab.com/job-families/engineering/development/backend/senior/)  
[![Senior Backend Engineer](https://about.gitlab.com/images/team/sahmed-crop.jpg)Senior Backend Engineer](https://handbook.gitlab.com/handbook/company/team/#suleimiahmed) | [Backend Engineer, Package:Container Registry](https://handbook.gitlab.com/job-families/engineering/development/backend/)  
[![Tim Rizzi](https://about.gitlab.com/images/team/timrizzi-crop.jpg)Tim Rizzi](https://handbook.gitlab.com/handbook/company/team/#trizzi) | [Principal Product Manager, Package](https://handbook.gitlab.com/job-families/product/product-manager/)  
### Package Format DRIs[](https://handbook.gitlab.com/handbook/engineering/devops/package/#package-format-dris)
Format | DRI  
---|---  
npm | @dmeshcharakou  
Maven | @10io  
PyPI | @radbatnag  
NuGet | @mkhalifa3  
Terraform | @radbatnag  
Generic | @dmeshcharakou  
## How We Work[](https://handbook.gitlab.com/handbook/engineering/devops/package/#how-we-work)
### Milestone Planning Process[](https://handbook.gitlab.com/handbook/engineering/devops/package/#milestone-planning-process)
Our milestone planning aligns closely with our product roadmap and engineering commitments. The process balances delivery of strategic initiatives with operational needs like security issues, customer bugs, and interlock commitments. Planning is led by the Engineering Manager with collaborative input from the Product Manager and Designer.
#### Planning Workflow[](https://handbook.gitlab.com/handbook/engineering/devops/package/#planning-workflow)
  1. **Engineering Manager opens the planning issue**
     * Reference the [Package Stage Milestone Planning epic](https://gitlab.com/groups/gitlab-org/-/epics/3591)
     * Create a new planning issue for the milestone
     * Assign to Engineering Managers, Product Manager, and Designer
     * Define initial goals based on roadmap and team capacity
  2. **Engineering Manager adds sustaining work**
     * Review and prioritize security vulnerabilities with upcoming due dates
     * Select approximately 8 bugs from the backlog to address in the milestone
     * Identify interlock commitments with upcoming due dates
     * Ensure bug priorities align with team capacity
     * Check [triage reports](https://gitlab.com/gitlab-org/quality/triage-reports/-/issues?sort=created_date&state=opened&label_name%5B%5D=devops::package&label_name%5B%5D=triage%20report) for current priorities
  3. **Product Manager and Designer contribute priorities**
     * Product Manager reviews goals for alignment with product direction
     * Product Manager adds feature issues aligned with product strategy
     * Designer adds UX improvement and design issues
     * Both provide feedback on proposed goals and capacity
  4. **Engineering Manager finalizes capacity planning**
     * Review issues in the current milestone for proper priority labels
     * Ensure all issues are labeled with either `Deliverable`, `Stretch`, `Package:P1`, or `Package:P2`
     * Use the [issues filter](https://gitlab.com/groups/gitlab-org/-/issues/?sort=created_date&state=opened&label_name%5B%5D=devops::package&not%5Blabel_name%5D%5B%5D=Deliverable&not%5Blabel_name%5D%5B%5D=Stretch&not%5Blabel_name%5D%5B%5D=Package:P2&not%5Blabel_name%5D%5B%5D=Package:P1) to identify gaps
     * Confirm there is enough work for Go, Rails, and frontend engineers
     * Verify capacity is not exceeded using the [functional breakdown board](https://gitlab.com/groups/gitlab-org/-/boards/1548554?label_name%5B%5D=group%3A%3Apackage%20registry)
  5. **Review next milestone and carryover**
     * Check what’s already scheduled for the next milestone
     * Use the [workflow board](https://gitlab.com/groups/gitlab-org/-/boards/1284221?label_name%5B%5D=devops::package) to track issue status
     * Identify what was completed and what carries over
     * Update carryover issues with the new milestone
  6. **Coordinate with project DRIs**
     * Message project owners to add feature issues for the milestone
     * Ensure all planned work is properly documented and linked


#### Issue Prioritization[](https://handbook.gitlab.com/handbook/engineering/devops/package/#issue-prioritization)
Issues are prioritized as:
  * `Package:P1`: Committed work for the milestone
  * `Package:P2` + `Stretch`: Stretch goals if capacity allows
  * `Deliverable`: Refined P1 issues ready for development


Non-roadmap items that are planned include:
  * Security vulnerabilities (to meet SLAs)
  * High-priority customer bugs
  * Interlock commitments (Geo, Protocells, etc.)
  * Minor reliability and performance fixes


#### Planning Checklist[](https://handbook.gitlab.com/handbook/engineering/devops/package/#planning-checklist)
Use this checklist to ensure comprehensive milestone planning:
  * Security vulnerabilities reviewed and prioritized
  * High-priority bugs identified and assigned
  * Interlock commitments documented
  * All P1 issues are weighted and refined
  * Carryover work from previous milestone updated
  * Next milestone preview completed
  * Project DRIs notified of planned work
  * Instrumentation requirements defined for new features
  * Capacity confirmed for Go, Rails, and frontend engineers


#### Key Planning Resources[](https://handbook.gitlab.com/handbook/engineering/devops/package/#key-planning-resources)
  * [Functional breakdown board](https://gitlab.com/groups/gitlab-org/-/boards/1548554?label_name%5B%5D=group%3A%3Apackage%20registry) - View issues by function across milestones
  * [Milestone board](https://gitlab.com/groups/gitlab-org/-/boards/1196366?label_name%5B%5D=group%3A%3Apackage%20registry) - See issues broken down by function
  * [Workflow board](https://gitlab.com/groups/gitlab-org/-/boards/1284221?label_name%5B%5D=devops::package) - Track issue status through the milestone
  * [Triage reports](https://gitlab.com/gitlab-org/quality/triage-reports/-/issues?sort=created_date&state=opened&label_name%5B%5D=devops::package&label_name%5B%5D=triage%20report) - Current bug priorities


### Style Guidelines and Architectural Standards[](https://handbook.gitlab.com/handbook/engineering/devops/package/#style-guidelines-and-architectural-standards)
To ensure efficient code reviews and maintainer approvals, all contributions must follow our established style guidelines and architectural standards.
#### Frontend Development[](https://handbook.gitlab.com/handbook/engineering/devops/package/#frontend-development)
  * Follow [GitLab frontend guidelines](https://docs.gitlab.com/ee/development/fe_guide/)
  * Adhere to [Vue.js best practices](https://docs.gitlab.com/ee/development/fe_guide/vue.html)
  * Use [Pajamas Design System](https://design.gitlab.com/) for consistency
  * Follow [accessibility standards](https://docs.gitlab.com/ee/development/fe_guide/accessibility/)
  * Review [multi-version compatibility guidelines](https://docs.gitlab.com/ee/development/multi_version_compatibility/)


#### Backend Development[](https://handbook.gitlab.com/handbook/engineering/devops/package/#backend-development)
  * Follow [GitLab development guidelines](https://docs.gitlab.com/ee/development/)
  * Adhere to [Ruby style guide](https://docs.gitlab.com/ee/development/backend/ruby_style_guide.html)
  * Use [database best practices](https://docs.gitlab.com/ee/development/database/)
  * Follow [GraphQL API guidelines](https://docs.gitlab.com/development/api_graphql_styleguide/)
  * Follow [API design guidelines](https://docs.gitlab.com/ee/development/api_styleguide.html)
  * Review [multi-version compatibility guidelines](https://docs.gitlab.com/ee/development/multi_version_compatibility/)


#### Container Registry (Go)[](https://handbook.gitlab.com/handbook/engineering/devops/package/#container-registry-go)
  * Follow [Go code style guidelines](https://docs.gitlab.com/ee/development/go_guide/)
  * Maintain compatibility with [OCI standards](https://github.com/opencontainers/specs)
  * Review [multi-version compatibility guidelines](https://docs.gitlab.com/ee/development/multi_version_compatibility/)


#### Security and Compliance[](https://handbook.gitlab.com/handbook/engineering/devops/package/#security-and-compliance)
  * Review [breaking changes and deprecation guidelines](https://docs.gitlab.com/ee/development/deprecation_guidelines/) before implementing breaking changes
  * Follow [security best practices](https://docs.gitlab.com/ee/development/secure_coding_guidelines.html)
  * Ensure [AppSec review](https://handbook.gitlab.com/handbook/security/product-security/security-platforms-architecture/application-security/appsec-reviews/) for security-sensitive changes


### Developer Workflow and Contribution Process[](https://handbook.gitlab.com/handbook/engineering/devops/package/#developer-workflow-and-contribution-process)
#### Issue Refinement[](https://handbook.gitlab.com/handbook/engineering/devops/package/#issue-refinement)
Before starting development, ensure issues are properly refined:
  * **Weight assignment** : All issues must have a weight estimate (1-5 scale)
  * **Implementation plan** : Include technical approach and any dependencies
  * **Acceptance criteria** : Clearly define what “done” means
  * **Label requirements** : Apply appropriate labels for type, category, workflow and Package:P1 or Package:P2.
  * **Milestone assignment** : Ensure the issue is assigned to the correct milestone


Use the [issues needing refinement filter](https://gitlab.com/groups/gitlab-org/-/issues/?label_name%5B%5D=devops::package&label_name%5B%5D=workflow::refinement) to identify work that needs attention.
Instrumentation is a key requirement for all features to measure impact and effectiveness. This helps us validate adoption and make data-driven decisions.
#### Async Updates[](https://handbook.gitlab.com/handbook/engineering/devops/package/#async-updates)
The purpose of async updates is to communicate progress and allow others to prepare for upcoming work. In an all-remote culture, we keep updates asynchronous and put them directly in issues.
Add a comment in your issue with the title `Async Update` once per week, or when something notable happens. It’s preferable to update the issue rather than related merge requests.
The async update comment should include:
  * Percentage complete (how much work is done to put all required MRs in review)
  * Confidence level in your estimate
  * Notes on what was done and whether review has started
  * Frontend or backend context if multiple people are working on the issue
  * Any blockers or risks


#### Labeling Requirements[](https://handbook.gitlab.com/handbook/engineering/devops/package/#labeling-requirements)
Ensure issues have the following labels before starting work:
  * **Type** : `type::feature`, `type::bug`, or `type::maintenance`
  * **Category** : `Category:Container Registry`, `Category:Package Registry`, or `Category:Virtual Registry`
  * **Priority** : `Package:P1`, `Package:P2`, or appropriate priority label
  * **Workflow** : `workflow::ready for development` before starting
  * **Milestone** : Assigned to the current or planned milestone


#### Collaboration with Design and Product[](https://handbook.gitlab.com/handbook/engineering/devops/package/#collaboration-with-design-and-product)
  * **Design collaboration** : Work with the Designer early in the refinement phase
  * **UX reviews** : Request UX feedback before implementation when applicable
  * **Product alignment** : Confirm feature scope with Product Manager before starting
  * **Design handoff** : Ensure design specs are complete before development begins


#### AppSec Review Process[](https://handbook.gitlab.com/handbook/engineering/devops/package/#appsec-review-process)
For security-sensitive changes:
  1. Identify if your change affects authentication, authorization, data handling, or external integrations
  2. Request an AppSec review early in the development process
  3. Include security considerations in your implementation plan
  4. Reference [security best practices](https://docs.gitlab.com/ee/development/secure_coding_guidelines.html) in your MR
  5. Address all AppSec feedback before merge


#### Code Review and Merge Process[](https://handbook.gitlab.com/handbook/engineering/devops/package/#code-review-and-merge-process)
  * Ensure all style guidelines are followed before requesting review
  * Include clear MR description with context and testing approach
  * Address all review feedback promptly
  * Obtain approval from appropriate maintainers
  * Ensure CI/CD pipeline passes before merging


### Request for Help (RFH) Process[](https://handbook.gitlab.com/handbook/engineering/devops/package/#request-for-help-rfh-process)
The Package team participates in GitLab’s Request for Help (RFH) process to support customer issues escalated by the Support team. RFH issues are tracked in the [gitlab-com/request-for-help](https://gitlab.com/gitlab-com/request-for-help) repository.
#### How RFH Works[](https://handbook.gitlab.com/handbook/engineering/devops/package/#how-rfh-works)
When Support escalates a customer issue to the Package team, they create an RFH issue using one of our templates:
  * [Package Registry template](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-PackageRegistry)
  * [Container Registry template](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-ContainerRegistry)


The entire team is notified through a group mention (`@gitlab-org/ci-cd/package-stage/container-registry-group` or `@gitlab-org/ci-cd/package-stage/package-registry-group`), and the issue is labeled with the appropriate help group label.
#### Response Time SLOs[](https://handbook.gitlab.com/handbook/engineering/devops/package/#response-time-slos)
The Package team commits to following First Response Time (FRT) SLOs based on [timelines](https://gitlab.com/gitlab-com/request-for-help#responsiveness-guidelines) in the request-for-help handbook page.
These SLOs represent the time to provide an initial response, not necessarily a complete resolution.
#### Integrating RFH into Team Workflow[](https://handbook.gitlab.com/handbook/engineering/devops/package/#integrating-rfh-into-team-workflow)
**Monitoring and Triage**
  * Check the RFH repository regularly for new issues assigned to the Package team
  * Respond to group mentions in Slack when new RFH issues are created
  * Triage issues to determine if they require immediate attention or can be scheduled


**Prioritization**
  * RFH issues are typically prioritized above planned work when they meet SLA requirements
  * Severity 1 and 2 issues may require immediate context switching
  * Severity 3 and 4 issues should be addressed within the SLO window but can be scheduled into the current or next milestone
  * If an RFH cannot be addressed within the SLO, escalate to the Engineering Manager


**Handling RFH Issues**
  1. **Initial Response** : Acknowledge the issue and provide initial investigation or workaround if available
  2. **Investigation** : Determine if the issue is a bug, missing documentation, or expected behavior
  3. **Resolution Path** : Choose one of the following: 
     * Provide a workaround
     * Create a bug report in the main GitLab project if needed
     * Provide documentation or configuration guidance
     * Escalate if the issue requires significant engineering effort
  4. **Communication** : Keep the Support team updated with progress and next steps
  5. **Closure** : When resolved, apply the appropriate closure label and complete any retrospective feedback


#### Closure Labels[](https://handbook.gitlab.com/handbook/engineering/devops/package/#closure-labels)
When closing an RFH issue, apply one of these labels to document the resolution:
  * `Closed::Workaround` - Issue resolved with a workaround
  * `Closed::Bug Fixed` - A bug was identified and fixed
  * `Closed::Other Request` - Related feature request or bug report created in public tracker
  * `Closed::Moved to Public Issue` - No workaround found, moved to public issue
  * `Closed::No Solution` - Could not be acted on due to missing details
  * `Closed::Insufficient Information` - Operational or non-product issue
  * `Closed::Documentation` - Resolved by following existing documentation


#### Retrospectives[](https://handbook.gitlab.com/handbook/engineering/devops/package/#retrospectives)
When an RFH issue is marked with `retrospective::started`, provide feedback addressing:
  * What could have prevented this RFH? (missing documentation, unclear processes, tooling gaps)
  * What materials or resources would have helped the customer solve this independently?
  * Suggestions for improving self-service offerings


Update the label to `retrospective::completed` or `retrospective::not needed` when done.
#### Key Resources[](https://handbook.gitlab.com/handbook/engineering/devops/package/#key-resources)
  * [RFH Repository](https://gitlab.com/gitlab-com/request-for-help)
  * [Support Handbook - How to Get Help](https://handbook.gitlab.com/handbook/support/workflows/how-to-get-help/)
  * [Package Registry RFH Template](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-PackageRegistry)
  * [Container Registry RFH Template](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-ContainerRegistry)


### Issue Management[](https://handbook.gitlab.com/handbook/engineering/devops/package/#issue-management)
#### Backlog Labeling Process[](https://handbook.gitlab.com/handbook/engineering/devops/package/#backlog-labeling-process)
When triaging issues, apply appropriate backlog labels based on commitment level:
  * **`backlog::prospective`**: Issues we plan to work on within the next 24 months
  * **`backlog::no-commitment`**: Issues with user interest but unlikely to be prioritized in the next 24 months


#### Issue Organization by Type[](https://handbook.gitlab.com/handbook/engineering/devops/package/#issue-organization-by-type)
##### Feature Issues (`type::feature`)[](https://handbook.gitlab.com/handbook/engineering/devops/package/#feature-issues-typefeature)
  * Assign to appropriate epics
  * Apply priority labels (`priority::1` through `priority::4`) to all epics
  * Close issues for unsupported formats (Go repository, RPM)
  * Move low-demand format requests to `backlog::no-commitment` (Rust, Dart, Swift, etc.)


##### Maintenance Issues (`type::maintenance`)[](https://handbook.gitlab.com/handbook/engineering/devops/package/#maintenance-issues-typemaintenance)
  * Assign to relevant maintenance epics: 
    * **Package Registry Maintenance Epic** (&19029)
    * **Container Registry Maintenance Epic** (&19037)
  * Sub-epic categories: 
    * Security and compliance
    * Performance optimization
    * Infrastructure & operations
    * Data management & cleanup
    * Code improvements
    * Testing & QA
    * Documentation


##### Bug Issues (`type::bug`)[](https://handbook.gitlab.com/handbook/engineering/devops/package/#bug-issues-typebug)
  * Apply priority labels to ensure proper triage
  * Label with `backlog::prospective` for bugs planned for resolution
  * Close stale bugs that no longer apply to current roadmap


#### Epic Management[](https://handbook.gitlab.com/handbook/engineering/devops/package/#epic-management)
  * Consolidate related epics to reduce fragmentation
  * Remove duplicate epics
  * Ensure all prospective epics have scoped priority labels
  * Regularly review epic scope and merge overlapping initiatives


#### Async Issue Updates[](https://handbook.gitlab.com/handbook/engineering/devops/package/#async-issue-updates)
The purpose of async updates is to communicate progress and allow others to prepare for upcoming work as necessary. In an all-remote culture, we keep the updates asynchronous and put them directly in the issues.
The async update communicates the progress and confidence using an issue comment and the milestone health status. Add a comment in your issue with the title `Async Update` once per week, or when something notable happens with regard to the issue. It’s preferable to update the issue rather than the related merge requests.
The async update comment should include:
  * what percentage complete the work is, in other words, how much work is done to put all the required MRs in review
  * the confidence of the person that their estimate is correct
  * notes on what was done and/or if review has started
  * it could be good to include whether this is a front end or back end update if there are multiple people working on it


#### Issue Weighting Guidelines[](https://handbook.gitlab.com/handbook/engineering/devops/package/#issue-weighting-guidelines)
Weight | Description | Confidence Level  
---|---|---  
1: Trivial | Well understood, no investigation needed, exact solution known | ≥90%  
2: Small | Well understood, minimal investigation needed, few surprises expected | ≥75%  
3: Medium | Well understood but requires investigation, some surprises expected | ≥60%  
Larger | Should be broken down into smaller issues | ≥50%  
An issue with weight 1 should take no more than 2 days to complete.
### Current Projects[](https://handbook.gitlab.com/handbook/engineering/devops/package/#current-projects)
#### Container Registry[](https://handbook.gitlab.com/handbook/engineering/devops/package/#container-registry)
  * [Metadata database GA](https://gitlab.com/groups/gitlab-org/-/epics/5521) (DRI: @hswimelar)
  * [Database load balancing](https://gitlab.com/groups/gitlab-org/-/epics/8591) (DRI: @jdrpereira)
  * [Background migration support](https://gitlab.com/groups/gitlab-org/-/epics/13609) (DRI: @suleimiahmed)
  * [Beta: Docker Virtual Registry](https://gitlab.com/groups/gitlab-org/-/epics/6061) (DRI: @adie.po)


#### Package Registry[](https://handbook.gitlab.com/handbook/engineering/devops/package/#package-registry)
  * [Virtual Registry support (Maven, npm, PyPI, NuGet)](https://gitlab.com/groups/gitlab-org/-/epics/15088) (DRI: @10io)
  * [Dependency Firewall](https://gitlab.com/groups/gitlab-org/-/epics/5133) (DRI: @dmeshcharakou)
  * [Package format improvements](https://gitlab.com/groups/gitlab-org/-/epics/12294) (DRI: @radbatnag)
  * [Test stability enhancements](https://gitlab.com/groups/gitlab-org/-/epics/15148) (DRI: @radbatnag)


## Technical Guidelines[](https://handbook.gitlab.com/handbook/engineering/devops/package/#technical-guidelines)
### Breaking Changes Process[](https://handbook.gitlab.com/handbook/engineering/devops/package/#breaking-changes-process)
Review and follow the [breaking changes, deprecations and removals guidance](https://docs.gitlab.com/ee/development/deprecation_guidelines/) as leadership approval is required before announcing or proceeding with any breaking change.
### Releasing New Package Formats[](https://handbook.gitlab.com/handbook/engineering/devops/package/#releasing-new-package-formats)
We follow a structured process for releasing new package formats:
  1. **Experiment Phase**
     * Feature flag enabled on staging
     * Comprehensive testing: 
       * Small and large package operations
       * Performance with hundreds of packages
       * All supported authentication methods
       * Custom GitLab-specific features
     * Document any issues in feature flag rollout issue
  2. **Beta Phase**
     * Limited GitLab.com rollout
     * Dogfooding with internal teams
     * Selected customer testing
     * Bug triage and resolution
  3. **Generally Available**
     * Full documentation update
     * Feature flag removal
     * Self-managed release
     * Release communications


Review the [guidelines on multi-version compatibility](https://docs.gitlab.com/development/multi_version_compatibility/) to ensure appropriate handling of changes relating to the backend and frontend.
### Alert and CI Flake Management[](https://handbook.gitlab.com/handbook/engineering/devops/package/#alert-and-ci-flake-management)
The team monitors the Slack channel [#g_container-registry_alerts](https://gitlab.enterprise.slack.com/archives/C046REGL9QD) for service alerts and CI notifications. Process for handling alerts:
  1. Everyone is responsible for monitoring alerts during their working hours
  2. When a new alert appears: 
     * Add 👀 emoji to signal you’re investigating
     * Review alert details (runbook, dashboard, pipeline, Sentry issue)
     * Use available resources to evaluate the problem
     * Determine if safe to ignore based on: 
       * Existing issue coverage
       * Auto-resolution
       * Logs showing resolution
     * If not safe to ignore: 
       * Review #production and #incidents-dotcom channels
       * Consider reporting an incident
       * Share details in #g_container-registry
     * Add a comment thread to document your review
     * Add ✅ emoji when resolved


#### Alert Occurrence Template[](https://handbook.gitlab.com/handbook/engineering/devops/package/#alert-occurrence-template)
```

## Alert Occurrence Update
- **Occurrence Count**: X (previously Y)
- **Date/Time**: [Insert timestamp]
- **Last occurrences**: [Insert slack link]

```

#### Key Resources[](https://handbook.gitlab.com/handbook/engineering/devops/package/#key-resources-1)
  * [Logs - Non-production](https://nonprod-log.gitlab.net/goto/f3fbccdb9dea6805ff5bbf1e0144a04e)
  * [Logs - Production](https://log.gprd.gitlab.net/goto/7dc6f73d5dd4cc4bebcd4af3b767cae4)
  * [Dashboard - Overview](https://dashboards.gitlab.net/d/registry-main/registry-overview?orgId=1)
  * [Profiler](https://console.cloud.google.com/profiler/gitlab-registry/cpu?project=gitlab-production)


## Product Context[](https://handbook.gitlab.com/handbook/engineering/devops/package/#product-context)
### Container Registry History[](https://handbook.gitlab.com/handbook/engineering/devops/package/#container-registry-history)
Originally launched in milestone 8.8, the Container Registry integrated Docker Distribution registry into GitLab. A key challenge was storage management - deleted images weren’t actually removed from storage without downtime-requiring garbage collection.
To address this and enable future features, we:
  1. Forked Docker Distribution
  2. Implemented online garbage collection
  3. Added a metadata database
  4. Created cleanup policies


This work enables future capabilities like:
  * More robust API and UI
  * Enterprise features (image signing, protection)
  * Improved stability and reliability


The registry adheres to OCI standards for Image and Distribution specifications while maintaining backward compatibility with Docker specifications.
## Measuring Results[](https://handbook.gitlab.com/handbook/engineering/devops/package/#measuring-results)
### Key Performance Indicators[](https://handbook.gitlab.com/handbook/engineering/devops/package/#key-performance-indicators)
  * Lighthouse Metric: (Count of Packages Published + Count of Containers Published) / Billable Users
  * Monthly Active Users (GMAU)
  * Error Budget compliance
  * Say-Do ratio for delivery commitments
  * Operating costs: 
    * Storage costs
    * Data transfer costs


### Dashboards[](https://handbook.gitlab.com/handbook/engineering/devops/package/#dashboards)
  * [Container Registry](https://log.gprd.gitlab.net/goto/e7b62a23a5a9cdc88aa1de3cdb392758)
  * [Package Registry Metrics](https://dashboards.gitlab.net/)
  * [Error Budgets](https://dashboards.gitlab.net/d/stage-groups-detail-package_registry/)


## Additional Resources[](https://handbook.gitlab.com/handbook/engineering/devops/package/#additional-resources)
  * [Package Quality Guidelines](https://handbook.gitlab.com/handbook/engineering/devops/package/quality/)
  * [Package Jobs To Be Done](https://handbook.gitlab.com/handbook/engineering/devops/package/jtbd/)
  * [Container Registry Documentation](https://docs.gitlab.com/ee/user/packages/container_registry/)
  * [Package Registry Documentation](https://docs.gitlab.com/ee/user/packages/package_registry/)
  * [Team YouTube Channel](https://www.youtube.com/playlist?list=PL05JrBw4t0KoPiSySNHTfvxC20i0LppMf) (includes demos, team meetings, customer summaries, and user interviews)


* * *
#####  [Package Group - GitLab Quality Assurance End-to-End Testing for the Package group](https://handbook.gitlab.com/handbook/engineering/devops/package/quality/)
Testing Strategy Local Development Testing Unit Tests Container Registry (Go): make test Package …
#####  [Package Stage - The most important use cases for our customers](https://handbook.gitlab.com/handbook/engineering/devops/package/jtbd/)
Overview The goal of this page is to create, share and iterate on the Jobs to be Done (JTBD) and …
Last modified February 7, 2026: [Changes appsec links and pages location to be within SPA (`fa505536`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/fa505536)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/devops/package/_index.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/devops/package/_index.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)