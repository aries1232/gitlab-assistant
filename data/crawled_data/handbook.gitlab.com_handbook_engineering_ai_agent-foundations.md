# Agent Foundations Group
The Agent Foundations group is focused on developing GitLab Duo Workflow, an AI system to automate tasks and help increase productivity in your development workflow.
## Vision[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#vision)
The Agent Foundations group is focused on developing GitLab the foundations of Agents and Flows, an AI system to automate tasks and help increase productivity in your development workflow.
### Team Members[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#team-members)
**Engineering Manager & Engineers**
Name | Role  
---|---  
[![Sebastian Rehm](https://about.gitlab.com/images/team/bastirehm-crop.jpg)Sebastian Rehm](https://handbook.gitlab.com/handbook/company/team/#bastirehm) | [Manager, Fullstack Engineering, AI-Powered:Duo Workflow](https://handbook.gitlab.com/job-families/engineering/development/management/fullstack-manager/)  
[![Alper Akgun](https://about.gitlab.com/images/team/aakgun-crop.jpg)Alper Akgun](https://handbook.gitlab.com/handbook/company/team/#a_akgun) |  [Staff Fullstack Engineer](https://handbook.gitlab.com/job-families/engineering/development/fullstack/), AI-powered:Agent Foundations  
[![Andras Herczeg](https://about.gitlab.com/images/team/AndrasHerczeg-crop.jpg)Andras Herczeg](https://handbook.gitlab.com/handbook/company/team/#andrasherczeg) |  [Senior Machine Learning Engineer](https://handbook.gitlab.com/job-families/engineering/development/data-science/machine-learning/), AI-powered:AI Model Validation  
[![Andrew Fontaine](https://about.gitlab.com/images/team/andrewfontaine-crop.jpg)Andrew Fontaine](https://handbook.gitlab.com/handbook/company/team/#afontaine) | [Staff Frontend Engineer, AI-powered:Duo Workflow](https://handbook.gitlab.com/job-families/engineering/development/frontend/)  
[![Fred de Gier](https://about.gitlab.com/images/team/fdegier-crop.jpg)Fred de Gier](https://handbook.gitlab.com/handbook/company/team/#fdegier) | [Staff Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/staff/)  
[![Halil Coban](https://about.gitlab.com/images/team/halilcoban-crop.jpg)Halil Coban](https://handbook.gitlab.com/handbook/company/team/#halilcoban) | [Senior Backend Engineer, AI-powered:Duo Workflow](https://handbook.gitlab.com/job-families/engineering/development/backend/)  
[![Joey Khabie](https://about.gitlab.com/images/team/joeykhabie-crop.jpg)Joey Khabie](https://handbook.gitlab.com/handbook/company/team/#joey_khabie) | [Backend Engineer, AI-powered:Duo Workflow](https://handbook.gitlab.com/job-families/engineering/development/backend/)  
[![Senior Machine Learning Engineer](https://about.gitlab.com/images/gitlab-logo-extra-whitespace.png)Senior Machine Learning Engineer](https://handbook.gitlab.com/handbook/company/team/#junminghuang) | [Senior Machine Learning Engineer](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/)  
[![Lindsey Shelton](https://about.gitlab.com/images/team/lindseyshelton-crop.jpg)Lindsey Shelton](https://handbook.gitlab.com/handbook/company/team/#lindsey-shelton) |  [Frontend Engineer](https://handbook.gitlab.com/job-families/engineering/development/frontend/), AI-powered:Duo Workflow  
[![Mikołaj Wawrzyniak](https://about.gitlab.com/images/team/mikolajwawrzyniak-crop.jpg)Mikołaj Wawrzyniak](https://handbook.gitlab.com/handbook/company/team/#mikolaj_wawrzyniak) |  [Staff Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/), AI-powered:Duo Workflow  
[![Roman Eisner](https://about.gitlab.com/images/team/romaneisner-crop.jpg)Roman Eisner](https://handbook.gitlab.com/handbook/company/team/#romaneisner) | [Backend Engineer](https://handbook.gitlab.com/job-families/engineering/development/backend/)  
[![Sam Beckham](https://about.gitlab.com/images/team/sambeckham-crop.jpg)Sam Beckham](https://handbook.gitlab.com/handbook/company/team/#samdbeckham) |  [Engineering Manager](https://handbook.gitlab.com/job-families/engineering/development/management/engineering-manager/), AI-powered:Workflow Catalog  
[![Surabhi Suman](https://about.gitlab.com/images/team/surabhisuman-crop.jpg)Surabhi Suman](https://handbook.gitlab.com/handbook/company/team/#ssuman3) | [Senior Backend Engineer, AI-powered:Duo Workflow](https://handbook.gitlab.com/job-families/engineering/development/backend/)  
[![Thomas Schmidt](https://about.gitlab.com/images/team/thomasschmidt-crop.jpg)Thomas Schmidt](https://handbook.gitlab.com/handbook/company/team/#thomas-schmidt) | Staff Backend Engineer  
[![Tim Morriss](https://about.gitlab.com/images/team/tmrrss-crop.jpg)Tim Morriss](https://handbook.gitlab.com/handbook/company/team/#tmrrss) | [Backend Engineer, AI-powered:Duo Workflow](https://handbook.gitlab.com/job-families/engineering/development/backend/)  
**Product, Design & Quality**
Name | Role  
---|---  
### ☎️ How to reach us[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#-how-to-reach-us)
Depending on the context here are the most appropriate ways to reach out to the Agent Foundations Group:
  * Slack Channel: `#g_agent_foundations`
  * Slack Groups: `@duo-workflow` (entire team) and `@duo-workflow-engs` (just engineers)


### Technical Components 🛠️[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#technical-components-)
Besides the main GitLab repository these are the key technical components we work with:
  1. [Duo Workflow Service within AI Gateway](https://gitlab.com/gitlab-org/modelops/applied-ml/code-suggestions/ai-assist/-/tree/main/duo_workflow_service) 🐍
  2. IDE Integration 🧩 
    1. [GitLab LSP](https://gitlab.com/gitlab-org/editor-extensions/gitlab-lsp)
    2. [GitLab VS Code Extension](https://gitlab.com/gitlab-org/gitlab-vscode-extension) + more extensions for specific IDEs


Additional projects that we mainly maintain:
  1. [Duo Workflow Tests](https://gitlab.com/gitlab-org/duo-workflow/testing/duo-workflow-tests)
  2. [Default Docker Image](https://gitlab.com/gitlab-org/duo-workflow/default-docker-image)


For an understanding of how these components work together, take a look at the [architecture](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/duo_workflow/).
## 📦 Team Processes[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#-team-processes)
### Goalkeeper Rotation[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#goalkeeper-rotation)
The Agent Foundations team uses a goalkeeper rotation to ensure incoming Request-for-Help, questions, and issues are triaged and directed to the appropriate people or teams. The goalkeeper acts as the first line of support, keeping work flowing smoothly and preventing bottlenecks. Every milestone 2 engineers are assigned to this to ensure appropriate coverage.
The responsibilities and further process are in the [Goalkeeper issue template](https://gitlab.com/gitlab-org/ai-engineering/agent-foundations/tasks/-/blob/main/.gitlab/issue_templates/goalkeeper.md).
### Retrospective[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#retrospective)
We believe that continuously evolving and improving the way we work is crucial to delivering good outcomes. Traditionally, retrospectives are used to facilitate this improvement. Due to our geographical distribution we cannot run typical sync retrospectives that include everyone. We’ve also found that completely async retrospectives only see limited participation and discussion.
We’re currently trialing a mixed retrospective format, where team members pair on filling in the retro issue. The process is as follows:
  1. Every milestone the [async-retrospective project](https://gitlab.com/gitlab-org/async-retrospectives) automatically creates an issue in the [agent-foundations retro project](https://gitlab.com/gl-retrospectives/data-science/ai-powered/agent-foundations/-/work_items) which contains a list of retro questions.
  2. Every 4th week a [donut Slackbot](https://www.donut.com/) will pair up all team members in random groups of two.
  3. Every group of two should pair on filling out the retro issue for the current iteration together within that week: 
    1. This should happen ideally through a sync meeting or alternatively via Slack.
    2. Focus on what happened the last two weeks, since the last pairing.
    3. Pairing should involve taking the time to think through the questions, talking about the answers with your pair and coming up with action items based on the identified problems.
    4. Expect an overall time commitment of 30 minutes to an hour for the bi-weekly pairing.
  4. Every 2nd week we have a 30-minute time blocker event, that is meant for everyone to take the time to answer Retro discussions.


### 📆 Regular team meetings[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#-regular-team-meetings)
**❗️Important** : For every meeting, the [Agent Foundations team’s meeting document](https://docs.google.com/document/d/15N9G3UWoB_u8KOErdk_aGk5IdBoxEFBWMSgg9FvwVXo/edit?tab=t.0#heading=h.j3rcm4sf2nc9) should be used, and filled with the meeting notes, as well as references to any other sync meeting agendas/notes/recordings which have recently occurred. This will make it easier for people to find any meeting notes.
#### Team Meetings[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#team-meetings)
  1. **Agent Foundations Meeting**
     * **When:** Every Monday, 15:00 UTC and every Wednesday 10:00 UTC
     * **What:** This meeting serves as a general sync meeting to bring up any current issues and blockers. We walk the board at least once a week on an alternating basis between the meetings to ensure clarity around current progress and priorities


### Shared calendars[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#shared-calendars)
  * AI-Powered Stage Calendar (Calendar ID: `c_n5pdr2i2i5bjhs8aopahcjtn84@group.calendar.google.com`)


### 📚 Agent Foundations Board Outline[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#-agent-foundations-board-outline)
The Agent Foundations team is following a milestone process. All currently prioritized issues are visualized in our [milestone board](https://gitlab.com/groups/gitlab-org/-/boards/7828018?milestone_title=Started&label_name\[\]=group%3A%3Aagent%20foundations). Overview issues that outline the goal and focus points of past milestone and the current one can be found in the [overarching epic](https://gitlab.com/groups/gitlab-org/-/work_items/18293).
We aim for ambitious but achievable planning of the current milestone, and only issues in the current milestone should be actively worked on. If there are no more issues available reach out to the EM/PM of the team for clarification.
We work with these statuses for issues:
  1. **New** : As of yet unclassified issues, which need to be updated to one of the used workflow labels or meta issues such as iteration overview.
  2. **Refinement** : Issues in this stage have been identified as important to be worked on but are not ready for development yet. This might be due to a variety of reasons such as missing or not finished designs or architectural questions that need to be clarified.
  3. **Ready for development** : Issues that are ready for implementation are moved to this list.
  4. **In dev** : When a developer begins work on an issue, they should move it to this list.
  5. **Blocked** : Issues in this stage currently cannot be further continued as they depend on other work being done first.
  6. **In review** : After development is complete and submitted to be reviewed, the issue should be moved to this list.
  7. **Verification** : Following a successful code and UX review, the issue should be moved to this list and the “verification” label should be applied.
  8. **Closed** : Once the issue is verified and confirmed to be working properly, it should be moved to this list, the “complete” label should be applied, and the issue should be closed.


We use labels to help with understanding the order in which issues should be worked on:
  1. **Deliverable** : These items are the primary deliverables of an iteration and should therefore be picked up first.
  2. **Stretch** : We aim to deliver most of these items, but as part of planning ambitiously some of them might slip.


## 👏 Communication[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#-communication)
The Agent Foundations Team communicates based on the following guidelines:
  1. Always prefer async communication over sync meetings.
  2. Don’t shy away from arranging a [sync call](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#-ad-hoc-sync-calls) when async is proving inefficient, however always record it to share with team members.
  3. By default communicate in the open.
  4. All work-related communication in Slack happens in the `#g_agent_foundations` channel.


### 📋 Weekly Async Updates[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#-weekly-async-updates)
We maintain a practice of weekly async status updates to ensure clear communication, track progress effectively, and maintain transparency across our team. This process aligns with our core values by fostering collaboration, driving results, and promoting efficiency through structured communication.
#### Timing and Frequency[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#timing-and-frequency)
  * Team members post updates every Wednesday
  * Updates are required for all assigned issues that are at least **In Dev**. For other assigned issues it is up to the assignee to decide whether an update is warranted.
  * Multiple updates may be needed if working on multiple issues


#### Template[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#template)
This is the template to use for the updates
```

## Async Status Update yyyy-mm-dd

- **Progress & Status**: _What progress have you made? What's the current state?_
- **Next Steps**: _What are your planned next actions?_
- **Blockers**: _Are you blocked or need assistance with this?_
- **How confident are you that this will make it to the current milestone?**
    - [ ] Not confident
    - [ ] Slightly confident
    - [ ] Very confident

_Remember to update the status!_

/cc @bastirehm

```

Be sure to tag your engineering manager, product manager, and any team members you are collaborating with.
#### Best practices[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#best-practices)
  * Be specific and concise in updates
  * Always include next steps, even if they’re tentative
  * Flag blockers early - don’t wait until they become critical
  * Use the template consistently for easier scanning
  * Link to relevant issues or documentation when appropriate


### ⏲ Time Off[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#-time-off)
Team members should add any [planned time off](https://handbook.gitlab.com/handbook/people-group/time-off-and-absence/time-off-types/) in the “Workday” slack app, in accordance with the [taking time off](https://handbook.gitlab.com/handbook/engineering/#taking-time-off) policy, including creating a [PTO coverage issue](https://gitlab.com/gitlab-com/engineering-division/pto-coverage/-/issues/new).
### 🤙 Ad-hoc sync calls[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#-ad-hoc-sync-calls)
We operate using async communication by default. There are times when a sync discussion can be beneficial and we encourage team members to schedule sync calls with the required team members as needed.
## 🔗 Useful Links[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#-useful-links)
  * [Monthly Retros](https://gitlab.com/gl-retrospectives/data-science/ai-powered/agent-foundations/-/work_items)
  * [LangGraph Workshop](https://gitlab.com/gitlab-org/duo-workflow/langgraph-workshop)


### 📝 Dashboards (internal only)[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#-dashboards-internal-only)
  * [Usage Metrics Tracking in Tableau](https://10az.online.tableau.com/#/site/gitlab/views/DuoWorkflowMetricsTracking/DuoWorkflowMetricsTracking?:iid=1)


### 📹 GitLab Unfiltered Playlist[](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/#-gitlab-unfiltered-playlist)
The Agent Foundations Group collates some video recordings related to the group and its team members in [a playlist](https://www.youtube.com/playlist?list=PL05JrBw4t0KoByUnA4Oq-AAins6hDFwyC) in the [GitLab Unfiltered](https://www.youtube.com/channel/UCMtZ0sc1HHNtGGWZFDRTh5A) YouTube channel.
* * *
#####  [Troubleshooting](https://handbook.gitlab.com/handbook/engineering/ai/agent-foundations/troubleshooting/)
Information about monitoring and logging tools of Flows.
Last modified February 4, 2026: [Document goalkeeper rotation process for Agent Foundations (`7d0906e5`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/7d0906e5)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/ai/agent-foundations/_index.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/ai/agent-foundations/_index.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)