# CodeBuild project source repository URLs do not contain sensitive credentials

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `codebuild_project_source_repo_url_no_sensitive_credentials` |
| 云平台 | AWS |
| 服务 | codebuild |
| 严重等级 | critical |
| 类别 | secrets |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Sensitive Data Identifications/Passwords, Sensitive Data Identifications/Security, Effects/Data Exposure |
| 资源类型 | AwsCodeBuildProject |
| 资源组 | devops |

## 描述

**AWS CodeBuild projects** with **Bitbucket sources** are assessed to confirm repository URLs do not embed credentials (for example, `x-token-auth:<token>@` or `user:password@`). The assessment includes both the primary source and all secondary sources.

## 风险

Credentials in URLs are **plainly exposed** in configs and logs, enabling unauthorized repo access. This can lead to: - **Source code theft** (C) - **Malicious commits/CI changes** (I) - **Supply-chain compromise** and lateral movement via token reuse

## 推荐措施

Use **OAuth/CodeStar Connections** or store tokens in **Secrets Manager/SSM**, never in the URL. Enforce **least privilege**, scope to needed repos, set short lifetimes, and rotate regularly. Audit configs and logs to remove leaked secrets. *Apply to primary and secondary sources.*

## 修复步骤


### Native IaC

```yaml
Resources:
  <example_resource_name>:
    Type: AWS::CodeBuild::Project
    Properties:
      Name: <example_resource_name>
      ServiceRole: <example_role_arn>
      Artifacts:
        Type: NO_ARTIFACTS
      Environment:
        Type: LINUX_CONTAINER
        Image: aws/codebuild/standard:5.0
        ComputeType: BUILD_GENERAL1_SMALL
      Source:
        Type: BITBUCKET
        Location: https://bitbucket.org/<example_owner>/<example_repo>.git  # FIX: remove embedded credentials; keep only the repo URL
        # This removes tokens/user:pass from the URL, eliminating exposed secrets
```

### Terraform

```hcl
resource "aws_codebuild_project" "<example_resource_name>" {
  name         = "<example_resource_name>"
  service_role = "<example_role_arn>"

  artifacts {
    type = "NO_ARTIFACTS"
  }

  environment {
    compute_type = "BUILD_GENERAL1_SMALL"
    image        = "aws/codebuild/standard:5.0"
    type         = "LINUX_CONTAINER"
  }

  source {
    type     = "BITBUCKET"
    location = "https://bitbucket.org/<example_owner>/<example_repo>.git" # FIX: sanitized URL without credentials
    # Removing credentials from the URL prevents sensitive data exposure
  }
}
```

### Other

1. In the AWS Console, go to CodeBuild and open your project
2. Click Edit > Source
3. Replace the repository URL with only the Bitbucket path (no credentials):
   - https://bitbucket.org/<workspace>/<repo>.git
4. If prompted for access, choose Connect using OAuth and authorize Bitbucket
5. Save changes
6. If you use Secondary sources, edit each one and remove any embedded credentials from their URLs

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html#codebuild-1](https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html#codebuild-1)
- [https://docs.aws.amazon.com/config/latest/developerguide/codebuild-project-source-repo-url-check.html](https://docs.aws.amazon.com/config/latest/developerguide/codebuild-project-source-repo-url-check.html)

## 技术信息

- Source Metadata：[sources/aws/codebuild_project_source_repo_url_no_sensitive_credentials/metadata.json](../../sources/aws/codebuild_project_source_repo_url_no_sensitive_credentials/metadata.json)
- Source Code：[sources/aws/codebuild_project_source_repo_url_no_sensitive_credentials/check.py](../../sources/aws/codebuild_project_source_repo_url_no_sensitive_credentials/check.py)
- Source Metadata Path：`sources/aws/codebuild_project_source_repo_url_no_sensitive_credentials/metadata.json`
- Source Code Path：`sources/aws/codebuild_project_source_repo_url_no_sensitive_credentials/check.py`
