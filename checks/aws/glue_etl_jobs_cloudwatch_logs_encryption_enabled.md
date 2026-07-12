# Glue ETL job has CloudWatch Logs encryption enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `glue_etl_jobs_cloudwatch_logs_encryption_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | glue |
| 重大度 | medium |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls (USA) |
| リソースタイプ | AwsGlueJob |
| リソースグループ | analytics |

## 説明

**AWS Glue ETL jobs** are evaluated for a **security configuration** with **CloudWatch Logs encryption** (`SSE-KMS`) enabled. Jobs without a security configuration, or with CloudWatch Logs encryption set to `DISABLED`, are highlighted.

## リスク

Unencrypted Glue logs weaken **confidentiality**. Log entries can expose credentials, PII, connection strings, and schema details. Anyone with log storage access can harvest secrets for **lateral movement** and data exfiltration, widening the blast radius of compromises.

## 推奨事項

Enable **at-rest encryption** for Glue logs via a **security configuration** using customer-managed KMS keys. Apply **least privilege** to KMS and CloudWatch Logs, rotate keys, and require all jobs to attach an approved configuration. Embed this baseline in IaC for consistent, **defense-in-depth** coverage.

## 修正手順


### Native IaC

```yaml
# CloudFormation: enable CloudWatch Logs encryption and attach to the job
Resources:
  ExampleSecurityConfiguration:
    Type: AWS::Glue::SecurityConfiguration
    Properties:
      Name: <example_resource_name>
      EncryptionConfiguration:
        CloudWatchEncryption:  # Critical: enable CloudWatch Logs encryption for Glue
          CloudWatchEncryptionMode: SSE-KMS  # Critical: must not be DISABLED
          KmsKeyArn: <example_kms_key_arn>   # Critical: KMS key used for encryption

  ExampleJob:
    Type: AWS::Glue::Job
    Properties:
      Role: <example_role_arn>
      Command:
        Name: glueetl
        ScriptLocation: s3://<example_script_path>
      SecurityConfiguration: !Ref ExampleSecurityConfiguration  # Critical: attach security configuration to the job
```

### Terraform

```hcl
# Enable CloudWatch Logs encryption and attach to the Glue job
resource "aws_glue_security_configuration" "example_resource_name" {
  name = "<example_resource_name>"

  encryption_configuration {
    cloudwatch_encryption {
      cloudwatch_encryption_mode = "SSE-KMS"          # Critical: enable CW Logs encryption
      kms_key_arn                = "<example_kms_key_arn>" # Critical: KMS key for encryption
    }
  }
}

resource "aws_glue_job" "example_resource_name" {
  name     = "<example_resource_name>"
  role_arn = "<example_role_arn>"

  command {
    name            = "glueetl"
    script_location = "s3://<example_script_path>"
  }

  security_configuration = aws_glue_security_configuration.example_resource_name.name # Critical: attach security config to job
}
```

### Other

1. In the AWS Glue console, go to Security configurations > Add security configuration
2. Enter a name, enable CloudWatch Logs encryption, select SSE-KMS, and choose/provide the KMS key ARN; Save
3. Go to Jobs, select the target job, click Edit
4. Set Security configuration to the one created in step 2
5. Save changes

## 参考資料

- [https://docs.aws.amazon.com/glue/latest/dg/console-security-configurations.html](https://docs.aws.amazon.com/glue/latest/dg/console-security-configurations.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Glue/cloud-watch-logs-encryption-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Glue/cloud-watch-logs-encryption-enabled.html)

## 技術情報

- Source Metadata：[sources/aws/glue_etl_jobs_cloudwatch_logs_encryption_enabled/metadata.json](../../sources/aws/glue_etl_jobs_cloudwatch_logs_encryption_enabled/metadata.json)
- Source Code：[sources/aws/glue_etl_jobs_cloudwatch_logs_encryption_enabled/check.py](../../sources/aws/glue_etl_jobs_cloudwatch_logs_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/glue_etl_jobs_cloudwatch_logs_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/glue_etl_jobs_cloudwatch_logs_encryption_enabled/check.py`
