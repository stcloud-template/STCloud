# Glue development endpoint has Job Bookmark encryption enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `glue_development_endpoints_job_bookmark_encryption_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | glue |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | analytics |

## 説明

**AWS Glue development endpoints** are assessed for an attached **security configuration** where **job bookmark encryption** is enabled. Endpoints lacking a security configuration are also identified.

## リスク

Unencrypted job bookmarks stored in S3 can be read or altered, exposing dataset paths, partitions, and processing state. This enables data discovery, state tampering, and replay/skip of workloads, impacting **confidentiality**, **integrity**, and **availability** of ETL pipelines.

## 推奨事項

Attach a **security configuration** to each development endpoint and enable **job bookmark encryption** with a managed KMS key. Apply **least privilege** to S3 and KMS, rotate keys, and align logs and data stores with consistent encryption for **defense in depth**. Regularly audit endpoints for missing or outdated configurations.

## 修正手順


### Native IaC

```yaml
# CloudFormation: Enable Job Bookmark encryption and attach to the Dev Endpoint
Resources:
  GlueSecurityConfiguration:
    Type: AWS::Glue::SecurityConfiguration
    Properties:
      Name: <example_resource_name>
      EncryptionConfiguration:
        JobBookmarksEncryption:
          JobBookmarksEncryptionMode: CSE-KMS  # Critical: enables Job Bookmark encryption
          KmsKeyArn: <example_kms_key_arn>     # Critical: KMS key used for Job Bookmark encryption

  GlueDevEndpoint:
    Type: AWS::Glue::DevEndpoint
    Properties:
      RoleArn: <example_role_arn>
      SecurityConfiguration: !Ref GlueSecurityConfiguration  # Critical: attach the security configuration to the Dev Endpoint
```

### Terraform

```hcl
# Terraform: Enable Job Bookmark encryption and attach to the Dev Endpoint
resource "aws_glue_security_configuration" "<example_resource_name>" {
  name = "<example_resource_name>"

  encryption_configuration {
    job_bookmarks_encryption {
      job_bookmarks_encryption_mode = "CSE-KMS"   # Critical: enables Job Bookmark encryption
      kms_key_arn                   = "<example_kms_key_arn>"  # Critical: KMS key used for Job Bookmark encryption
    }
  }
}

resource "aws_glue_dev_endpoint" "<example_resource_name>" {
  name                   = "<example_resource_name>"
  role_arn               = "<example_role_arn>"
  security_configuration = aws_glue_security_configuration.<example_resource_name>.name  # Critical: attach the security configuration
}
```

### Other

1. In the AWS Console, go to Glue > Security configurations > Add security configuration
2. Enter a name, then under Advanced settings enable Job bookmark encryption and select a KMS key (or enter its ARN); Save
3. Go to Glue > Dev endpoints
4. Create a new Dev endpoint (or recreate the existing one) and set Security configuration to the configuration created in step 2
5. Create the endpoint to apply the setting

## 参考資料

- [https://docs.aws.amazon.com/glue/latest/dg/console-security-configurations.html](https://docs.aws.amazon.com/glue/latest/dg/console-security-configurations.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Glue/job-bookmark-encryption-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Glue/job-bookmark-encryption-enabled.html)

## 技術情報

- Source Metadata：[sources/aws/glue_development_endpoints_job_bookmark_encryption_enabled/metadata.json](../../sources/aws/glue_development_endpoints_job_bookmark_encryption_enabled/metadata.json)
- Source Code：[sources/aws/glue_development_endpoints_job_bookmark_encryption_enabled/check.py](../../sources/aws/glue_development_endpoints_job_bookmark_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/glue_development_endpoints_job_bookmark_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/glue_development_endpoints_job_bookmark_encryption_enabled/check.py`
