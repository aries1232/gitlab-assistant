# Developer Onboarding
Awesome! You’re about to become a GitLab developer! Here you’ll find everything you need to start developing.
Awesome! You’re about to become a GitLab developer! Make sure you’ve checked out our [handbook](https://handbook.gitlab.com/handbook/) beforehand, so you get a feeling of how we work at GitLab. Below you’ll find everything you need to start developing. If something is missing, add it (as goes with everything at GitLab)!
## GitLab Environments[](https://handbook.gitlab.com/handbook/engineering/workflow/developer-onboarding/#gitlab-environments)
We have multiple [GitLab environments](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/environments/).
On those instances, please enable the [performance bar](https://docs.gitlab.com/ee/administration/monitoring/performance/performance_bar.html) by pressing `p` then `b` (even on production.)
Then, read how to use and enable the [production Canary](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/environments/canary-stage/) on GitLab.com.
## Getting started with GitLab development[](https://handbook.gitlab.com/handbook/engineering/workflow/developer-onboarding/#getting-started-with-gitlab-development)
To start development, follow the instructions for the [GitLab Development Kit](https://gitlab.com/gitlab-org/gitlab-development-kit).
## GitLab Repositories[](https://handbook.gitlab.com/handbook/engineering/workflow/developer-onboarding/#gitlab-repositories)
GitLab consists of many subprojects. A curated list of GitLab Repositories can be found at the [GitLab Engineering Projects](https://handbook.gitlab.com/handbook/engineering/projects/) page.
Almost all repositories are available on both GitLab.com and dev.gitlab.org. We also mirror to dev.gitlab.org for availability reasons and [GitHub](https://github.com/gitlabhq) for historical reasons.
All issues should be filed on GitLab.com.
## Infrastructure[](https://handbook.gitlab.com/handbook/engineering/workflow/developer-onboarding/#infrastructure)
For everything related to infrastructure, check out the [Infrastructure handbook](https://handbook.gitlab.com/handbook/engineering/infrastructure/). In particular [production architecture](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production/architecture/) might be useful for onboarding.
If you need a VPS for any reason, it’s probably easiest to set one up at DigitalOcean. Ask another developer for access.
## Basics of GitLab development[](https://handbook.gitlab.com/handbook/engineering/workflow/developer-onboarding/#basics-of-gitlab-development)
### Workflow[](https://handbook.gitlab.com/handbook/engineering/workflow/developer-onboarding/#workflow)
Please see the [engineering workflow document](https://handbook.gitlab.com/handbook/engineering/workflow/) in the handbook and read the [developer documentation](https://docs.gitlab.com/ee/development/).
### Security[](https://handbook.gitlab.com/handbook/engineering/workflow/developer-onboarding/#security)
Read the [developer security documentation](https://gitlab.com/gitlab-org/release/docs/blob/master/general/security/engineer.md) prior to working on a security issue.
### Quality[](https://handbook.gitlab.com/handbook/engineering/workflow/developer-onboarding/#quality)
One of GitLab’s strengths is its high quality of software. To achieve this we’ve introduced some requirements to all source code that is contributed. All requirements are mentioned in [the Contribution guide](https://about.gitlab.com/community/contribute/). Make sure you read and follow it.
### Dependencies[](https://handbook.gitlab.com/handbook/engineering/workflow/developer-onboarding/#dependencies)
GitLab can be installed through an Omnibus package or from source on different Linux distributions and macOS. In order to maintain portability, we need to avoid adding extra dependencies and use of exotic database extensions. Every time you choose between changes in the application code or adding new dependencies, you should give priority to the first because this is easier to maintain and set up. If you still need to bring new dependencies to GitLab, ask another developer or the CTO for advice.
### Submit your code[](https://handbook.gitlab.com/handbook/engineering/workflow/developer-onboarding/#submit-your-code)
In GitLab all code should go through a review process before it can be merged. Make sure you submit a merge request for any changes you’ve made. When the merge request is ready, it should be assigned to [someone else on the team](https://handbook.gitlab.com/handbook/engineering/workflow/code-review/). This person is then responsible for reviewing your code and merging it. Optionally, you can request another developer to help or review by writing a comment. If a merge request is not assigned, it will probably be ignored and create unnecessary delays.
Don’t work on one task for multiple days before submitting a merge request. Even the biggest task can be split into smaller tasks. Try to submit a merge request for each part of the functionality. This means that we expect multiple merge requests per week from you. Smaller merge requests are more likely to receive good feedback and will get merged sooner.
Unless the change is very minor, or is fixing a bug that was introduced in the same version, create a changelog entry using the [`Changelog` Git commit trailer](https://docs.gitlab.com/ee/development/changelog.html). Do not include your name in the entry as we only do that to give recognition to volunteer contributors.
### Working on GitLab EE (developer licenses)[](https://handbook.gitlab.com/handbook/engineering/workflow/developer-onboarding/#working-on-gitlab-ee-developer-licenses)
GitLab EE requires an active license key.
GitLab team members can follow [these instructions](https://handbook.gitlab.com/handbook/support/internal-support/#gitlab-plan-or-license-for-team-members) to acquire or renew a license.
Wider community members should contact the [Developer Relations Engineering team](https://handbook.gitlab.com/handbook/marketing/developer-relations/engineering/community-contributors-workflows/#contributing-to-the-gitlab-enterprise-edition-ee).
### Ruby Gems[](https://handbook.gitlab.com/handbook/engineering/workflow/developer-onboarding/#ruby-gems)
Follow the [development guidelines for Ruby gems](https://docs.gitlab.com/ee/development/gems.html).
## Get involved with the wider community[](https://handbook.gitlab.com/handbook/engineering/workflow/developer-onboarding/#get-involved-with-the-wider-community)
  * Become a [Merge Request Coach](https://handbook.gitlab.com/job-description-library/expert/merge-request-coach/)
  * Join the [Community Discord](https://discord.gg/gitlab)
  * Encourage teams to host [Community Office Hours](https://handbook.gitlab.com/handbook/marketing/developer-relations/engineering/community-contributors-workflows/#community-office-hours)
  * Reach out to the [Developer Relations Engineering team](https://handbook.gitlab.com/handbook/marketing/developer-relations/engineering/) on Slack in `#developer-relations-engineering`
  * Involve the community in things you do
  * Have conversations in public
  * Triage team issues and label with `quick win` where applicable, especially in advance of [Hackathons](https://about.gitlab.com/community/hackathon/)
  * Use the [Community Forks](https://gitlab.com/gitlab-community)
  * Consider [live streaming](https://handbook.gitlab.com/handbook/marketing/marketing-operations/youtube/#public-or-private-streaming) and [pairing sessions](https://handbook.gitlab.com/handbook/marketing/developer-relations/engineering/community-pairing-sessions/), with team members and/or the community
  * Record meetings for the [GitLab Unfiltered](https://www.youtube.com/channel/UCMtZ0sc1HHNtGGWZFDRTh5A) YouTube channel (handbook info [here](https://handbook.gitlab.com/handbook/marketing/marketing-operations/youtube/))
  * Champion requests from community members and raise concerns internally
  * Reach out offline to connect with community members on channels like X/Twitter or LinkedIn


## Relevant links[](https://handbook.gitlab.com/handbook/engineering/workflow/developer-onboarding/#relevant-links)
  * [Engineering Handbook](https://handbook.gitlab.com/handbook/engineering/)
  * [Engineering Workflow](https://handbook.gitlab.com/handbook/engineering/workflow/)
  * [Product Handbook](https://handbook.gitlab.com/handbook/product/)


Last modified March 4, 2026: [Rename job-families to job-description-library (`6f520606`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/6f520606)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/workflow/developer-onboarding.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/workflow/developer-onboarding.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)