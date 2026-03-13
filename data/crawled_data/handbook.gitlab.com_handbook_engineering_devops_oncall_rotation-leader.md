# Rotation Leaders
Welcome to the Rotation Leader role for the DevOps Tier 2 On-Call program. As a Rotation Leader, you are responsible for the health, fairness, and effectiveness of your team’s on-call rotation. This guide outlines your core responsibilities and how to execute them.
## Your Role and Responsibilities[](https://handbook.gitlab.com/handbook/engineering/devops/oncall/rotation-leader/#your-role-and-responsibilities)
Rotation Leaders are expected to:
  * [align according to Infrastructure Platform expectations](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/incident-management/on-call/#responsibilities-for-rotation-leaders),
  * coordinate the DevOps on-call rotation (adding and removing shifts),
  * ensure there are enough team members to [provide adequate coverage](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/incident-management/on-call/tier-2/#coverage-expectations),
  * ensure those team members understand their role,
  * serve as a point of escalation on the escalation path, and
  * conduct regular reviews on the effectiveness of the rotation


## Managing the Schedule[](https://handbook.gitlab.com/handbook/engineering/devops/oncall/rotation-leader/#managing-the-schedule)
### Building and Maintaining the Rotation[](https://handbook.gitlab.com/handbook/engineering/devops/oncall/rotation-leader/#building-and-maintaining-the-rotation)
While [general guidance is provided](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/incident-management/on-call/#how-many-people-are-needed-to-set-up-a-rotation), you are responsible for the overall structure and composition of the rotation:
  * Target 8 people per region (APAC, EMEA, AMER) for balanced workload and flexibility, but minimally 6
  * Maximum 12 people before reassessing team structure
  * This means engineers will be on call one week for every 6-12 weeks, or between 22-43 days of the year
  * Publish schedules at least one month in advance so team members can plan


### The Schedule[](https://handbook.gitlab.com/handbook/engineering/devops/oncall/rotation-leader/#the-schedule)
**To publish, manage, or view the schedule which includes AMER, EMEA, and APAC DevOps Rotations within it:**
  * Use Incident.io as your single source of truth for all scheduling 
    * [See all team members on a rotation here](https://app.incident.io/gitlab/catalog/Schedule/01K611MG8T5CW874Q5JZER3H0Z)
    * [Access the on-call schedule here](https://app.incident.io/gitlab/on-call/schedules/01K611MG8T5CW874Q5JZER3H0Z)
    * [See all management included in escalations here](https://app.incident.io/gitlab/catalog/Schedule/01K611ZT9YX2PSA8WAMEP6A66G)
    * [Access the escalation schedule here](https://app.incident.io/gitlab/on-call/schedules/01K611ZT9YX2PSA8WAMEP6A66G)
  * Create overrides when someone needs coverage swapped
  * Communicate schedule changes promptly to affected team members
  * Track future scheduling 3-6 months in advance when possible


### Coverage Hours[](https://handbook.gitlab.com/handbook/engineering/devops/oncall/rotation-leader/#coverage-hours)
[See coverage expectations here.](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/incident-management/on-call/tier-2/#coverage-expectations)
### Public Holidays[](https://handbook.gitlab.com/handbook/engineering/devops/oncall/rotation-leader/#public-holidays)
[See here.](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/incident-management/on-call/tier-2/#public-holidays)
## Regular Reviews[](https://handbook.gitlab.com/handbook/engineering/devops/oncall/rotation-leader/#regular-reviews)
Every quarter, conduct a review of:
  * [Do we need more Subject Matter Experts?](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/incident-management/on-call/tier-2/#how-to-determine-if-we-need-a-specific-set-of-subject-matter-experts-to-form-a-tier-2-rotation)
  * How many times was each person on-call? Was anyone on-call more than once every 4 weeks? How fairly were shifts distributed?
  * How many times are team members paged during a shift?
  * Did anyone burn out or report unsustainable load?
  * Did you meet your [coverage and response time goals](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/incident-management/on-call/tier-2/#metrics-that-can-be-reviewed-to-assist-in-this-decision) for each region?
  * Are there services generating too few pages (potential coverage gaps) or exessively (alert fatigue)?
  * Time to Fix: How long from declaration to resolution?
  * Are there patterns around what gets escalated, from who, and why?
  * Are escalations going to the right teams on first try (target 90%+)?


## Onboarding New Team Members[](https://handbook.gitlab.com/handbook/engineering/devops/oncall/rotation-leader/#onboarding-new-team-members)
### Adding Someone to the Rotation[](https://handbook.gitlab.com/handbook/engineering/devops/oncall/rotation-leader/#adding-someone-to-the-rotation)
[See: Getting added to a rotation.](https://handbook.gitlab.com/handbook/engineering/devops/oncall/joining-and-leaving-rotation/#how-do-i-get-added-to-the-rotation)
### Required Onboarding Resources[](https://handbook.gitlab.com/handbook/engineering/devops/oncall/rotation-leader/#required-onboarding-resources)
[Ensure new team members have access to and understand the 1st shift information](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/incident-management/on-call/tier-2/#resource-locations).
## Iterate[](https://handbook.gitlab.com/handbook/engineering/devops/oncall/rotation-leader/#iterate)
As escalations come in, identify gaps in documentation:
  * When Tier 2 engineers escalate, ask what information would have helped them resolve it faster
  * Use post-incident retrospectives to identify runbook gaps
  * Prioritize creating or updating runbooks for frequent escalation patterns
  * Monitor whether incidents reference runbooks
  * Identify runbooks that aren’t being used and update or remove them
  * Create new runbooks based on escalation patterns
  * Aim to cover 80% of common incidents


For S1/S2 incidents (or significant S3/S4 incidents):
  * Ensure 100% of escalated S1/S2 incidents have a formal retrospective or write-up
  * Lead retrospectives in a blameless manner, focusing on system improvements
  * Document what was learned and what can be improved
  * Track action items and follow up on completion


## Quick Reference: Key Responsibilities[](https://handbook.gitlab.com/handbook/engineering/devops/oncall/rotation-leader/#quick-reference-key-responsibilities)
**Schedule Management:**
  * Maintain 6-12 people in rotation
  * Publish schedules 1+ month in advance
  * Track effectiveness quarterly
  * Cap individual rotation frequency at once per 4 weeks maximum


**Onboarding:**
  * Add new members to Incident.io
  * Provide tool access and documentation
  * Support first shifts
  * Ensure training completion


**Workload Tracking:**
  * Monitor pages per shift
  * Track incident response metrics
  * Watch for burnout indicators
  * Conduct quarterly effectiveness reviews


**Team Support:**
  * Help with schedule conflicts and swaps
  * Create overrides for absences
  * Address unsustainable load
  * Support escalations during incidents


**Improvement:**
  * Identify runbook gaps
  * Lead blameless retrospectives
  * Track metrics and trends
  * Share learnings with the team


### Related Pages[](https://handbook.gitlab.com/handbook/engineering/devops/oncall/rotation-leader/#related-pages)
  * [Joining and Leaving the Rotation](https://handbook.gitlab.com/handbook/engineering/devops/oncall/joining-and-leaving-rotation/) — Manage team member add/removal
  * [Coverage and Scheduling](https://handbook.gitlab.com/handbook/engineering/devops/oncall/coverage-and-scheduling/) — Manage and publish schedules
  * [Measuring Success of the Tier 2 On-Call Program](https://handbook.gitlab.com/handbook/engineering/devops/oncall/measuring-success/) — Track rotation health metrics
  * [Communication and Culture](https://handbook.gitlab.com/handbook/engineering/devops/oncall/communication-and-culture/) — Foster blameless culture in your rotation


Last modified February 25, 2026: [Consolidate Tier 2 escalation pages (`dd3a3fed`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/dd3a3fed)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/devops/oncall/rotation-leader.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/devops/oncall/rotation-leader.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)