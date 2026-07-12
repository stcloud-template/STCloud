# AWS WAF Classic Regional rule group has at least one rule

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `waf_regional_rulegroup_not_empty` |
| クラウドプラットフォーム | AWS |
| サービス | waf |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls |
| リソースタイプ | AwsWafRegionalRuleGroup |
| リソースグループ | security |

## 説明

**AWS WAF Classic Regional rule groups** are evaluated to confirm they contain at least one **rule**. Groups with no rule entries are considered empty.

## リスク

An empty rule group contributes no filtering in a web ACL, letting requests bypass inspection within that group. This erodes **defense in depth** and can enable injection, brute-force, or bot traffic to reach applications, threatening **confidentiality**, **integrity**, and **availability**.

## 推奨事項

Apply **least privilege**: populate each rule group with vetted rules aligned to your threat model, using `ALLOW`, `BLOCK`, or `COUNT` actions as appropriate. Remove or disable unused groups to avoid false assurance. Validate behavior in staging and monitor metrics to maintain **defense in depth**.

## 修正手順


### CLI

```text
aws waf-regional update-rule-group --rule-group-id <rule-group-id> --updates Action=INSERT,ActivatedRule={Priority=1,RuleId=<rule-id>,Action={Type=BLOCK}} --change-token <change-token>
```

### Native IaC

```yaml
# CloudFormation: Ensure WAF Classic Regional Rule Group has at least one rule
Resources:
  <example_resource_name>:
    Type: AWS::WAFRegional::RuleGroup
    Properties:
      Name: <example_resource_name>
      MetricName: <example_resource_name>
      ActivatedRules:
        - Priority: 1  # Critical: adds a rule so the rule group is not empty
          RuleId: <example_resource_id>  # Critical: references an existing rule to include in the group
          Action:
            Type: BLOCK
```

### Terraform

```hcl
# Ensure WAF Classic Regional Rule Group has at least one rule
resource "aws_wafregional_rule_group" "<example_resource_name>" {
  name        = "<example_resource_name>"
  metric_name = "<example_resource_name>"

  # Critical: adds a rule so the rule group is not empty
  activated_rule {
    priority = 1
    rule_id  = "<example_resource_id>"  # existing rule ID
    action {
      type = "BLOCK"
    }
  }
}
```

### Other

1. In the AWS Console, go to AWS WAF & Shield and switch to AWS WAF Classic
2. Select the correct Region, then choose Rule groups
3. Open the target rule group and click Edit rule group
4. Click Add rule to rule group, select an existing rule, choose an action (e.g., BLOCK), and click Update
5. Save changes to ensure the rule group contains at least one rule

## 参考資料

- [https://docs.aws.amazon.com/cli/latest/reference/waf-regional/update-rule-group.html](https://docs.aws.amazon.com/cli/latest/reference/waf-regional/update-rule-group.html)
- [https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-groups.html](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-groups.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-3](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-3)

## 技術情報

- Source Metadata：[sources/aws/waf_regional_rulegroup_not_empty/metadata.json](../../sources/aws/waf_regional_rulegroup_not_empty/metadata.json)
- Source Code：[sources/aws/waf_regional_rulegroup_not_empty/check.py](../../sources/aws/waf_regional_rulegroup_not_empty/check.py)
- Source Metadata Path：`sources/aws/waf_regional_rulegroup_not_empty/metadata.json`
- Source Code Path：`sources/aws/waf_regional_rulegroup_not_empty/check.py`
