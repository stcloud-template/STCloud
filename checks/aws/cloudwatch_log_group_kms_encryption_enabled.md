# CloudWatch log group is encrypted with an AWS KMS key

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `cloudwatch_log_group_kms_encryption_enabled` |
| 云平台 | AWS |
| 服务 | cloudwatch |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure |
| 资源类型 | Other |
| 资源组 | monitoring |

## 描述

**CloudWatch log groups** are assessed for **at-rest encryption** by checking if an **AWS KMS key** is associated with the log group via `kmsKeyId`.

## 风险

Without a **customer-managed KMS key**, logs rely on service-managed encryption, limiting control and auditability. - Confidentiality: weaker key-policy barriers against unauthorized reads - Integrity/availability: no custom rotation or rapid revoke, hindering incident response and compliance

## 推荐措施

Associate each log group with a **customer-managed KMS key** via `kmsKeyId`. - Enforce **least privilege** in key and IAM policies, granting `kms:Decrypt` only to required principals - Enable rotation and monitor key usage - Separate keys by app/tenant to support **defense in depth** and rapid revocation

## 修复步骤


### CLI

```text
aws logs associate-kms-key --log-group-name <LOG_GROUP_NAME> --kms-key-id arn:aws:kms:<REGION>:<ACCOUNT_ID>:key/<KEY_ID>
```

### Native IaC

```yaml
# CloudFormation: Encrypt a CloudWatch Log Group with KMS
Resources:
  <example_resource_name>:
    Type: AWS::Logs::LogGroup
    Properties:
      KmsKeyId: arn:aws:kms:<REGION>:<ACCOUNT_ID>:key/<KEY_ID>  # Critical: associates a CMK to encrypt the log group
```

### Terraform

```hcl
# Encrypt a CloudWatch Log Group with KMS
resource "aws_cloudwatch_log_group" "<example_resource_name>" {
  name       = "<example_resource_name>"
  kms_key_id = "arn:aws:kms:<REGION>:<ACCOUNT_ID>:key/<KEY_ID>" # Critical: associates a CMK to encrypt the log group
}
```

### Other

1. In the AWS Console, go to CloudWatch > Log groups
2. Click Create log group and enter a name
3. Under Encryption, select KMS key and provide the key ARN
4. Click Create log group
5. For existing log groups, the console cannot attach a KMS key; use the CLI command provided

## 参考资料

- [https://docs.aws.amazon.com/cli/latest/reference/logs/associate-kms-key.html](https://docs.aws.amazon.com/cli/latest/reference/logs/associate-kms-key.html)
- [https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_log_group](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_log_group)
- [https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/client/associate_kms_key.html](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs/client/associate_kms_key.html)
- [https://support.icompaas.com/support/solutions/articles/62000233436-ensure-cloudwatch-log-groups-are-protected-by-aws-kms](https://support.icompaas.com/support/solutions/articles/62000233436-ensure-cloudwatch-log-groups-are-protected-by-aws-kms)
- [https://varunmanik1.medium.com/proactively-mitigating-a-medium-severity-prowler-issue-enabling-kms-encryption-for-cloudwatch-logs-51d43416c7fc](https://varunmanik1.medium.com/proactively-mitigating-a-medium-severity-prowler-issue-enabling-kms-encryption-for-cloudwatch-logs-51d43416c7fc)

## 技术信息

- Source Metadata：[sources/aws/cloudwatch_log_group_kms_encryption_enabled/metadata.json](../../sources/aws/cloudwatch_log_group_kms_encryption_enabled/metadata.json)
- Source Code：[sources/aws/cloudwatch_log_group_kms_encryption_enabled/check.py](../../sources/aws/cloudwatch_log_group_kms_encryption_enabled/check.py)
- Source Metadata Path：`sources/aws/cloudwatch_log_group_kms_encryption_enabled/metadata.json`
- Source Code Path：`sources/aws/cloudwatch_log_group_kms_encryption_enabled/check.py`
