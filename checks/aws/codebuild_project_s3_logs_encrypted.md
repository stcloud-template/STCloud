# CodeBuild project S3 logs are encrypted at rest

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `codebuild_project_s3_logs_encrypted` |
| クラウドプラットフォーム | AWS |
| サービス | codebuild |
| 重大度 | low |
| カテゴリ | encryption, logging |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| リソースタイプ | AwsCodeBuildProject |
| リソースグループ | devops |

## 説明

**CodeBuild projects** with **S3 log delivery** are evaluated for **encryption at rest** on their S3 log objects. Only projects that write logs to S3 are in scope.

## リスク

Unencrypted build logs jeopardize **confidentiality**. Logs can include secrets, environment data, and error traces. If the bucket is misconfigured or storage is accessed, attackers can harvest credentials and map the pipeline, enabling **lateral movement** and build tampering that impacts **integrity**.

## 推奨事項

Enable encryption at rest for S3 logs on CodeBuild projects. Prefer `SSE-KMS` with customer-managed keys to control access and rotation. Enforce encryption via bucket policy, apply **least privilege** to log access, and monitor access patterns. *If needed*, segregate logs and keep them private.

## 修正手順


### CLI

```text
aws codebuild update-project --name <project-name> --logs-config s3Logs={status=ENABLED,location=<bucket-name>/<path>,encryptionDisabled=false}
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
        ComputeType: BUILD_GENERAL1_SMALL
        Image: aws/codebuild/amazonlinux2-x86_64-standard:5.0
      Source:
        Type: NO_SOURCE
      LogsConfig:
        S3Logs:
          Status: ENABLED
          Location: <bucket-name>/<path>
          EncryptionDisabled: false  # Critical: ensures S3 logs are encrypted at rest
```

### Terraform

```hcl
resource "aws_codebuild_project" "<example_resource_name>" {
  name         = "<example_resource_name>"
  service_role = "<example_role_arn>"

  artifacts { type = "NO_ARTIFACTS" }

  environment {
    compute_type = "BUILD_GENERAL1_SMALL"
    image        = "aws/codebuild/amazonlinux2-x86_64-standard:5.0"
    type         = "LINUX_CONTAINER"
  }

  source { type = "NO_SOURCE" }

  logs_config {
    s3_logs {
      status              = "ENABLED"
      location            = "<bucket-name>/<path>"
      encryption_disabled = false  # Critical: enables encryption for S3 logs
    }
  }
}
```

### Other

1. Open the AWS CodeBuild console and select your project
2. Choose Edit, then open the Logs section
3. Under S3 logs, select Enabled and choose the Bucket/Path
4. Ensure Disable S3 log encryption is unchecked (encryption enabled)
5. Save changes

## 参考資料

- [https://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html#change-project-console-logs](https://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html#change-project-console-logs)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html#codebuild-3](https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html#codebuild-3)
- [https://support.icompaas.com/support/solutions/articles/62000233685-ensure-s3-logs-for-codebuild-projects-are-encrypted-at-rest](https://support.icompaas.com/support/solutions/articles/62000233685-ensure-s3-logs-for-codebuild-projects-are-encrypted-at-rest)
- [https://hub.powerpipe.io/mods/turbot/steampipe-mod-aws-compliance/benchmarks/control.codebuild_project_s3_logs_encryption_enabled](https://hub.powerpipe.io/mods/turbot/steampipe-mod-aws-compliance/benchmarks/control.codebuild_project_s3_logs_encryption_enabled)

## 技術情報

- Source Metadata：[sources/aws/codebuild_project_s3_logs_encrypted/metadata.json](../../sources/aws/codebuild_project_s3_logs_encrypted/metadata.json)
- Source Code：[sources/aws/codebuild_project_s3_logs_encrypted/check.py](../../sources/aws/codebuild_project_s3_logs_encrypted/check.py)
- Source Metadata Path：`sources/aws/codebuild_project_s3_logs_encrypted/metadata.json`
- Source Code Path：`sources/aws/codebuild_project_s3_logs_encrypted/check.py`
