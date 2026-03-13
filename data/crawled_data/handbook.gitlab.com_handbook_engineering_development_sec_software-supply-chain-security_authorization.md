# Authorization Group
## Planning[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/#planning)
Our [Planning issues](https://gitlab.com/gitlab-org/software-supply-chain-security/authorization/team-tasks/-/issues?sort=created_date&state=opened&label_name%5B%5D=Planning%20Issue&first_page_size=50) are the SSOT of what we’re working on now, and what we’re working on next. We also have an [issue board](https://gitlab.com/gitlab-org/gitlab/-/boards/9750781?milestone_title=Started&label_name\[\]=group%3A%3Aauthorization) to view these from a `workflow` perspective. To maintain the issue lists leadership (EM+PM) will keep the lists triaged.
### Workflow[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/#workflow)
Label | Definition  
---|---  
`~workflow::ready for development` | Ready to be picked up by an engineer. `~priority::1` being the highest priority.  
`~workflow::scheduling` or lacking a `~workflow` label | Shouldn’t be picked up by an engineer and needs to be triaged by leadership. If leadership has no intention on this work being done anytime soon, they should assign the ~Backlog milestone.  
`~workflow::refinement` | Needs further investigation by engineering. After refininement, an issue should have a weight assigned and the workflow label should be updated to `~workflow::scheduling`  
`~workflow::solution validation` | Needs Product input before work can begin  
`~workflow::design` | Needs design input to proceed and/or is actively being worked on by UX  
## Weekly async issue updates[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/#weekly-async-issue-updates)
At the end of every week, each engineer is expected to provide a quick async update on the epic/issue they are working on by commenting on their assigned issues using the following template:
```


### Async issue update

* Current status:
<!--- Please provide a quick summary of the current status (one sentence) -->

* Shipping this milestone: <!-- Not confident | Slightly confident | Very confident -->

* Scope reduction opportunities: <!-- No | Yes, ... -->

/health_status <!-- on_track | needs_attention | at_risk -->
/label <!-- ~"workflow::In dev" | ~"workflow::In review" | ~"workflow::verification" |~"workflow::blocked" -->

<!-- Please apply a :triangular_flag_on_post: emoji to this comment. Fore more information see https://gitlab.com/jayswain/automated-reporting -->

```

We do this to encourage our team to be more async in collaboration and to allow the community and other team members to know the progress of issues that we are actively working on.
## Group Members[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/#group-members)
[Authorization group](https://gitlab.com/gitlab-org/software-supply-chain-security/authorization) can be `@` mentioned on GitLab with `@gitlab-org/software-supply-chain-security/authorization`.
The following people are permanent members of the group:
Name | Role  
---|---  
[![Ayush Billore](https://about.gitlab.com/images/team/ayush-crop.jpg)Ayush Billore](https://handbook.gitlab.com/handbook/company/team/#abime) |  [Backend Engineer](https://handbook.gitlab.com/job-families/engineering/backend-engineer/), Software Supply Chain Security:Authorization  
[![Ajay Thomas](https://about.gitlab.com/images/team/ajaythomas-crop.jpg)Ajay Thomas](https://handbook.gitlab.com/handbook/company/team/#ajaythomasinc) |  [Engineering Manager](https://handbook.gitlab.com/job-families/engineering/development/management/engineering-manager/), Software Supply Chain Security:Authorization  
[![Alex Buijs](https://about.gitlab.com/images/team/alexbuijs-crop.jpg)Alex Buijs](https://handbook.gitlab.com/handbook/company/team/#alexbuijs) |  [Senior Fullstack Engineer](https://handbook.gitlab.com/job-families/engineering/development/fullstack/), Software Supply Chain Security:Authorization  
[![Daniel Tian](https://about.gitlab.com/images/team/danieltian-crop.jpg)Daniel Tian](https://handbook.gitlab.com/handbook/company/team/#dftian) | [Senior Frontend Engineer, Software Supply Chain Security:Authorization](https://handbook.gitlab.com/job-families/engineering/development/frontend/#senior-frontend-engineer)  
[![Diane Russel](https://about.gitlab.com/images/team/dianerussel-crop.jpg)Diane Russel](https://handbook.gitlab.com/handbook/company/team/#dlrussel) |  [Backend Engineer](https://handbook.gitlab.com/job-families/engineering/backend-engineer/), Software Supply Chain Security:Authorization  
[![Eugie Limpin](https://about.gitlab.com/images/team/eugielimpin-crop.jpg)Eugie Limpin](https://handbook.gitlab.com/handbook/company/team/#eugielimpin) |  [Senior Fullstack Engineer](https://handbook.gitlab.com/job-families/engineering/development/fullstack/), Software Supply Chain Security:Authorization  
[![Hinam Mehra](https://about.gitlab.com/images/team/HinamMehra-crop.jpg)Hinam Mehra](https://handbook.gitlab.com/handbook/company/team/#hmehra) |  [Senior Fullstack Engineer](https://handbook.gitlab.com/job-families/engineering/development/fullstack/), Software Supply Chain Security:Authorization  
[![Ian Anderson](https://about.gitlab.com/images/gitlab-logo-extra-whitespace.png)Ian Anderson](https://handbook.gitlab.com/handbook/company/team/#imand3r) |  [Staff Backend Engineer](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/), Software Supply Chain Security:Authorization  
[![Jay Swain](https://about.gitlab.com/images/team/jayswain-crop.jpg)Jay Swain](https://handbook.gitlab.com/handbook/company/team/#jayswain) | [Senior Backend Engineer, Software Supply Chain Security:Authorization](https://handbook.gitlab.com/job-families/engineering/development/backend/senior/)  
[![Matthew MacRae-Bovell](https://about.gitlab.com/images/team/mmacrae-bovell-crop.jpg)Matthew MacRae-Bovell](https://handbook.gitlab.com/handbook/company/team/#mmacrae-bovell) |  [Backend Engineer](https://handbook.gitlab.com/job-families/engineering/backend-engineer/), Software Supply Chain Security:Authorization  
## Team Google Drive[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/#team-google-drive)
Documents are saved [here](https://drive.google.com/drive/folders/1XGKbOM46ujoZbv9HMWPtx1x2Mp4Ku3bg) for the authorization group.
## Team Meetings[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/#team-meetings)
Our group holds synchronous meetings to gain additional clarity and alignment on our async discussions. We aspire to [record](https://handbook.gitlab.com/handbook/tools-and-tips/zoom/) all of our meetings as our team members are spread across several time zones and often cannot attend at the scheduled time.
We have a weekly team sync meeting with rotating AMER/APAC and EMEA/AMER friendly time slots: Tues 20:00 UTC and Weds 14:30 UTC. Relevant [recordings](https://drive.google.com/drive/folders/1_QjpV0TCELapJW2sXzTOViUUWXQyVj3r) and [doc](https://docs.google.com/document/d/1NGfuCaCNtyaN1qQwARhSh9cCNZkCVG-VisdK5GyP_N4/edit?usp=sharing)
## Planning for PTO[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/#planning-for-pto)
We follow the [Engineering process for taking time off](https://handbook.gitlab.com/handbook/engineering/#taking-time-off) and [GitLab team members Guide to Time Off](https://handbook.gitlab.com/handbook/people-group/time-off-and-absence/time-off-types/).
## Group Shared Calendar[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/#group-shared-calendar)
The [Authorization Group Shared Calendar](https://calendar.google.com/calendar/embed?src=c_97507fb9234d07c2561c1b1ccc98cab1462bf0364214f2cc4917eee8a86b7cdd%40group.calendar.google.com&ctz=America%2FDetroit) is used to make sure PTO events are visible to everyone on the team. Subscribe to this calendar to see events (OOO and others) associated with AuthZ engineers.
### Syncing your Time Off by Deel entries to the Shared Calendar[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/#syncing-your-time-off-by-deel-entries-to-the-shared-calendar)
Below are the steps to add the calendar to Time Off by Deel:
  1. Open Slack
  2. Open app in slack “Time Off by Deel”
  3. Go to tab “Home”,
  4. Click on the dropdown “Your Events”, and select “Calendar Sync”.
  5. Under “Additional calendars to include?”, click on “Add calendar”.
  6. Add the following calendar ID: `c_97507fb9234d07c2561c1b1ccc98cab1462bf0364214f2cc4917eee8a86b7cdd@group.calendar.google.com`


Great job! 🎉 Your PTO events will be synced to Authorization Group Shared Calendar from now on. 🚀
## Collaboration[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/#collaboration)
### Code Review[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/#code-review)
Because this group works on components of the application that have a [far-reaching impact](https://handbook.gitlab.com/handbook/engineering/development/#reducing-the-impact-of-far-reaching-work), we take these extra steps in order to reduce our risk of a production incident:
  1. Our team’s merge requests should be assigned to another Authorization team member for first review in order to build more institutional knowledge across the team. This review should be done as a [reviewer](https://docs.gitlab.com/ee/development/code_review.html#the-responsibility-of-the-reviewer). The Authorization approval counts as the approval matching the role of the Authorization Reviewer, e.g. having a Backend Review from Authorization counts as a Backend Review. Once approved, the Authorization Reviewer should request a review from a Maintainer from the appropriate [maintainer category](https://docs.gitlab.com/ee/development/code_review.html#approval-guidelines).
  2. Authorization related merge requests (those touching custom roles and policies related code) require a review by an [Authorization Engineer](https://gitlab.com/groups/gitlab-org/govern/authorization/approvers/-/group_members?with_inherited_permissions=exclude). This is guarded by using the `CODEOWNERS` feature of GitLab.


### Engineering Refinement[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/#engineering-refinement)
#### Overview[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/#overview)
Engineering refinement is about creating alignment among all team members. To ensure an issue is ready to move into development and that the issue will match everyone’s expectations when the work is delivered.
The goal of the refinement process is to:
  * Collaborate with stakeholders and domain experts, since often times `~group::authorization` is making changes in parts of the product owned by other teams.
  * Raise any questions or concerns.
  * Outline an implementation plan. This is especially important when backend changes need to unblock frontend work.
  * Ensure issue is ready to be worked on.
  * Breakdown a big issues into smaller tasks, so they can be picked up by different engineers.
  * Assign a weight to the issue or the individual tasks.


#### How will refinement be conducted?[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/#how-will-refinement-be-conducted)
  * We will have a weekly meeting with rotating AMER/APAC and EMEA/AMER friendly time slots. Attendance is optional. The calendar will act as a reminder for team members to work on refinement weekly. These meetings can also promote candid discussion for other ongoing issues that engineers are facing.
  * The purpose of these meetings will be to refine the issues that have been assigned the [workflow::refinement](https://gitlab.com/groups/gitlab-org/-/issues/?sort=updated_desc&state=opened&label_name%5B%5D=group%3A%3Aauthorization&label_name%5B%5D=workflow%3A%3Arefinement&first_page_size=20) label.
  * If an issue requires further research, an engineer can conduct more research outside of the meeting. In a later meeting, the more refined issues can then be estimated.
  * If an engineer is conducting refinement async, they can follow the steps listed below, summarize findings (and proposals if you have any) and mention other team members and involved counterparts.
  * If it seems unlikely to reach an agreement during the opened discussion or there is a clear misunderstanding, it can be added as an agenda to the sync meeting. Engineers can optionally also those who might be able to help because of their expertise.


#### Steps[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/#steps)
  * Ensure the issue is fully understood.
  * Check the issue description for completeness. 
    * Does it have the necessary designs?
    * Is the expected functionality clearly articulated?
    * Are there dependencies? On other teams or on other issues?
  * If the issue is not complete: 
    * Tag `@jrandazzo` (PM) or `@ajaythomasinc` (EM), so they know that the item can not be fully groomed. They can help complete the issue and outline what is needed.
  * Break down the issue into tasks. 
    * If the issue requires both frontend and backend work, then we can create different tasks to divide that work. This will allow different engineers to collaborate on the issue together.
    * If it’s a new or complicated feature, specify what can be delivered in the first iteration, and what can be delivered in future iterations.
  * Outline an implementation plan 
    * If the issue requires both frontend and backend work, define the request/response structure of API endpoints to ensure there is minimal computation in the Vue components.
    * If further research is needed to figure out the implementation plan, a spike issue can be created. We can circle back to the issue once we have the findings from the spike.
  * Assign a weight using [t-shirt sizing approach](https://handbook.gitlab.com/handbook/engineering/business-technology/data-team/how-we-work/planning/#t-shirt-sizing-approach), set the label `~workflow::scheduling` and tag `@ajaythomasinc` and `@jrandazzo`. If the issue has been broken down into tasks, weights can be assigned to each of the tasks.
  * Once the next steps are clear, update the description of the issue(s) and unassign yourself.


## Links and resources[](https://handbook.gitlab.com/handbook/engineering/development/sec/software-supply-chain-security/authorization/#links)
  * Our Slack channels 
    * SSCS:Authorization [#g_sscs_authorization](https://gitlab.slack.com/archives/C0610LVCSAY)


Last modified October 9, 2025: [Updated Authorization page about shared team calendar (`bbf031c3`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/bbf031c3)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/development/sec/software-supply-chain-security/authorization.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/development/sec/software-supply-chain-security/authorization.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)