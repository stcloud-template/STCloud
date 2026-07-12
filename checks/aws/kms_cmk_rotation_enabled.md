# KMS customer-managed symmetric CMK has automatic rotation enabled

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `kms_cmk_rotation_enabled` |
| クラウドプラットフォーム | AWS |
| サービス | kms |
| 重大度 | high |
| カテゴリ | encryption |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark |
| リソースタイプ | AwsKmsKey |
| リソースグループ | security |

## 説明

**Customer-managed KMS symmetric keys** in the `Enabled` state are evaluated to confirm `automatic rotation` of key material is configured

## リスク

Without **automatic rotation**, long-lived key material increases confidentiality and integrity risk. If a KMS key is exposed, attackers can unwrap data keys and decrypt stored data until the key changes. It also reduces crypto agility and may conflict with mandated rotation policies.

## 推奨事項

Enable **automatic rotation** on customer-managed symmetric KMS keys and choose a rotation period that meets policy. Enforce **least privilege** and **separation of duties** for key administration versus usage. Monitor key lifecycle events and use on-demand rotation when compromise is suspected.

## 修正手順


### CLI

```text
aws kms enable-key-rotation --key-id <KEY_ID>
```

### Native IaC

```yaml
# CloudFormation: KMS key with automatic rotation enabled
Resources:
  <example_resource_name>:
    Type: AWS::KMS::Key
    Properties:
      EnableKeyRotation: true  # Critical: enables automatic rotation so the key passes the check
      KeyPolicy:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              AWS: !Sub arn:aws:iam::${AWS::AccountId}:root
            Action: "kms:*"
            Resource: "*"
```

### Terraform

```hcl
# KMS key with automatic rotation enabled
resource "aws_kms_key" "<example_resource_name>" {
  enable_key_rotation = true  # Critical: enables automatic rotation so the key passes the check
}
```

### Other

1. In the AWS Console, go to Key Management Service (KMS)
2. Open Customer managed keys and select the enabled symmetric key
3. Go to the Key rotation section
4. Check Enable automatic key rotation
5. Save changes

## 参考資料

- [https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html)
- [https://aws.amazon.com/blogs/security/how-to-get-ready-for-certificate-transparency/](https://aws.amazon.com/blogs/security/how-to-get-ready-for-certificate-transparency/)

## 技術情報

- Source Metadata：[sources/aws/kms_cmk_rotation_enabled/metadata.json](../../sources/aws/kms_cmk_rotation_enabled/metadata.json)
- Source Code：[sources/aws/kms_cmk_rotation_enabled/check.py](../../sources/aws/kms_cmk_rotation_enabled/check.py)
- Source Metadata Path：`sources/aws/kms_cmk_rotation_enabled/metadata.json`
- Source Code Path：`sources/aws/kms_cmk_rotation_enabled/check.py`
