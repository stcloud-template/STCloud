# Athena workgroup encrypts query results in S3 with server-side encryption

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `athena_workgroup_encryption` |
| 云平台 | AWS |
| 服务 | athena |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark, Effects/Data Exposure |
| 资源类型 | AwsAthenaWorkGroup |
| 资源组 | analytics |

## 描述

**Athena workgroups** are evaluated for **encryption of query results** to confirm result data is stored encrypted at rest, whether saved in Amazon S3 or via managed query results

## 风险

Unencrypted query outputs can be read at rest by unintended principals through S3 misconfigurations or cross-account access. Impact: **Confidentiality loss**, enabling **data exfiltration** and supporting **lateral movement** by exposing sensitive fields outside intended boundaries.

## 推荐措施

Enable and enforce **workgroup result encryption** with **AWS KMS customer managed keys** (`SSE_KMS` or managed results with a KMS key). Set a minimum encryption level and prevent client overrides. Apply **least privilege** to key and result access, rotate keys, and audit usage to maintain defense in depth.

## 修复步骤


### CLI

```text
aws athena update-work-group --work-group <workgroup_name> --configuration-updates ResultConfigurationUpdates={EncryptionConfiguration={EncryptionOption=SSE_S3}}
```

### Native IaC

```yaml
# CloudFormation: Enable encryption of Athena workgroup query results
Resources:
  <example_resource_name>:
    Type: AWS::Athena::WorkGroup
    Properties:
      Name: <example_resource_name>
      WorkGroupConfiguration:
        ResultConfiguration:
          EncryptionConfiguration:
            EncryptionOption: SSE_S3  # Critical: enables server-side encryption for query results
```

### Terraform

```hcl
# Terraform: Enable encryption of Athena workgroup query results
resource "aws_athena_workgroup" "<example_resource_name>" {
  name = "<example_resource_name>"

  configuration {
    result_configuration {
      output_location = "s3://<example_bucket>/"  # Required S3 path for query results
      encryption_configuration {
        encryption_option = "SSE_S3"  # Critical: enables encryption for query results
      }
    }
  }
}
```

### Other

1. In the AWS Console, go to Amazon Athena > Workgroups
2. Select the workgroup and click Edit
3. Under Query result configuration, set a Results location if empty
4. Check Encrypt query results and select SSE-S3
5. Click Save changes

## 参考资料

- [https://aws.amazon.com/blogs/big-data/introducing-managed-query-results-for-amazon-athena/](https://aws.amazon.com/blogs/big-data/introducing-managed-query-results-for-amazon-athena/)
- [https://docs.aws.amazon.com/athena/latest/ug/managed-results.html](https://docs.aws.amazon.com/athena/latest/ug/managed-results.html)
- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Athena/encryption-enabled.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/aws/Athena/encryption-enabled.html)
- [https://docs.aws.amazon.com/athena/latest/ug/encrypting-managed-results.html](https://docs.aws.amazon.com/athena/latest/ug/encrypting-managed-results.html)
- [https://docs.aws.amazon.com/athena/latest/ug/encrypting-query-results-stored-in-s3.html](https://docs.aws.amazon.com/athena/latest/ug/encrypting-query-results-stored-in-s3.html)
- [https://docs.aws.amazon.com/athena/latest/ug/workgroups-minimum-encryption.html](https://docs.aws.amazon.com/athena/latest/ug/workgroups-minimum-encryption.html)
- [https://aws.amazon.com/blogs/aws/launch-amazon-athena-adds-support-for-querying-encrypted-data/](https://aws.amazon.com/blogs/aws/launch-amazon-athena-adds-support-for-querying-encrypted-data/)

## 技术信息

- Source Metadata：[sources/aws/athena_workgroup_encryption/metadata.json](../../sources/aws/athena_workgroup_encryption/metadata.json)
- Source Code：[sources/aws/athena_workgroup_encryption/check.py](../../sources/aws/athena_workgroup_encryption/check.py)
- Source Metadata Path：`sources/aws/athena_workgroup_encryption/metadata.json`
- Source Code Path：`sources/aws/athena_workgroup_encryption/check.py`
