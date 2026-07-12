# S3 Glacier vault has no policy or its policy does not allow access to everyone

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `glacier_vaults_policy_public_access` |
| クラウドプラットフォーム | AWS |
| サービス | glacier |
| 重大度 | critical |
| カテゴリ | internet-exposed |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/AWS Foundational Security Best Practices, Effects/Data Exposure, TTPs/Initial Access/Unauthorized Access |
| リソースタイプ | Other |
| リソースグループ | storage |

## 説明

**Glacier vault** access policy is evaluated for exposure to **public principals**. The finding highlights `Allow` statements that grant access to `Principal: '*'` (including wildcard forms), and notes when a vault lacks a policy.

## リスク

Publicly grantable vault access undermines **confidentiality** and **integrity**. Anyone could list, retrieve, or delete archives, leading to data exposure or loss. Attackers may also trigger large retrieval operations, degrading **availability** and driving unexpected costs.

## 推奨事項

Enforce **least privilege** on vault policies: restrict to specific AWS accounts or roles, avoid `Principal: '*'`, and grant only necessary actions. Apply **defense in depth** with **Vault Lock** for immutable retention and continuous review and monitoring of access to prevent broad or unintended exposure.

## 修正手順


### CLI

```text
aws glacier delete-vault-access-policy --account-id <ACCOUNT_ID> --vault-name <VAULT_NAME>
```

### Native IaC

```yaml
# CloudFormation: Glacier vault without an access policy (no public access)
Resources:
  <example_resource_name>:
    Type: AWS::Glacier::Vault
    Properties:
      VaultName: <example_resource_name>
      # AccessPolicy omitted to remove any public access and pass the check
```

### Terraform

```hcl
# Glacier vault with no access policy (not public)
resource "aws_glacier_vault" "<example_resource_name>" {
  name = "<example_resource_name>"
  # access_policy omitted to remove any public access and pass the check
}
```

### Other

1. In AWS Console, open Amazon S3 Glacier (Classic)
2. Go to Vaults and select the target vault
3. Open the Access policy tab and click Edit
4. Remove the policy (clear all content) or delete it
5. Save changes

## 参考資料

- [https://docs.aws.amazon.com/amazonglacier/latest/dev/access-control-overview.html](https://docs.aws.amazon.com/amazonglacier/latest/dev/access-control-overview.html)

## 技術情報

- Source Metadata：[sources/aws/glacier_vaults_policy_public_access/metadata.json](../../sources/aws/glacier_vaults_policy_public_access/metadata.json)
- Source Code：[sources/aws/glacier_vaults_policy_public_access/check.py](../../sources/aws/glacier_vaults_policy_public_access/check.py)
- Source Metadata Path：`sources/aws/glacier_vaults_policy_public_access/metadata.json`
- Source Code Path：`sources/aws/glacier_vaults_policy_public_access/check.py`
