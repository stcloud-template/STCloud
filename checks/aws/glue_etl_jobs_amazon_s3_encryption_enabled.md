# Glue job has S3 encryption enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `glue_etl_jobs_amazon_s3_encryption_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | glue |
| 重大度 | high |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Effects/Data Exposure |
| リソースタイプ | Other |
| リソースグループ | analytics |

## 説明

**AWS Glue ETL jobs** are validated to use **Amazon S3 at-rest encryption** (`SSE-S3` or `SSE-KMS`) when writing outputs, either through an attached security configuration or via job arguments. Jobs missing a security configuration or with S3 encryption disabled are identified.

## リスク

Storing job outputs in S3 without **at-rest encryption** weakens **confidentiality**. Plaintext objects can be exposed via misconfigured bucket policies, compromised credentials, or media reuse, and lack **KMS key controls**, rotation, and audit trails-hindering incident response and compliance.

## 推奨事項

Require **S3 encryption** for all Glue jobs via security configurations, preferring **SSE-KMS**. Apply **least privilege** to KMS keys, restrict key usage and rotate regularly. Enforce defense-in-depth with bucket policies that require encrypted writes, and monitor with key and S3 access logs.

## 修正手順


### Native IaC

```yaml
# CloudFormation: Attach a Security Configuration with S3 encryption to a Glue job
Resources:
  GlueSecurityConfiguration:
    Type: AWS::Glue::SecurityConfiguration
    Properties:
      Name: <example_resource_name>
      EncryptionConfiguration:
        S3Encryptions:
          - S3EncryptionMode: SSE-S3  # CRITICAL: Enables S3 encryption for Glue outputs

  GlueJob:
    Type: AWS::Glue::Job
    Properties:
      Name: <example_resource_name>
      Role: <example_role_arn>
      Command:
        Name: glueetl
        ScriptLocation: s3://<example_resource_name>/script.py
      SecurityConfiguration: !Ref GlueSecurityConfiguration  # CRITICAL: Applies encrypted security configuration to the job
```

### Terraform

```hcl
# Terraform: Attach a Security Configuration with S3 encryption to a Glue job
resource "aws_glue_security_configuration" "sec" {
  name = "<example_resource_name>"

  s3_encryption {
    s3_encryption_mode = "SSE-S3"  # CRITICAL: Enables S3 encryption for Glue outputs
  }
}

resource "aws_glue_job" "job" {
  name     = "<example_resource_name>"
  role_arn = "<example_role_arn>"

  command {
    script_location = "s3://<example_resource_name>/script.py"
  }

  security_configuration = aws_glue_security_configuration.sec.name  # CRITICAL: Applies encrypted security configuration to the job
}
```

### Other

1. In the AWS Console, go to AWS Glue > Security configurations > Create security configuration
2. Enable S3 encryption and choose SSE-S3 (or SSE-KMS with your key)
3. Save the configuration
4. Go to AWS Glue > Jobs > select your job > Edit
5. Under Job details, set Security configuration to the encrypted configuration you created
6. Save the job

## 参考資料

- [https://docs.aws.amazon.com/glue/latest/dg/console-security-configurations.html](https://docs.aws.amazon.com/glue/latest/dg/console-security-configurations.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Glue/s3-encryption-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Glue/s3-encryption-enabled.html)

## 技術情報

- Source Metadata：[sources/aws/glue_etl_jobs_amazon_s3_encryption_enabled/metadata.json](../../sources/aws/glue_etl_jobs_amazon_s3_encryption_enabled/metadata.json)
- Source Code：[sources/aws/glue_etl_jobs_amazon_s3_encryption_enabled/check.py](../../sources/aws/glue_etl_jobs_amazon_s3_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/glue_etl_jobs_amazon_s3_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/glue_etl_jobs_amazon_s3_encryption_enabled/check.py`
