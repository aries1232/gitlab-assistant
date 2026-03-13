# Plan:Knowledge Engineering Team
## Plan:Knowledge team[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#planknowledge-team)
The Plan:Knowledge team develops [Knowledge Management categories](https://handbook.gitlab.com/handbook/product/categories/#knowledge-group):
  * Wiki
  * GitLab Pages
  * Text Editors
  * Markdown


Learn more on our [direction page](https://about.gitlab.com/direction/plan/knowledge/).
### Team members[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#team-members)
Name | Role  
---|---  
### Stable counterparts[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#stable-counterparts)
Name | Role  
---|---  
[![Alex Fracazo](https://about.gitlab.com/images/team/alexfracazo-crop.jpg)Alex Fracazo](https://handbook.gitlab.com/handbook/company/team/#afracazo) |  [Senior Product Designer](https://handbook.gitlab.com/job-families/product/product-designer/#senior-product-designer), Plan:Knowledge  
[![Costel Maxim](https://about.gitlab.com/images/team/CMaxim-crop.jpg)Costel Maxim](https://handbook.gitlab.com/handbook/company/team/#cmaxim) |  [Senior Security Engineer, Application Security](https://handbook.gitlab.com/job-families/security/application-security/#senior-application-security-engineer), Plan (Project Management, Product Planning, Certify), Create:Source Code, Growth, Fulfillment:Purchase, Fulfillment:Provision, Fulfillment:Utilization, Systems:Gitaly  
[![Heinrich Lee Yu](https://about.gitlab.com/images/team/heinrichleeyu-crop.jpg)Heinrich Lee Yu](https://handbook.gitlab.com/handbook/company/team/#engwan) |  [Principal Engineer](https://handbook.gitlab.com/job-families/engineering/development/management/principal-engineer/), Plan  
[![John Hope](https://about.gitlab.com/images/team/johnhope-crop.jpg)John Hope](https://handbook.gitlab.com/handbook/company/team/#johnhope) |  [Director of Engineering](https://handbook.gitlab.com/job-families/engineering/development/management/director/), Plan  
[![Naman Jagdish Gala](https://about.gitlab.com/images/team/namanjagdishgala-crop.jpg)Naman Jagdish Gala](https://handbook.gitlab.com/handbook/company/team/#ngala) |  [Senior Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/), Plan:Knowledge  
[![Natalia Tepluhina](https://about.gitlab.com/images/team/nataliatepluhina-crop.jpg)Natalia Tepluhina](https://handbook.gitlab.com/handbook/company/team/#ntepluhina) |  [Principal Engineer](https://handbook.gitlab.com/job-families/engineering/development/management/principal-engineer/), Plan  
[![Piotr Skorupa](https://about.gitlab.com/images/team/piotrskorupa-crop.jpg)Piotr Skorupa](https://handbook.gitlab.com/handbook/company/team/#pskorupa) |  [Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/), Plan:Knowledge  
[![Vanessa Otto](https://about.gitlab.com/images/team/vanessaotto-crop.jpg)Vanessa Otto](https://handbook.gitlab.com/handbook/company/team/#vanessaotto) |  [Staff Frontend Engineer](https://handbook.gitlab.com/job-families/engineering/development/frontend/staff/), Plan:Knowledge  
### Hiring chart[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#hiring-chart)
Check out our [jobs page](https://about.gitlab.com/jobs/) for current openings.
## How we work[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#how-we-work)
### Picking something to work on[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#picking-something-to-work-on)
The [build board](https://gitlab.com/groups/gitlab-org/-/boards/5454834) shows upcoming release work. The ~“workflow::ready for development” column is ordered by priority.
Engineering Manager adds the following labels at the start of the milestone:
Label | Meaning  
---|---  
`~Deliverable` | We have committed to customers that we will deliver this item in the current milestone.  
`~Stretch` | We have not committed to deliver the item but will attempt to make progress on it  
It’s OK not to take the top item if you are not confident you can solve it, but please post in `#g_knowledge`.
### Capacity[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#capacity)
#### Estimating effort[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#estimating-effort)
When estimating the effort involved in upcoming work, we use the same approach and numerical scale as other groups in the Plan stage.
When weighting an issue for a milestone, we use a lightweight, relative estimation approach, recognizing that [tasks often take longer than you think](https://erikbern.com/2019/04/15/why-software-projects-take-longer-than-you-think-a-statistical-model.html). These weights are primarily used for capacity planning, ensuring that the total estimated effort aligns with each group’s capacity for a milestone.
##### Key Principles[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#key-principles)
  * **Relative Estimation:** We focus on the relative complexity and effort required for each issue rather than precise time estimates.
  * **Aggregate Focus:** The sum of all issue weights should be reasonable for the milestone, even if individual issues vary in actual time taken.
  * **Flexibility:** It’s acceptable for an issue to take more or less time than its weight suggests. Variations are expected due to differences in individual expertise and familiarity with the work.


##### Weight Definitions[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#weight-definitions)
Weight | Meaning  
---|---  
1 | Trivial, does not need any testing  
2 | Small, needs some testing but nothing involved  
3 | Medium, will take some time and collaboration  
4 | Substantial, will take significant time and collaboration to finish  
5 | Large, will take a major portion of the milestone to finish  
**Initial Planning:** During milestone planning, tasks can be estimated up to a weight of **5** if necessary. However, as the milestone approaches and the team moves closer to starting implementation, any task with a weight larger than **3** should be decomposed into smaller, more manageable issues or tasks with lower weights.
**Why This Approach:** Allowing larger weights early on provides flexibility in high-level planning. Breaking down tasks closer to implementation ensures better clarity, reduces risk, and facilitates more accurate tracking and execution.
We assess the available capacity for a milestone by reviewing recent milestones and upcoming team availability. This ensures that our milestone planning remains realistic and achievable based on the collective effort estimated through these weights.
Typically, 3-month rolling average is a good indicator of the team’s capacity. Knowledge is a new team and determining capacity will be difficult at the beginning without clear historical data.
The PM and EM will work to fit ~Deliverable issues into no more than 75% of the team’s capacity and allocate the rest to ~Stretch issues.
#### Refinement[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#refinement)
Engineering manager reviews `~"workflow::refinement"` issues on every team meeting. Issues with the [highest priority](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#priority-labels) are assigned to individual engineers, who are responsible for moving issue to `~workflow::ready for development`.
Engineers can put the following template into the issue description:
```

### Implementation plan

<!--
Ready for development means replying yes to the following questions:

- Is this issue sufficiently small enough? If not, break it into smaller issues
- Is it assigned to the correct domain (e.g. frontend, backend)? If not, break it into two issues for the respective domains
– Is the issue clear and easy to understand? If not, try asking further clarification questions and update the description once they are received

If more than 2 MRs are needed, consider adding a table like the following to the description (e.g. under `Implementation plan`).
-->

| Description | MR |
|-|-|
| MR 1 | |
| MR 2 | |
| Documentation | |

**Reasoning:**

<!--
Add some initial thoughts on how you might break down this issue. A bulleted list is fine.

This will likely require the code changes similar to the following:

- replace the hex driver with a sonic screwdriver
- rewrite backups to magnetic tape
- send up semaphore flags to warn others

Links to previous examples. Discussions on prior art. Notice examples of the simplicity/complexity in the proposed designs.
-->

/label ~"workflow::ready for development"

/label ~"frontend-weight::X"

/label ~"backend-weight::X"

/weight X

```

#### Weighing bugs[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#weighing-bugs)
Estimating bugs is inherently difficult. The majority of the effort in fixing bugs is finding the cause, and then a bug can be accurately estimated. Additionally, velocity is used to measure the amount of new product output, and bug fixes are typically fixes on a feature that has been tracked and had a weight attached to it previously.
Because of this, we do not weigh bugs during ~“workflow::planning breakdown”. If an engineer picks up a bug and determines that there will be a significant level of effort in fixing it (for example, a large migration is needed), we then will want to prioritize it against feature deliverables. Ping the product manager with this information so they can determine when the work should be scheduled.
### Refinement[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#refinement-1)
#### Board-Walk (weekly)[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#board-walk-weekly)
Team-members meet to walk the [Build Board](https://gitlab.com/groups/gitlab-org/-/boards/5454834) once a week. 25 minutes are allocated for this sync call but it may be completed much more quickly than that. The EM is DRI and attendance is optional except for PM. It is recorded and shared in the [#g_knowledge Slack channel](https://app.slack.com/client/T02592416/C04R571QF5E). The recording will be made public only if no security or other confidential issues are discussed. The [agenda](https://docs.google.com/document/d/1SZrFiipmH5GX5CYL-nOuc8NNqSs-AXCvHOzajwy06vk/edit?usp=sharing) is available internally and all team-members are encouraged to contribute updates and questions.
The purpose of this meeting is to:
  * Update on the status of work in progress
  * Identify blockers and risk
  * Reprioritize
  * Ask for help


DRIs should keep issues up to date with [workflow labels](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#use-of-labels) and [health status](https://handbook.gitlab.com/handbook/engineering/devops/plan/#keeping-health-status-accurate) on an ongoing basis rather than waiting for this meeting.
#### Planning Meeting (monthly)[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#planning-meeting-monthly)
A planning meeting is held once per month, prior to the start of the milestone. The Product Manager is the DRI for scheduling it.
Attendance is optional for engineers but participation is not. The meeting will have an agenda and will be recorded. It may involve any or all of the following:
  * Setting priorities and expectations.
  * Estimating tasks.
  * Breaking down and collaborating on scope.
  * Clarifying requirements.
  * Estimating capacity and carry-over.


As much as possible these tasks should be completed asynchronously, reducing the work required in the meeting. The purpose of the meeting is to start the upcoming milestone in the best possible shape for success.
#### Refinement sessions (ad-hoc)[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#refinement-sessions-ad-hoc)
Team-members are encouraged to propose refinement sync meetings for large issues and/or new features. The goal is to explore concerns and unknowns while sharing knowledge and gathering different perspectives on the problem.
A refinement meeting might have an agenda with topics like:
  * Product requirements
  * Technical challenges
  * Technical alternatives
  * How to iterate on the solution proposed


As an outcome, the meeting could produce a list of issues, with an estimated milestone, to iterate over.
#### Asynchronous-first[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#asynchronous-first)
Most planning is done asynchronously. Some tools and processes are observed to make this more efficient.
Since issues can only have one milestone attached, the `~"Next Up"` label is used to mark items for the upcoming milestone, regardless of whether they already have a milestone or not. PM and EM should remove this label from any issues prior to the start of planning, then add it to prospective issues and any expected to slip the current milestone during the planning process.
Using this label, it’s possible to easily analyze the upcoming milestone. The [Planning Board](https://gitlab.com/groups/gitlab-org/-/boards/7109724) mimics the Build Board but is scoped to this label instead of the current milestone. Use it to:
  * View the current workflow state of all proposed issues.
  * Plan capacity by totalling weight values for each list.
  * Understand blocking relationships that may be resolvable before the milestone starts.


When the new milestone starts, the milestone can be added all issues with the `~"Next Up"` label in a bulk action, and the label itself removed.
### Workflow[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#workflow)
#### Use of Labels[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#use-of-labels)
Proper labelling of issues helps with the classification, traceability and quantification of work the team can and is doing. Some labels are essential. The table below describes these and gives the reason why.
Label | Use | Handbook Guidance | DRI  
---|---|---|---  
~workflow::* | Communicates the current workflow state of an issue. Important for understanding progress & quantifying risk during the course of a milestone. | Updating Issues Throughout Development | Engineer  
~type::* | Communicates the type of work being done. Used to quantify and report the split of work to roles inside and outside GitLab. | [Work Type Classification](https://handbook.gitlab.com/handbook/product/groups/product-analysis/engineering/metrics/#work-type-classification) |   
~Deliverable/~Stretch | ~Deliverable communicates to customers and stakeholders that we intend to deliver an issue within the assigned milestone. ~Stretch indicates that it might be started during the milestone but is not expected to complete. | [Release Scoping Labels](https://docs.gitlab.com/ee/development/labels/#release-scoping-labels) | Engineering Manager  
#### Async update[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#async-update)
We aim to make the status of each epic and issue clear and easily accessible for our teammates, counterparts and users.
The primary source of truth for this information is the `~workflow::*` label and the health status.
But when the issue spends more than in a week in the `~"workflow::in dev"`, `~"workflow::in review"` or `~"workflow::verification"` DRI also leaves an async update on the it using the [“Knowledge - async update” comment template](https://gitlab.com/groups/gitlab-org/-/comment_templates/1000436).
To keep the track of what issues may need an async update, you can use the following GLQL query:
```

```glql
---
display: list
fields: title, labels("workflow::*"), healthStatus
---
group = "gitlab-org" and assignee = currentUser() and label in ("workflow::in dev", "workflow::in review", "workflow::verification") and opened = true
```

```

### Priority labels[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#priority-labels)
We use `~Knowledge::P1/P2/P3` labels to indicate issue priority within the `~workflow::*` steps and milestones.
  * Product Manager is the DRI for these labels, but everybody on the team can assign/adjust them.
  * Before the milestone starts, the PM and EM will review the priorities for all issues included in that milestone. It’s expected that: - 40% of issues have `~Knowledge::P1` - 30% of issues have `~Knowledge::P2` - 30% of issues have `~Knowledge::P3`, and those issues can’t be `~Deliverable`’s
  * We also use these labels outside of milestones to keep track of our highest priorities.
  * If anyone on the team wants an issue to be scheduled, they should add the appropriate priority label.
  * We don’t have a dedicated `P4` label, not having `~Knowledge::P*` label is equivalent to `~Knowledge::P4`.
  * When issues are moved to another `~workflow::*` stage, it’s likely that the priority will be changed.
  * `~Knowledge::P*` labels are completely different from `~priority::*` labels that are used only for bugs.


### Collaboration with other teams[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#collaboration-with-other-teams)
To avoid rework we reach out to other teams early when working on the following domains:
Team | Domain overlap  
---|---  
[Pipeline Authoring](https://handbook.gitlab.com/handbook/engineering/devops/verify/pipeline-authoring/) | GitLab Pages [.gitlab-ci.yml syntax](https://docs.gitlab.com/ee/ci/yaml/)  
### Application Performance[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#application-performance)
Additional dashboards are available in Grafana that show application performance of parts of the application for which the team is responsible.
  * [Stage-Group Dashboard](https://dashboards.gitlab.net/d/stage-groups-knowledge/stage-groups-knowledge-group-dashboard?orgId=1) (including 28-day Error Budget)
  * [Error Budget Detail](https://dashboards.gitlab.net/d/stage-groups-detail-knowledge/stage-groups-knowledge-group-error-budget-detail?orgId=1)


## Useful links[](https://handbook.gitlab.com/handbook/engineering/devops/plan/knowledge/#useful-links)
  * [Plan:Knowledge](https://gitlab.com/groups/gitlab-org/-/boards/1569369?scope=all&utf8=%E2%9C%93&state=opened&label_name\[\]=group%3A%3Aknowledge) - Apply a milestone filter to see work in the current release
  * [#s_plan](https://gitlab.slack.com/archives/s_plan) in Slack
  * [Recorded meetings](https://www.youtube.com/playlist?list=PL05JrBw4t0KouWOCpPdlVZmwr3QCqhQ94)
  * [Retrospectives](https://gitlab.com/gl-retrospectives/plan/issues?scope=all&utf8=%E2%9C%93&state=all&label_name\[\]=retrospective)


Last modified December 5, 2025: [Remove sub-departments by flattening stages against the department (`8ff941c7`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/8ff941c7)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/devops/plan/knowledge.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/devops/plan/knowledge.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)