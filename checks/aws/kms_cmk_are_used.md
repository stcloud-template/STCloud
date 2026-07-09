# KMS customer managed key is enabled or scheduled for deletion

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `kms_cmk_are_used` |
| 云平台 | AWS |
| 服务 | kms |
| 严重等级 | low |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsKmsKey |
| 资源组 | security |

## 描述

**Customer-managed KMS keys** are assessed by key state. Keys in `Enabled` are considered in use. Keys not `Enabled` and not `PendingDeletion` are identified as unused, while those in `PendingDeletion` are recognized as scheduled for removal.

## 风险

Keeping **unused CMKs** increases **attack surface** and **cost**. If such keys are re-enabled or misconfigured, they can grant unintended decryption, impacting **confidentiality**. Deleting a key mistakenly thought unused can cause **irrecoverable data loss**, harming **availability**.

## 推荐措施

Adopt a **key lifecycle**: confirm actual usage with logs, owners, and tags; keep keys `Enabled` only when required; otherwise **schedule deletion** with a waiting period. Enforce **least privilege** to enable/disable or delete keys, require approvals, and monitor KMS activity with **separation of duties**.

## 修复步骤


### CLI

```text
aws kms enable-key --key-id <key_id>
```

### Native IaC

```yaml
# CloudFormation: ensure the KMS CMK is enabled
Resources:
  <example_resource_name>:
    Type: AWS::KMS::Key
    Properties:
      Enabled: true  # Critical: enables the key so its state is "Enabled" (PASS)
      KeyPolicy:
        Version: '2012-10-17'
        Statement:
          - Sid: Enable IAM User Permissions
            Effect: Allow
            Principal:
              AWS: !Sub arn:aws:iam::${AWS::AccountId}:root
            Action: 'kms:*'
            Resource: '*'
```

### Terraform

```hcl
# Terraform: ensure the KMS CMK is enabled
resource "aws_kms_key" "<example_resource_name>" {
  is_enabled = true  # Critical: sets key state to Enabled (PASS)
}
```

### Other

1. Sign in to the AWS Console and open Key Management Service (KMS)
2. Go to Customer managed keys and select the affected key
3. Choose Key actions > Enable
4. Confirm to enable the key

## 参考资料

- [https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-determining-usage.html](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-determining-usage.html)

## 技术信息

- Source Metadata：[sources/aws/kms_cmk_are_used/metadata.json](../../sources/aws/kms_cmk_are_used/metadata.json)
- Source Code：[sources/aws/kms_cmk_are_used/check.py](../../sources/aws/kms_cmk_are_used/check.py)
- Source Metadata Path：`sources/aws/kms_cmk_are_used/metadata.json`
- Source Code Path：`sources/aws/kms_cmk_are_used/check.py`
