# AWS WAF Classic Regional rule has at least one condition

ST Cloud check knowledge base entry.

## チェック項目情報

| 項目 | 値 |
| --- | --- |
| チェック項目 ID | `waf_regional_rule_with_conditions` |
| クラウドプラットフォーム | AWS |
| サービス | waf |
| 重大度 | medium |
| カテゴリ | Uncategorized |
| チェックタイプ | Software and Configuration Checks/AWS Security Best Practices, Software and Configuration Checks/Industry and Regulatory Standards/NIST 800-53 Controls |
| リソースタイプ | AwsWafRegionalRule |
| リソースグループ | security |

## 説明

**AWS WAF Classic Regional rules** have one or more **conditions (predicates)** attached (IP, byte/regex, geo, size, SQLi/XSS) to define which requests the rule evaluates

## リスク

An empty rule never matches, letting traffic bypass that control. This weakens defense-in-depth and can impact **confidentiality** (data exfiltration), **integrity** (SQLi/XSS), and **availability** (missing rate/size limits), depending on Web ACL order and default action.

## 推奨事項

Define precise **conditions** for each rule (e.g., IP, pattern, geo, size) and avoid placeholder rules. Apply **least privilege** filtering, review rule order, and use layered controls for **defense in depth**. Regularly validate and monitor rule effectiveness.

## 修正手順


### CLI

```text
aws waf-regional update-rule --rule-id <example_rule_id> --change-token $(aws waf-regional get-change-token --query ChangeToken --output text) --updates '[{"Action":"INSERT","Predicate":{"Negated":false,"Type":"IPMatch","DataId":"<example_ipset_id>"}}]'
```

### Native IaC

```yaml
# Add at least one condition to a WAF Classic Regional Rule
Resources:
  <example_resource_name>:
    Type: AWS::WAFRegional::Rule
    Properties:
      Name: <example_resource_name>
      MetricName: <example_metric_name>
      Predicates:
        - Negated: false         # CRITICAL: ensures the predicate is applied as-is
          Type: IPMatch          # CRITICAL: predicate type
          DataId: <example_ipset_id>  # CRITICAL: attaches an existing IP set as a condition
```

### Terraform

```hcl
# WAF Classic Regional rule with at least one condition
resource "aws_wafregional_rule" "<example_resource_name>" {
  name        = "<example_resource_name>"
  metric_name = "<example_metric_name>"

  predicate {
    data_id = "<example_ipset_id>"  # CRITICAL: attaches existing IP set as the condition
    type    = "IPMatch"             # CRITICAL: predicate type
    negated = false                  # CRITICAL: apply condition directly
  }
}
```

### Other

1. Open the AWS Console and go to AWS WAF, then select Switch to AWS WAF Classic
2. In the left pane, choose Regional and click Rules
3. Select the target rule and choose Add rule
4. Click Add condition, set When a request to does, choose IP match (or another type), and select an existing condition (e.g., an IP set)
5. Click Update to save the rule with the condition

## 参考資料

- [https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-rules-editing.html](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-rules-editing.html)
- [https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-2](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-2)
- [https://docs.aws.amazon.com/config/latest/developerguide/waf-regional-rule-not-empty.html](https://docs.aws.amazon.com/config/latest/developerguide/waf-regional-rule-not-empty.html)

## 技術情報

- Source Metadata：[sources/aws/waf_regional_rule_with_conditions/metadata.json](../../sources/aws/waf_regional_rule_with_conditions/metadata.json)
- Source Code：[sources/aws/waf_regional_rule_with_conditions/check.py](../../sources/aws/waf_regional_rule_with_conditions/check.py)
- Source Metadata Path：`sources/aws/waf_regional_rule_with_conditions/metadata.json`
- Source Code Path：`sources/aws/waf_regional_rule_with_conditions/check.py`
