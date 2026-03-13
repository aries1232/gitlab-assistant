# EOC Onboarding Buddies
## Introduction[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-oncall-onboarding-buddy/#introduction)
Engineers on-call (EOC) onboarding buddies play a crucial role in ensuring a positive and effective onboarding experience for new engineers joining the on-call rotation. Being on call can be very stressful, particularly for engineers who are new to the role or unfamiliar with our systems and processes. That’s why it’s essential that all new engineers joining the on-call rotation be assigned a buddy who is ready and willing to assist with the onboarding process. These buddies are experienced on-call engineers who can provide guidance and support and share their invaluable knowledge.
The EOC on-call buddy system is designed to:
  * Accelerate the on-call onboarding process for new engineers
  * Reduce stress and anxiety associated with on-call responsibilities
  * Help new engineers gain confidence in their ability to handle incidents
  * Ensure that new team members become self-sufficient on-call engineers more quickly
  * Promote knowledge sharing and best practices within the team


By pairing new engineers with experienced buddies, we create a supportive environment that allows for faster learning, better incident response, and a more resilient team overall. This system not only benefits the new engineers but also strengthens our entire on-call process by continuously refining and sharing our collective expertise.
Definitions used in this document:
  * **EOC-Buddy** : An experienced on-call engineer who volunteers to mentor and guide new engineers through the on-call onboarding process
  * **EOC-Shadow** : A new engineer who is going through the on-call onboarding process under the guidance of a Buddy


## Buddy Responsibilities[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-oncall-onboarding-buddy/#buddy-responsibilities)
The role of a EOC-Buddy is important in helping new engineers become confident and effective on-call responders. Here are the key responsibilities:
  * Schedule an initial call with the EOC-Shadow
  * Review the on-call runbook project together and explain the general workflow of incident response
  * Ensure EOC-Shadow has access to all necessary tools, dashboards, and alerting systems
  * Walk through the escalation policy and communication channels used during incidents
  * Invite EOC-Shadow into incident Zoom calls during active incidents
  * Share personal experiences and lessons learned from past incidents
  * Be available as primary respondent during their shadow shifts
  * Provide secondary support during EOC-Shadow’s first few on-call shifts
  * Check in periodically on the progress and offer help


## How Can I Become An On-call Onboarding Buddy?[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-oncall-onboarding-buddy/#how-can-i-become-an-on-call-onboarding-buddy)
The EOC buddy program operates on a volunteer basis, allowing experienced engineers to contribute to the team’s growth based on their willingness and capacity. Please make sure to check the [Buddy Responsibilities](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-oncall-onboarding-buddy/#buddy-responsibilities) section.
If you are willing to become a EOC-Buddy, add yourself to `@eoc-buddies` Slack group via [sre-oncall-onboarding-buddy project](https://gitlab.com/gitlab-com/gl-infra/ops-team/toolkit/eoc-buddies-members/-/tree/main?ref_type=heads). This Slack group receives notifications when EOC-Shadows are looking for buddies. When you find a suitable match, respond to the request and notify both your manager and the EOC-Shadow.
## Workflow[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-oncall-onboarding-buddy/#workflow)
### Being an EOC-Shadow[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-oncall-onboarding-buddy/#being-an-eoc-shadow)
  1. Join the `#eoc-shadowing` Slack channel introduce yourself
  2. Ping the `@eoc-buddies` Slack group in the channel, specify your timezone and availability and clearly state that you’re looking for a buddy
  3. Once a Buddy is assigned, schedule an initial coffee chat with your new EOC-Buddy. Get to know each other and discuss expectations and suitable schedules for sync calls
  4. Join the [SRE Shadow rotation schedule](https://app.incident.io/gitlab/on-call/schedules/01K5YWAGZ7YCQGAG7ATQ9XQWHW) in incident.io and align your shifts with your EOC-Buddy’s on-call shifts.
  5. Schedule weekly 45-minute calls with your EOC-Buddy. These calls should occur after each on-call weekly shift. Review and discuss incidents from the past week
  6. Begin responding to S3/S4 incidents as primary responder. Your Buddy will provide guidance and support. Document learnings and questions
  7. Continue working through the SRE-oncall onboarding issue, track your progress and completion of required tasks


### Being an EOC-Buddy[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-oncall-onboarding-buddy/#being-an-eoc-buddy)
  1. Join the `eoc-buddies` Slack group
  2. When a buddy is requested via the Slack group, review if the timezone is suitable and if you have the capacity to be assigned to the EOC-Shadow
  3. Organize initial coffee chat with your EOC-Shadow
  4. Discuss the time for periodic call after each of your weekly shifts. Review the process for the Shadow to be a primary respondent for S3/S4 incidents. Be available as a secondary respondent for each incident
  5. Regularly check onboarding progress and provide additional support when needed


### FAQs[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-oncall-onboarding-buddy/#faqs)
#### What if I cannot find a buddy?[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-oncall-onboarding-buddy/#what-if-i-cannot-find-a-buddy)
Please talk to your manager and ask for help. Your manager will look into available engineers in your timezone and find a suitable buddy.
#### Can I shadow other engineers and not just my on-call buddy?[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-oncall-onboarding-buddy/#can-i-shadow-other-engineers-and-not-just-my-on-call-buddy)
Absolutely! It is encouraged that you shadow any EOCs and incidents whenever you feel is right for you. Meeting with other engineers will help you to get a wider knowledge and diverce approach to troubleshooting and incident management.
Last modified November 19, 2025: [Update handbook pages to point to Incident.io (`7bb50e99`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/7bb50e99)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-oncall-onboarding-buddy.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-oncall-onboarding-buddy.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)