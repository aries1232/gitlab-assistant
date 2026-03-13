# SRE Onboarding
## Onboarding Template[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#onboarding-template)
SRE onboarding is mostly handled by two issue templates:
  1. [Machine setup](https://gitlab.com/gitlab-com/gl-infra/production-engineering/-/blob/master/.gitlab/issue_templates/onboarding-sre-machine-setup.md)
  2. [Gather context](https://gitlab.com/gitlab-com/gl-infra/production-engineering/-/blob/master/.gitlab/issue_templates/onboarding-sre-context.md)


These are assigned to the SRE when they start. This will guide them through different areas of the system, starting off with some simple tasks and help both the SRE and the SRE manager through various access issues.
There is a third issue template for [oncall onboarding](https://gitlab.com/gitlab-com/gl-infra/production-engineering/-/blob/master/.gitlab/issue_templates/onboarding-oncall.md), which should be completed after the first two and will probably take at least 3 months from the start date to complete.
## GitLab.com Infrastructure Management[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#gitlabcom-infrastructure-management)
The SRE teams use [Terraform](https://www.terraform.io/) and [Chef](https://www.chef.io/) for configuration management of GitLab.com infrastructure.
### Terraform[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#terraform)
Terraform configuration is currently divided into three environment:
  * [production](https://ops.gitlab.net/gitlab-com/gl-infra/config-mgmt/-/tree/master/environments/gprd)
  * [staging](https://ops.gitlab.net/gitlab-com/gl-infra/config-mgmt/-/tree/master/environments/gstg)
  * [ops](https://ops.gitlab.net/gitlab-com/gl-infra/config-mgmt/-/tree/master/environments/ops)


There is [shared terraform config](https://ops.gitlab.net/gitlab-com/gl-infra/config-mgmt/-/blob/master/environments/ops/shared-configurations.tf) for both staging and production to keep topology parity between these environments. Instance sizing, fleet sizes and other environment specific configuration is set in variable files for staging, production and ops.
The state for terraform is maintained in object storage, the master branch should always represent the current state of infrastructure. Changes should be merged and applied through CI.
### Chef[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#chef)
Chef is a critical part of SRE infrastructure management. Currently it is used for OS patching, applying system level configuration and installing the omnibus package for releases. Here are a few notable cookbooks which will be a good starting-point for new SREs:
  * [cookbook-omnibus-gitlab](https://gitlab.com/gitlab-cookbooks/cookbook-omnibus-gitlab): This cookbook is responsible for creating a `gitlab.rb` on every server that has GitLab installed. This config file is used by the omnibus package.
  * [gitlab-cookbooks](https://gitlab.com/gitlab-cookbooks): This is a collection of cookbooks that are used for GitLab.com.


### Releases[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#releases)
Releases candidates are deployed to GitLab.com through auto-deployments that occur throughout the week. For information about how releases at GitLab.com read about [the releases process](https://handbook.gitlab.com/handbook/engineering/deployments-and-releases/deployments/#gitlabcom-deployments-process) visit the [release project documentation](https://gitlab.com/gitlab-org/release/docs/blob/master/README.md). documentation.
For information about GitLab.com deployments and patches see the following release docs:
  * [release documentation for deployer](https://gitlab.com/gitlab-org/release/docs/blob/master/general/deploy/gitlab-com-deployer.md)
  * [post-deployment patch documentation](https://gitlab.com/gitlab-org/release/docs/blob/master/general/deploy/post-deployment-patches.md)


## Where to find things[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#where-to-find-things)
### Repositories[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#repositories)
The following repositories are used for GitLab.com infrastructure management. These repository locations are the remotes that the SRE team uses for pushes, issues and MRs. Mirrors are setup in case that GitLab.com is unavailable. Repositories that are necessary for assets, configuration, infrastructure, releases and patch management use <https://ops.gitLab.net> as a remote.
  1. [terraform](https://ops.gitlab.net/gitlab-com/gl-infra/config-mgmt): This is the repository that holds all terraform configuration for the GitLab.com staging, production and operations environments. There is a [repository mirror](https://gitlab.com/gitlab-com/gl-infra/config-mgmt) on GitLab.com .
  2. [chef cookbooks](https://gitlab.com/groups/gitlab-cookbooks): These repositories are the cookbooks used for GitLab.com. Runlists for the fleets are configured in roles. There are repository mirrors for these cookbooks on [ops.gitLab.com](https://ops.gitlab.net/gitlab-cookbooks).
  3. [chef](https://gitlab.com/gitlab-com/gl-infra/chef-repo): This repository contains all role and node attributes for GitLab.com infrastructure. It also has the environment configurations for production, staging and ops for cookbook version pinning.
  4. [runbooks](https://gitlab.com/gitlab-com/runbooks/): This repository contains runbooks, howtos and alert definitions for GitLab.com. Alerts defined in this repository are automatically applied to the monitoring infrastructure when merged to master. For more information see the [alert section](https://gitlab.com/gitlab-com/runbooks/-/tree/master#alerts). There is a [repository mirror](https://ops.gitlab.net/gitlab-com/runbooks/) on ops.GitLab.net.


### Dashboards[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#dashboards)
It is useful to have the following dashboards bookmarked and easily accessible
  1. [Grafana](https://dashboards.gitlab.net/d/RZmbBr7mk/gitlab-triage)
  2. [Google Cloud](https://console.cloud.google.com/home/dashboard?project=gitlab-production&pli=1)
  3. [System Logs](https://log.gprd.gitlab.net/app/kibana)
  4. [Fastly](https://manage.fastly.com/dashboard/services/652MHuIME217ZATbh7vFWC/datacenters/all) CDN


### Cloud Providers[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#cloud-providers)
  1. [Google Cloud](https://console.cloud.google.com/home/dashboard?project=gitlab-production&pli=1)
  2. [Amazon Web Services](https://console.aws.amazon.com/console/home?region=us-east-1)


### Monitoring tools[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#monitoring-tools)
  1. [incident.io](https://app.incident.io/gitlab/dashboard) Alerting
  2. [Grafana](https://dashboards.gitlab.net/d/bd2Kl9Imk/host-stats?orgId=1) Performance Monitoring
  3. [Alert Dashboard](https://dashboards.gitlab.net/d/SOn6MeNmk/alerts)


### Issue Trackers[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#issue-trackers)
It is useful to have the following issue trackers bookmarked and easily accessible
  1. [On Call Issues](https://gitlab.com/gitlab-com/gl-infra/production-engineering/-/issues/?sort=closed_at_desc&state=opened&label_name%5B%5D=oncall)
  2. [Production Incidents Issues](https://gitlab.com/gitlab-com/gl-infra/production/issues?label_name%5B%5D=incident)
  3. [Change Management Issues](https://gitlab.com/gitlab-com/gl-infra/production/issues?label_name%5B%5D=change)


### Yubikey[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#yubikey)
SREs should be using a [YubiKey](https://www.yubico.com) and should not have keys on their laptop. It is recommended to have a spare YubiKey to avoid being locked out of your accounts if you lose your primary key.
Follow the [yubikey runbook](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/uncategorized/yubikey.md) to set up
## Credentials[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#credentials)
The following is intended to be a comprehensive list of credentials and access that need to be set up, which are not covered above or elsewhere in the handbook. The list may not be up to date. If something is missing, please add it.
  1. SSH Key - this is provided to you by the yubikey setup
  2. [GitLab.com](https://gitlab.com) account
  3. [GitLab.com](https://gitlab.com) admin account
  4. [dev.GitLab.org](https://dev.gitlab.org) account
  5. [ops.GitLab.net](https://ops.gitlab.net) account
  6. Chef access
  7. Cloud Providers
     * Amazon Web Services
     * Azure
     * Digital Ocean
     * Google Cloud


## Slack Channels[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#slack-channels)
  * Oncall-related channels: 
    * `production`
    * `incident-management`
    * `alerts`
    * `announcements`
    * `dev-escalation`
    * `feed_alerts-general`
    * `cloud-provider-alerts`
  * Infrastructure channels: 
    * `infrastructure-lounge`
    * `infra-read-feed`
    * `g_release_and_deploy`
    * `infra_capacity-planning`
    * `ansible`
    * `kubernetes`
    * `terraform`


## Zendesk[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#zendesk)
Every SRE should register for a “Light Agent” account in ZenDesk. Often times incidents are generated from customer reports, and it’s useful to see their submission and the back and forth with support. You can also leave internal notes for support engineers so that they can gather more information for troubleshooting purposes.
## Time Off by Deel[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#time-off-by-deel)
We use Time Off by Deel to notify and delegate for planned timeoff. When setting up your integrations with Slack, be sure to run the `/time-off-deel help` command then click _Go to Home Tab_ then in the drop-down select _Calendar Sync_ then _Add Calendar_ to add the team’s shared Google Calendar (ID: `gitlab.com_oji6dki1frc8g8qq9feuu1jtd0@group.calendar.google.com`) as an “Additional calendars to include?”.
## Suggested Software Tools[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#suggested-software-tools)
As production engineers we are allowed to utilize a linux workstation. The list below is mostly comprised of macOS tools. You’ll need to find the linux equivalent to match the linux distro of your choice.
In addition to the standard tools for interacting with the rest of GitLab, the following tools help when working on production issues.
Required tools
  1. [Homebrew](https://brew.sh)
  2. [SSH, properly configured](https://gitlab.com/gitlab-com/gl-infra/infrastructure/blob/master/onboarding/ssh-config)
  3. [chef, knife, berkshelf](https://docs.chef.io/workstation/install_workstation/)
  4. kubectl (`brew install kubernetes-cli`)


Nice to have
  1. iTerm (`brew install iterm2`) or kitty (`brew install kitty`) (bear in mind that kitty requires more configuration to get it up and running so it’s targeted at more advanced users)
  2. macOS doesn’t source ~/.bashrc file by default, so if you want it to be processed, you need to source it in your profile file (which you might need to create manually). Why to create the rc file at all instead of keeping everything in the profile? some tools default to rc so they will not process the profile at all. There are actually more differences, see: [About bash_profile and bashrc on macOS](https://scriptingosx.com/2017/04/about-bash_profile-and-bashrc-on-macos/)
  3. macOS doesn’t have bash completion feature by default, to install it: `brew install bash-completion` and enable it: `echo "[ -f /usr/local/etc/bash_completion ] && . /usr/local/etc/bash_completion" >> ~/.bashrc`
  4. fzf used for fuzzy completion in shell, e.g. history search or filepaths, (`brew install fzf` + `echo "[ -f ~/.fzf.bash ] && source ~/.fzf.bash" >> ~/.bashrc`)
  5. the default length of bash history on macOS is 500, to extend the number of entries kept and save the timestamp you can add to your .bashrc for example:


```

export HISTFILESIZE=2000000
export HISTSIZE=1000000
export HISTTIMEFORMAT="%d/%m/%y %T "

```

  1. helm - “Kubernetes package manager” (`brew install kubernetes-helm`)
  2. minikube (`brew install minikube`) and virtualbox (`https://www.virtualbox.org/wiki/Downloads`)
  3. GCP cli [gcloud quickstart macos](https://cloud.google.com/sdk/docs/quickstart-macos)
  4. Digital Ocean cli (`brew install doctl`)
  5. Azure cli (`brew install azure-cli`)
  6. AWS cli (`pip3 install awscli --upgrade`)
  7. A text editor such as [Sublime](https://www.sublimetext.com/), [Textmate](https://macromates.com), [MacVim](https://macvim.org/), or [neovim](https://neovim.io)
  8. watch (`brew install watch`)
  9. tmux/tmate (`brew install tmux tmate`)
  10. A markdown editor such as [macdown](https://macdown.uranusjr.com) (`brew install macdown`)
  11. [BitBar](https://github.com/matryer/xbar) with [GitLab Plugin](https://gitlab.com/devin/gitlab-bitbar)
  12. To [install gnu utils and replace mac utilities](https://apple.stackexchange.com/questions/69223/how-to-replace-mac-os-x-utilities-with-gnu-core-utilities) use the –with-default-names option.
  13. when using gpg, you will be asked for a password. Querying for passwords can be facilitated by different tools, but a fairly standard and widely supported one is pinentry-mac (`brew install pinentry-mac`). To tell your gpg agent to use it: `echo 'pinentry-program /usr/local/bin/pinentry-mac' >> ~/.gnupg/gpg-agent.conf`


### Brew Files[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#brew-files)
There are sample brew files in the [Infrastructure Project](https://gitlab.com/gitlab-com/gl-infra/infrastructure/tree/master/onboarding)
### iOS apps[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#ios-apps)
  1. [Slack](https://apps.apple.com/us/app/slack/id618783545)
  2. [Zoom](https://apps.apple.com/us/app/zoom-workplace/id546505307)
  3. [incident.io](https://apps.apple.com/ca/app/incident-io/id6471268530)
  4. [Working Copy](https://apps.apple.com/us/app/working-copy-git-client/id896694807) (Optional)


## Reference Material[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding/#reference-material)
List of relevant reference material that an engineer may need to brush up on
  1. [Chef](https://docs.chef.io)
  2. [Terraform Docs](https://developer.hashicorp.com/terraform/docs) or [getting started guide](https://developer.hashicorp.com/terraform/intro)


Last modified January 14, 2026: [Remove archived Slack channels from SRE Onboarding page (`84897299`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/84897299)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/infrastructure-platforms/production-engineering/networking-and-incident-management/sre-onboarding.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)