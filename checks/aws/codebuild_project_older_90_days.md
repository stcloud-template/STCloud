# CodeBuild project has been invoked in the last 90 days

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `codebuild_project_older_90_days` |
| 云平台 | AWS |
| 服务 | codebuild |
| 严重等级 | medium |
| 类别 | ci-cd |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | AwsCodeBuildProject |
| 资源组 | devops |

## 描述

**AWS CodeBuild projects** are assessed for recent activity using the last build invocation timestamp. Projects not invoked within `90 days` or never built are treated as **inactive**.

## 风险

**Inactive projects** increase **attack surface**. Dormant webhooks or **source credentials** can be abused, and attached **IAM roles** may retain excessive permissions. Stale configs can expose **secrets** in env vars or logs, threatening build **integrity** and data **confidentiality**, while adding avoidable cost and operational sprawl.

## 推荐措施

Implement lifecycle management: review projects idle over `90 days`, confirm ownership and need, then delete or archive. Revoke unused webhooks, tokens, and service roles; rotate any secrets. Enforce **least privilege**, tagging, and periodic audits to reduce **attack surface** and keep the build environment tidy and defensible.

## 修复步骤


### Other

1. Open the AWS Console and go to CodeBuild
2. In Build projects, select the project
3. Click Start build, then confirm Start build
4. Wait for the build to start to update the last invoked time

## 参考资料

- [https://docs.aws.amazon.com/codebuild/latest/userguide/delete-project.html](https://docs.aws.amazon.com/codebuild/latest/userguide/delete-project.html)
- [https://support.icompaas.com/support/solutions/articles/62000233684-ensure-codebuild-project-has-been-invoked-in-the-last-90-days](https://support.icompaas.com/support/solutions/articles/62000233684-ensure-codebuild-project-has-been-invoked-in-the-last-90-days)

## 技术信息

- Source Metadata：[sources/aws/codebuild_project_older_90_days/metadata.json](../../sources/aws/codebuild_project_older_90_days/metadata.json)
- Source Code：[sources/aws/codebuild_project_older_90_days/check.py](../../sources/aws/codebuild_project_older_90_days/check.py)
- Source Metadata Path：`sources/aws/codebuild_project_older_90_days/metadata.json`
- Source Code Path：`sources/aws/codebuild_project_older_90_days/check.py`
