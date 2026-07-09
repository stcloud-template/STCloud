# CodeBuild project has CloudWatch Logs or S3 logging enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `codebuild_project_logging_enabled` |
| 云平台 | AWS |
| 服务 | codebuild |
| 严重等级 | medium |
| 类别 | logging |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsCodeBuildProject |
| 资源组 | devops |

## 描述

**CodeBuild projects** are assessed for **logging configuration** to Amazon **CloudWatch Logs** or **S3**, identifying when at least one destination is `enabled` for build logs and events.

## 风险

Absence of **build logging** creates blind spots for **integrity** and **accountability**. Attackers or misconfigurations can alter artifacts, exfiltrate data, or misuse credentials with little trace, hindering **forensics** and **incident response**. Missing telemetry impedes correlation with other alerts, risking source code and secret **confidentiality**.

## 推荐措施

Enable a log destination for every project-**CloudWatch Logs** or **S3** (preferably both). Enforce **defense in depth**: encrypt logs, set retention, and restrict access on a least-privilege basis. Centralize and monitor logs, alert on anomalies, and avoid sensitive data in output. Use immutable retention to preserve **auditability**.

## 修复步骤


### CLI

```text
aws codebuild update-project --name <project-name> --logs-config "cloudWatchLogs={status=ENABLED}"
```

### Native IaC

```yaml
# CloudFormation: Enable logging on a CodeBuild project
Resources:
  <example_resource_name>:
    Type: AWS::CodeBuild::Project
    Properties:
      Name: <example_resource_name>
      ServiceRole: <example_resource_id>
      Artifacts:
        Type: NO_ARTIFACTS
      Environment:
        Type: LINUX_CONTAINER
        ComputeType: BUILD_GENERAL1_SMALL
        Image: aws/codebuild/standard:5.0
      Source:
        Type: NO_SOURCE
      LogsConfig:
        CloudWatchLogs:
          Status: ENABLED  # Critical: Enables CloudWatch logging to pass the check
```

### Terraform

```hcl
# Terraform: Enable logging on a CodeBuild project
resource "aws_codebuild_project" "<example_resource_name>" {
  name         = "<example_resource_name>"
  service_role = "<example_resource_id>"

  artifacts { type = "NO_ARTIFACTS" }

  environment {
    compute_type = "BUILD_GENERAL1_SMALL"
    image        = "aws/codebuild/standard:5.0"
    type         = "LINUX_CONTAINER"
  }

  source { type = "NO_SOURCE" }

  logs_config {
    cloudwatch_logs {
      status = "ENABLED"  # Critical: Enables CloudWatch logging to pass the check
    }
  }
}
```

### Other

1. In the AWS Console, go to CodeBuild > Build projects and open your project
2. Under Logs, click Edit
3. Check CloudWatch logs and save (or enable S3 logs instead)
4. Confirm the project now shows logging enabled

## 参考资料

- [https://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html#change-project-console-logs](https://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html#change-project-console-logs)
- [https://codefresh.io/learn/devops-tools/aws-codebuild-the-basics-and-a-quick-tutorial/](https://codefresh.io/learn/devops-tools/aws-codebuild-the-basics-and-a-quick-tutorial/)
- [https://asecure.cloud/a/cfgrule_codebuild-project-logging-enabled/](https://asecure.cloud/a/cfgrule_codebuild-project-logging-enabled/)
- [https://support.icompaas.com/support/solutions/articles/62000233680-ensure-that-codebuild-projects-have-s3-or-cloudwatch-logging-enabled](https://support.icompaas.com/support/solutions/articles/62000233680-ensure-that-codebuild-projects-have-s3-or-cloudwatch-logging-enabled)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html#codebuild-4](https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html#codebuild-4)

## 技术信息

- Source Metadata：[sources/aws/codebuild_project_logging_enabled/metadata.json](../../sources/aws/codebuild_project_logging_enabled/metadata.json)
- Source Code：[sources/aws/codebuild_project_logging_enabled/check.py](../../sources/aws/codebuild_project_logging_enabled/check.py)
- Source Metadata Path：`sources/aws/codebuild_project_logging_enabled/metadata.json`
- Source Code Path：`sources/aws/codebuild_project_logging_enabled/check.py`
