# CodeBuild report group exports to S3 are encrypted at rest

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `codebuild_report_group_export_encrypted` |
| 云平台 | AWS |
| 服务 | codebuild |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/NIST CSF Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS, Software and Configuration Checks/Industry and Regulatory Standards/HIPAA Controls (USA), Software and Configuration Checks/Industry and Regulatory Standards/ISO 27001 Controls, Software and Configuration Checks/Industry and Regulatory Standards/SOC 2 |
| 资源类型 | AwsCodeBuildProject |
| 资源组 | devops |

## 描述

**CodeBuild report groups** with export type `S3` are evaluated to confirm their exported test results are encrypted at rest with a **KMS key**. Report groups configured with `NO_EXPORT` are out of scope.

## 风险

**Unencrypted S3 exports** leave report data in plaintext, weakening confidentiality. If a bucket is misconfigured, compromised, or accessed by insiders, attackers can harvest test outputs for secrets, tokens, build paths, and system details, enabling credential theft and lateral movement.

## 推荐措施

Enable at-rest encryption for report exports using **KMS** (prefer **customer managed keys**). Apply least privilege: restrict key usage to the CodeBuild role and required principals, enable rotation, and audit key usage. Combine with S3 bucket policies for **defense in depth**.

## 修复步骤


### CLI

```text
aws codebuild update-report-group --arn <report-group-arn> --export-config "exportConfigType=S3,s3Destination={bucket=<bucket-name>,encryptionDisabled=false}"
```

### Native IaC

```yaml
# CloudFormation: Enable encryption for CodeBuild report group S3 exports
Resources:
  <example_resource_name>:
    Type: AWS::CodeBuild::ReportGroup
    Properties:
      Name: <example_resource_name>
      Type: TEST
      ExportConfig:
        ExportConfigType: S3
        S3Destination:
          Bucket: <example_resource_name>
          EncryptionDisabled: false  # Critical: ensures S3 exports are encrypted at rest
          # Uses AWS managed key by default
```

### Terraform

```hcl
# Enable encryption for CodeBuild report group S3 exports
resource "aws_codebuild_report_group" "<example_resource_name>" {
  name = "<example_resource_name>"
  type = "TEST"

  export_config {
    type = "S3"
    s3_destination {
      bucket              = "<example_resource_name>"
      encryption_disabled = false  # Critical: ensures S3 exports are encrypted at rest
      # Uses AWS managed key by default
    }
  }
}
```

### Other

1. Open the AWS Console and go to CodeBuild > Report groups
2. Select the report group and click Edit
3. Ensure Export to Amazon S3 is enabled and a bucket is set
4. Expand Additional configuration and enable encryption by choosing Default AWS managed key (or select a KMS key)
5. Ensure Disable artifact encryption is NOT selected
6. Save changes

## 参考资料

- [https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html#codebuild-7](https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html#codebuild-7)
- [https://www.pulumi.com/registry/packages/aws/api-docs/codebuild/reportgroup/](https://www.pulumi.com/registry/packages/aws/api-docs/codebuild/reportgroup/)
- [https://docs.aws.amazon.com/codebuild/latest/userguide/report-group-export-settings.html](https://docs.aws.amazon.com/codebuild/latest/userguide/report-group-export-settings.html)
- [https://docs.aws.amazon.com/codebuild/latest/userguide/security-encryption.html](https://docs.aws.amazon.com/codebuild/latest/userguide/security-encryption.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html](https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html)
- [https://docs.amazonaws.cn/en_us/codebuild/latest/userguide/report-group-export-settings.html](https://docs.amazonaws.cn/en_us/codebuild/latest/userguide/report-group-export-settings.html)
- [https://docs.aws.amazon.com/codebuild/latest/userguide/test-report-group-create-console.html](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report-group-create-console.html)
- [https://docs.aws.amazon.com/codebuild/latest/userguide/update-report-group-console.html](https://docs.aws.amazon.com/codebuild/latest/userguide/update-report-group-console.html)
- [https://docs.aws.amazon.com/codebuild/latest/userguide/report-group-create.html](https://docs.aws.amazon.com/codebuild/latest/userguide/report-group-create.html)
- [https://docs.amazonaws.cn/en_us/codebuild/latest/userguide/test-report-group-create-console.html](https://docs.amazonaws.cn/en_us/codebuild/latest/userguide/test-report-group-create-console.html)

## 技术信息

- Source Metadata：[sources/aws/codebuild_report_group_export_encrypted/metadata.json](../../sources/aws/codebuild_report_group_export_encrypted/metadata.json)
- Source Code：[sources/aws/codebuild_report_group_export_encrypted/check.py](../../sources/aws/codebuild_report_group_export_encrypted/check.py)
- Source Metadata Path：`sources/aws/codebuild_report_group_export_encrypted/metadata.json`
- Source Code Path：`sources/aws/codebuild_report_group_export_encrypted/check.py`
