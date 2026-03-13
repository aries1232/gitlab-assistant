# Release Tools
Guide to GitLab’s tools for new releases
## Introduction[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/release-tools/#introduction)
[Release Tools](https://gitlab.com/gitlab-org/release-tools/) is a project maintained by the [Delivery team](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/gitlab-delivery/delivery/), and used by Release Managers to perform releases of GitLab and its components. Release Tools works by running CI pipelines for specific purposes, such as tagging a new release or notifying merge requests about deployments. Some of these pipelines are triggered automatically (e.g. as part of a deploy), while others are triggered by users (e.g. using a chatops command).
## Common Links[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/release-tools/#common-links)
| **GitLab.com project** | <https://gitlab.com/gitlab-org/release-tools> | | **ops.gitlab.net mirror** | <https://ops.gitlab.net/gitlab-org/release/tools> | | **Developer documentation** | <https://gitlab.com/gitlab-org/release-tools/-/tree/master/doc> |
## High-level overview of the release process[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/release-tools/#high-level-overview-of-the-release-process)
When Release Tools performs a release, it will roughly perform the following steps:
  1. Update one or more version files, such as the `VERSION` file in GitLab
  2. Update any additional files, such as Helm chart files
  3. Generate a changelog
  4. Commit the changes
  5. Create an annotated tag for these changes
  6. Push all this to the appropriate project


The exact steps vary a bit between projects. For example, for Gitaly release we also need to update some files in GitLab so it uses the correct Gitaly version.
## Using Release Tools[](https://handbook.gitlab.com/handbook/engineering/infrastructure-platforms/release-tools/#using-release-tools)
Release Tools is only to be used by active Release Managers, and members of the Delivery team for testing purposes (e.g. when testing new functionality). Using Release Tools is primarily done through chatops and Slack. For example, to tag a self-managed release you’d run:
```

/chatops run release tag 42.0.0

```

This would then start the release tagging process of GitLab version 42.0.0.
For more information, refer to the [release/docs project](https://gitlab.com/gitlab-org/release/docs/) project.
Last modified June 19, 2025: [Move more pages from infrastructure to infrastructure-plaforms (`9026ac0b`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/9026ac0b)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/infrastructure-platforms/release-tools.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/infrastructure-platforms/release-tools.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)