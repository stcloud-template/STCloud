# CloudTrail trail has log file validation enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `cloudtrail_log_file_validation_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | cloudtrail |
| 重大度 | medium |
| カテゴリ | logging, forensics-ready |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| リソースタイプ | AwsCloudTrailTrail |
| リソースグループ | monitoring |

## 説明

**AWS CloudTrail trails** are evaluated for **log file integrity validation** being enabled (`LogFileValidationEnabled`). When enabled, CloudTrail generates signed digest files to verify that S3-delivered log files remain unchanged.

## リスク

Without validation, adversaries can alter, forge, or delete audit entries without detection, compromising log **integrity** and non-repudiation. This impairs investigations, enables alert evasion, and obscures unauthorized changes across regions or accounts.

## 推奨事項

Enable **log file integrity validation** on all trails (`LogFileValidationEnabled=true`). Enforce **least privilege** on the logs bucket, retain and protect digest files (e.g., S3 Object Lock/MFA Delete), and monitor validation results to support **defense in depth**.

## 修正手順


### CLI

```text
aws cloudtrail update-trail --name <trail_name> --enable-log-file-validation
```

### Native IaC

```yaml
# CloudFormation: Enable log file validation on a CloudTrail trail
Resources:
  <example_resource_name>:
    Type: AWS::CloudTrail::Trail
    Properties:
      S3BucketName: <example_resource_name>
      EnableLogFileValidation: true  # Critical: enables integrity validation for delivered log files
```

### Terraform

```hcl
# Enable log file validation on a CloudTrail trail
resource "aws_cloudtrail" "<example_resource_name>" {
  name               = "<example_resource_name>"
  s3_bucket_name     = "<example_resource_name>"
  enable_log_file_validation = true  # Critical: ensures CloudTrail writes signed digests to detect tampering
}
```

### Other

1. Open the AWS Console and go to CloudTrail
2. Click Trails and select <trail_name>
3. Click Edit
4. In Additional/Advanced settings, check Enable log file validation
5. Click Save changes

## 参考資料

- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html)
- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-enabling.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-enabling.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudTrail/cloudtrail-log-file-integrity-validation.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudTrail/cloudtrail-log-file-integrity-validation.html)
- [https://deepwiki.com/acantril/learn-cantrill-io-labs/7.1-cloudtrail-log-file-integrity](https://deepwiki.com/acantril/learn-cantrill-io-labs/7.1-cloudtrail-log-file-integrity)

## 技術情報

- Source Metadata：[sources/aws/cloudtrail_log_file_validation_enabled/metadata.json](../../sources/aws/cloudtrail_log_file_validation_enabled/metadata.json)
- Source Code：[sources/aws/cloudtrail_log_file_validation_enabled/check.py](../../sources/aws/cloudtrail_log_file_validation_enabled/check.py)
- Source Metadata Path：`sources/aws/cloudtrail_log_file_validation_enabled/metadata.json`
- Source Code Path：`sources/aws/cloudtrail_log_file_validation_enabled/check.py`
