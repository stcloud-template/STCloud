# Glue development endpoint has S3 encryption enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `glue_development_endpoints_s3_encryption_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | glue |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| リソースタイプ | Other |
| リソースグループ | analytics |

## 説明

**AWS Glue development endpoints** are evaluated for an attached **security configuration** with **S3 encryption**. Endpoints lacking a security configuration, or with `s3_encryption` set to `DISABLED`, are flagged by this check.

## リスク

Unencrypted S3 writes from dev endpoints leave ETL outputs, temp data, and scripts readable at rest. A misconfigured bucket or stolen creds can expose sensitive content, harming **confidentiality** and triggering compliance issues.

## 推奨事項

Attach a **Glue security configuration** to each dev endpoint with **S3 encryption** enabled; prefer `SSE-KMS` with customer-managed keys. Enforce **least privilege** on IAM and KMS key policies, and extend encryption to logs and bookmarks for **defense in depth**.

## 修正手順


### Native IaC

```yaml
# CloudFormation: Glue Dev Endpoint with S3 encryption via Security Configuration
Resources:
  SecurityConfig:
    Type: AWS::Glue::SecurityConfiguration
    Properties:
      Name: <example_resource_name>
      EncryptionConfiguration:
        S3Encryptions:
          - S3EncryptionMode: SSE-S3  # CRITICAL: enables S3 encryption for the security configuration

  DevEndpoint:
    Type: AWS::Glue::DevEndpoint
    Properties:
      EndpointName: <example_resource_name>
      RoleArn: <example_role_arn>
      SecurityConfiguration: !Ref SecurityConfig  # CRITICAL: attaches the encrypted security configuration to the dev endpoint
```

### Terraform

```hcl
# Terraform: Glue Dev Endpoint with S3 encryption
resource "aws_glue_security_configuration" "secure" {
  name = "<example_resource_name>"
  encryption_configuration {
    s3_encryption {
      s3_encryption_mode = "SSE-S3"  # CRITICAL: enables S3 encryption
    }
  }
}

resource "aws_glue_dev_endpoint" "dev" {
  name     = "<example_resource_name>"
  role_arn = "<example_role_arn>"

  security_configuration = aws_glue_security_configuration.secure.name  # CRITICAL: attaches encrypted security configuration
}
```

### Other

1. In the AWS Console, go to AWS Glue > Security configurations > Create security configuration
2. Under S3 encryption, select Server-side encryption (SSE-S3) and save
3. Go to AWS Glue > Development endpoints > Create development endpoint
4. Fill required fields and set Security configuration to the one created in step 2
5. Create the endpoint and delete the old endpoint (without encryption) if it exists

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Glue/s3-encryption-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Glue/s3-encryption-enabled.html)
- [https://docs.aws.amazon.com/glue/latest/dg/encryption-security-configuration.html](https://docs.aws.amazon.com/glue/latest/dg/encryption-security-configuration.html)

## 技術情報

- Source Metadata：[sources/aws/glue_development_endpoints_s3_encryption_enabled/metadata.json](../../sources/aws/glue_development_endpoints_s3_encryption_enabled/metadata.json)
- Source Code：[sources/aws/glue_development_endpoints_s3_encryption_enabled/check.py](../../sources/aws/glue_development_endpoints_s3_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/glue_development_endpoints_s3_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/glue_development_endpoints_s3_encryption_enabled/check.py`
