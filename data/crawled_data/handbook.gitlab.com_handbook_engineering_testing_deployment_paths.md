# Deployment Workflow
## GitLab Deployment Workflow[](https://handbook.gitlab.com/handbook/engineering/testing/deployment_paths/#gitlab-deployment-workflow)
The following diagram illustrates the complete deployment workflow from developer commit to production deployment on GitLab.com and self-managed releases.
```

Documentation Updates
Self-Managed Release Path
GitLab.com Deployment Path
Developer Workflow
Parallel
Developer commits to feature branch
Create Merge Request
CI/CD Pipeline runs
Code Review & Approval
Merge to default branch
Deployer Pipeline Triggered
Deploy to Staging Canary  
gstg-cny
Deploy to Staging Ref  
gstg-ref  
Sandbox Testing
E2E Smoke Tests  
targeting gstg-cny (blocking)
Deploy to Production Canary  
gprd-cny
E2E Smoke Tests  
targeting gprd-cny (blocking)
Wait Period  
30 minutes
Manual Promotion
Deploy to Staging  
gstg
Production Checks
Deploy to Production  
gprd
Live on GitLab.com
Merged to default branch
Monthly release cycle  
3rd Thursday of month
Create stable branch  
e.g., 17-2-stable-ee
Tag version  
e.g., v17.2.0
Build release packages  
Omnibus, Docker, etc.
Publish to packages.gitlab.com
Available for Self-Managed  
installations
Patch releases  
Twice monthly
Tag patch version  
e.g., v17.2.1
Docs updated on main
Deployed to docs.gitlab.com  
within 1 hour
Stable branch docs  
e.g., docs.gitlab.com/17.2/

```

## Post-Deployment Migrations[](https://handbook.gitlab.com/handbook/engineering/testing/deployment_paths/#post-deployment-migrations)
Post-deployment migrations have their own dedicated workflow and are not guaranteed to run within a specific timeframe. The deployment team reserves the right to run them when deemed necessary. However, they are always executed prior to release management tasks.
For more details, see the [Post-Deploy Migration (PDM) Execution](https://handbook.gitlab.com/handbook/engineering/deployments-and-releases/deployments/#post-deploy-migration-pdm-execution) section in the deployments handbook.
## Related Documentation[](https://handbook.gitlab.com/handbook/engineering/testing/deployment_paths/#related-documentation)
For additional context on the deployment process, refer to the [Deploying Packages](https://handbook.gitlab.com/handbook/engineering/deployments-and-releases/deployments/#deploying-packages) section in the deployments and releases handbook.
Last modified December 15, 2025: [Add deployment paths documentation (`56a49071`)](https://gitlab.com/gitlab-com/content-sites/handbook/commit/56a49071)
[ ](https://gitlab.com/gitlab-com/content-sites/handbook/blob/main/content/handbook/engineering/testing/deployment_paths.md) - [ ](https://gitlab.com/-/ide/project/gitlab-com/content-sites/handbook/edit/main/-/content/handbook/engineering/testing/deployment_paths.md) - please [contribute](https://handbook.gitlab.com/handbook/about/contributing/). [ ![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](https://creativecommons.org/licenses/by-sa/4.0/)