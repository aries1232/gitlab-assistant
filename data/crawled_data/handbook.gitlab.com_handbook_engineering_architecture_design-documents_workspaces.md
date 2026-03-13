# Workspaces
This page contains information related to upcoming products, features, and functionality. It is important to note that the information presented is for informational purposes only. Please do not rely on this information for purchasing or planning purposes. The development, release, and timing of any products, features, or functionality may be subject to change or delay and remain at the sole discretion of GitLab Inc. 
Status | Authors | Coach | DRIs | Owning Stage | Created  
---|---|---|---|---|---  
ongoing |  `vtak[](https://gitlab.com/vtak)` |  `grzesiek[](https://gitlab.com/grzesiek)` |  `michelle-chen[](https://gitlab.com/michelle-chen)` `adebayo_a[](https://gitlab.com/adebayo_a)` |  devops create |  2022-11-15   
## Introduction[](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/#introduction)
A common obstacle faced by developers when first contributing to a project is the setup of their local development environment. The time-consuming process of managing interrelated dependencies and fixing version compatibility issues can be demotivating, especially for those who only contribute occasionally or switch between multiple projects frequently. In complicated environments, development teams may also impose restrictions, authentication credentials, build procedures, and standards that add to the fragile nature of the development environment.
At the end of the day, developers want to spend less time managing their development environment and more time contributing high-quality code. And at GitLab, our mission is to ensure everyone can contribute. With Workspaces, our goal is to eliminate the responsibility of configuring and maintaining a local development environment.
## Objectives[](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/#objectives)
See our [Workspaces direction page](https://about.gitlab.com/direction/create/remote_development/workspaces/) for more information.
## Glossary[](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/#glossary)
  1. **GitLab VS Code fork** : An internal fork of the VSCode project.
  2. **Web IDE** : An IDE built on top of GitLab VS Code fork by adding GitLab context. This IDE runs purely in the browser.
  3. **GitLab VS Code fork for Workspaces** : An IDE built on top of GitLab VS Code fork by applying patches making it suitable to use in Workspaces. This IDE runs a server and an optional client which is used to connect remotely.
  4. **GitLab Workflow extension** : An extension which adds GitLab features to VS Code.
  5. **GitLab Agent for Kubernetes(agentk)** : A component for solving any GitLab<->Kubernetes integration tasks.
  6. **GitLab Agent for Workspaces(agentw)** : A component for solving any GitLab<->Workspace integration tasks.
  7. **GitLab Agent Server(KAS)** : A server running alongside GitLab Rails application to facilitate connections between different GitLab Agents(agentk, agentw) and GitLab and vice versa.


## Overview[](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/#overview)
Each workspace is run as a group of user provided containers in a Pod in Kubernetes through an integration with GitLab Agent for Kubernetes(agentk). We inject an IDE(e.g. GitLab VS Code fork for Workspaces) in each Pod. We aim to be IDE agnostic. The workspace can either be accessed through GitLab Workspaces Proxy deployed in the user’s Kubernetes cluster or through the bi-directional gRPC tunnel established by the GitLab Agent for Workspaces(agentw) injected in the workspace.
## Architecture[](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/#architecture)
See [Architecture for Kubernetes setup](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/architecture_kubernetes_setup/) for detailed implementation details.
## Decisions[](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/#decisions)
  1. [001: Configuration format to use](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/decisions/001_configuration_format_to_use/)
  2. [002: Provision compute and storage for a workspace](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/decisions/002_provision_compute_and_storage/)
  3. [003: Authorizing user to create and access a workspace](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/decisions/003_authorizing_user_to_create_and_access_workspace/)
  4. [004: Authentication of user traffic to access a workspace](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/decisions/004_authentication_of_user_traffic_to_access_workspace/)
  5. [005: Explicitly define the user/group ID of the containers at runtime](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/decisions/005_explicitly_set_user_group_id_of_containers/)
  6. [006: Automatic termination of a workspace](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/decisions/006_automatic_termination_of_workspace/)
  7. [007: Create workspaces from private projects](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/decisions/007_create_workspace_from_private_projects/)
  8. [008: Use SSH to access non-HTTP services running in a workspace](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/decisions/008_use_ssh_to_access_non_http_services/)
  9. [009: Allow mapping of GitLab Agent for Kubernetes(agentk) to groups](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/decisions/009_allow_mapping_of_agentk_to_groups/)
  10. [010: Extensions marketplace for GitLab VS Code fork for Workspaces](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/decisions/010_extensions_marketplace_for_vscode/)
  11. [011: Integrate GitLab Duo features inside a workspace](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/decisions/011_integrate_duo_features_inside_workspace/)
  12. [012: Automatic suspension of a workspace](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/decisions/012_automatic_suspension_of_workspace/)
  13. [013: Create workspaces from private container images](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/decisions/013_create_workspace_from_private_container/)
  14. [014: Default container image and configuration for Workspaces](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/decisions/014_default_container_image_and_configuration/)
  15. [015: Allow mapping of GitLab Agent for Kubernetes(agentk) to GitLab Cluster](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/decisions/015_allow_mapping_of_agentk_to_gitlab_cluster/)
  16. [016: Allow users to run sudo commands inside a workspace](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/decisions/016_allow_users_to_run_sudo_commands/)
  17. [017: Allow users to build and run containers inside a workspace](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/decisions/017_allow_users_to_build_and_run_containers/)
  18. [018: Remove GitLab Workspaces Proxy to simplify setup](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/decisions/018_remove_gitlab_workspaces_setup/)


## Helpful Links[](https://handbook.gitlab.com/handbook/engineering/architecture/design-documents/workspaces/#helpful-links)
  * [Workspaces direction](https://about.gitlab.com/direction/create/remote_development/workspaces/)
  * [Workspaces | Category Strategy epic](https://gitlab.com/groups/gitlab-org/-/epics/7419)
  * [Workspaces | Market analysis](https://gitlab.com/groups/gitlab-org/-/epics/8131)
  * [Create Remote Development Group YouTube playlist](https://www.youtube.com/playlist?list=PL05JrBw4t0KrRQhnSYRNh1s1mEUypx67-)


Last modified April 30, 2025: [Fix typo "feliciate" to faciliatte (`ba4ae07b`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/ba4ae07b)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/architecture/design-documents/workspaces/_index.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/architecture/design-documents/workspaces/_index.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)