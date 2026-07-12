# Cloud KMS key does not grant access to allUsers or allAuthenticatedUsers

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `kms_key_not_publicly_accessible` |
| クラウドプラットフォーム | AWS |
| サービス | kms |
| 重大度 | critical |
| カテゴリ | internet-exposed, identity-access |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Industry and Regulatory Standards/AWS Foundational Security Best Practices, TTPs/Initial Access/Unauthorized Access, Effects/Data Exposure |
| リソースタイプ | AwsKmsKey |
| リソースグループ | security |

## 説明

**KMS keys** are assessed for **excessive access** in key policies or grants, including `*` principals and broadly scoped permissions to multiple identities.

## リスク

Broad access to a **KMS key** enables unauthorized `kms:Decrypt` and data-key generation, breaking **confidentiality**. With admin rights, attackers can change policies or schedule deletion, undermining control **integrity** and threatening **availability** of data dependent on the key.

## 推奨事項

Apply **least privilege** to KMS keys: - Restrict principals to specific roles and accounts - Prefer narrow, time-bound grants - Separate key administration from usage - Use conditions to limit context - Review regularly and remove wildcard or cross-account exposure

## 修正手順


### CLI

```text
aws kms put-key-policy --key-id <example_resource_id> --policy-name default --policy '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::<account_id>:root"},"Action":"kms:*","Resource":"*"}]}'
```

### Native IaC

```yaml
# CloudFormation: restrict KMS key policy to account root (removes any public access)
Resources:
  <example_resource_name>:
    Type: AWS::KMS::Key
    Properties:
      KeyPolicy:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              AWS: arn:aws:iam::<account_id>:root  # Critical: only account root can access; prevents public "*" principals
            Action: kms:*
            Resource: '*'
```

### Terraform

```hcl
# Restrict KMS key policy to the account root to avoid any public ("*") principals
data "aws_caller_identity" "current" {}

resource "aws_kms_key" "<example_resource_name>" {
  policy = jsonencode({
    Version   = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Principal = { AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root" } # Critical: limit to account root to remove public access
        Action    = "kms:*"
        Resource  = "*"
      }
    ]
  })
}
```

### Other

1. Open AWS Console > Key Management Service (KMS)
2. Select the affected key and go to the Key policy tab
3. Click Edit and remove any statement with Principal set to "*" (or AWS: "*")
4. Ensure a statement exists that allows only arn:aws:iam::<account_id>:root
5. Save changes

## 参考資料

- [https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudKMS/publicly-accessible-kms-cryptokeys.html](https://www.trendmicro.com/cloudoneconformity/knowledge-base/gcp/CloudKMS/publicly-accessible-kms-cryptokeys.html)
- [https://support.icompaas.com/support/solutions/articles/62000232904-1-9-ensure-cloud-kms-cryptokeys-are-not-accessible-to-anonymous-or-public-users-automated-](https://support.icompaas.com/support/solutions/articles/62000232904-1-9-ensure-cloud-kms-cryptokeys-are-not-accessible-to-anonymous-or-public-users-automated-)
- [https://docs.aws.amazon.com/kms/latest/developerguide/determining-access.html](https://docs.aws.amazon.com/kms/latest/developerguide/determining-access.html)

## 技術情報

- Source Metadata：[sources/aws/kms_key_not_publicly_accessible/metadata.json](../../sources/aws/kms_key_not_publicly_accessible/metadata.json)
- Source Code：[sources/aws/kms_key_not_publicly_accessible/check.py](../../sources/aws/kms_key_not_publicly_accessible/check.py)
- Source Metadata Path：`sources/aws/kms_key_not_publicly_accessible/metadata.json`
- Source Code Path：`sources/aws/kms_key_not_publicly_accessible/check.py`
