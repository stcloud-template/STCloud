# AWS Organization has opted out of all AI services and child accounts cannot override the policy

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `organizations_opt_out_ai_services_policy` |
| クラウドプラットフォーム | AWS |
| サービス | organizations |
| 重大度 | medium |
| カテゴリ | gen-ai |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Effects/Data Exposure |
| リソースタイプ | Other |
| リソースグループ | governance |

## 説明

**AWS Organizations** is assessed for an AI services opt-out policy that sets `services.default.opt_out_policy` to `optOut` and blocks child overrides via `@@operators_allowed_for_child_policies` set to `@@none`.

## リスク

Without an enforced opt-out, AI services may store and use your content for model training, weakening **confidentiality** and **data sovereignty**. If child accounts can override, they can re-enable data use, risking unintended cross-Region retention and exposure of logs, documents, or code processed by these services.

## 推奨事項

Establish an org-wide AI services opt-out: set the default to `optOut` and prohibit child policy overrides (`@@none`). Apply at the highest scope, gate exceptions through change control, and review periodically. Align with **least privilege** and **data minimization** to prevent unintended content sharing with managed AI services.

## 修正手順


### Native IaC

```yaml
# CloudFormation: Opt out of all AI services and prevent child overrides
Resources:
  AiServicesOptOutPolicy:
    Type: AWS::Organizations::Policy
    Properties:
      Name: <example_resource_name>
      Type: AISERVICES_OPT_OUT_POLICY
      Content: |
        { "services": { "default": { "opt_out_policy": { "@@assign": "optOut", "@@operators_allowed_for_child_policies": ["@@none"] } } } }
        # Critical: @@assign "optOut" opts out org-wide; @@operators... ["@@none"] blocks child overrides
      TargetIds:
        - <example_resource_id> # Critical: attach to the organization root (e.g., r-xxxx)
```

### Terraform

```hcl
# Enable AI services opt-out policy type
resource "aws_organizations_organization" "<example_resource_name>" {
  enabled_policy_types = ["AISERVICES_OPT_OUT_POLICY"]  # Critical: allow AI opt-out policies
}

# Create the AI opt-out policy
resource "aws_organizations_policy" "<example_resource_name>" {
  name    = "<example_resource_name>"
  type    = "AISERVICES_OPT_OUT_POLICY"
  content = <<JSON
{ "services": { "default": { "opt_out_policy": { "@@assign": "optOut", "@@operators_allowed_for_child_policies": ["@@none"] } } } }
JSON
  # Critical: @@assign "optOut" opts out; @@operators... ["@@none"] prevents child overrides
}

# Attach policy to the org root
resource "aws_organizations_policy_attachment" "<example_resource_name>" {
  policy_id = aws_organizations_policy.<example_resource_name>.id
  target_id = aws_organizations_organization.<example_resource_name>.roots[0].id  # Critical: attach to root
}
```

### Other

1. In the AWS Management Console, open AWS Organizations using the management account
2. Go to Policies > AI services opt-out
3. Click Opt out from all services and confirm
4. Verify the policy is attached to the Root and shows default -> opt_out_policy -> @@assign: optOut with @@operators_allowed_for_child_policies set to ["@@none"]

## 参考資料

- [https://docs.aws.amazon.com/organizations/latest/userguide/disable-policy-type.html](https://docs.aws.amazon.com/organizations/latest/userguide/disable-policy-type.html)
- [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out_all.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out_all.html)
- [https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out_syntax.html](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out_syntax.html)

## 技術情報

- Source Metadata：[sources/aws/organizations_opt_out_ai_services_policy/metadata.json](../../sources/aws/organizations_opt_out_ai_services_policy/metadata.json)
- Source Code：[sources/aws/organizations_opt_out_ai_services_policy/check.py](../../sources/aws/organizations_opt_out_ai_services_policy/check.py)
- Source Metadata Path：`sources/aws/organizations_opt_out_ai_services_policy/metadata.json`
- Source Code Path：`sources/aws/organizations_opt_out_ai_services_policy/check.py`
