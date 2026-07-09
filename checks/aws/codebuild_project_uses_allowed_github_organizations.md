# CodeBuild project using GitHub uses an allowed GitHub organization

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `codebuild_project_uses_allowed_github_organizations` |
| 云平台 | AWS |
| 服务 | codebuild |
| 严重等级 | high |
| 类别 | software-supply-chain, ci-cd |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices |
| 资源类型 | AwsCodeBuildProject |
| 资源组 | devops |

## 描述

**CodeBuild projects** sourcing from **GitHub/GitHub Enterprise** with a service role that trusts CodeBuild are evaluated by deriving the repository's organization from its URL and comparing it to an **allowed organizations** list.

## 风险

Using repos from **untrusted GitHub orgs** can let external workflows assume the project role and obtain AWS credentials. - Confidentiality: data/secrets exfiltration - Integrity: unauthorized changes - Availability: build abuse or service disruption

## 推荐措施

Limit sources to **approved GitHub organizations** via an explicit allowlist. Enforce **least privilege** on the CodeBuild service role and avoid admin rights. Apply **separation of duties** for allowlist changes and add **defense in depth** (branch protections, reviews, monitoring) to prevent workflow abuse.

## 修复步骤


### CLI

```text
aws codebuild update-project --name <example_resource_name> --source type=GITHUB,location=https://github.com/<ALLOWED_GITHUB_ORG>/<REPO>
```

### Native IaC

```yaml
# CloudFormation: point CodeBuild project to a repo in an allowed GitHub org
Resources:
  <example_resource_name>:
    Type: AWS::CodeBuild::Project
    Properties:
      ServiceRole: <example_resource_arn>
      Artifacts:
        Type: NO_ARTIFACTS
      Environment:
        Type: LINUX_CONTAINER
        ComputeType: BUILD_GENERAL1_SMALL
        Image: aws/codebuild/standard:7.0
      Source:
        Type: GITHUB
        Location: https://github.com/<ALLOWED_GITHUB_ORG>/<REPO>  # FIX: repo org must be in the allowed list
```

### Terraform

```hcl
# Terraform: set CodeBuild source to a repo under an allowed GitHub org
resource "aws_codebuild_project" "<example_resource_name>" {
  name         = "<example_resource_name>"
  service_role = "<example_resource_arn>"

  artifacts { type = "NO_ARTIFACTS" }

  environment {
    compute_type = "BUILD_GENERAL1_SMALL"
    image        = "aws/codebuild/standard:7.0"
    type         = "LINUX_CONTAINER"
  }

  source {
    type     = "GITHUB"
    location = "https://github.com/<ALLOWED_GITHUB_ORG>/<REPO>" # FIX: use an allowed GitHub org
  }
}
```

### Other

1. Open the AWS Console and go to CodeBuild > Build projects
2. Select the project and click Edit
3. In Source, set Repository URL to https://github.com/<ALLOWED_GITHUB_ORG>/<REPO>
4. Click Update to save

## 参考资料

- [https://medium.com/@adan.alvarez/gaining-long-term-aws-access-with-codebuild-and-github-873324638784](https://medium.com/@adan.alvarez/gaining-long-term-aws-access-with-codebuild-and-github-873324638784)
- [https://paul-hands-phd.medium.com/using-aws-codebuild-to-set-up-github-continuous-integration-19b92efbd094](https://paul-hands-phd.medium.com/using-aws-codebuild-to-set-up-github-continuous-integration-19b92efbd094)
- [https://docs.aws.amazon.com/codebuild/latest/userguide/connections-github-app.html](https://docs.aws.amazon.com/codebuild/latest/userguide/connections-github-app.html)
- [https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html)

## 技术信息

- Source Metadata：[sources/aws/codebuild_project_uses_allowed_github_organizations/metadata.json](../../sources/aws/codebuild_project_uses_allowed_github_organizations/metadata.json)
- Source Code：[sources/aws/codebuild_project_uses_allowed_github_organizations/check.py](../../sources/aws/codebuild_project_uses_allowed_github_organizations/check.py)
- Source Metadata Path：`sources/aws/codebuild_project_uses_allowed_github_organizations/metadata.json`
- Source Code Path：`sources/aws/codebuild_project_uses_allowed_github_organizations/check.py`
