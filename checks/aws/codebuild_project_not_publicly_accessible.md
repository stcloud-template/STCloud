# CodeBuild project visibility is private

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `codebuild_project_not_publicly_accessible` |
| 云平台 | AWS |
| 服务 | codebuild |
| 严重等级 | high |
| 类别 | internet-exposed, ci-cd |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Effects/Data Exposure |
| 资源类型 | AwsCodeBuildProject |
| 资源组 | devops |

## 描述

**AWS CodeBuild project visibility** is assessed to identify projects exposed to the public. Projects with `project_visibility` set to `PUBLIC_READ` (or not `PRIVATE`) allow anyone to access build results, logs, and artifacts.

## 风险

Public visibility degrades CIA: - Logs may leak secrets, tokens, and source details - Artifacts are downloadable, enabling tampering and supply-chain malware - Adversaries gain CI/CD insights for reconnaissance and lateral movement

## 推荐措施

Set visibility to `PRIVATE` and share only with trusted principals using narrowly scoped policies. Apply **least privilege** to logs and artifacts, keeping them private. Manage secrets via **Secrets Manager** or **Parameter Store**, avoid printing them, and validate artifacts (e.g., checksums).

## 修复步骤


### CLI

```text
aws codebuild update-project-visibility --project-arn <PROJECT_ARN> --project-visibility PRIVATE
```

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
        Type: NO_SOURCE
      Visibility: PRIVATE  # Critical: makes the project private so builds aren't publicly accessible
```

### Terraform

```hcl
resource "aws_codebuild_project" "<example_resource_name>" {
  name         = "<example_resource_name>"
  service_role = "<example_role_arn>"

  artifacts { type = "NO_ARTIFACTS" }

  environment {
    compute_type = "BUILD_GENERAL1_SMALL"
    image        = "aws/codebuild/standard:5.0"
    type         = "LINUX_CONTAINER"
  }

  source { type = "NO_SOURCE" }

  project_visibility = "PRIVATE" # Critical: ensures the project is not publicly accessible
}
```

### Other

1. Open the AWS Console and go to CodeBuild
2. Select your build project
3. Click Edit
4. Set Project visibility to Private
5. Save changes

## 参考资料

- [https://docs.aws.amazon.com/codebuild/latest/userguide/public-builds.html](https://docs.aws.amazon.com/codebuild/latest/userguide/public-builds.html)
- [https://docs.aws.amazon.com/cli/latest/reference/codebuild/update-project-visibility.html](https://docs.aws.amazon.com/cli/latest/reference/codebuild/update-project-visibility.html)

## 技术信息

- Source Metadata：[sources/aws/codebuild_project_not_publicly_accessible/metadata.json](../../sources/aws/codebuild_project_not_publicly_accessible/metadata.json)
- Source Code：[sources/aws/codebuild_project_not_publicly_accessible/check.py](../../sources/aws/codebuild_project_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/aws/codebuild_project_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/aws/codebuild_project_not_publicly_accessible/check.py`
