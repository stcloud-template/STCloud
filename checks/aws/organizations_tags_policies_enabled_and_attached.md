# AWS Organization has tag policies enabled and attached

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `organizations_tags_policies_enabled_and_attached` |
| クラウドプラットフォーム | AWS |
| サービス | organizations |
| 重大度 | low |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices |
| リソースタイプ | Other |
| リソースグループ | governance |

## 説明

**AWS Organizations** tag policies are evaluated for their presence and attachment to organization targets (accounts or OUs), distinguishing between no policies, policies defined but not attached, and policies attached to at least one target.

## リスク

Absent or unattached tag policies cause inconsistent or missing tags, undermining: - **Confidentiality** via bypassed tag-based access conditions - **Integrity** through misclassified resources and drift - **Availability** when automation, cost routing, or incident scoping that rely on tags break

## 推奨事項

Enable **tag policies** and attach them to relevant roots/OUs/accounts. Define mandatory keys (e.g., `Environment`, `CostCenter`) with allowed values. Apply **defense in depth** by using tags in IAM conditions and SCPs. Start with validation-only, then enforce, and continuously monitor compliance across accounts.

## 修正手順


### Native IaC

```yaml
# CloudFormation: Create and attach a Tag Policy
Resources:
  TagPolicy:
    Type: AWS::Organizations::Policy
    Properties:
      Name: <example_resource_name>
      Type: TAG_POLICY  # Critical: defines a Tag Policy type
      Content:
        tags:
          Environment:
            tag_key:
              "@@assign": "Environment"
      TargetIds:
        - <example_resource_id>  # Critical: attaches the policy to an account/OU/root
```

### Terraform

```hcl
# Create a Tag Policy
resource "aws_organizations_policy" "<example_resource_name>" {
  name    = "<example_resource_name>"
  type    = "TAG_POLICY"  # Critical: defines a Tag Policy type
  content = jsonencode({
    tags = {
      Environment = {
        tag_key = { "@@assign" = "Environment" }
      }
    }
  })
}

# Attach the Tag Policy to a target (Root/OU/Account)
resource "aws_organizations_policy_attachment" "<example_resource_name>" {
  policy_id = aws_organizations_policy.<example_resource_name>.id
  target_id = "<example_resource_id>"  # Critical: attaches the policy to an account/OU/root
}
```

### Other

1. Sign in to the AWS Management Console with the organization management account
2. Open AWS Organizations > Policies > Tag policies
3. If prompted, click Enable tag policies
4. Click Create policy, enter a name, add minimal valid content (e.g., define one tag key), and create the policy
5. Select the policy and click Attach
6. Choose the Root, an OU, or at least one account and confirm
7. The check passes when a tag policy exists and is attached to a target

## 参考資料

- [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html)

## 技術情報

- Source Metadata：[sources/aws/organizations_tags_policies_enabled_and_attached/metadata.json](../../sources/aws/organizations_tags_policies_enabled_and_attached/metadata.json)
- Source Code：[sources/aws/organizations_tags_policies_enabled_and_attached/check.py](../../sources/aws/organizations_tags_policies_enabled_and_attached/check.py)
- Source Metadata Path：`sources/aws/organizations_tags_policies_enabled_and_attached/metadata.json`
- Source Code Path：`sources/aws/organizations_tags_policies_enabled_and_attached/check.py`
