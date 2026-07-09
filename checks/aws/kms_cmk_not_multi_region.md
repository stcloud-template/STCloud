# AWS KMS customer managed key is single-Region

ST Cloud check knowledge base entry.

## 检查项信息

| 字段 | 内容 |
| --- | --- |
| 检查项 ID | `kms_cmk_not_multi_region` |
| 云平台 | AWS |
| 服务 | kms |
| 严重等级 | medium |
| 类别 | encryption |
| 检查类型 | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices |
| 资源类型 | AwsKmsKey |
| 资源组 | security |

## 描述

**AWS KMS customer-managed keys** in an `Enabled` state are assessed for the `multi-Region` setting. The finding highlights keys with the `multi-Region` property enabled.

## 风险

Shared key material across Regions lets access in one Region decrypt data from another, eroding **confidentiality** and **data residency**. A misconfigured policy or weaker controls in a replica expand the blast radius. For signing/HMAC keys, compromise enables cross-Region signature forgery, impacting **integrity** and **auditability**.

## 推荐措施

Prefer **single-Region keys** by default; use **multi-Region** only with a documented need. Apply **least privilege** and **separation of duties**; limit who can create or replicate such keys. Isolate per Region/tenant/workload, standardize policy and logging across Regions, and retire multi-Region keys where unnecessary.

## 修复步骤


### Native IaC

```yaml
# CloudFormation: create a single-Region KMS key
Resources:
  ExampleKmsKey:
    Type: AWS::KMS::Key
    Properties:
      MultiRegion: false  # Critical: ensures the key is single-Region to pass the check
      KeyPolicy:          # Minimal policy required for key creation
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              AWS: !Sub arn:aws:iam::${AWS::AccountId}:root
            Action: 'kms:*'
            Resource: '*'
```

### Terraform

```hcl
# Terraform: create a single-Region KMS key
resource "aws_kms_key" "example" {
  multi_region = false  # Critical: creates a single-Region key to pass the check
}
```

### Other

1. In the AWS Console, go to Key Management Service (KMS) > Customer managed keys
2. Identify keys showing Multi-Region: Yes (these FAIL the check)
3. Click Create key and ensure Multi-Region is not selected (single-Region)
4. Update your services/aliases to use the new single-Region key
5. Re-encrypt or rotate data to the new key where required
6. After migration, disable the old multi-Region key and schedule its deletion

## 参考资料

- [https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html#multi-region-concepts](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html#multi-region-concepts)
- [https://docs.aws.amazon.com/kms/latest/developerguide/mrk-when-to-use.html](https://docs.aws.amazon.com/kms/latest/developerguide/mrk-when-to-use.html)

## 技术信息

- Source Metadata：[sources/aws/kms_cmk_not_multi_region/metadata.json](../../sources/aws/kms_cmk_not_multi_region/metadata.json)
- Source Code：[sources/aws/kms_cmk_not_multi_region/check.py](../../sources/aws/kms_cmk_not_multi_region/check.py)
- Source Metadata Path：`sources/aws/kms_cmk_not_multi_region/metadata.json`
- Source Code Path：`sources/aws/kms_cmk_not_multi_region/check.py`
