# Glue development endpoint has CloudWatch Logs encryption enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `glue_development_endpoints_cloudwatch_logs_encryption_enabled` |
| 云平台 | AWS |
| 服务 | glue |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| 资源类型 | Other |
| 资源组 | analytics |

## 描述

**AWS Glue development endpoints** are assessed for an associated **security configuration** that enables **CloudWatch Logs encryption**. It confirms the endpoint references a configuration and that log encryption is not `DISABLED`.

## 风险

Unencrypted Glue logs erode **confidentiality**: credentials, connection strings, and data samples may be readable to unintended principals, enabling **lateral movement**. Lack of KMS-backed encryption weakens **auditability** and **separation of duties**.

## 推荐措施

Attach a **security configuration** to all development endpoints with **CloudWatch Logs encryption** enabled using a tightly scoped **KMS key**. Apply **least privilege** to key and log access, rotate keys, and standardize configs via IaC to enforce **defense in depth**.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Glue Security Configuration with CloudWatch Logs encryption enabled
Resources:
  <example_resource_name>:
    Type: AWS::Glue::SecurityConfiguration
    Properties:
      Name: <example_resource_name>
      EncryptionConfiguration:
        CloudWatchEncryption:
          CloudWatchEncryptionMode: SSE-KMS  # Critical: enables CloudWatch Logs encryption
          KmsKeyArn: <kms_key_arn>           # Critical: KMS key used for encrypting Glue logs
```

### Terraform

```hcl
# Glue Security Configuration with CloudWatch Logs encryption enabled
resource "aws_glue_security_configuration" "<example_resource_name>" {
  name = "<example_resource_name>"

  encryption_configuration {
    cloudwatch_encryption {
      cloudwatch_encryption_mode = "SSE-KMS"  # Critical: enables CloudWatch Logs encryption
      kms_key_arn                = "<kms_key_arn>"  # Critical: KMS key used for encrypting Glue logs
    }

    # Required blocks for valid config (kept minimal)
    job_bookmarks_encryption { job_bookmarks_encryption_mode = "DISABLED" }
    s3_encryption             { s3_encryption_mode             = "DISABLED" }
  }
}
```

### Other

1. In the AWS Console, go to Glue > Security configurations > Add security configuration
2. Enter a name and enable CloudWatch Logs encryption
3. Select a KMS key (or enter its ARN) and click Create
4. Go to Glue > Dev endpoints
5. Create a new Dev endpoint (or delete and recreate the existing one) and select the new Security configuration
6. Create the endpoint to apply the encryption

## 参考资料

- [https://docs.aws.amazon.com/glue/latest/dg/console-security-configurations.html](https://docs.aws.amazon.com/glue/latest/dg/console-security-configurations.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Glue/cloud-watch-logs-encryption-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Glue/cloud-watch-logs-encryption-enabled.html)

## 技术信息

- Source Metadata：[sources/aws/glue_development_endpoints_cloudwatch_logs_encryption_enabled/metadata.json](../../sources/aws/glue_development_endpoints_cloudwatch_logs_encryption_enabled/metadata.json)
- Source Code：[sources/aws/glue_development_endpoints_cloudwatch_logs_encryption_enabled/check.py](../../sources/aws/glue_development_endpoints_cloudwatch_logs_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/glue_development_endpoints_cloudwatch_logs_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/glue_development_endpoints_cloudwatch_logs_encryption_enabled/check.py`
