# AWS account is a member of an active AWS Organization

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `organizations_account_part_of_organizations` |
| クラウドプラットフォーム | AWS |
| サービス | organizations |
| 重大度 | medium |
| カテゴリ | identity-access |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | governance |

## 説明

**AWS account** membership in **AWS Organizations** with organization status `ACTIVE`. Assesses if the account is associated with an organization and that the organization state is `ACTIVE`.

## リスク

Absence of **AWS Organizations** weakens governance across accounts. Without **SCP guardrails** and centralized policy, excessive permissions, unsafe network settings, or risky services may be enabled, threatening **confidentiality** and **integrity**. Fragmented logging and response slow containment, impacting **availability** and increasing cost exposure.

## 推奨事項

Operate all accounts under **AWS Organizations** (preferably with *all features*). Structure OUs, enforce **SCPs** for least privilege, and apply separation of duties between management and member accounts. Centralize logging and billing to support defense-in-depth, and routinely review org membership and policies.

## 修正手順


### CLI

```text
aws organizations create-organization
```

### Terraform

```hcl
# Creates an AWS Organization so this account becomes a member (status ACTIVE)
resource "aws_organizations_organization" "<example_resource_name>" {
  # Critical: creating this resource makes the account part of an active AWS Organization
}
```

### Other

1. Sign in to the AWS Management Console with the account to remediate
2. Open the AWS Organizations console
3. Click "Create an organization"
4. Confirm to create (default is All features)
5. Verify the organization status shows Active on the Settings page

## 参考資料

- [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html)
- [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_view_org.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_view_org.html)

## 技術情報

- Source Metadata：[sources/aws/organizations_account_part_of_organizations/metadata.json](../../sources/aws/organizations_account_part_of_organizations/metadata.json)
- Source Code：[sources/aws/organizations_account_part_of_organizations/check.py](../../sources/aws/organizations_account_part_of_organizations/check.py)
- Source Metadata Path：`sources/aws/organizations_account_part_of_organizations/metadata.json`
- Source Code Path：`sources/aws/organizations_account_part_of_organizations/check.py`
