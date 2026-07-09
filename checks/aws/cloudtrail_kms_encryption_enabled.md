# CloudTrail trail logs are encrypted at rest with a KMS key

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudtrail_kms_encryption_enabled` |
| 云平台 | AWS |
| 服务 | cloudtrail |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| 资源类型 | AwsCloudTrailTrail |
| 资源组 | monitoring |

## 描述

**AWS CloudTrail trails** are evaluated for use of **SSE-KMS** with a customer-managed KMS key to encrypt delivered log files at rest in S3. Trails without a configured KMS key are identified. *Applies to single-Region and multi-Region trails.*

## 风险

Absent a **customer-managed KMS key**, log protection relies only on storage permissions. Bucket misconfigurations or stolen credentials can expose audit data, aiding evasion and lateral movement. Missing key-level controls, rotation, and usage audit weaken **confidentiality** and **forensic integrity**.

## 推荐措施

Enable **SSE-KMS** on every trail using a **customer-managed KMS key**. Apply **least privilege** so only authorized roles can `Decrypt`, and enforce **separation of duties** between key admins and log readers. Rotate keys and monitor key usage to provide **defense in depth** for CloudTrail data.

## 修复步骤


### CLI

```text
aws cloudtrail update-trail --name <trail_name> --kms-key-id <kms_key_arn_or_id>
```

### Native IaC

```yaml
# CloudFormation: enable KMS encryption for an existing/new CloudTrail
Resources:
  <example_resource_name>:
    Type: AWS::CloudTrail::Trail
    Properties:
      S3BucketName: <example_resource_name>
      KmsKeyId: <example_resource_id>  # Critical: sets the KMS key to encrypt CloudTrail logs at rest
```

### Terraform

```hcl
# Enable KMS encryption for CloudTrail
resource "aws_cloudtrail" "<example_resource_name>" {
  name           = "<example_resource_name>"
  s3_bucket_name = "<example_resource_name>"
  kms_key_id     = "<example_resource_id>" # Critical: uses this KMS key to encrypt CloudTrail logs
}
```

### Other

1. In the AWS Console, go to CloudTrail > Trails
2. Select the trail <trail_name>, click Edit
3. Under Log file encryption, choose Use a KMS key and select <cloudtrail_kms_key>
4. Click Save changes

## 参考资料

- [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/encrypting-cloudtrail-log-files-with-aws-kms.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/encrypting-cloudtrail-log-files-with-aws-kms.html)
- [https://trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudTrail/cloudtrail-logs-encrypted.html](https://trendmicro.com/cloudoneconformity/knowledge-base/aws/CloudTrail/cloudtrail-logs-encrypted.html)
- [https://www.stream.security/rules/ensure-cloudtrail-logs-are-encrypted-at-rest](https://www.stream.security/rules/ensure-cloudtrail-logs-are-encrypted-at-rest)
- [https://www.clouddefense.ai/compliance-rules/cis-v130/logging/cis-v130-3-7](https://www.clouddefense.ai/compliance-rules/cis-v130/logging/cis-v130-3-7)

## 技术信息

- Source Metadata：[sources/aws/cloudtrail_kms_encryption_enabled/metadata.json](../../sources/aws/cloudtrail_kms_encryption_enabled/metadata.json)
- Source Code：[sources/aws/cloudtrail_kms_encryption_enabled/check.py](../../sources/aws/cloudtrail_kms_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/cloudtrail_kms_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/cloudtrail_kms_encryption_enabled/check.py`
