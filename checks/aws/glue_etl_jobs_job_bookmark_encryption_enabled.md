# Glue ETL job has Job bookmark encryption enabled

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `glue_etl_jobs_job_bookmark_encryption_enabled` |
| 云平台 | AWS |
| 服务 | glue |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| 资源类型 | Other |
| 资源组 | analytics |

## 描述

**AWS Glue ETL jobs** should link a **security configuration** with **job bookmark encryption** enabled. Bookmark encryption must not be `DISABLED` (e.g., use `CSE-KMS`). Jobs lacking a security configuration are treated as not protecting bookmark metadata.

## 风险

Unencrypted **job bookmarks** in S3 expose execution state and data pointers, reducing **confidentiality**. Altered bookmarks can trigger reruns, skips, or reprocessing, harming **integrity**. Missing security configs may also leave logs and temporary objects unencrypted.

## 推荐措施

Attach a **Glue security configuration** to every job and enable **job bookmark encryption** (e.g., `CSE-KMS`). Use **customer-managed KMS keys**, enforce **least privilege** on key usage, and rotate keys. For **defense in depth**, also encrypt **S3 temp data** and **CloudWatch logs** in the same configuration.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: Enable Glue Job bookmark encryption via Security Configuration
Resources:
  <example_resource_name>:
    Type: AWS::Glue::SecurityConfiguration
    Properties:
      Name: <example_resource_name>
      EncryptionConfiguration:
        JobBookmarksEncryption:
          JobBookmarksEncryptionMode: CSE-KMS  # CRITICAL: Enables job bookmark encryption
          KmsKeyArn: <example_kms_key_arn>     # CRITICAL: KMS key used to encrypt job bookmarks
```

### Terraform

```hcl
# Terraform: Enable Glue Job bookmark encryption via Security Configuration
resource "aws_glue_security_configuration" "<example_resource_name>" {
  name = "<example_resource_name>"

  encryption_configuration {
    job_bookmarks_encryption {
      job_bookmarks_encryption_mode = "CSE-KMS"      # CRITICAL: Enables job bookmark encryption
      kms_key_arn                    = "<example_kms_key_arn>"  # CRITICAL: KMS key for bookmarks
    }
  }
}
```

### Other

1. In the AWS Console, go to AWS Glue > Security configurations > Add security configuration
2. Enter a name and under Advanced settings enable Job bookmark encryption
3. Select a KMS key (or paste the key ARN) and click Create
4. Go to AWS Glue > Jobs, select the job, click Edit
5. Under Advanced properties, set Security configuration to the one created above
6. Click Save

## 参考资料

- [https://docs.aws.amazon.com/glue/latest/dg/console-security-configurations.html](https://docs.aws.amazon.com/glue/latest/dg/console-security-configurations.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Glue/job-bookmark-encryption-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Glue/job-bookmark-encryption-enabled.html)

## 技术信息

- Source Metadata：[sources/aws/glue_etl_jobs_job_bookmark_encryption_enabled/metadata.json](../../sources/aws/glue_etl_jobs_job_bookmark_encryption_enabled/metadata.json)
- Source Code：[sources/aws/glue_etl_jobs_job_bookmark_encryption_enabled/check.py](../../sources/aws/glue_etl_jobs_job_bookmark_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/glue_etl_jobs_job_bookmark_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/glue_etl_jobs_job_bookmark_encryption_enabled/check.py`
